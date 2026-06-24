#!/bin/bash
# Hook: Block staging of secret-pattern files (A3-002 / EXP-005 T6).
# Fires on PreToolUse for Bash calls. Filters to commands containing
# `git add`. Resolves the stage-set and tests each filename against the
# DSM_0.2.C §1 / CLAUDE.md "Secret Exposure Prevention" pattern list. If
# any staged file matches a sensitive pattern, blocks with the §1 alert.
#
# Mechanizes the prose rule that was previously agent-discipline only
# (DSM_0.2.C §1; DSM_7.0 §2.1.8 concedes "DSM has no Claude-specific
# secret scanner hook today"). This hook is that scanner.
#
# Override: a blanket "stage everything" does NOT bypass this check (per
# §1). A deliberate override requires a confirmation file listing the
# approved path: .claude/staging-secrets-confirmed.txt (same model as
# validate-cross-repo-write.sh, BL-391).
#
# Exit codes:
#   0 — allow (not a git add, or no staged file matches a secret pattern)
#   2 — block (a staged filename matches a sensitive pattern, unconfirmed)

set -e

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('tool_input', {}).get('command', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")

# Only act on git add commands.
echo "$COMMAND" | grep -qE '(^|[;&|]|\s)git\s+add(\s|$)' || exit 0

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
CONFIRM_FILE="$REPO_ROOT/.claude/staging-secrets-confirmed.txt"

# Sensitive filename patterns (DSM_0.2.C §1 / CLAUDE.md Secret Exposure Prevention).
# Bash extended-glob patterns matched against each candidate's basename.
shopt -s extglob nocasematch
matches_secret() {
  local name="$1"
  case "$name" in
    .env|.env.*|*.key|*.pem|*.p12|*.pfx|*.keystore) return 0 ;;
    credentials.*|secrets.*|*_secret*|*secret*|*password*) return 0 ;;
    *) return 1 ;;
  esac
}

# Resolve the candidate stage-set.
# Strip the leading "...git add" and collect remaining tokens.
ADD_ARGS=$(echo "$COMMAND" | sed -E 's/.*git[[:space:]]+add[[:space:]]*//')

# Decide whether this is a bulk add (-A / --all / . / -u / no explicit files).
BULK=0
EXPLICIT_FILES=()
if [ -z "$ADD_ARGS" ]; then
  BULK=1
else
  for tok in $ADD_ARGS; do
    case "$tok" in
      -A|--all|-u|--update|.|:/|\*) BULK=1 ;;
      -*) : ;;                       # other flags, ignore
      *) EXPLICIT_FILES+=("$tok") ;; # a path argument
    esac
  done
  # No explicit file paths after stripping flags -> treat as bulk.
  [ ${#EXPLICIT_FILES[@]} -eq 0 ] && BULK=1
fi

# Build the candidate list.
CANDIDATES=()
if [ "$BULK" -eq 1 ]; then
  # Everything git would stage: porcelain shows modified + untracked.
  while IFS= read -r line; do
    f="${line:3}"             # strip the 2-char status + space
    [ -n "$f" ] && CANDIDATES+=("$f")
  done < <(git -C "$REPO_ROOT" status --porcelain 2>/dev/null)
else
  CANDIDATES=("${EXPLICIT_FILES[@]}")
fi

# Test each candidate's basename.
HITS=()
for f in "${CANDIDATES[@]}"; do
  base=$(basename "$f")
  if matches_secret "$base"; then
    # Honor an explicit per-path confirmation.
    if [ -f "$CONFIRM_FILE" ] && grep -qxF "$f" "$CONFIRM_FILE" 2>/dev/null; then
      continue
    fi
    HITS+=("$f")
  fi
done
shopt -u nocasematch

[ ${#HITS[@]} -eq 0 ] && exit 0

cat >&2 <<EOF
BLOCKED (DSM_0.2.C §1 Secret Exposure Prevention): the following staged
file(s) match a sensitive filename pattern and must not be committed:

$(printf '  - %s\n' "${HITS[@]}")

A blanket "stage everything" does NOT override this check. If a match is a
genuine, safe-to-commit file, add its exact path to
.claude/staging-secrets-confirmed.txt (one path per line) and retry.
EOF
exit 2
