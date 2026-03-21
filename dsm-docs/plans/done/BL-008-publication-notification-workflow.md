# BL-008: Publication Notification Workflow

**Priority:** High
**Source:** Inbox -- 2026-03-21_dsm-central_blog-tracking-collaboration.md
**Trigger:** Next blog post publication

## Description

DSM Central now maintains a blog content tracking index at `dsm-docs/blog/README.md`.
When blog-poster publishes a post, it must send an inbox entry to DSM Central confirming
publication (filename, date, URL).

## Tasks

- [ ] Add publication notification step to `dsm-docs/content-operations.md`
- [ ] Include the entry template from DSM Central
- [ ] Note: LinkedIn is promotion-only (share link), not a separate publication target

## Entry Template

```markdown
### [YYYY-MM-DD] Blog published: {short title}

**Type:** Notification
**Priority:** Low
**Source:** dsm-blog-poster

Published `{filename}` on YYYY-MM-DD.
URL: {blog post URL}
```
