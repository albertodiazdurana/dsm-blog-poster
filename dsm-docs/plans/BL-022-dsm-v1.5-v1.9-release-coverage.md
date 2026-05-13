# BL-022: DSM v1.5-v1.9 cumulative release coverage (multi-front)

**Status:** Open
**Priority:** High
**Date Created:** 2026-05-12 (Session 22)
**Source:** User direction in S22 to bundle the accumulated release work into one BL with a clear front-by-front checklist.
**Origin:** DSM shipped five minor versions (v1.5.0 through v1.9.0) without a release-coverage cycle. Two prior BLs partially addressed the gap (BL-018 for the v1.5/v1.6 release post; BL-021 for the v1.7-v1.9 features-post update) but neither named the full set of artifacts that drift when DSM bumps a version. This BL closes that gap as one piece of work and formalizes the pattern for future version bumps.

## Supersedes

- **BL-021** (Features post update for DSM v1.7-v1.9) , fully absorbed by Front B. Same target file, same count delta (114 to 129), same 14 F-entries.
- **BL-018** (DSM v1.5.x / v1.6.x release post) , absorbed by Front A (release post), Front B (features post update), Front D (linkedin-posts.md record), Front E (LinkedIn cross-post). The v1.5/v1.6 reconstruction trail enumeration (specific BACKLOG-{344,345,372,377,378,379,380,386,402} files) and the candidate story angle ("How DSM learned to bootstrap itself") live in `dsm-docs/plans/done/BL-018-dsm-v1-5-v1-6-release-post.md`; read that file when working Front A for the v1.5/v1.6 cluster.

Both prior BLs were valid scopes; they were too narrow. This BL owns the full cycle.

## Problem statement

A DSM version bump cascades into several artifacts in this project. The cascade is silent unless explicitly tracked: the features post drifts in count, the About page drifts in principle list, the LinkedIn audience loses the thread, the portfolio repo loses awareness, and the canonical "release story" never gets written. Each drift is small in isolation; together they erode the project's authority on a methodology it exists to publish.

Concrete state as of 2026-05-12:

- FEATURES.md is at 129 entries (last blog-side update: S21, at 114).
- DSM_6.0 lists 12 principles (Principle 1.12 "Don't be a Hero, Delegate the Effort" added in v1.7.0); About page still lists 11.
- No release blog post exists for any version since v1.4.5 (published S14, 2026-04-07). v1.5.0 through v1.9.0 are uncovered.
- No LinkedIn cross-post for any release since v1.4.5.
- dsm-portfolio (`~/dsm-data-science-portfolio-working-folder/`) has not received a release notification past v1.4.x.

## Fronts (the checklist)

Six fronts. Each is independent; each must be either delivered or explicitly deferred with a reason.

### Front A: Release blog post(s)

Write a story-shaped release post following the existing CLAUDE.md structure (Hook, Insight, Fix, Bonus, Takeaway). User decision at drafting time: one post bundling v1.5-v1.9, or two posts split by narrative cluster (v1.5/v1.6 "DSM learns to bootstrap itself" + v1.7-v1.9 "DSM learns to police itself"). Bundled is cheaper; split is honester to the actual narrative arcs. Recommendation: split.

Reconstruction trail per CLAUDE.md DSM Version Release Coverage. Primary source for v1.7-v1.9 is the consolidated inbox entry now at `_inbox/done/2026-05-12_dsm-central-v1.7-v1.9-features.md`, which carries the full F-entry / BL / DSM-ref / story-angle table.

### Front B: Features post update

`content/blog/2026-03-20-dsm-features-three-dimensions/index.md`. Count update 114 to 129 (verify with `grep -cE '^- \*\*F-[0-9]+' ~/dsm-agentic-ai-data-science-methodology/FEATURES.md` before publishing). Weave the 14 new F-entries (F-115 through F-128) into the three dimensions as one-to-two-sentence integrations, not a list. Provisional dimension mapping is in the consolidated inbox entry; validate during drafting.

### Front C: About page

