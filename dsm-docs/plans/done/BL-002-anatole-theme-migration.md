# Migrate from PaperMod to Anatole theme

**Created:** 2026-03-17 (Session 8)
**Priority:** High
**Status:** In Progress

## Motivation

Adopt a split-layout design inspired by nhatcher.com: fixed left sidebar (profile, logo, social links) with scrollable right content area. PaperMod's single-column design cannot achieve this without fragile overrides. Anatole provides this layout natively.

## Scope

- Replace PaperMod git submodule with Anatole
- Migrate hugo.yaml configuration to Anatole parameters
- Migrate custom partials (home_info.html, logo, homepage eight principles)
- Preserve all existing content (blog posts, drafts)
- Preserve favicon, logo, and OpenGraph images
- Verify GitHub Actions deployment still works
- Verify custom domain (take-ai-bite.com) unaffected

## Implementation Branch

`feature/BL-002-anatole-theme`

## Acceptance Criteria

- Site builds with Anatole theme
- Split layout: fixed left sidebar + scrollable right content
- All published posts render correctly
- Logo, favicon, social links preserved
- GitHub Pages deployment works