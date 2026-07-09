# BL-025: DSM v1.10-v1.14 cumulative release coverage (multi-front)

**Status:** Open
**Priority:** High
**Date Created:** 2026-05-28 (Session 23)
**Source:** S23 inbox triage (3 entries: `_inbox/2026-05-31_dsm-central-v1.12-smoke-tests.md`, `_inbox/agentic-ai-data-science-methodology.md`, `_inbox/IronCalc.md` is unrelated to this BL).
**Origin:** DSM shipped five minor versions (v1.10.0 through v1.14.0) between 2026-05-29 and 2026-06-01 while this project was finishing the v1.5-v1.9 coverage cycle (BL-022). The BL-022 pattern is to formalize a fresh cycle per version-range rather than retrofit the prior one.

## Pipeline reference

Follows the 6-stage Version Release Coverage pipeline in CLAUDE.md ("Detect → Open BL → Ship factual updates → Write release post → Cross-post and record → Close").

## Stage 0/1 deltas (verified S23)

Verification commands run 2026-05-28:

- **Feature count drift:** 7. Current `~/dsm-agentic-ai-data-science-methodology/FEATURES.md` = 136 entries. `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` claims 129. New entries: F-130 through F-136.
- **Principle count drift:** 1. Current `DSM_6.0` = 13 principles. `content/about.md` claims "The Twelve Principles". New: §1.13 "Introduce Once, Then Deepen" (F-135).

## Version range and feature inventory

| Version | Date | Notable F-entries |
|---------|------|------------------|
| v1.10.0 | 2026-05-29 | TBD (verify against CHANGELOG; likely includes pre-F-130 features that did not generate spoke notifications) |
| v1.11.0 | 2026-05-31 | F-130 (transcript replace_all guard), F-131 (wrap-up Step 0.5 pre-confirms cross-repo targets) |
| v1.12.0 | 2026-05-31 | F-132 (collision-safe dated inbox-done filenames), F-133 (smoke tests as named DSM artifact) |
| v1.13.0 | 2026-06-01 | F-134 (User-Reframes-Proposal Handling sub-rule, DSM_0.2 §8.0.1) |
| v1.14.0 | 2026-06-01 | F-135 (Introduce Once, Then Deepen, DSM_6.0 §1.13) |

Per-version mapping above is provisional, validate by reading CHANGELOG.md sections at drafting time. Same-day version bumps (v1.11+v1.12 on 2026-05-31; v1.13+v1.14 on 2026-06-01) are candidates for bundling per the CLAUDE.md rule "same-day version bumps are treated as one release in the post".

## Dependencies and ordering

- **BL-022 (v1.5-v1.9) blocks this BL's Stage 3.** Release-post work should land for v1.5-v1.9 before drafting v1.10-v1.14 release post(s), so the reader sees the methodology arc in order.
- **Stage 2 (factual updates) does NOT block on BL-022.** Features post count + About principle list are simple corrections that should land in the same session as Stage 1 per CLAUDE.md, even if Stage 3 waits. Skipping Stage 2 lets drift compound.

## Fronts (the checklist, BL-022 structure)

### Front A: Release blog post(s)

Story-shaped post(s) following the 5-part structure (Hook, Insight, Fix, Bonus, Takeaway). Bundling decision at Gate 1 of chunked drafting:
- 1 bundled post covering v1.10-v1.14 (cheapest).
- 2 posts split by same-day clusters (v1.11+v1.12 as one cluster, v1.13+v1.14 as another).
- 5 separate posts (most thorough, likely overkill given small per-version footprints).

Reconstruction trail per CLAUDE.md pipeline Stage 3 mandatory reading order.

**Blocked on:** BL-022 Front A completion.

