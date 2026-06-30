# BL-027: DSM v1.15-v1.17 cumulative release coverage (multi-front)

**Status:** Open
**Priority:** High
**Date Created:** 2026-06-30 (Session 27)
**Source:** S27 inbox triage. Entries: `_inbox/2026-06-16_dsm-central-v1.16.0-features.md` (F-137..F-140, count 136 -> 140), `_inbox/dsm-agentic-ai-data-science-methodology.md` (F-141, v1.17.0), `_inbox/2026-06-23_dsm-align-update.md` (alignment v1.14 -> v1.17, informational).
**Origin:** DSM shipped v1.15.0 through v1.17.0 (released through 2026-06-18) while this project was finishing earlier coverage cycles. Per the BL-022/BL-025 pattern, a fresh cycle is formalized per version range rather than retrofitting the prior one.

## Pipeline reference

Follows the 6-stage Version Release Coverage pipeline in CLAUDE.md ("Detect -> Open BL -> Ship factual updates -> Write release post -> Cross-post and record -> Close").

## Stage 0/1 deltas (verified S27)

Verification commands run 2026-06-30:

- **Feature count:** `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` = **142** (numbering is F-000..F-141, 0-indexed, so 142 entries; max index F-141). `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` claims **129**. Drift = **13** (F-129 through F-141).
- **Principle count:** `grep -cE '^### 1\.[0-9]+' DSM_6.0` = **14**. `content/about.md` = "The Fourteen Principles". Drift = **0** (resolved S26, PR #45; §1.14 "Observe Before Engaging" already added).

## Important: absorbs BL-025 Front B

BL-025 (v1.10-v1.14) Front B was scoped 129 -> 136 but **never shipped**, so the features post is still at 129. This BL's Front B therefore covers the full 129 -> 142 span (F-129 through F-141), satisfying **both** BL-025 Front B and BL-027 Front B in one edit. BL-025 Front B is marked Done-by-BL-027 on this BL's completion.

## Version range and feature inventory (the 13 new entries)

| F-entry | Date | Title (short) |
|---------|------|---------------|
| F-129 | 2026-05-31 | Cross-repo writes are write-only (DSM_0.2.C §2) |
| F-130 | 2026-05-31 | Transcript replace_all guard (DSM_0.2 §7) |
| F-131 | 2026-05-31 | /dsm-wrap-up Step 0.5 pre-confirms known cross-repo targets |
| F-132 | 2026-05-31 | Collision-safe dated inbox-done filenames |
| F-133 | 2026-05-31 | Smoke tests as a named DSM artifact (DSM_4.0.A §7) |
| F-134 | 2026-06-01 | User-Reframes-Proposal Handling sub-rule (DSM_0.2 §8.0.1) |
| F-135 | 2026-06-01 | Introduce Once, Then Deepen writing principle (DSM_6.0 §1.13) |
| F-136 | 2026-06-09 | Soft Injection / Frame Capture safety protocol (+ DSM_6.0 §1.14 Observe Before Engaging) |
| F-137 | 2026-06-15 | Voice-Attribution Review for byline content (DSM_0.2.C §2.3) |
| F-138 | 2026-06-15 | Read-Before-Draft for OSS contributions (DSM_0.2.D §9) |
| F-139 | 2026-06-15 | Open-PR CI status surfaced at boot and wrap-up |
| F-140 | 2026-06-15 | STAA reminder logic with crash-recovery off-by-one fix |
| F-141 | 2026-06-18 | Subchapter/paragraph bite + file-first editable delivery (DSM_0.2 §8.10 Gate 3) |

F-129 through F-135 carry over from the BL-025 range (v1.10-v1.14) that Front B never shipped; F-136 through F-141 are the v1.15-v1.17 range proper.

## Dependencies and ordering

- **BL-022 (v1.5-v1.9) and BL-025 (v1.10-v1.14) Stage 3 block this BL's Stage 3.** Release-post work should land in version order so the reader sees the methodology arc in sequence.
- **Stage 2 (factual updates) does NOT block on prior BLs.** The features post count + weave are simple corrections that should land in the same session as Stage 1 per CLAUDE.md, even if Stage 3 waits.

## Fronts (the checklist)

### Front A: Release blog post(s)
Story-shaped post(s) following the 5-part structure (Hook, Insight, Fix, Bonus, Takeaway). Reconstruction trail per CLAUDE.md pipeline Stage 3. **Blocked on:** BL-022 + BL-025 Front A.

### Front B: Features post update
`content/blog/2026-03-20-dsm-features-three-dimensions/index.md`. Count 129 -> 142. Weave F-129 through F-141 into the three dimensions as integrations, not a list. **Status: shipped S27** (see Outcomes). Weaving map:
- **Human Oversight (guardrails grow outward + lifecycle):** F-129 (cross-repo write-only), F-136 (Soft Injection / Frame Capture), F-137 (Voice-Attribution Review), F-132 (collision-safe inbox-done), F-131 (wrap-up cross-repo pre-confirm), F-130 (transcript replace_all guard), F-139 (open-PR CI at boot), F-140 (STAA reminder crash-recovery fix).
- **Knowledge Provenance (name-the-practice / read-the-source):** F-133 (smoke tests as named artifact), F-135 (Introduce Once Then Deepen), F-138 (Read-Before-Draft for OSS, extends the existing Read-the-Manual paragraph).
- **Experience Accumulation (reasoning lessons -> protocol):** F-134 (User-Reframes-Proposal, promoted across six recurrences), F-141 (file-first editable delivery, validated live on a 4-part blog series).

### Front C: About page principle list
**Status: Done (2026-06-24, S26, PR #45)** — About at "The Fourteen Principles"; §1.14 "Observe Before Engaging" added, verified against DSM_6.0 §1.14. No drift remaining.

### Front D: linkedin-posts.md canonical record
After each LinkedIn post in Front E publishes, record URL + "Status: Published". **Blocked on:** Front E.

### Front E: LinkedIn cross-post(s)
One LinkedIn post per release blog post produced in Front A. 250-400 words, first-person, hashtags, "Full post:" link. /humanizer pre-publish gate. **Blocked on:** Front A.

### Front F: dsm-portfolio inbox notification
**Status: Done (2026-06-30, S27)** — written to `~/dsm-data-science-portfolio-working-folder/_inbox/2026-06-30_dsm-blog-poster_dsm-v1.15-v1.17-release.md` (Stage 2 factual-update notice: features post 142, BL-027 opened, release post pending). Cross-repo write gate cleared (content + path approved, create-only, no git in target per F-129).

## Out of scope

- BL-022 (v1.5-v1.9) and BL-025 (v1.10-v1.14) release-post work (separate cycles, block this Stage 3).
- BL-024 (Haystack), BL-007 (IronCalc): unrelated source threads.
- F-136 / F-141 as standalone posts: strong angles (Frame Capture as "prompt injection wearing a polite hat"; the recursive-irony of F-141 drafted with the old chat-block model) but they belong in the release post; file a separate BL only if the weaving compresses them too much and the standalone angle stays compelling.

## Success criteria

All six fronts marked Done or explicitly Deferred with a recorded reason. Move BL to `done/` on closure. On closure, also move BL-025 to `done/` (its Front B satisfied here) if its remaining fronts are resolved or deferred.

## Stage status (S27)

- **Stage 0/1:** Done. Drift recorded (features 129 -> 142; principles 14 = 14).
- **Stage 2:** Done. Front B shipped, Front C already done (S26), Front F shipped.
- **Stage 3 (Front A) + Stage 4 (Fronts D/E):** pending, blocked on BL-022 + BL-025 release-post sequencing.

## Outcomes

- (S27) Front B shipped: features post 129 -> 142, F-129..F-141 woven tight across the three dimensions; humanizer pass (1 fix), hugo build clean. Commit / PR: TBD.
- (S27) Front F shipped: portfolio inbox notification written.
- (S27) Front C confirmed already done (S26, PR #45).
