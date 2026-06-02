# BL-024: "Investigation-first" blog post + LinkedIn cross-post (Haystack OSS arc)

**Status:** Open
**Priority:** Medium
**Date Created:** 2026-05-28 (Session 23)
**Source:** `~/_projects/heating-systems-conversational-ai/dsm-docs/blog/journal.md` (entry `### [2026-05-08] Investigation-first: how a code gap became a docs gap`)
**Origin:** `_inbox/done/heating-systems-conversational-ai.md` (S23 triage). Spoke offered the journal entry for blog-poster extraction per the publication notification workflow.
**Trigger:** After BL-022 Stage 3 (DSM v1.5-v1.9 release post) lands.

## Problem statement

The heating-systems-conversational-ai spoke ran a 6-day OSS contribution arc into Haystack: issue #3263 (2026-05-02) to PR #11268 merge (2026-05-08, merge commit `9e0798aa`). The journal entry (66 lines) captures two reframes that shaped the work ("missing feature" -> "missing docs", "Haystack PR" -> "upstream ollama-python issue"), a three-repo reviewer-dynamic contrast (engaged maintainer vs. silent vs. unsponsored), and a load-bearing claim: the investigation is the artifact, not the patch. The patch was ~50 lines of docs and ~10 minutes to write; the investigation was the multi-day work that made it land cleanly. The voice and concrete-artifact density already align with the take-ai-bite.com register. No drafting blocker beyond scheduling.

This is portfolio-resonant content, AI Engineer audience, with a strong thread to TAB's "Earn Your Assertions" principle (read the source before claiming, run the pre-flight). It also extends the existing trainer/PM/PMO post arc with a non-DSM-tooling story: same discipline applied to an external OSS workflow.

## Story angle

"Investigation-first: how a code gap became a docs gap."

Hook: a "missing feature" that turned out to be a missing docs section once the source was read end-to-end. Insight: the patch is small (~50 lines, 10 minutes) and the investigation is large (read 697-line generator, pre-flight the example, scope across three repos). Takeaway: investigation is the artifact that earns the maintainer's attention; the patch is a receipt.

Secondary thread: the three-repo reviewer dynamics (haystack#11268 with engaged maintainer + targeted comments + 1-day merge, haystack-integrations#473 silent, ollama-python#663 open without sponsor) as a concrete example of why same-contribution-different-repo coordination matters.

## Reconstruction trail

Primary source: `~/_projects/heating-systems-conversational-ai/dsm-docs/blog/journal.md` lines 153-218.

Supporting artifacts (linked from the source):
- `deepset-ai/haystack-core-integrations#3263` (original issue)
- `deepset-ai/haystack#11268` (merged PR, the docs patch)
- `deepset-ai/haystack-integrations#473` (landing-page example, still open)
- `ollama/ollama-python#663` (upstream issue, still open)
- Merge commit `9e0798aa`

No additional source reading needed. The journal entry was written with publication in mind (voice constraints from BL-005 Test Plan honored: no volunteer @-mentions, concrete artifact references throughout).

## Candidate structure

1. **Hook (1 paragraph):** the framing collapse. Filed as "Haystack is missing a feature." Reading the chat-generator end-to-end showed the capability already worked. The missing thing was the docs section that would let a reader know.
2. **The pre-flight catch (1 paragraph):** `Tool.from_function` from older docs vs. the real `create_tool_from_function`. Two minutes to catch, public correction avoided.
3. **The split (1-2 paragraphs):** one issue became three PRs in three repos (haystack#11268, haystack-integrations#473, ollama-python#663). Tool-choice peeled off because it belonged in ollama-python, not Haystack. Scoping by where the symbol actually lives.
4. **Three reviewer dynamics (1-2 paragraphs):** engaged-and-fast vs. silent vs. unsponsored. Same contribution, three response cadences. The only way to know which is which is to be in all three.
5. **The DoR audit (1 paragraph):** end-of-session question caught a missing release note + untemplated PR body before maintainer's first read. Discipline applied to the contribution itself.
6. **Takeaway (1 paragraph):** the patch is the receipt, the investigation is the artifact. Six days from filed to merged, ~50 lines of docs, ~10 minutes of patch writing. The other six days were reading 697 lines of generator, running pre-flight against six adversarial prompts, drafting and verifying the behavioral claim.

Target length: 1500-2500 words. Read time ~10-15 min.

## Success criteria

1. One blog post deployed to `https://take-ai-bite.com/blog/YYYY-MM-DD-investigation-first-haystack-arc/` (or similar slug, owner picks at draft time).
2. All concrete artifacts (PR/issue numbers, merge commit, dates, line counts) preserved from the source.
3. "Investigation is the artifact, not the patch" landing as the explicit takeaway, not implicit.
4. Voice calibration from `content/about-me.md` + `content/about.md` before drafting.
5. /humanizer pre-publish gate.
6. LinkedIn cross-post (Post 15 in `dsm-docs/blog/linkedin-posts.md`), 250-400 words, extracts the "investigation-first as credibility" angle. Hashtag set TBD per BL-023 research.
7. Notification back to heating-systems spoke (per Publication Notification Workflow, BL-008) so the source journal entry moves to its done state.

## Out of scope

- Standalone Substack draft (Option 3 in the S23 triage was declined).
- Deep dive into Haystack's chat-generator architecture as a tutorial (would dilute the story shape).
- General OSS contribution guidance (the story is specific to this arc; the takeaway generalizes but the prose stays concrete).

## Dependencies

- BL-022 Stage 3 (DSM v1.5-v1.9 release post) lands first.
- BL-023 (LinkedIn hashtag research) may complete by the time Post 15 is drafted; if so, apply its findings.
