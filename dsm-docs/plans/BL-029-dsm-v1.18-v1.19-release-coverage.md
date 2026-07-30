# BL-029: DSM v1.18.0-v1.19.0 release coverage (multi-front)

**Status:** Open
**Priority:** High
**Date Created:** 2026-07-30 (Session 33)
**Source:** S33 inbox triage. Entries: `_inbox/dsm-agentic-ai-data-science-methodology.md` (2026-07-28 FEATURES push, F-143..F-146, v1.19.0), `_inbox/2026-07-30_dsm-align-update.md` (alignment v1.18.0 -> v1.19.0, informational).
**Origin:** DSM shipped v1.19.0 on 2026-07-28. The cycle spans two versions rather than one because v1.18.0 was only half-covered: its Front B shipped in S32 as a carry-over from BL-027, but no v1.18.0 BL was ever opened and no v1.18.0 release post exists. See "Split state of v1.18.0" below.

## Pipeline reference

Follows the 6-stage Version Release Coverage pipeline in CLAUDE.md ("Detect -> Open BL -> Ship factual updates -> Write release post -> Cross-post and record -> Close").

## Stage 0/1 deltas (verified S33, 2026-07-30)

Verification commands run against `~/dsm-agentic-ai-data-science-methodology/`:

- **Feature count:** `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` = **147**. `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` claims **143**. Drift = **4** (F-143 through F-146).
- **Principle count:** `grep -cE '^### 1\.[0-9]+' DSM_6.0_AI_Collaboration_Principles_v1.0.md` = **14**. `content/about.md` = "The Fourteen Principles". Drift = **0**, and this was verified by comparing **all fourteen heading texts** against the numbered list in `about.md`, not by the count alone. The count gate is blind to a one-out-one-in slot swap (the S30 §1.13 incident, repeated at the feature layer in S32), so a matching count is not evidence on its own. All fourteen match verbatim, including §1.13 "Forward the Why" (corrected S30) and §1.14 "Observe Before Engaging". v1.19.0 shipped *mechanisms for* §1.13, not a new principle.

### Note on the F-000 indexing convention

FEATURES.md numbers from **F-000**, so the entry count is one higher than the highest index: F-000..F-146 is 147 entries. FEATURES.md's own `**Current count:** 146` line reports the highest index rather than the count, and therefore disagrees with the canonical gate command in CLAUDE.md by one. The features post has always tracked the **gate count** (at S32 it read 143 when the highest index was F-142), so **147 is the correct target**. BL-027 documented the same convention for its own cycle. The hub's off-by-one count line is a DSM Central issue, not a blog-poster one; worth reporting upstream, out of scope here.

## Split state of v1.18.0

v1.18.0 (F-142 "Forward the Why", BL-473) was recorded in BL-027's "Carried forward, NOT closed" section as belonging to a future cycle. S32 then shipped the Front B half of it (features post 142 -> 143, PR #59) without opening a BL for the cycle.

The consequence, verified S33:

- **Front B for v1.18.0: done** (S32). F-142 is already woven into the features post, which is why this BL's Front B is scoped 143 -> 147 and covers only F-143..F-146.
- **Front A for v1.18.0: never opened.** `content/blog/` holds four release posts covering v1.5 through v1.17; there is no v1.18.0 release post. No v1.18.0 BL exists either, only annotations inside BL-025 and BL-027.

MEMORY.md's claim that the cascade is "fully closed through v1.18.0" is accurate for the factual updates and inaccurate for the release post. This BL takes ownership of the orphaned Front A so it stops being invisible; the alternative (scoping this cycle to v1.19.0 only) would leave the gap with no home, which is the evaporation failure mode BL-027 avoided by writing its carry-forward down.

**Net effect on scope:** Front A covers **F-142 through F-146**. Front B covers **F-143 through F-146**. The two ranges differ by exactly F-142, for the reason above.

## Version range and feature inventory (the 4 new entries)

