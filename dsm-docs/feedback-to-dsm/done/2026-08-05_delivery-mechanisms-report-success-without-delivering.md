# Two delivery mechanisms report success while delivering nothing to the spoke

**Date:** 2026-08-05
**Project:** dsm-blog-poster
**Session:** S34. Both findings surfaced while executing v1.20.0's own spoke actions, not while looking for defects.
**Severity:** Silent non-delivery, with one live wrong-path risk. Nothing was destroyed and nothing is unrecoverable. What makes this worth filing is that both mechanisms emit a **success signal** while delivering nothing, so neither is discoverable by running it and reading the result.
**Suggested targets:** `scripts/commands/dsm-align.md` Step 10b sub-step (e); `scripts/sync-commands.sh` (`PROJECT_COMMANDS` / `PROJECT_TARGET` design); `CHANGELOG.md` v1.20.0 BL-481 spoke action.

**Relationship to the prior reports:** third and fourth instances of the pattern filed in
`done/2026-07-30_ugrep-shim-breaks-dsm-go-baseline-checksums.md` (Instances 1 and 2) and
widened in `2026-08-05_local-state-files-assumed-gitignored-are-tracked.md` (Instance 3).
Filed separately rather than appended to Instance 3 because that report is titled around
gitignore state; two command-delivery findings under that title would not be found by
anyone searching for either symptom. The shared pattern is restated and extended in the
final section rather than assumed.

---

## Finding A: `/dsm-align` Step 10e cannot install BL-484's new matcher

**What the spec says.** Step 10e, merging hook entries into a spoke's `settings.json`:

> - If ANY command from the template entry is already present in `settings.hooks[event]`,
>   skip appending this entry (idempotency: match on command, not object equality)

**What the template contains.** `scripts/templates/settings-hooks.json` lists the same
script under three different matchers:

```
PreToolUse:
  { matcher: "Edit",  command: .claude/hooks/validate-transcript-edit.sh   }
  { matcher: "Bash",  command: .claude/hooks/validate-rename-staging.sh    }
  { matcher: "Write", command: .claude/hooks/validate-cross-repo-write.sh  }   <- 1st
  { matcher: "Edit",  command: .claude/hooks/validate-cross-repo-write.sh  }   <- 2nd
  { matcher: "Bash",  command: .claude/hooks/validate-cross-repo-write.sh  }   <- 3rd, new in BL-484
```

**The consequence.** Executed literally, the `Write` entry is appended first. Its command
is then present in the event, so the `Edit` and `Bash` entries both match the skip
condition and are dropped. BL-484's entire purpose , extending the cross-repo write guard
to Bash file operations , can never reach any spoke through this step. The merge reports
`settings.json: already ok` and writes nothing.

**Evidence that the rule was never run against this input shape.** This spoke's
`settings.json` already carried `Edit -> validate-cross-repo-write.sh` before today.
Command-only matching would have skipped that entry at the time it was installed, so
whoever installed it was not applying the published rule. The rule and the deployed
result disagree, and the deployed result is the correct one.

**What this session did.** Used `(matcher, command)` as the idempotency key. That
installed the `Bash` entry, left the two project-local entries untouched
(`validate-parallel-wrapup.sh` on `UserPromptSubmit`, a `SessionStart` chmod), and is
idempotent on re-run. Proposed as the fix.

**Note on scope.** Until this lands, `cp`, `mv`, `>`, `>>`, `tee` and `rsync` reach any
path in an affected spoke ungated. BL-484's own CHANGELOG entry describes the Bash branch
as a floor rather than a proof, which is right, but a floor that never installs is not a
floor.

---

## Finding B: `sync-commands.sh` deploys five commands where no spoke can see them

**What the CHANGELOG asks.** v1.20.0, BL-481:

> The backlog skills point at the active `dsm-docs/plans/` tree rather than the legacy
> `plan/backlog/` tree.
> **Spoke action:** Run `scripts/sync-commands.sh --deploy`.

**What the script does.** `scripts/sync-commands.sh` splits its 20 commands in two:

```
USER_TARGET="${HOME}/.claude/commands"
PROJECT_TARGET="${REPO_DIR}/.claude/commands"
PROJECT_COMMANDS="dsm-backlog.md dsm-backlog-done.md dsm-checkpoint.md
                  dsm-review-feedback.md dsm-version-update.md"
```

