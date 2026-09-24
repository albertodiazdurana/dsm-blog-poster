# BL-033: DSM v1.20.0 to v1.26.3 release coverage

**Status:** Open
**Priority:** High
**Date Opened:** 2026-09-16
**Origin:** S36 Stage 0. `/dsm-go` Step 1.8 reported last-align 1.20.0 against CHANGELOG 1.25.0 at boot; by wrap-up Central was at 1.26.3. Four inbox notifications from Central are unprocessed, the most recent pushed 2026-09-04.

## Scope, and why it starts at v1.20.0

**BL-029 owns v1.18.0 to v1.19.0 and is still open**, blocked at Gate 1 on the thesis,
not on drafting. This BL does not absorb it and does not re-cover its range. Scoping by
what is unowned rather than by what triggered the cycle is the S33 lesson: the trigger
was v1.25.0, but everything from v1.20.0 forward is unowned, and scoping to the trigger
alone would strand six releases.

Range: **v1.20.0 (2026-08-05) through v1.26.3**, seven releases.

## Problem, with deltas measured 2026-09-16

| Artifact | Claims | Gate | Delta |
|---|---|---|---|
| `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` | 147 features | `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` = **176** | **29 behind** |
| `content/about.md` | The Fourteen Principles | `grep -cE '^### 1\.[0-9]+'` = **14** | none |

**The principle check was run on heading TEXT, not on the count.** All fourteen §1.x
headings were compared against the list MEMORY records from S33: §1.1 Take a Bite
through §1.14 Observe Before Engaging, with §1.13 Forward the Why. No same-slot
replacement. This matters because the count gate is structurally blind to a one-out-one-in
swap, which is exactly what v1.18.0 did when it replaced §1.13, and a matching count
was reported as "no drift" at the time. Recording the method so the next cycle does not
have to re-establish that the check was real.

**The 29-entry gap is the largest this project has carried.** Prior cycles ran 84→90,
90→114, 114→129, 129→142, 142→143, 143→147.

## Unprocessed inbox notifications

All four are in `_inbox/dsm-agentic-ai-data-science-methodology.md` and none has been
read for content. The most recent (2026-09-04, S258) covers v1.26.0 to v1.26.3 and
carries five F-entries verbatim:

- **F-171** sessions refusing at boot on the newest models, traced to one phrase in an always-loaded block
- **F-172** the always-loaded instruction file cut by 43%
- **F-173** a completeness check that could never report complete (the `8/9` scaffold count)
- **F-174** the reasoning log's before-acting entry renamed from "thinking" to "plan"
- **F-175** the punctuation rule retired in favour of an on-demand skill

## Three items that are already actionable and do not wait for Stage 2

**1. F-175 resolves the defect this project found independently in S36, in the opposite
direction.** S36's `/dsm-align` found the §17.1 template carrying three `**Scope.**`
paragraphs with no `### Punctuation` heading above them, held `last-align.txt` at 1.20.0
rather than regenerate, and proposed restoring the rule. Central found the same defect
and **retired the rule instead**. Verified 2026-09-16: `grep -c 'The rule governs files
that reach a reader'` against the current template returns 0. So the resolution is to
**remove** the Punctuation section from this project's CLAUDE.md, not to restore it, and
no upstream feedback report is owed , filing one would report a defect already fixed.

**2. `last-align.txt` is held at 1.20.0 on a reason that is now stale.** Its note says
"advance once the punctuation question is decided". It is decided. The marker must not
simply be advanced, because `/dsm-align` has still never run against 1.26.3; the note
needs correcting so a future boot does not read a resolved hold as an open one.

**3. F-173 names this project by name.** The ghost `dsm-docs/inbox/` folder, holding
only an empty `.gitkeep`, was created to satisfy a ninth canonical folder that no
specification lists, and it inflates the boot scaffold count to a false 9/9. S36's
`/dsm-align` reported it as a collision and did not remove it, per the report-don't-
auto-fix rule. F-173 is upstream confirmation that it is a ghost, so removal is now
evidenced rather than inferred. It is one tracked empty file.

## S37 progress (2026-09-16), the three already-actionable items are all done

1. **Punctuation section removed.** `/dsm-align` ran 1.20.0 → 1.26.3 and regenerated the
   §17.1 managed block from `DSM_0.2.T_Alignment_Templates.md`. The scripted diff was
   exactly three hunks: `### Punctuation` removed (F-175), and the transcript delimiter +
   Pre-Gen-Brief label renamed thinking → plan (F-174). No upstream feedback owed.
