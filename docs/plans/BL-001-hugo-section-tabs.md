# Separate content sections with nav tabs

**Created:** 2026-03-12 (Session 6)
**Priority:** Medium
**Trigger:** When non-DSM project blog posts are ready to publish

## Description

Split `content/blog/` into separate Hugo content sections to distinguish DSM ecosystem posts from other project posts. Each section gets its own nav tab, list page, and RSS feed.

**Current state:** All posts live under `content/blog/`.

**Target structure:**
```
content/dsm/          # DSM ecosystem posts (Central, Graph Explorer, blog-poster, etc.)
content/projects/     # Non-DSM projects (from ~/\_projects/)
```

**Changes required:**
- Create `content/dsm/` and `content/projects/` sections
- Move existing posts to `content/dsm/`
- Add menu entries in `hugo.toml` for both sections
- Update or remove the current `blog` menu entry
- Verify tags/categories still work across sections
- Check that archives and search cover both sections
- Update any internal cross-links between posts

**Considerations:**
- URL structure changes (e.g., `/blog/take-a-bite/` becomes `/dsm/take-a-bite/`). May need Hugo aliases for redirects if posts are already indexed.
- PaperMod supports multiple sections natively.
- The homepage `mainSections` param may need updating to show posts from both sections.