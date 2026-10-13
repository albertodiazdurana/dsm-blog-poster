# BL-035: DSM v1.26.7 to v1.29.0 release coverage

**Status:** OPEN
**Priority:** Medium
**Date Opened:** 2026-10-09
**Author:** Alberto (S40)
**Origin:** S40 Stage 0. `/dsm-go` Step 1.8 reported last-align 1.26.6 against CHANGELOG 1.29.0 at boot; `/dsm-align` ran 1.26.6 → 1.29.0 (check-only, alignment block in sync). One Central inbox notification (`agentic-ai-data-science-methodology.md`, covering v1.26.7 through v1.29.0, dated 2026-10-05 to 2026-10-09) was read in full and held pending this BL.

## Scope, and why it starts at v1.26.7

**BL-034 owns v1.26.4 through v1.26.6** (Stage 2 closed S39; Stages 3-5 still open). **BL-029 owns v1.18.0 to v1.19.0 and is still open**, blocked at Gate 1 on the thesis. This BL covers only the unowned range above v1.26.6 and does not absorb either neighbour.

Range: **v1.26.7 (2026-10-05) through v1.29.0 (2026-10-09)**, seven releases (1.26.7, 1.26.8, 1.27.0, 1.27.1, 1.27.2, 1.28.0, 1.29.0), nine F-entries. v1.27.1 shipped no new F-entry (transform/documentation fix only).

## Problem, with deltas measured 2026-10-09

| Artifact | Claims | Gate | Delta |
|---|---|---|---|
| `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` | 180 features | `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` = **189** | **9 behind** |
| `content/about.md` | The Fourteen Principles | `grep -cE '^### 1\.[0-9]+'` = **14** | none |

**The principle check was run on heading TEXT, not just the count.** None of F-180..F-188 is a new DSM_6.0 §1.x principle (they are boot/wrap-up/align tooling, `/dsm-staa` and `/dsm-align` audits, an egress rule in §5.8, a lessons-file bound in §8.3, and the `/dsm-new-spoke` bootstrap in §25.7). about.md's "The Fourteen Principles" heading + 14 numbered items still match. **Front C is a no-op this cycle.** Recording the method so the next cycle does not re-establish that the check was real.

**The counting convention (S37, carried):** the canonical gate `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` EQUALS FEATURES.md's own `**Current count:**` line (both **189** on 2026-10-09). No +1 F-000 discrepancy. The post tracks the gate; re-run it at edit time since it moves whenever Central ships.

## The nine F-entries (verbatim-sourced from the Central notification)

- **F-180 (v1.26.7, 2026-10-05)** — Session start now checks the FEATURES and README feature counts against the real number of entries, so a stale total can't slip onto the public page (BACKLOG-569, `/dsm-go` Step 2f). The running total was hand-maintained; a release that added entries without bumping it left both numbers wrong until someone noticed. Boot now recomputes the real count and flags a mismatch with both the claimed and the measured number, staying quiet when they agree. The counting-side companion to the existing Step 2e downstream-notification guard.

- **F-181 (v1.26.8, 2026-10-05)** — Session start stops silently skipping a merged branch it could not delete, and the rule it followed is corrected (BACKLOG-565, `/dsm-go`, DSM_0.2 §20.4). The safe delete checks a branch against its own remote copy, not against the main line; a branch genuinely merged to main whose remote lagged refused to delete and was swallowed, accumulating unseen. Cleanup now reports such a branch as a leftover and never reaches for force-delete. The methodology text that mis-described the criterion is corrected.

- **F-182 (v1.26.8, 2026-10-05)** — Wrap-up stops dropping a project's inbox by mistaking every project for the public mirror (BACKLOG-566, `/dsm-wrap-up`, `/dsm-quick-wrap-up`). The mirror-protection guard identified the mirror by the absence of one hub-only file — but every ordinary project also lacks it, so the guard treated every project as the mirror and left each one's inbox changes out of the wrap-up commit, logging the omission as if intended. The guard now identifies the mirror positively (absence of every role signal a real project carries); hub, clone, and spoke all commit their own inbox normally.

- **F-183 (v1.27.0, 2026-10-06)** — Scanning for leaked personal data no longer risks leaking it (BACKLOG-571, DSM_0.2.C §5.8). A sensitive-project egress scan of transcript/memory/reasoning-lessons must now report only generically ("clean", or line numbers) and never echo a matched name — or a search pattern containing one — back into those same append-only files. A new core rule stops the control from becoming the leak; an always-loaded pointer keeps it visible where the transcript is written.

- **F-184 (v1.27.0, 2026-10-06)** — The session-analysis agent no longer carries personal names into durable, propagating lessons (BACKLOG-572, `/dsm-staa`). The command reads a whole transcript (which can hold names) and appends to a lessons file that propagates to the hub and into every future startup context. It now keeps every quoted excerpt and saved lesson name-free (role, not name), states the propagation chain inline, and recommends scrubbing names before analysis on projects that declare a privacy policy.

- **F-185 (v1.27.0, 2026-10-06)** — Setting up a fresh public-mirror fork is smoother and less misleading (BACKLOG-573/574/575/577, Cloned-Mirror Kick-off). Kick-off prints the exact one-line ignore rule a fresh fork needs (without editing the git exclude file itself); the drift check no longer labels a mirror's load-bearing command copies as orphaned-and-deletable; Kick-off ends with a readiness checklist of the environment tools the boot gates depend on; and a cross-repo-write guard that shipped non-executable on the mirror is corrected so it runs.

