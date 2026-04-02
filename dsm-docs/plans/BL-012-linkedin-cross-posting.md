# BL-012: LinkedIn Cross-Posting Automation

**Created:** 2026-04-02 (Session 13)
**Priority:** Medium
**Trigger:** When next blog post is ready to publish

## Description

Set up an automated pipeline to cross-post blog content to LinkedIn personal profile when new posts are published on take-ai-bite.com.

## Proposed approach

Semi-automated with human review (Buffer scheduling):
1. Hugo generates RSS feed at take-ai-bite.com/index.xml
2. Buffer picks up new entries and creates a draft LinkedIn post
3. Author reviews the draft, edits the text for LinkedIn tone, adds an image if needed, then approves
4. Buffer publishes on approval

This keeps the per-turn review model: no content goes to LinkedIn without human judgment on the final text.

Upgrade path (if custom formatting needed later):
- LinkedIn API via GitHub Actions using `w_member_social` OAuth scope
- Pain point: access tokens expire every 60 days, refresh tokens every 365 days
- Would allow richer formatting and programmatic image attachment

## Known limitations

1. **Humanizer gap.** RSS pulls the Hugo `description` field as LinkedIn text. The blog post is humanized, the LinkedIn summary is not unless manually edited during review.
2. **Plain text only.** LinkedIn supports rich formatting (bold, lists); RSS descriptions are plain text. Custom formatting requires manual editing in Buffer.
3. **No image control.** RSS may not carry the featured image reliably. Images must be added manually in Buffer during review.
4. **Polling delay.** Buffer does not poll RSS in real time. Hours can pass between publishing and the draft appearing in Buffer.
5. **Free tier ceiling.** 3 channels, 10 scheduled posts. Fine for current volume, but adding more platforms hits the limit.

## Success criteria

- [ ] Buffer account connected to LinkedIn personal profile
- [ ] RSS feed monitored by Buffer
- [ ] Draft review workflow tested (Buffer draft -> manual edit -> approve -> publish)
- [ ] Test post published to LinkedIn from a new blog entry
- [ ] Workflow documented in dsm-docs/content-operations.md

## Notes

- Buffer free tier: 3 channels, 10 scheduled posts (sufficient for current volume)
- Alternative: Zapier (RSS trigger -> LinkedIn action), but free tier more limited
- Consider adding a `linkedin_summary` field to Hugo frontmatter for posts, pre-humanized for LinkedIn use