# Two published `/dsm-go` snippets fail against their real input: Step 5 baseline checksums and the Step 1.8 CHANGELOG version read

**Pushed:** 2026-07-31 (S33 wrap-up, to `dsm-central/_inbox/dsm-blog-poster.md`)

**Date:** 2026-07-30
**Project:** dsm-blog-poster
**Sessions:** Instance 1 filed by the STAA run analyzing S32 (finding originated in the S32 `/dsm-go` boot, 2026-07-25). Instance 2 and the shared-pattern section added in S33 (2026-07-30), found at the S33 boot.
**Severity:** Two skill defects, both in the "wrong answer that looks like a legitimate answer" class. Neither loses data. See each instance for its own severity and suggested target.

**Filename note:** this file is still named for Instance 1 because the inbox action item and `.claude/last-staa.txt` reference it by that name. The scope is both instances.

---

# Instance 1: Step 5 baseline checksums are silently empty under Claude Code's `grep` shim

**Severity:** Skill defect, silent. Every session baseline written under this harness is missing its entire checksum section, and the pipeline reports success.
**Suggested target:** `~/.claude/commands/dsm-go.md` lines 538-539 (the two checksum lines of the Step 5 baseline snippet). Two characters each.

## Summary

`/dsm-go` Step 5's baseline snippet uses `grep -v '^\?'` and `grep '^\?'` to split
tracked from untracked entries in `git status --porcelain`. In a Claude Code Bash
session, `grep` is not GNU grep: it is a shell function that execs the `claude`
binary as `ugrep -G`. ugrep rejects `^\?` as invalid syntax, so both checksum
lines produce **zero output**, and because the error comes from the middle of a
pipeline with no `pipefail`, the pipeline still **exits 0**.

The result is a baseline file that has its `# Checksums` header and nothing under
it, written without any failure signal an exit-code check would catch.

## Concrete incident

S32's boot hit this and worked around it locally (rewrote both lines as `awk` on
`$1`), attributing it to "a ugrep-aliased shell". That attribution was too
narrow, which is why this is being filed rather than left as a local note: the
shim is injected by Claude Code, not by this machine's shell config, so the
defect is active in every DSM project running under this harness version.

Reproduced firsthand during the STAA run:

```
$ type grep
grep is a function
grep ()
{
    ...
    local _cc_bin="${CLAUDE_CODE_EXECPATH:-}";
    [[ -x $_cc_bin ]] || _cc_bin=/home/berto/.local/bin/claude;
    ...
    ( exec -a ugrep "$_cc_bin" -G --ignore-files --hidden -I --exclude-dir=.git ... )
}

$ grep --version
ugrep 7.5.0 x86_64-pc-linux-gnu +sse2; -P:pcre2jit; ...
```

The two lines verbatim from `dsm-go.md:538-539`, run in this repo with a working
tree of 3 modified and 1 untracked file:

```
$ git status --porcelain | grep -v '^\?' | awk '{print $2}' | xargs -r md5sum
ugrep: error: error at position 5
(?m)^?
     \___invalid syntax

pipeline exit=0
stdout bytes: 0
```

Identical result for line 539 (`grep '^\?'`). Both sections of the baseline's
checksum block are empty; nothing errors at the pipeline level.

## Root cause

A BRE `\?` **immediately after `^`** is interpreted differently by the two
engines, and only in that position:

- **GNU grep 3.7:** treats `\?` there as a literal `?`. Verified: `grep -c '^\?'`
  on a two-line fixture returns 1 (the `??` line only), not 2, so it is matching
  a literal question mark, which is what the snippet intends.
- **ugrep 7.5.0 `-G`:** treats `\?` as the optional quantifier and applies it to
  `^`, which is unquantifiable, so it errors at parse time.

This is narrow. The same escape used as a normal quantifier is portable:
`grep 'a\?b'` returns identical results under both engines. The defect is
specifically a quantifier with nothing to quantify, which GNU silently
reinterprets as a literal and ugrep refuses.

**Scope check across the skill set.** All 20 `dsm-*.md` skills were swept for
BRE-escape grep patterns. Three other sites use GNU BRE extensions and were
tested individually: all three are **fine** under the shim, no fix needed.

