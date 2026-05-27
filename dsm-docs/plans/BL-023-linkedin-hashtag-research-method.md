# BL-023: LinkedIn hashtag research method

**Status:** Open
**Priority:** Medium
**Date Created:** 2026-05-12 (Session 22)
**Source:** User direction in S22 after switching the standard hashtag set from `#DSM` to `#Leadership` for Fragment 3 of the PM post LinkedIn series (BL-020). The switch was driven by intuition; this BL replaces the intuition with a method.
**Origin:** Posts 1-9 of `dsm-docs/blog/linkedin-posts.md` use a hand-picked set of 4-5 hashtags. None of those choices are grounded in reach data. The series is now eight posts deep with no measurement of which tags actually broaden the audience.

## Problem statement

The blog-poster project publishes a LinkedIn post for every release blog post and (since BL-020) for every fragment of long-form post series. The standard hashtag set evolved by intuition: `#ProjectManagement #PMP #HumanAICollaboration #DSM #TakeAIBite` was the working set through Post 9; from Fragment 3 of the PM series onward it became `#ProjectManagement #PMP #HumanAICollaboration #Leadership #TakeAIBite`. The swap was a guess that `#Leadership` reaches a broader audience than `#DSM`. The guess might be right; it is currently unverified.

Two related gaps:

1. **No data behind the choice.** LinkedIn surfaces an estimated audience size and recent post volume for any hashtag on hashtag search, but we have never collected it. We do not know whether `#Leadership` is 10x the volume of `#DSM` or 1000x. We do not know whether high-volume hashtags actually correlate with higher reach for our specific posts (high volume + low engagement is a real failure mode).
2. **No audience model.** "Top-ranking hashtags" depends on which audience the post is trying to reach. A PM-credentialing audience and an AI-research audience overlap but are not identical. Optimizing for one starves the other. A method has to name the target audience for each post type before it can recommend tags.

## Out of scope for this BL

- **Building automation.** The deliverable here is a method (a documented procedure), not a script or tool. A separate BL can wire any executable parts later.
- **Doing the research for the existing posts.** Once the method exists, the next BL can apply it. BL-023's deliverable is the method itself.
- **Other social platforms.** LinkedIn only. Mastodon, Bluesky, X cross-posting are separate concerns.

## Deliverables

1. A short research-design document (1-3 pages) at `dsm-docs/research/2026-MM-DD_linkedin-hashtag-method.md` covering:
   - **Audience segmentation:** the 2-4 distinct audiences this project's LinkedIn posts target (e.g., PM practitioners, AI engineers, methodology authors, technical leadership).
   - **Tag pool sourcing:** where candidate tags come from (LinkedIn search, competitor profiles, industry articles, tag-discovery tools).
   - **Ranking signal(s):** what makes a tag "top-ranking" for our purposes (raw follower count, recent-post volume, engagement-to-volume ratio, audience overlap with our target segment).
   - **Selection rule:** given a candidate pool and ranking signal(s), how many tags per post, what mix (broad + narrow + brand), how the brand tag (`#TakeAIBite`) is preserved.
   - **Measurement plan:** what we will track on published posts to validate or refute the method (impressions, click-through to the blog, profile views, follower delta).
2. A pointer in `dsm-docs/blog/linkedin-posts.md` to the research file once it lands, so the next post drafter knows where the rule lives.

## Open questions to address during drafting

- Is LinkedIn's published hashtag follower count the right signal, or is it gameable / outdated?
- Should the method recommend tag rotation (different tag sets across posts in a series) or consistency (same set across the series for brand recognition)?
- How does the method handle a post that legitimately targets a new audience (e.g., a release post about DSM tooling vs a leadership-framed PM post)?
- Are there tools (Shield, Taplio, AuthoredUp) worth a paid trial, or is manual research enough at this volume?

## Success criteria

1. The research file exists with all five components above.
2. The method is concrete enough that someone other than the author can apply it to a new post and produce a defensible hashtag set.
3. At least one published LinkedIn post is drafted using the method, with the resulting tag choices documented in `linkedin-posts.md` alongside the standard fields.
4. A measurement note is added to the post entry so a follow-up review (3-4 weeks later) can compare against the prior intuition-driven baseline.

## Notes

- This is research-design work, not research execution. The execution (applying the method to existing or future posts) is a follow-up BL.
- The method should be lightweight. The LinkedIn cross-post is a side artifact of blog publishing; we want a 10-minute procedure, not a 2-hour data-collection ritual per post.
- Pair this BL with a calendar reminder roughly one month after the method ships, to actually look at the LinkedIn analytics on the posts that used it. Otherwise we replace an unmeasured intuition with an unmeasured method.