`content/about.md`. Change "The Eleven Principles" heading to "The Twelve Principles." Add Principle 12 to the list: **Don't be a Hero, Delegate the Effort** -- (one-line description matching the rhythm of the other 11; suggested: "Use parallel subagents when the work has independent threads, with explicit per-task user approval.") Verify the principle's wording against DSM_6.0 §1.12 before committing.

### Front D: linkedin-posts.md canonical record

`dsm-docs/blog/linkedin-posts.md`. For each LinkedIn post produced in Front E, append a Post N entry following the existing schema (URL, Status, Blog post link, Text body, hashtags). One entry per published LinkedIn post.

### Front E: LinkedIn cross-post

One LinkedIn post per release blog post produced in Front A. If Front A produces one post, Front E produces one. If Front A splits into two, Front E produces two. Each follows the existing series pattern (250 to 400 words, first-person, hashtags, "Full post:" link). /humanizer gate before publishing.

### Front F: dsm-portfolio inbox notification

Write a cross-repo notification to `~/dsm-data-science-portfolio-working-folder/_inbox/`. Filename: `YYYY-MM-DD_dsm-blog-poster_dsm-v1.5-v1.9-release.md`. Content: short summary of the release, link to the published release blog post(s), call out any portfolio-relevant features. Triggers the cross-repo write confirmation gate (first cross-repo write of this session to dsm-portfolio).

## Checklist

Tick items as they complete. Each front is independent unless noted.

### Front A , Release blog post(s)

- [ ] Decide bundling: one post for v1.5-v1.9, or two posts (v1.5/v1.6 cluster + v1.7-v1.9 cluster). Recommendation: two.
- [ ] Read the v1.5/v1.6 reconstruction trail in `dsm-docs/plans/done/BL-018-dsm-v1-5-v1-6-release-post.md` (specific BL files + candidate story angle "How DSM learned to bootstrap itself").
- [ ] Read the v1.7-v1.9 reconstruction trail in `_inbox/done/2026-05-12_dsm-central-v1.7-v1.9-features.md` (consolidated F-entry / BL / story-angle table).
- [ ] Read CHANGELOG entries in DSM Central between v1.5.0 and v1.9.0.
- [ ] Read reasoning lessons (`.claude/reasoning-lessons.md`) for v1.5-v1.9 [auto]/[STAA] entries.
- [ ] Draft outline (Gate 2: TOC with per-section length budgets).
- [ ] Draft post (chunked, one section at a time per Gate 3).
- [ ] Voice calibration check against `content/about-me.md` + `content/about.md`.
- [ ] /humanizer pre-publish gate.
- [ ] User review of full assembled post(s) (Gate 4).
- [ ] Publish to `content/blog/YYYY-MM-DD-dsm-vX-release/index.md`.
- [ ] Record published URL(s) in this BL's "Outcomes" section below.

### Front B , Features post update (count and weaving)

- [x] Verify current count: `grep -cE '^- \*\*F-[0-9]+' ~/dsm-agentic-ai-data-science-methodology/FEATURES.md`. Target: whatever this returns (currently 129).
- [x] Update title in `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` from "114" to current count.
- [x] Update description in front matter.
- [x] Update opening and closing paragraphs (six occurrences of "114" total per grep).
- [x] Weave F-115/F-126/F-128/F-127 into Human Oversight section (provisional; validate during drafting).
- [x] Weave F-118/F-119/F-120/F-121/F-125/F-123 into Knowledge Provenance section.
- [x] Weave F-116/F-117/F-122/F-124 into Experience Accumulation section.
- [x] /humanizer pre-publish gate.
- [x] User review.
- [x] Publish (commit + push, Hugo rebuild).

### Front C , About page principle list

- [x] Verify current principle count in DSM_6.0: `grep -cE '^### 1\.[0-9]+' ~/dsm-agentic-ai-data-science-methodology/DSM_6.0_AI_Collaboration_Principles_v1.0.md`. Currently 12.
- [x] Change `content/about.md` heading from "The Eleven Principles" to "The Twelve Principles."
- [x] Add Principle 12: **Don't be a Hero, Delegate the Effort** -- {one-line description matching the rhythm of the other 11; verify wording against DSM_6.0 §1.12 before committing}.
- [x] /humanizer pre-publish gate (light, one-line addition).
- [x] User review.
- [x] Publish.