`REPO_DIR` is **DSM Central's own directory**. Those five commands are therefore written
to a folder that only a Claude Code session running inside DSM Central can resolve. No
spoke reads it.

**What a spoke resolves instead.** Claude Code resolves a command from the project's own
`.claude/commands/` first, then falls back to `~/.claude/commands/`. Checked across the
ecosystem:

| Repository | own `.claude/commands/` | consequence for the five |
|---|---|---|
| dsm-blog-poster | none | falls through to user-level |
| dsm-data-science-portfolio-working-folder | none | falls through to user-level |
| dsm-graph-explorer | none | falls through to user-level |
| dsm-take-ai-bite | 20 files | shadows user-level, 7 of the 20 stale |
| DSM Central | 5 files | current, the only place `--deploy` reaches |

The user-level copies are orphans from before the project-level split and no code path
writes them:

| Command | user-level | tracked source | bytes (user / source) |
|---|---|---|---|
| `dsm-backlog-done` | 2026-03-20 | 2026-04-24 | 1,746 / 2,539 |
| `dsm-backlog` | 2026-04-22 | 2026-08-05 | 6,048 / 10,379 |
| `dsm-checkpoint` | 2026-04-22 | 2026-07-28 | 1,503 / 4,089 |
| `dsm-review-feedback` | 2026-04-22 | 2026-07-30 | 2,475 / 2,649 |
| `dsm-version-update` | 2026-04-22 | 2026-06-08 | 5,630 / 7,048 |

All five differ from source. The oldest is four and a half months behind.

**Both signals report success.** Verified by capturing md5 before and after rather than
by reading the script's summary:

```
$ ./scripts/sync-commands.sh --check
Checked: 20/20 | OK: 20 | Drifted: 0 | Missing: 0

$ md5sum ~/.claude/commands/dsm-backlog.md
687b529213168d36e6861d0ea43d154d

$ ./scripts/sync-commands.sh --deploy
Deployed 15 user-level commands to /home/berto/.claude/commands
Deployed 5 project-level commands to /home/berto/dsm-agentic-ai-data-science-methodology/.claude/commands

$ md5sum ~/.claude/commands/dsm-backlog.md
687b529213168d36e6861d0ea43d154d          <- unchanged
$ stat -c %y ~/.claude/commands/dsm-backlog.md
2026-04-22                                <- unchanged
```

`--check` returns OK because it compares each command against *its own designated
target*, and for these five that target is Central's project folder, which is current.
The file a spoke actually loads is outside the comparison entirely. BL-479 made `--check`
reliable at the thing it measures; this is a different thing.

**Two concrete live consequences, both verified by content.**

1. **Wrong path and wrong naming convention.** The spoke-visible `/dsm-backlog` instructs
   the agent to find the highest number in `plan/backlog/developments/`,
   `plan/backlog/improvements/` and `plan/backlog/done/`, then create the file at
   `plan/backlog/{developments|improvements}/BACKLOG-XXX_short-description.md`. None of
   those directories exists in this project, whose convention is
   `dsm-docs/plans/BL-{NNN}-short-title.md`. The tracked source has carried the corrected
   union-scan and the `dsm-docs/plans/` target since BL-481. This session filed BL-031 by
   hand against `CLAUDE.md` rather than through the skill, which is the only reason it
   landed in the right tree.

2. **A shipped feature that cannot be used.** The spoke-visible `/dsm-checkpoint` is 43
   lines against the source's 82. The missing half includes the entire
   `## Causal-Forward Next Steps (Delegating face of Forward the Why, DSM_6.0 §1.13)`
   section, which is **F-146**, shipped in v1.19.0. A spoke running `/dsm-checkpoint`
   gets the pre-F-146 template and no indication anything is absent.

**A third shape, in take-ai-bite.** That repo has its own `.claude/commands/` with 20
files, 7 of which differ from source, including `dsm-go.md` (49,509 bytes against the
current 59,058) and `dsm-align.md`. Because project-level shadows user-level, take-ai-bite
runs a `/dsm-go` that predates BL-482, BL-487, BL-488 and BL-489 **even though the
user-level copy on the same machine is current**. `--deploy` does not write there either.
So the failure has two directions: no project folder means falling through to a stale
user-level copy, and having one means shadowing a current user-level copy with a stale
project one. Both report OK.