| F-entry | Date | Title (short) | Central BL | Location |
|---------|------|---------------|-----------|----------|
| F-143 | 2026-07-28 | A bite is the smallest increment the reviewer can verify | BL-478 | DSM_6.0 §1.1 |
| F-144 | 2026-07-28 | Informed-consent gate before high-token-cost fan-out actions | BL-476 | DSM_0.2 §8.9.2 |
| F-145 | 2026-07-28 | Downstream Impact Map for cross-BL coupling | BL-474 | BL template, §1.13 Registering face |
| F-146 | 2026-07-28 | Causal-forward session handoffs | BL-475 | wrap-up / checkpoint skills, §1.13 Delegating face |

F-142 (v1.18.0, "Forward the Why", DSM_6.0 §1.13) is in Front A's range but not Front B's; it shipped to the features post in S32.

## Dependencies and ordering

Stated in the causal-forward form F-146 itself specifies (what the continuation requires, what it depends on, what order that forces, what breaks if skipped).

- **`scripts/sync-commands.sh --deploy` in DSM Central** (spoke actions from Central BL-474 + BL-475) is a **conditional** prerequisite, not a blocker. It delivers the new optional `## Downstream Impact Map` BL-template section (F-145) and the causal-forward pending-list requirement in `/dsm-wrap-up`, `/dsm-quick-wrap-up`, and `/dsm-checkpoint` (F-146). Verified S33: the deployed `~/.claude/commands/dsm-backlog.md` does **not** carry the new section; the Central source does. **What breaks if skipped:** nothing in this BL fails, but any BL authored before the deploy (including this one) cannot use the new section, and wrap-up pending lists keep the pre-F-146 shape. **Order forced:** deploy before the next BL is authored, if the new section is wanted on it. Central's own CHANGELOG warns that `--check` is currently unreliable (BL-479), so run `--deploy` directly.
- **Front B does not block on Front A.** Per CLAUDE.md, Stage 2 factual updates ship in the same session as Stage 1 where the budget allows, even when Stage 3 waits.
- **No prior-cycle blocker.** BL-022, BL-025, and BL-027 are all closed, so unlike BL-027 this cycle's Stage 3 is not waiting on an earlier release post.

**This BL does not use the `## Downstream Impact Map` section**, because the deploy has not landed and the deployed template does not offer it. Its absence here is a sequencing fact, not an oversight.

## Fronts (the checklist)

### Front A: Release blog post , **ONE post** (decided S33)

**Status: Open.** Covers **v1.18.0 + v1.19.0** (F-142 through F-146) as a single post. Story-shaped, 5-part structure (Hook, Insight, Fix, Bonus, Takeaway). Drafted under the DSM_0.2 §8.10 chunked-drafting protocol, Gates 1-4, file-first.

**Bundling decision:** one post, decided by the author at Stage 1 rather than deferred to Gate 1. The narrative basis: v1.18.0 **named** Forward the Why as a principle and left it unimplemented; v1.19.0 shipped the two mechanisms that make it adoptable, F-145 (Registering) and F-146 (Delegating). The hub's own inbox notification frames the release that way.

**Live risk, carried into Gate 1 and NOT resolved by the one-post decision:** the thesis this arc most naturally produces , *a principle is not real until it has a mechanism* , sits close to the published thesis of Post B, "The rules that almost cover the case" (2026-07-25), which argued that a principle does not stop the failure it warns against until the behavior is named at the decision point. The count decision does not settle the thesis. Gate 1 must either differentiate the thesis explicitly or accept and signpost the continuity. Two posts three weeks apart with near-identical theses is the outcome to avoid.