- **F-186 (v1.27.2, 2026-10-08)** — Two `/dsm-align` audits that catch a backlog item going invisible or a finished design left marked unfinished (BL-557 + BL-580, `/dsm-align` Steps 11d/11e). The active backlog index was never checked against the files on disk — an item filed without its index row was invisible (two sat that way ~5 months). A separate gap let a design item whose decision was already written stay listed as open work. Two report-only audits now run in the hub's alignment pass (set-difference both ways; decision-record-vs-active cross-reference), both silent when clean so they don't become ignored warnings. With the done-index audit they make three axes of one question: does the record of what there is to do still match reality.

- **F-187 (v1.28.0, 2026-10-09)** — The cross-project lessons file now has a size bound and a prune, so it stops growing without limit (BACKLOG-567, DSM_0.2.A §8.3, `/dsm-staa` Step 7b). The hub's aggregation of lessons from every project had attribution and dedup rules but nothing capping size or removing stale entries, so it grew past the boot-primed file it feeds and its signal thinned. It now carries a soft size bound, a per-entry length ceiling, and a prune (archive codified lessons, consolidate duplicates, retire dead-project lessons, each leaving a tombstone). An honest long-term target — the first prune confirmed the file is mostly irreducible value — and a no-op on spokes, which have no such file.

- **F-188 (v1.29.0, 2026-10-09)** — A fresh directory can be set up as a new spoke with one command (BACKLOG-578, DSM_0.2.A §25.7, `/dsm-new-spoke`). Turning an uninitialized directory into a spoke had no clean path: the only setup command assumed a cloned mirror and would register the directory as its own hub. `/dsm-new-spoke <hub-path>` scaffolds the directory as a spoke of an existing hub (points it at the hub, builds the standard folders, runs spoke alignment); session start now recognizes the mistaken case and routes to the command instead of failing on it.

**Narrative clustering (for Stage 3, thesis TBD at Gate 1):** candidate clusters, with collision risk flagged against the neighbour BLs:
- **"The guard that needed guarding"** — F-182 (a guard that treated every project as the mirror and dropped inboxes), F-181 (a cleanup that swallowed the refusal that mattered), F-183 (a scan that could become the leak), F-186 (an index nobody audited). A control misfiring or going unwatched is the through-line. This is the most differentiated candidate; it does not reuse BL-034's frames.
- **Egress/confidentiality** — F-183 + F-184. **Collision risk:** BL-034's F-176 already carried the confidentiality theme; a Front A here must not retell it.
- **Context-cost** — F-187 (hub lessons-file bound). **Collision risk:** BL-034's F-177/178/179 cluster already told "keep the always-loaded context lean"; F-187 is the hub-aggregation sibling and would retell it.
- **Onboarding/mirror** — F-185 + F-188 (fork-init, new-spoke bootstrap).

The Front A thesis must differ from BL-033's "structural fix" frame, BL-034's "lean context" + confidentiality frames, and BL-029's pending thesis, or posts collide. Decide the cluster and thesis at Stage 3 Gate 1.

## Stage checklist (per CLAUDE.md DSM Version Release Coverage)

- [x] **Stage 0 — Detect.** Range named (v1.26.7–1.29.0, 9 F-entries), deltas measured, notification located and read (S40).
- [x] **Stage 1 — Open the BL.** This file. Deltas recorded above.
- [ ] **Stage 2 — Factual updates.**
  - [x] Front B — features post **180 → 189, PUBLISHED live** 2026-10-13 at https://take-ai-bite.com/blog/2026-03-20-dsm-features-three-dimensions/ via PR #74 (merge aa78d77), deploy run 38383613267 success. Wove F-180..F-188 across the three dimensions (F-181/182 → Human oversight/Session lifecycle; F-185+F-188 → Knowledge provenance/Protocol inheritance; F-186+F-180 → Versioned knowledge; F-183 → confidentiality outward edge; F-184+F-187 → Experience accumulation/Reasoning extraction). Count updated in title/description/opening/closing. Gate 4: seam/dedup pass (4 new→host seams framed as sequels, not re-introductions) + /humanizer clean (artifact grep clean; 2 readability fixes, voice preserved). Verified live cache-busted: 189 ×12, 0 stale 180, all weave phrases serving, age:0.
  - [x] Front C — About page. **No change needed, verified S40** on heading TEXT: DSM_6.0 has 14 §1.x headings; `content/about.md` "The Fourteen Principles" + 14 items match; none of F-180..F-188 is a new §1.x principle. Recorded, not edited.
  - [ ] Front F — portfolio inbox notification to `~/dsm-data-science-portfolio-working-folder/_inbox/` (cross-repo write gate).
- [ ] **Stage 3 — Release post (Front A).** Pending. Thesis TBD at Gate 1 (see clustering above; differentiate from BL-033/BL-034/BL-029).
- [ ] **Stage 4 — LinkedIn cross-post (Front E) + record (Front D).** Pending.
- [ ] **Stage 5 — Close.** Pending.

## Acceptance criteria

- [x] Central notification read and moved to `_inbox/done/2026-10-09_agentic-ai-data-science-methodology.md` (archived at Front B publish, PR #74)
- [x] Features post count reconciled against the gate at edit time (gate = 189; FEATURES.md Current count 189; 0 stale 180 live)
- [ ] Stage gates marked complete or deferred in this file (Front F + Stage 3-5 pending)
