# BL-026: IronCalc ACCRINT contribution arc blog post

**Status:** Done (published 2026-06-08, Session 24)
**Priority:** Medium
**Date Created:** 2026-05-28 (Session 23)
**Source:** `~/dsm-external-contribution-storage/IronCalc/dsm-docs/blog/2026-06-02_accrint-accrintm-story.md` (when complete; currently in section-by-section drafting upstream).
**Origin:** `_inbox/done/2026-06-02_IronCalc.md` (S23 triage). Spoke is drafting a long-form engineering story about contributing ACCRINTM and ACCRINT to IronCalc (open-source Rust spreadsheet engine).
**Trigger:** When the source draft completes upstream. Spoke notification will arrive when ready.

## Outcome (2026-06-08, Session 24)

**Done.** Published on take-ai-bite.com as a single long-form piece (candidate C of IronCalc BL-007's A/B/C set).

- **Live URL:** https://take-ai-bite.com/blog/2026-06-03-ironcalc-accrint-story/ (verified live: title, body, blog index, "hold together over weeks" edit all present)
- **Category:** Engineering. ~3,800 words. Deployed via PR #37 (merge to main, 2026-06-08).

**Scope questions resolved:**
1. **Venue:** take-ai-bite.com under "Engineering" (single venue; candidates B and A will cross-link internally per IronCalc BL-007).
2. **Voice:** recast in take-ai-bite.com voice with the TAB/DSM rule applied (no standalone "DSM" noun; "the versioned methodology"). Humanizer gate passed (line-84 single-thing TAB reframe).
3. **LinkedIn extract:** Post 16 pending/optional (hashtags likely #Rust #OpenSource #HumanAICollaboration).

**Ordering note:** the recorded soft dependency ("BL-022 Stage 3 should land first") was consciously bypassed by user decision in S24 to publish C this session. BL-022 Post 2 (v1.9 "Slip-catching") remains pending.

**Cross-spoke follow-up (pending):** IronCalc BL-007 (EC governance repo) needs candidate C marked published + URL recorded, and the IronCalc spoke notified to move its source draft (`2026-06-02_accrint-accrintm-story.md`) to done/.

## Problem statement

The IronCalc spoke is preparing a ~3750 word, 6-section public-blog story about a Rust OSS contribution arc: ACCRINTM (PR #865, the warm-up) and ACCRINT (PR #1077 merged 2026-06-01, merge commit `90066e06`, the hard climb). The narrative spine is "reproducibility as the throughline": source-anchored research (Mayle SSCM lineage, Microsoft DAX spec), a multi-period quasi-coupon algorithm, an odd-long-first-coupon day-count subtlety reverse-engineered against an Excel oracle, an end-of-month divergence between DAX-documented spec and shipping Excel with no derivable rule, a public GitHub discussion that surfaced the divergence with reproducible evidence, and the maintainer's recorded decision.

This is not blog-poster source material in the same sense as DSM-spoke entries (it is targeted at a *public dev blog*, audience Rust / OSS contributors, not the take-ai-bite.com methodology audience). The triage choice is: does the blog-poster pipeline take it, or does it stay on the IronCalc spoke's own publication track?

## Open scope questions (resolve when source is ready)

1. **Distribution venue.** Take-ai-bite.com is methodology-positioned; this is engineering-positioned. Either (a) publish on take-ai-bite.com as a "deep work" tag piece, (b) publish standalone on a separate dev-blog venue, or (c) leave with IronCalc's own pipeline.
2. **LinkedIn extract.** If a take-ai-bite.com version ships, a LinkedIn cross-post (Post 16+) is the natural extension. Hashtag set TBD (likely #Rust #OpenSource not the PM-series #ProjectManagement set).
3. **Voice constraint.** The source enforces provenance-clean voice (no DSM session numbers, no decision IDs, no internal file paths; Microsoft sources and public GitHub URLs only). The blog-poster pipeline's voice calibration is a different register; need to decide whether to keep the provenance-clean voice or re-cast in take-ai-bite.com voice.

## Reconstruction trail (when source is ready)

Primary: `~/dsm-external-contribution-storage/IronCalc/dsm-docs/blog/2026-06-02_accrint-accrintm-story.md`

Public reference points (all citable, already noted in source):
- ACCRINT PR: https://github.com/ironcalc/IronCalc/pull/1077
- D6 design discussion: https://github.com/ironcalc/IronCalc/discussions/1076
- ACCRINTM PR: https://github.com/ironcalc/IronCalc/pull/865

## Dependencies

- BL-022 Stage 3 should land first (existing release coverage owes the audience the v1.5-v1.9 story before introducing an off-topic engineering piece).
- BL-024 (Haystack OSS arc) is a sibling. If both run, the order is BL-024 first (smaller scope, ready source) then BL-026 (waiting on upstream drafting).

## Success criteria (placeholder)

Defer to when source is ready and scope questions above are resolved.
