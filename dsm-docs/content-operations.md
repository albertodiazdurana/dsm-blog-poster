# Content Operations Guide

This document defines the content operations scope and practices for the DSM Blog Poster project. It serves as a reference for the agent and the project owner when creating, publishing, and distributing public-facing content.

## Role Definition

This project operates in the role of **Content Operations Lead** for the Take AI Bite brand. In a company context, this maps to a Content Manager or Digital Content Strategist -- responsible for the full content lifecycle:

1. **Creation** -- Writing blog posts, generating images, crafting social media copy
2. **Legal clearance** -- Verifying licensing, attribution, and platform compliance
3. **Publishing** -- Hugo site builds, deployment, SEO, OpenGraph
4. **Distribution** -- LinkedIn posting, cross-platform repurposing, link management
5. **Analytics** -- Tracking engagement, impressions, reach (future)

## Legal and Licensing

### AI-Generated Assets

Before using any AI-generated content (images, code, text) in public-facing deliverables:

1. **Check licensing terms** for the specific tool and tier being used
2. **Document** the tool, tier, date, and licensing status alongside the asset
3. **Flag high-risk scenarios:** free tiers that retain ownership, public gallery clauses, tools with post-date policy changes

**Vetted tools for image generation (free tier, commercial rights):**

| Tool | Commercial Rights | Trade-off |
|------|------------------|-----------|
| Ideogram | Yes, no ownership claim | Public gallery |
| Leonardo.ai | Yes, non-exclusive royalty-free | Public feed, 150 tokens/day |
| DeepAI | Yes, 100% retained | Lower quality |

**Tools to avoid on free tier:**

| Tool | Issue |
|------|-------|
| Recraft AI | Free tier: no commercial rights, images are Recraft's property (post 2024-08-12) |

Full research: `dsm-docs/research/2026-03-09_ai-asset-licensing-research.md`

### Platform Terms of Service

When publishing to external platforms, verify:
- Content meets platform ToS (LinkedIn, GitHub)
- No copyrighted material used without permission
- Attribution provided where required

## Asset Management

### Logo

- **Source of truth:** `dsm-docs/assets/logo_cropped.png` (516x516, cropped)
- **Original source:** `dsm-docs/assets/cute-robot-with-cookie-no-legs-no-mouth.webp` (1024x1024, Ideogram)
- **Derived files in static/:** `logo.png` (1024x1024), `apple-touch-icon.png` (180x180), `favicon.ico` (32x32)
- **History:** `dsm-docs/logo-creation.md`

Other repos needing the logo copy from `dsm-docs/assets/logo_cropped.png` and derive sizes locally.

### Image Pipeline

When adding new images to the site:
1. Store source file in `dsm-docs/assets/`
2. Derive size-specific files using Pillow (Python)
3. Place Hugo-served files in `static/`
4. Document provenance (tool, licensing) in relevant docs

## Distribution Channels

### Blog (take-ai-bite.com)

- Hugo static site, Anatole theme
- Deployed via GitHub Actions on push to main
- OpenGraph image: `static/logo.png`
- Content in `content/blog/YYYY-MM-DD-slug/index.md`

### LinkedIn

- Cross-post blog content with adapted copy (conversational, not just a link dump)
- Preview images are cached at share time -- cannot be updated retroactively
- Use LinkedIn Post Inspector to verify/refresh cached previews before sharing
- Featured section links can be refreshed by removing and re-adding them
- First post: https://www.linkedin.com/posts/albertodiazdurana_take-ai-bite-activity-7436142360511717376-lWF7

### GitHub

- Blog source: https://github.com/albertodiazdurana/dsm-blog-poster
- Public DSM principles: https://github.com/albertodiazdurana/take-ai-bite

## Lessons Learned

| Date | Lesson | Reference |
|------|--------|-----------|
| 2026-03-09 | Always verify AI tool licensing before deploying generated assets publicly | `dsm-docs/research/2026-03-09_ai-asset-licensing-research.md` |
| 2026-03-09 | LinkedIn caches preview images at share time; old posts cannot be updated | S4 session |
| 2026-03-09 | Crop whitespace from logos before deploying -- small favicons need tight framing | `dsm-docs/logo-creation.md` |