---

## Why neither is caught

Neither mechanism has a check that measures what a spoke actually loads.

- Step 10e's idempotency is asserted in prose and never exercised against a template
  containing a repeated command. The template acquired its second repeat in BL-484;
  nothing re-ran the rule against it.
- `--check` measures source against designated target. The set of files a spoke resolves
  is not the set of designated targets, and no step compares the two.
- `/dsm-align` Step 11 explicitly skips on spokes ("Skip this step if the project is not
  DSM Central"), so the one drift check in the alignment path never runs where the stale
  files live.

## Proposed fixes

**A , Step 10e.** Change the idempotency key from `command` to `(matcher, command)`. One
sentence in the spec. The current wording, "match on command, not object equality", was
correct when no command appeared under two matchers, and silently became wrong when one
did. Worth stating the general form in §19.1's terms: a uniqueness rule is an assertion
about the data it will run against, and it needs re-running when that data changes shape.

**B , targeting.** Two candidate directions, and the choice is Central's because they
imply different intents:

- If the five are meant to be available everywhere, they are not project commands and
  should deploy to `USER_TARGET` like the other fifteen. The `PROJECT_COMMANDS` split then
  disappears.
- If they are meant to be Central-only, the stale user-level orphans should be deleted, so
  a spoke invoking `/dsm-backlog` fails visibly instead of running a four-month-old
  version. Failing loudly beats succeeding wrongly.

Either way, `--check` should compare against **resolution order** rather than designated
target, so a shadowing or orphaned copy is reported rather than invisible. That single
change would have surfaced all of this without anyone looking for it.

**C , the CHANGELOG line.** BL-481's spoke action names a remedy that cannot deliver the
fix it promises. Worth correcting in place so a spoke reading v1.20.0 does not conclude,
as this session initially did, that running the deploy satisfies it.

## How this extends the pattern

Instance 3's report widened the shared cause to **a published assertion about input or
environment that is never verified at authoring time**, and proposed that a property a
skill claims should be expressible as a check and shipped as one. Both findings here fit
that statement without stretching it. What they add is a fourth value on the
failure-signal axis:

| | Instance 1 (ugrep) | Instance 2 (CHANGELOG) | Instance 3 (gitignore) | A (Step 10e) | B (sync targets) |
|---|---|---|---|---|---|
| What is published | a runnable snippet | a format description | a property claim | a merge algorithm | a remedy + a target map |
| Mismatch between | snippet and execution environment | spec and its own source file | claim and the environment it was never installed into | spec and its own template file | remedy and the environment that consumes it |
| True anywhere? | yes, under GNU grep | no, nowhere | yes, in DSM Central only | no, nowhere | yes, in DSM Central only |
| Failure signal | exit 0, silent at execution | exit 1, silent at effect | none at all | none; reports `already ok` | **success reported, twice** |
| What catches it | reading tool output | comparing spec to the file it names | running the assertion as a check | running the rule against the real template | comparing against resolution order |

Instance 3 argued that a prose claim is worse than a broken snippet because a snippet at
least fails when run. Finding B is worse again: it does not merely lack a failure signal,
it emits a **positive** one. `--check` says 20/20 OK and `--deploy` says 20 commands
deployed, and both are true statements about the wrong set. An agent that dutifully runs
the spoke action, reads the output, and reports the action satisfied has done everything
right and is still wrong.

The discipline that catches all five is the same, and Finding B sharpens it: verify
against **what the consumer actually loads**, not against what the producer intended to
send.

## Related

- `done/2026-07-30_ugrep-shim-breaks-dsm-go-baseline-checksums.md` , Instances 1 and 2
- `2026-08-05_local-state-files-assumed-gitignored-are-tracked.md` , Instance 3, pending
  the same push
- v1.20.0 BL-485 (DSM_0.2 §19.1, Published Snippets Are Run Before They Ship) , the rule
  written to close this class. Both findings here predate it and neither would have been
  caught by its fenced-block trigger alone; Finding A is a prose algorithm and Finding B
  is a targeting design, so both fall under §19.1's second trigger form
- v1.20.0 BL-484 (the Bash matcher Finding A blocks), BL-481 (the fix Finding B blocks),
  BL-479 (`--check` reliability, correct but orthogonal)