| Site | Pattern | Under shim |
|------|---------|-----------|
| `dsm-go.md:538` | `grep -v '^\?'` | **BROKEN**, exit 0, no output |
| `dsm-go.md:539` | `grep '^\?'` | **BROKEN**, exit 0, no output |
| `dsm-go.md:391` | `grep -v '^\*\|main\|session-'` | OK, matches GNU |
| `dsm-light-go.md:90` | `grep -v '^\*\|main\|session-'` | OK, matches GNU |
| `dsm-wrap-up.md:60` | `grep -c '^+- \*\*F-[0-9]\+'` | OK, matches GNU |

So this is a two-line fix, not a sweep.

## Why it matters

The baseline's checksums are the mechanism `/dsm-wrap-up` uses to tell
**pre-existing uncommitted files** apart from **this session's work**. That
discrimination is load-bearing, not cosmetic: S32 relied on exactly it to split
its commits so that S31's STAA output stayed attributed to S31 rather than being
folded into S32's commit. With an empty checksum block, wrap-up has the file
list from `git status --porcelain` (which is written correctly, line 536) but no
content fingerprints, so it cannot detect that a pre-existing file was
*modified* during the session.

The failure is silent in the direction that matters: exit 0, file written,
`# Checksums` header present. An agent that reads the tool output sees the ugrep
diagnostic (S32 did); an agent that trusts exit codes ships an incomplete
baseline and never knows.

## Proposed fixes

**Primary, two characters per line.** Replace the escaped quantifier with a
POSIX bracket expression, which is unambiguous in both engines:

```bash
git status --porcelain | grep -v '^[?]' | awk '{print $2}' | xargs -r md5sum >> .claude/session-baseline.txt
git status --porcelain | grep '^[?]'    | awk '{print $2}' | xargs -r md5sum >> .claude/session-baseline.txt
```

Verified in this repo under **both** engines. Under the shim it now produces the
3 tracked checksums and the 1 untracked checksum correctly. `grep -vE '^\?'`
(explicit ERE) also works under both and is an equally valid fix; the bracket
form is preferred because it needs no flag change.

**Secondary, portability convention.** DSM skill snippets are executed by an
agent in a Bash tool whose `grep` may be a harness-provided ugrep shim. Worth a
one-line convention wherever snippets are published: prefer POSIX bracket
expressions or explicit `-E` over GNU BRE escapes. The three sites in the table
above happen to be safe, so this is a guard against future additions rather than
a cleanup.

## Adjacent observation, unverified

By inspection only, not tested: `awk '{print $2}'` on the same two lines
mis-handles rename entries. `git status --porcelain` renders a rename as
`R  old -> new`, so `$2` is the OLD path, which no longer exists on disk and
would make `md5sum` error. If the Hub is editing these two lines anyway, it may
be worth checking. Flagged at low confidence because no rename case was
constructed to confirm it.

---

# Instance 2: the Step 1.8 CHANGELOG version read can never report a match

**Added S33 (2026-07-30), found at the `/dsm-go` boot of this session.**

**Severity:** Skill defect. The grep itself fails loudly (exit 1), but the *effect* is silent: the conditional-align optimization that Step 1.8 exists to provide can never fire, so `/dsm-align` runs on every session and reports no drift, which looks correct.
**Suggested target:** `scripts/commands/dsm-go.md:431`, `scripts/commands/dsm-align.md:528`, and the marker template at `scripts/commands/dsm-align.md:546`. Also `dsm-align.md:463` (the persistent-report header field).

## Summary

Both skills specify reading the DSM version from Central's CHANGELOG as "the latest
`## [vX.Y.Z]` heading":

- `dsm-go.md:431` , "Read `{dsm-central}/CHANGELOG.md` → extract the latest `## [vX.Y.Z]` heading (first match)."
- `dsm-align.md:528` , "resolve the current DSM version from `{dsm-central}/CHANGELOG.md` (latest `## [vX.Y.Z]` heading)"

CHANGELOG headings carry **no `v` prefix**. Meanwhile the marker template at
`dsm-align.md:546` writes `dsm-version: vX.Y.Z`, **with** the prefix. So the two
sides of Step 1.8's comparison are stored in different formats.

## Evidence

Run against `~/dsm-agentic-ai-data-science-methodology/`:

