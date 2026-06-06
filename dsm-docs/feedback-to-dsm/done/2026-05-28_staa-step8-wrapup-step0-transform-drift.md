# Transform drift between `/dsm-staa` Step 8 and `/dsm-wrap-up` Step 0 (compact-mirror regeneration)

**Date:** 2026-05-28
**Project:** dsm-blog-poster
**Session:** STAA run analyzing S21
**Severity:** Skill defect (produces a silently-empty mirror; recoverable, no data loss)
**Suggested target:** `/dsm-staa` Step 8 + `/dsm-wrap-up` Step 0 (the two regenerators), and DSM_0.2.A Reasoning Lessons Protocol (canonical spec)

## Summary

`/dsm-staa` Step 8 and `/dsm-wrap-up` Step 0 are documented as implementing "the same rule" for regenerating `.claude/reasoning-lessons-compact.md`, and the skill explicitly states they must update together. They have drifted: the awk transform published in `/dsm-staa` Step 8 gates the body on a `## Categories` heading, but this spoke's `.claude/reasoning-lessons.md` has no such heading. Running Step 8's awk verbatim discarded **every** entry and produced a header-only mirror. The transform that `/dsm-wrap-up` Step 0 actually ran (per the committed mirror) does not gate on `## Categories`.

## Concrete incident

During a `/dsm-staa` run on this spoke (analyzing Session 21), Step 8 instructed me to regenerate the compact mirror with this awk:

```awk
/^## Categories/ { found = 1; next }
!found { next }
/^### / { print; next }
/^- \[(auto|STAA)\] S[0-9]+ \[[^]]+\]: / { sub(...); print "- " $0; next }
{ print }
```

This spoke's `.claude/reasoning-lessons.md` is structured as:

```
# Reasoning Lessons

Entries tagged `[STAA]` are from Session Transcript Analysis. Format: ...
Scope: ...

---

- [STAA] S8 [ecosystem]: ...
- [auto] S9 [ecosystem]: ...
...
```

There is no `## Categories` heading and no `### Category` subheadings, the entries are a flat list after a `---` rule. Because `!found { next }` discards all input until a `## Categories` line that never appears, the awk emitted only the 9-line freshness header, 0 entries. `wc -l` on the result: 10 lines, versus 68 expected.

The previously committed mirror (generated at the S22 `/dsm-wrap-up` on 2026-05-28T01:23) contains all entries correctly stripped, and it **includes** the `# Reasoning Lessons` guideline header in its body. That output is impossible from Step 8's gated awk. So `/dsm-wrap-up` Step 0 is running a different, non-gating transform.

Recovery: I regenerated with the non-gating form (drop the `## Categories`/`!found` lines, keep the `### ` passthrough and the prefix-strip), matching the committed format. Result: 68 lines, all 51 entries present.

## Root cause (two candidates, Hub to disambiguate)

1. **File-template drift.** DSM_0.2.A may have standardized a `## Categories` + `### Category` structure for `reasoning-lessons.md` after this spoke's file was created. This spoke's file predates that and was never migrated, so a transform written against the new structure fails against the old one. Fix: migrate the spoke file (add `## Categories` and category headings), OR make the transform tolerant of both shapes.

2. **Transform drift between the two regenerators.** The awk literally published in `/dsm-staa` Step 8 differs from whatever `/dsm-wrap-up` Step 0 actually executes (the committed mirror proves Step 0 does not gate on `## Categories`). The skill's own cross-reference note says: "If the rule changes ... both /dsm-wrap-up Step 0 and /dsm-staa Step 8 must update together." That synchronization has lapsed.

Both are plausible and not mutually exclusive. The observable fact is: the Step 8 awk, copy-pasted as written, silently empties the mirror for any spoke whose `reasoning-lessons.md` lacks `## Categories`.

## Why it matters

`/dsm-go` Step 1.5 reads the compact mirror as boot-time canonical context. A header-only mirror means the next session boots with **zero** reasoning lessons in context, and the failure is silent: the regeneration command exits 0, the file is written, nothing errors. A spoke that trusted Step 8's awk verbatim would quietly lose its entire lessons context until the next wrap-up overwrote it.

## Proposed fixes

- **Reconcile the two transforms to one canonical awk** stored in DSM_0.2.A and referenced (not re-inlined) by both `/dsm-staa` Step 8 and `/dsm-wrap-up` Step 0. Re-inlining the script in two skill files is the drift mechanism itself.
- **Make the canonical awk shape-tolerant:** treat `## Categories` as optional. If absent, do not gate, pass the body through (matching current `/dsm-wrap-up` behavior). This keeps older flat-structured spoke files working without forced migration.
- **Add a post-generation sanity check:** after regenerating, assert the mirror's stripped-entry count equals the source's `grep -cE '^- \[(auto|STAA)\]'` count. A mismatch (e.g. 0 vs 51) should warn loudly rather than commit a silently-empty mirror.

## Related

- `/dsm-staa` Step 8 (origin: BL-433, S207)
- `/dsm-wrap-up` Step 0
- DSM_0.2.A Reasoning Lessons Protocol (canonical spec the two should defer to)
- `/dsm-go` Step 1.5 (consumer of the mirror)
