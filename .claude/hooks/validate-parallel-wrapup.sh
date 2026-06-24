#!/usr/bin/env bash
# Hook: Block wrap-up skills when invoked from a parallel session (A3-004 / EXP-005 T6).
# Fires on UserPromptSubmit. Mechanizes DSM_0.2.A §7.11 "Parallel Session
# Guard for Wrap-Up Skills", previously agent-discipline only.
#
# Block condition (§7.11, verbatim): the prompt invokes /dsm-wrap-up,
# /dsm-light-wrap-up, or /dsm-quick-wrap-up AND .claude/parallel-sessions.txt
# contains a section whose CLAUDE_PID matches this Claude Code instance with
# State: active. In that case the current context IS a parallel session and
# must not run a main-session wrap-up.
#
# Deliberately a SEPARATE hook from transcript-reminder.sh: that hook's
# documented invariant is "always exits 0; never block". This guard is the
# only UserPromptSubmit case that blocks, so it lives on its own to keep the
# reminder hook's invariant intact (EXP-005 D3 design decision).
#
# Test seam: if _DSM_TEST_CLAUDE_PID is set, it is used as this instance's
# claude PID instead of walking the process tree (lets the block path be
# unit-tested in a fixture with no real claude ancestor).
#
# Exit codes:
#   0 — allow (not a wrap-up prompt, no registry, PID undetermined, no
#       matching active section)
#   2 — block (wrap-up prompt from an active parallel session)

set +e

INPUT=$(cat)
PROMPT=$(echo "$INPUT" | python3 -c "
import sys, json
try:
    print(json.load(sys.stdin).get('prompt',''))
except Exception:
    print('')
" 2>/dev/null || echo "")

# Only act on the three wrap-up skills (allow leading whitespace).
echo "$PROMPT" | grep -qE '^[[:space:]]*/dsm-(wrap-up|light-wrap-up|quick-wrap-up)([[:space:]]|$)' || exit 0

REGISTRY=".claude/parallel-sessions.txt"
[ -f "$REGISTRY" ] || exit 0

# Determine this instance's claude PID (test seam, else process-tree walk).
MY_CLAUDE_PID="${_DSM_TEST_CLAUDE_PID:-}"
if [ -z "$MY_CLAUDE_PID" ]; then
  pid=$PPID
  for _ in $(seq 1 10); do
    [ -z "$pid" ] && break
    [ "$pid" = "1" ] && break
    read ppid comm < <(ps -o ppid=,comm= -p "$pid" 2>/dev/null)
    [ -z "$ppid" ] && break
    if [ "$comm" = "claude" ]; then MY_CLAUDE_PID=$pid; break; fi
    pid=$ppid
  done
fi
# Fail-open: if the PID cannot be determined, do not block (matches the
# reminder hook's fail-safe posture).
[ -n "$MY_CLAUDE_PID" ] || exit 0

# State-aware section scan: a section matches iff it carries BOTH this PID
# and State: active. Checked at each section boundary and at EOF so the
# field order within a section does not matter.
BLOCK=$(awk -v mypid="$MY_CLAUDE_PID" '
  function check() { if (pid==mypid && state=="active") found=1 }
  /^## / { check(); pid=""; state="" }
  /^CLAUDE_PID:/ { pid=$2 }
  /^State:/ { state=$2 }
  END { check(); if (found) print "BLOCK" }
' "$REGISTRY")

[ "$BLOCK" = "BLOCK" ] || exit 0

cat >&2 <<'EOF'
Wrap-up skills cannot run from parallel sessions. Use
`/dsm-parallel-session-wrap-up` to end this parallel session, or switch to
the main session tab for full wrap-up.
EOF
exit 2
