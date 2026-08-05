# BL-030: Structural prune of `.claude/reasoning-lessons.md`

**Status:** Open
**Priority:** Medium
**Date Opened:** 2026-08-05
**Origin:** `/dsm-staa` pass on S33 (2026-08-05). The over-budget state had been flagged without action in S31, S32, the S32 STAA run, the S33 `/dsm-go` boot report, and the S33 `/dsm-wrap-up`. This BL is the conversion of that flag into an owned work item, per the S33 STAA lesson that a flag repeated across N sessions measures the flag's inefficacy rather than the problem.

## Problem

`.claude/reasoning-lessons.md` holds **115 entries / 67,049 bytes**. `DSM_0.2.A` §8.1 targets roughly 70 entries and caps the derived compact mirror at 8 KB; the mirror is currently an order of magnitude over that. `/dsm-go` Step 1.5 reads the mirror as boot-time canonical context, so the overage is paid at every session start.

**Entry-level trimming has been demonstrated not to close the gap.** The S32 STAA run pruned 5 entries and the file still grew. This STAA pass ran a larger increment, 4 thematic merges plus 6 drops, removing 12 entries, while appending 12 new ones:

| | Before | After |
|---|---|---|
| Entries | 115 | 115 |
| Bytes | 60,862 | 67,049 |

Net zero entries and **+6,187 bytes**. Merging entries consolidates duplication but lengthens the survivors, and each session appends 5 to 8 more. The file cannot converge without a structural change.

## Root cause

Three structural properties are missing, and each one blocks a different part of the fix:

1. **No categories.** The file is a flat list. The §8.1 transform already preserves `### Category` headings and is explicitly shape-tolerant about their absence, so the mirror inherits the flatness. Without grouping there is no unit to consolidate against.
2. **No stable identifiers.** Entries cross-reference each other positionally (`#31`, `#52`, `#90`, `#74/#77`), and **those references are already stale**: `#31` claims to be about restructuring a post into extracts while entry 31 is the S23 verify-claims lesson, and `#52` claims merge-over-squash while entry 52 is figures-by-thesis. Prior prunes broke them silently. Any future prune inherits the same breakage, which makes pruning feel unsafe and is part of why it keeps slipping.
3. **No retention rule.** Nothing decides when a lesson leaves. Entries are added by `/dsm-wrap-up` Step 0 and `/dsm-staa` Step 6 with no counterpart removing them, so the file is append-only by construction.

## Scope

- Introduce `### Category` headings and assign every entry. The transform requires `###` be reserved exclusively for category headings (§8.1 "Heading convention"), so guideline header lines must stay `##` or bold.
- Replace positional `#NN` cross-references with stable identifiers, or convert them to descriptive references (`the S31 verify-the-rule's-scope lesson`). The twelve S33 STAA entries already use the descriptive form and can serve as the pattern.
- Consolidate within categories. The four merges landed in this pass (overclaim family, deploy verification, harness/classifier constraint, BL-023 slug) are the first increment and the shape to follow.
- Define a retention rule so the file self-limits: candidates are a per-category cap, an age or supersession test, or promotion-on-recurrence to CLAUDE.md.
- Re-verify against the §8.1 entry target and the 8 KB mirror cap after each increment, and record the measured before/after rather than asserting improvement.

## Out of scope

- LLM-driven compression of lesson bodies. §8.1 is explicit that the mirror is trim-only and that compression beyond trim is tracked upstream under BL-427 Step 5.
- Editing the canonical transform. `DSM_0.2.A` §8.1 is the single source of truth and re-inlining a divergent copy is the documented BL-447 drift bug.

## Carried forward, not owned by this BL

Two lessons call for a CLAUDE.md amendment that has never been made. Both have been carried across the S31, S32 and S33 STAA markers without an owner; `/dsm-staa` does not edit CLAUDE.md, which is why they keep surviving. Neither is a prune candidate, both need a decision:

- **Hook-scoring dimensions** (`[STAA] S23`). Its own text says "Implies a Stage-3 Hook-rule amendment in CLAUDE.md" for the six-dimension hook comparison at Gate 2.
- **Gate-4 title-claim check** (`[STAA] S29`). Add "does the title's implied verb match what the version genuinely did?" to the release-post Gate 4, so a title overclaim lands in one deploy rather than two.

## Success criteria

- Live file at or near the §8.1 entry target, with the measured count recorded.
- Compact mirror regenerated via the canonical §8.1 transform, both sanity checks silent.
- No positional `#NN` cross-references remain, or all of them resolve correctly.
- A retention rule is written into the file's own header, so the next session inherits it without re-deriving.

## Notes

Increment 1 landed during the S33 STAA pass and is already in the working tree: 4 merges, 6 drops, 12 appends. The measurement table above is that increment's result and is the evidence this BL exists.
