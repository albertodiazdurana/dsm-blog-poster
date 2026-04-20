# Expose category filtering as a navbar dropdown

**Created:** 2026-03-12 (Session 6), reframed 2026-04-14 (Session 20)
**Priority:** Medium
**Trigger:** Now (S20 implementation)

## Description

Posts already use a `categories` taxonomy, and Hugo auto-generates `/categories/{name}/` pages that filter posts by category. The feature works on click but is not discoverable from the header. Users cannot tell that filtering exists without first visiting a post and clicking its category badge.

Add a "Categories" dropdown to the top-right of the navbar that lists all categories alphabetically. Each entry links to the corresponding `/categories/{name}/` page. A "Browse all" item at the top of the dropdown links to `/categories/`.

Move the theme switcher from the top-right to the far left of the navbar so the new dropdown sits where users expect filter controls.

## Original framing (superseded)

The original BL-001 proposed splitting `content/blog/` into separate Hugo sections (`content/dsm/`, `content/projects/`) with their own nav tabs. That approach was reframed because the existing taxonomy already provides the filtering capability, just without UI affordance. Adding a dropdown is lower-cost and keeps URLs stable.

## Implementation

1. Override `themes/anatole/layouts/partials/navbar.html` at project level (`layouts/partials/navbar.html`)
2. Add a Categories dropdown to `nav__list--end` using the existing `optionswitch` pattern
3. Source the list dynamically from `site.Taxonomies.categories.Alphabetical`
4. First dropdown child: "Browse all" -> `/categories/`
5. Move theme switcher from `nav__list--end` to `nav__list` (as first item)
6. Build locally, verify dropdown renders and links work
7. Commit on session branch

## Acceptance

- Categories dropdown visible in top-right of navbar on all pages
- Dropdown lists all 9 current categories alphabetically
- "Browse all" link present at top of dropdown
- Each category link navigates to `/categories/{name}/` and shows filtered posts
- Theme switcher moved to far left of navbar, still functional
- No regression on mobile (Anatole's navbar collapses on small screens)