```
$ grep -m3 '^## \[' CHANGELOG.md
## [1.19.0] - 2026-07-28
## [1.18.0] - 2026-07-12
## [1.17.1] - 2026-07-09

$ grep -m1 '^## \[v' CHANGELOG.md ; echo "exit=$?"
exit=1

$ grep -c '^## \[v' CHANGELOG.md ; echo "exit=$?"
0
exit=1
```

And the stored marker, this project's `.claude/last-align.txt` before this session:

```
dsm-version: v1.18.0
```

## Why it matters

Step 1.8's procedure is: read `dsm-version` from `last-align.txt`, read the latest
CHANGELOG heading, and **skip `/dsm-align` if they match**. The step documents its own
rationale explicitly, that the previous unconditional run cost "~30-40% on Sonnet" and
that a version match means no template changed.

Because the marker stores `v1.19.0` and the CHANGELOG yields `1.19.0`, a literal
comparison finds them different **every session**, forever. The optimization can never
fire. An agent that silently normalizes the `v` gets the intended behaviour; an agent
that follows the written spec does not, and there is nothing in the step that tells it
to normalize.

The failure direction is the expensive-but-plausible one: `/dsm-align` runs, finds no
drift, reports `check-only`, and the session looks healthy while having paid the full
context cost the step was written to avoid.

## Observed this session

The S33 boot ran `grep -m1 '^## \[v' CHANGELOG.md` verbatim from the spec and got an
empty result. The version had to be recovered by re-reading the file head and observing
the actual format. The session then compared `v1.18.0` against `1.19.0` by normalizing
by hand, concluded correctly that they differ, and ran `/dsm-align`. The right outcome
was reached, but by departing from the spec rather than following it.

## Proposed fixes

**Primary.** Make the two formats agree. Either specify the heading as
`## [X.Y.Z]` in both skills and drop the `v` from the marker template, or keep the
marker's `v` and state explicitly that the comparison strips it. The first is simpler
and matches Keep-a-Changelog, which the CHANGELOG's own header cites.

A pattern that works against the real file:

```bash
grep -m1 -oE '^## \[[0-9]+\.[0-9]+\.[0-9]+\]' CHANGELOG.md
```

**Secondary.** Step 1.8's decision table has no branch for "version read returned
nothing". It covers "file does not exist" (treat as mismatch, force align) but not an
empty read, which is exactly what the current spec produces. Adding "empty read →
force align, and warn" would make the failure visible rather than leaving the agent to
improvise, which is what happened here.

---

# Shared pattern across both instances

Both defects are a **canonical snippet published in a skill that does not match its
actual input**, producing a wrong answer shaped like a legitimate one. That is the
common cause and the reason they are filed together.

The failure modes are **not** identical, and the difference matters for how each gets
caught:

| | Instance 1 (ugrep) | Instance 2 (CHANGELOG) |
|---|---|---|
| Mismatch is between | the snippet and the **execution environment** (correct GNU BRE, rejected by the shim) | the spec and its **own source file** (a format the CHANGELOG does not use) |
| Exit code | **0**, the error is mid-pipeline with no `pipefail` | **1**, the grep fails honestly |
| Where the silence is | at **execution**: a complete-looking baseline with an empty section | at **effect**: a correct-looking align run that silently never skips |
| What catches it | reading tool output instead of the exit code | comparing the spec against the file it names |

An earlier framing in this session claimed both exit 0. That was checked and is wrong
for Instance 2; the table above is the verified version.

**Suggested convention, covering both.** A published snippet is an assertion about its
input and its environment, and neither is verified at authoring time. Worth a
standing rule wherever skills publish runnable snippets: the snippet must be run
against the real file, in the harness the agent actually uses, before it ships. Both
instances would have been caught by one execution.

## Related

- `/dsm-go` Step 5 (session baseline), Instance 1's sole affected site
- `/dsm-go` Step 1.8 and `/dsm-align` Step 13, Instance 2's sites
- `/dsm-wrap-up` (consumer of the checksums; the baseline distinction it depends on)
- `done/2026-05-28_staa-step8-wrapup-step0-transform-drift.md`, prior STAA-filed
  skill-snippet defect in this project. Same shape: a published snippet that
  fails silently on a spoke and produces a plausible-looking artifact.
- S32 `[auto]` reasoning lesson on shell failure modes that report success
  (`git commit -m` with nested quotes; `sed` with a case-insensitive flag). This
  is a third instance, and the common fix in all three is reading the actual
  output rather than the exit code.