**Update (S29):** v1.10-v1.17 split by theme (not BL range) into two posts. **Post A** (v1.10-v1.12 guardrails cluster, F-129..F-132) is **PUBLISHED (2026-07-06)**: "How Take AI Bite builds its own guardrails", https://take-ai-bite.com/blog/2026-07-06-tab-safe-defaults-release/ (PR #52). Post A covers this BL's F-130/F-131/F-132 (plus F-129 from BL-027's carry-over). The v1.13-v1.14 features from this BL's range (F-134 User-Reframes-Proposal, F-135 Introduce Once) belong to **Post B** (v1.13-v1.17 cluster), still pending. Front E LinkedIn for Post A pending. Sequencing + closure tracked in BL-027 (which absorbs this BL's remaining fronts).

### Front B: Features post update

`content/blog/2026-03-20-dsm-features-three-dimensions/index.md`. Count update 129 → 136 (verify before publishing). Weave F-130 through F-136 into the three dimensions as integrations, not a list.

Provisional mapping (validate during drafting):
- **Human Oversight:** F-130 (transcript replace_all guard), F-131 (cross-repo target pre-confirm), F-132 (collision-safe inbox-done filenames). All three are structural-enforcement hardenings on the wrap-up / transcript / inbox infrastructure.
- **Knowledge Provenance:** F-133 (smoke tests as named DSM artifact), F-135 (Introduce Once Then Deepen). Both name and locate a practice that already existed; classic DSM "name the industry-standard practice, give it a repo home" pattern.
- **Experience Accumulation:** F-134 (User-Reframes-Proposal Handling). Pattern promoted from reasoning lessons across six recurrences, exactly the experience-into-protocol thread.

### Front C: About page principle list

**Status: Done (2026-06-08, S24)** — verified live at take-ai-bite.com/about/ (deployed via PR #37). "The Thirteen Principles" heading + §1.13 "Introduce Once, Then Deepen" added in the matching tagline style; wording verified against DSM_6.0 §1.13. Bundled with the IronCalc post deploy.

`content/about.md`. "The Twelve Principles" → "The Thirteen Principles". Add §1.13 "Introduce Once, Then Deepen" to the numbered list, in the tagline style matching the existing 12. Verify wording against DSM_6.0 §1.13 before committing.

### Front D: linkedin-posts.md canonical record

After each LinkedIn post in Front E publishes, record its URL and "Status: Published" in `dsm-docs/blog/linkedin-posts.md`. Triggers cross-repo write only if pushing to ecosystem inboxes.

### Front E: LinkedIn cross-post(s)

One LinkedIn post per release blog post produced in Front A. 250-400 words, first-person, hashtags, "Full post:" link. /humanizer pre-publish gate. Hashtag selection method per BL-023 if landed in time.

**Blocked on:** Front A.

### Front F: dsm-portfolio inbox notification

Write to `~/dsm-data-science-portfolio-working-folder/_inbox/YYYY-MM-DD_dsm-blog-poster_dsm-v1.10-v1.14-release.md` with summary and links to released posts. Triggers cross-repo write confirmation gate.

## Stage 2 same-session opportunity

Stage 2 fronts (B + C + F) are the cheap "stop the bleeding" updates. Per CLAUDE.md pipeline, ship Stage 2 in the same session as Stage 1 when time permits. S23 has Stage 1 done (this BL); Stage 2 decision is for the next user turn.

## Out of scope

- BL-022 work (v1.5-v1.9, still in progress).
- BL-024 (IronCalc post) and BL-026 (if filed for IronCalc story): unrelated source threads.
- F-133 (smoke tests) as a standalone blog post: the inbox entry flagged it as a strong candidate ("name the industry-standard practice, give it a repo home"), but it belongs in the release post under Knowledge Provenance, not a standalone. If the release-post weaving compresses it too much and the standalone angle remains compelling, file a separate BL at that time.
- F-134 (User-Reframes-Proposal) as standalone: same reasoning. Strong human-AI collaboration angle ("the principle existed for four months but the behavior still failed six times"), but the release post is the right home in the current cycle.

## Success criteria

Identical to BL-022: all six fronts marked Done or explicitly Deferred with a recorded reason. Move BL to `done/` on closure.
