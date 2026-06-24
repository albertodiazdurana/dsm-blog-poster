#!/bin/bash
# Hook: Block single-quoted heredoc appends to the session transcript (A3-005 / EXP-005 T6).
# Fires on PreToolUse for Bash calls. Mechanizes the DSM_0.2 §7 anti-pattern
# (also DSM_7.0 §2.1.5): a single-quoted heredoc (`<< 'EOF'`) writing to
# .claude/session-transcript.md suppresses shell expansion, so `$(date +%H:%M)`
# lands as a literal string instead of the timestamp (observed portfolio S69).
#
# Narrow scope: blocks ONLY when the command both references the transcript
# AND uses a single-quoted heredoc delimiter. Unquoted heredocs (`<< EOF`) and
# `cat >` (the /dsm-go Step 6 reset) are legitimate and pass. This is the
# zero-legitimate-use case; the broad "all Bash writes to the transcript" variant
# is intentionally NOT enforced (regex-on-shell-text is approximate).
#
# Exit codes:
#   0 — allow (not a transcript write, or not a single-quoted heredoc)
#   2 — block (single-quoted heredoc targeting the session transcript)

set -e

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    print(json.load(sys.stdin).get('tool_input', {}).get('command', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")

# Must reference the session transcript.
echo "$COMMAND" | grep -q 'session-transcript\.md' || exit 0

# Must contain a single-quoted heredoc delimiter: << '...' or <<- '...'
# (optional whitespace between << and the quote).
echo "$COMMAND" | grep -qE "<<-?[[:space:]]*'" || exit 0

cat >&2 <<'MSG'
BLOCKED (DSM_0.2 §7 heredoc anti-pattern): a single-quoted heredoc
(<< 'EOF') writing to .claude/session-transcript.md suppresses shell
expansion, so timestamps like $(date +%H:%M) are written literally instead
of evaluated (observed portfolio S69).

FIX: capture the timestamp into a variable and use an UNQUOTED heredoc:
  NOW=$(date +%H:%M)
  cat >> .claude/session-transcript.md << EOF
  <------------Start Thinking / ${NOW}------------>
  ...
  EOF
Or prefer the Edit-tool append path (read last 3 lines, anchor on the last
non-empty line).
MSG
exit 2