### Front D , linkedin-posts.md canonical record

- [ ] For each LinkedIn post published in Front E, append a Post N entry to `dsm-docs/blog/linkedin-posts.md` following the existing schema (URL, Status, Blog post link, Text body, hashtags).

### Front E , LinkedIn cross-post(s)

- [ ] Draft one LinkedIn post per release blog post produced in Front A (250-400 words, first-person, hashtags, "Full post:" link).
- [ ] /humanizer pre-publish gate per LinkedIn post.
- [ ] User review per LinkedIn post.
- [ ] Publish on LinkedIn.
- [ ] Record published URL(s) in this BL's "Outcomes" section below.

### Front F , dsm-portfolio inbox notification

- [x] Draft notification file content: short summary of the release(s), links to published release blog post(s), call out portfolio-relevant features.
- [x] Confirm cross-repo write gate (first cross-repo write to dsm-portfolio this session).
- [x] Write to `~/dsm-data-science-portfolio-working-folder/_inbox/YYYY-MM-DD_dsm-blog-poster_dsm-v1.5-v1.9-release.md`.
- [x] Note delivery in this BL's "Outcomes" section.

### Closure

- [ ] All 6 fronts marked complete OR explicitly deferred with reason recorded in "Outcomes" below.
- [ ] CLAUDE.md "DSM Version Release Coverage" section verified up to date with the 6-front pattern (already done as part of BL-022 creation, but re-check on closure).
- [ ] Move BL-022 to `dsm-docs/plans/done/` with Date Completed.

## Outcomes

(Fill in as fronts complete.)

- Front A published URL(s): (deferred to next session)
- Front B published commit: Session 22 (2026-05-12); features post moved 114 to 129, 14 F-entries woven, humanized, committed and pushed on `session-22/2026-05-12` branch.
- Front C published commit: Session 22 (2026-05-12); About page moved to "The Twelve Principles" with Principle 12 added, committed on same branch.
- Front E LinkedIn URL(s): (pending Front A)
- Front F notification delivered: 2026-05-12 to `~/dsm-data-science-portfolio-working-folder/_inbox/2026-05-12_dsm-blog-poster_dsm-v1.5-v1.9-features-update.md`.
- Deferrals: Front A (release blog post), Front D, Front E all deferred to the next session per user direction at S22 end. Stage 3 of the pipeline picks up there.

## Success criteria

1. All 6 fronts either delivered or explicitly deferred (with reason recorded in this BL).
2. Features post count update verified by `grep -c` immediately before publishing, not from memory.
3. About page reflects the actual DSM_6.0 principle count and the new principle's wording.
4. At least one release blog post published; LinkedIn cross-post(s) recorded in linkedin-posts.md.
5. dsm-portfolio inbox notification delivered.
6. CLAUDE.md "DSM Version Release Coverage" section updated to formalize the 6-front pattern, so the next version bump has the checklist as a load-bearing rule (not a one-time scope decision).

## Out of scope

- Reconstruction of v1.0-v1.4 coverage (those releases were covered in their own time).
- Splitting the LinkedIn release post(s) into series fragments. Series treatment is reserved for the long-form posts (PM post, BL-020). Release posts get one LinkedIn post each unless the user calls otherwise.
- Adding a release-coverage automation script. The pattern can be a checklist for now; tool support comes later if the cadence justifies it.

## Workflow note

Fronts are independent and can be parallelized across sessions:

- B and C are small ground-truth updates and can ship on their own (the count is wrong NOW; the About principle list is wrong NOW). They do not need to wait for A.
- A is the heavy creative front and likely takes its own session(s).
- D and E follow A.
- F is small and can ship with B or with A.

Suggested order: B + C + F together (small, factual, ship today) → A → E → D.

## Future-proofing

Front-by-front pattern is formalized in CLAUDE.md "DSM Version Release Coverage" after this BL is approved. The next DSM version bump should produce the same 6-front BL automatically. If a front becomes consistently empty across versions (e.g., About page never changes for most version bumps), the formalization can mark it conditional rather than mandatory.