2. **`last-align.txt` corrected and advanced to 1.26.3.** The hold is discharged; the note
   now records what the run found rather than a hold reason. Hooks: 3 updated from Central;
   `settings.json` merged (BL-484 Bash matcher, first landing on this spoke).
3. **Ghost `dsm-docs/inbox/` deleted** (`git rm dsm-docs/inbox/.gitkeep`). Boot scaffold
   count drops from a false 9/9 to a true 8/8.

**Inbox processed.** The FEATURES rolling archive (now spanning F-147..F-175, not just the
four notifications named above) was read in full and archived to
`_inbox/done/2026-09-04_dsm-agentic-ai-data-science-methodology.md`; the two align
notifications were archived too. Front B still reads it from `done/` at weave time.

**Central notified (Front-F-adjacent, but about the deploy, not the release).** Appended a
question to `~/dsm-agentic-ai-data-science-methodology/_inbox/dsm-blog-poster.md` asking
whether `scripts/sync-commands.sh --deploy` will run at Central, since the v1.20-v1.26
spoke actions require it and this project loads ~4-month-stale `/dsm-*` command copies.
That deploy is Central's operation, not this spoke's.

## Stage checklist (per CLAUDE.md DSM Version Release Coverage)

- [x] **Stage 0 , Detect.** Range named, deltas measured, notifications located.
- [x] **Stage 1 , Open the BL.** This file. Deltas recorded above.
- [x] **Stage 2 , Factual updates** (all three fronts done S37)
  - [x] Front B , features post 147 → 176 (commit d6e3a5e). Wove F-147..F-175 as narrative threads across the three dimensions (11 weave points + a meta-through-line on the self-catching-check pattern), count updated in all 4 places, Gate 4 passed (dedup + /humanizer, 2 rule-9 density fixes, em-dash 0). +910 words (3482 → 4392). **PUBLISHED via PR #68 (merge 922501f), deploy run 35979127525 success (25s); verified live 2026-09-24 at https://take-ai-bite.com/blog/2026-03-20-dsm-features-three-dimensions/ , "176" serves, age:0, 0 stale "147 features".**
  - [x] Front C , About page. **No change needed, verified S37 2026-09-24 on heading TEXT not count:** DSM_6.0 has 14 §1.x headings (1.1 Take a Bite … 1.14 Observe Before Engaging, 1.13 Forward the Why); `content/about.md` heading "The Fourteen Principles" + 14 numbered items match all 14 heading texts exactly. No same-slot swap. Recorded rather than skipped so a future session does not re-run the check.
  - [x] Front F , portfolio inbox notification sent S37 2026-09-24 to `~/dsm-data-science-portfolio-working-folder/_inbox/2026-09-24_dsm-blog-poster_dsm-v1.26-release.md` (Low priority, informational: 147→176 features, 14 principles unchanged).
- [ ] **Stage 3 , Release post (Front A).** Note the ordering dependency with BL-029 below.
- [ ] **Stage 4 , LinkedIn cross-post (Front E) + record (Front D)**
- [ ] **Stage 5 , Close**

## Ordering dependency with BL-029, and a candidate that may dissolve it

BL-029's Front A has been carried unstarted across four checkpoints, blocked at Gate 1
because the arc that v1.18-v1.19 naturally produces ("a principle is not real until it
has a mechanism") sits too close to the published thesis of Post B, "The rules that
almost cover the case" (2026-07-25).

**v1.26.0 supplies a candidate thesis that the older range could not.** F-171 and F-172
are one story: a session that would not start, three rounds of trimming that were the
wrong theory, a single phrase as the cause, and a 43% reduction kept from an experiment
whose premise the evidence disproved. S36 already published the author's own account of
that incident as "He Who Must Not Be Named"
(https://take-ai-bite.com/blog/2026-09-01-he-who-must-not-be-named/) plus LinkedIn Post 26.

That creates a real question for Gate 1 rather than an answer: the incident is **already
covered** from the author's side, so a release post covering F-171/F-172 risks being the
same story told twice, which is the exact collision blocking BL-029. Decide deliberately
whether the release post cross-references the published piece and covers what it did not
(the reduction, the retired rule, the checks that could never fire), or whether this
range's Front A skips that cluster entirely.

## Acceptance criteria

- [x] All inbox notifications read and moved to `_inbox/done/YYYY-MM-DD_{source}.md` per the dated-archive convention (S37; the archive spans F-147..F-175)
- [ ] Features post count reconciled against the gate at the time of the edit, not against the 176 recorded here, since the gate moves
- [x] The three already-actionable items above are resolved (S37: Punctuation removed, marker advanced, ghost deleted)
- [ ] Stage gates marked complete or deferred in this file
