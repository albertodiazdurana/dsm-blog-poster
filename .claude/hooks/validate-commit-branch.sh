#!/bin/bash
# Hook: Block commits that would land directly on main/master (A3-003 / EXP-005 T6).
# Fires on PreToolUse for Bash calls. Filters to commands containing
# `git commit`. If the current branch is main or master, blocks with the
# DSM_0.2 §20.8 Post-Merge Branch Recreation fix text.
#
# Mechanizes the prose rule (DSM_0.2 §20.8 + §20.1: main "Only receives
# merges from Level 2 session branches") that was previously
# user-catches-it (origin: dsm-blog-poster S17 hit it twice).
#
# Bypass (the two legitimate direct-to-main cases, per §20.8): the
# /dsm-go "Git Pre-Step" initial commit, and explicit user-requested hub
# maintenance. A confirmation file authorizes the next commit on main:
# .claude/commit-on-main-confirmed.txt (presence = one-shot allow).
#
# Exit codes:
#   0 — allow (not a git commit, or current branch is not main/master,
#       or a confirmation file is present)
#   2 — block (git commit while on main/master, unconfirmed)

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

# Only act on git commit commands.
echo "$COMMAND" | grep -qE '(^|[;&|]|\s)git\s+commit(\s|$)' || exit 0

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
BRANCH=$(git -C "$REPO_ROOT" branch --show-current 2>/dev/null || echo "")

# Only main/master are protected.
case "$BRANCH" in
  main|master) ;;
  *) exit 0 ;;
esac

# One-shot bypass for the documented legitimate cases.
CONFIRM_FILE="$REPO_ROOT/.claude/commit-on-main-confirmed.txt"
if [ -f "$CONFIRM_FILE" ]; then
  exit 0
fi

cat >&2 <<EOF
BLOCKED (DSM_0.2 §20.8 Post-Merge Branch Recreation Rule): you are about to
commit directly on '$BRANCH'. main/master only receives merges from Level 2
session branches (§20.1); a direct commit silently violates the Three-Level
Branching Strategy.

FIX , create a session branch first:
  git checkout -b session-{N}/{YYYY-MM-DD}-{purpose}
then re-run the commit. After an in-session PR merge, chain it:
  gh pr merge {N} --merge --delete-branch && git checkout -b session-{N}/{YYYY-MM-DD}-{purpose}

Legitimate direct-to-main cases (initial repo commit, deliberate hub
maintenance): create .claude/commit-on-main-confirmed.txt and retry.
EOF
exit 2