**Reconstruction trail (mandatory reading order, all paths in DSM Central):**
1. `dsm-docs/blog/feature-trail.md` , the v1.18/v1.19 sections plus "Narrative threads". Expect rows to be unpopulated for this range; the trail is lazily populated per blog thread by design (Central BL-455), so populating it is part of this work, not a precondition. Price that at Gate 2 (the S31 lesson: verify a "mandatory source" is populated for your scope before accepting a gate's cost estimate).
2. `dsm-docs/plans/done/BACKLOG-473_*.md` (F-142), `BACKLOG-474_*`, `BACKLOG-475_*`, `BACKLOG-476_*`, `BACKLOG-478_*`.
3. Inbox origins in `_inbox/done/` for any inbox-sourced BL above.
4. `.claude/reasoning-lessons.md` in Central, `[auto]` / `[STAA]` entries tied to v1.18-v1.19.
5. `CHANGELOG.md` for both versions.

**Hook candidate (surfaced by the hub itself, not selected):** F-145's origin note records that the Downstream Impact Map's **first instance inside DSM was wrong in both rows, and the mechanism's own reconcile step is what caught it**. The hub's notification calls this "the more interesting story than the feature itself". Score it against the other candidates at Gate 2 on the S23 dimensions (reader-recognition, principle-fit, surprise, image-compressibility, stakes, time-to-point) and let the author rank; do not adopt it silently because it is the only one written down.

**Other candidate seeds:** F-144's origin (a session that spent ~3.0M tokens across two research passes, exhausted the usage window, and returned a partial deliverable after the second pass died mid-run) is a concrete, high-stakes, reader-recognisable incident. F-143's origin (weak wording found to live in the spoke-facing template rather than the protocol everyone assumed it came from) is the most methodology-shaped.

**Anti-patterns (from CLAUDE.md):** do not list features mechanically, do not write a changelog summary. **Additional, from S29:** do not title it "How Take AI Bite learned to X" unless the capability is genuinely new this version; check the title's implied verb at Gate 4, not post-publish.

### Front B: Features post update

**Status: Open.** `content/blog/2026-03-20-dsm-features-three-dimensions/index.md`. Count **143 -> 147** everywhere it appears (title, description, opening, closing , four occurrences found at lines 2, 5, 14, 122). Weave F-143..F-146 into the three dimensions as narrative threads, not a list.

Proposed weaving map (to be confirmed when drafting):
- **Human Oversight:** F-143 (a bite is what the reviewer can verify; the permission window is not the gate , note this pairs with the existing text on review gates), F-144 (informed-consent gate before high-token-cost fan-out).
- **Knowledge Provenance:** F-145 (Downstream Impact Map, coupling recorded at the moment it is settled), F-146 (causal-forward handoffs, the why travels inside the format). These two are the Registering and Delegating faces of the same principle and read best adjacent.
- **Experience Accumulation:** no new entry this cycle.

**Slot-swap check required before editing** (per S32): F-143 restates what a *bite* is, which the post may already describe under the older "one function, test, next function" framing. Grep the post for the old description as well as the count; a count-only update would leave a contradicted paragraph standing.

### Front C: About page principle list

**Status: Done , no action required (verified S33).** `content/about.md` is at "The Fourteen Principles" and all fourteen entries match the DSM_6.0 §1.1-§1.14 heading texts verbatim. v1.19.0 added mechanisms for §1.13, not a principle. Verified by heading text, not by count.

### Front D: linkedin-posts.md canonical record

**Status: Open.** Record the URL and "Status: Published" on the Post N entry after Front E publishes. Next post number: 25.

### Front E: LinkedIn cross-post

**Status: Open.** One post for the single Front A post. Draft in `dsm-docs/blog/linkedin-posts.md` as Post 25. Format 250-400 words, first person, hashtags, "Full post:" link. `#TakeAIBite` per the CLAUDE.md convention; drop `#DSM`. /humanizer pre-publish gate.

**Per S31:** lead with a different asset than the blog post's opening, so the cross-post is an alternative entry point rather than a preview. **BL-023 data point to record:** predict the slug branch pre-publication and log the outcome; Posts 21, 23, and 24 were three consecutive lead-3-hashtag hits, which does not resolve the S28 non-determinism finding.

### Front F: dsm-portfolio inbox notification

**Status: Done (2026-07-31, S33).** Written to `~/dsm-data-science-portfolio-working-folder/_inbox/2026-07-31_dsm-blog-poster_dsm-v1.19-release.md`. Both gates cleared with the body and path surfaced in conversation and explicitly approved (cross-repo write per Cross-Repo Write Safety, byline content per Voice-Attribution Review); create-only, no git operations in the target per F-129.

Content: Stage 2 summary (features post 143 -> 147 with the four entries named, About page unchanged and why), plus a counting note explaining the F-000 indexing so the portfolio does not re-derive the 147-versus-146 discrepancy if it runs the gate command itself. Format matched to the S27 precedent at `_inbox/done/2026-06-30_dsm-blog-poster_dsm-v1.15-v1.17-release.md`.

Filename carries 2026-07-31, the actual write date, not the 2026-07-30 this BL originally recorded. A dated-filename convention exists to make collisions impossible; a date that is not the write date defeats it.

## Out of scope

- The GE Epoch-5 multi-agent post (`_inbox/2026-07-06_dsm-graph-explorer_epoch5-multi-agent-blog-post.md`) , unrelated content thread, needs its own BL.
- BL-007 (IronCalc candidates A + B), BL-016, BL-017 , unrelated content threads.
- Fixing FEATURES.md's `**Current count:**` off-by-one , a DSM Central issue; report upstream rather than editing the hub from here.
- Adopting F-145/F-146 into this project's own BL and wrap-up practice beyond what `sync-commands.sh --deploy` delivers , that is a tooling change, not release coverage.

## Success criteria

All six fronts marked Done or explicitly Deferred with a recorded reason. On closure: verify the CLAUDE.md "DSM Version Release Coverage" section still matches the pipeline shape, move this BL to `dsm-docs/plans/done/` with a Date Completed, and update `dsm-docs/plans/README.md`.

## Stage status

- **Stage 0 (Detect):** Done (S33). Two versions behind; range named as v1.18.0-v1.19.0.
- **Stage 1 (Open BL):** Done (S33). This file. Deltas recorded.
- **Stage 2 (Ship factual updates):** **Done (S33).** Front B shipped (features post 143 -> 147, plus a correction to the F-142 paragraph's implementation overclaim); Front C verified Done by heading text; Front F written and confirmed.
- **Stage 3 (Front A):** Open. One post, bundling decided S33; thesis and hook open at Gate 1.
- **Stage 4 (Fronts E then D):** Open.
- **Stage 5 (Close):** Open.

## Outcomes

- **(S33) Front B shipped.** Features post 143 -> 147. F-143 placed as the definition the per-turn review paragraph's existing list was already instantiating; F-144 added as a second non-suppressible instance in Safety guardrails (count two -> three, paragraph split at the cost seam because the addition made it the post's longest at 218 words); F-145/F-146 absorbed into a rewritten Forward the Why passage. That passage also **corrected an overclaim**: the S32 text read "three places that used to be flat now carry it", which claimed implementation of all three faces when v1.18.0 had named the principle without shipping a mechanism. It now reads "it names three faces", and the planning face is stated plainly as still only named. Repetition pass before /humanizer per BL-454; humanizer clean against the current ruleset; build verified at the page (0 stale "143" in rendered HTML, meta description and blog index updated). Commit `b8daf2e`.
- **(S33) Front C verified Done.** No change needed; all fourteen DSM_6.0 §1.x heading texts compared against `content/about.md`.
- **(S33) Front F shipped.** Portfolio notification written to `_inbox/2026-07-31_dsm-blog-poster_dsm-v1.19-release.md`.
- **(S33) Stage 2 closed.** Fronts A, D, E remain.

### Carried forward, not owned by this BL

Two DSM Central defects were found while running Stage 0/1 and are filed in `dsm-docs/feedback-to-dsm/2026-07-30_ugrep-shim-breaks-dsm-go-baseline-checksums.md`, **pending push**: the ugrep shim silently emptying `/dsm-go` Step 5 baseline checksums, and the `## [vX.Y.Z]` CHANGELOG heading spec that never matches the real format, which defeats Step 1.8's conditional-align optimization. Neither belongs to this cycle's fronts; both were surfaced by it.
