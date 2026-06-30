# BL-028: Bump GitHub Pages actions off deprecated Node 20

**Status:** Open
**Priority:** Low
**Date Created:** 2026-06-30 (Session 27)
**Source:** S27 deploy of PR #47. The Pages deploy run logged: "Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/deploy-pages@v4."
**Origin:** GitHub is retiring Node 20 from Actions runners (https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/). Actions still declaring `runs.using: node20` are force-run on Node 24 with a warning during the transition. When the forced fallback ends, a node20-pinned action will fail to start.

## Problem

`.github/workflows/hugo.yml` pins four official actions at majors that predate the Node 24 runtime:

| Action | Was | Latest (verified node24) |
|--------|-----|--------------------------|
| `actions/checkout` | v4 | v7.0.0 (`using: node24`) |
| `actions/configure-pages` | v5 | v6.0.0 (`using: node24`) |
| `actions/upload-pages-artifact` | v3 | v5.0.0 (`using: composite`) |
| `actions/deploy-pages` | v4 | v5.0.0 (`using: node24`) |

The site build itself uses no Node (Hugo is a Go binary; Dart Sass is a standalone binary), so this is purely the runtime that executes the JS actions. Deploys are currently green; the risk is future breakage when GitHub ends the forced fallback.

## Verification done (S27)

Latest release tags pulled via `gh api repos/<r>/releases/latest`. Each tag's `action.yml` `runs.using` checked via `gh api .../contents/action.yml?ref=<tag>` and confirmed node24 (or composite). The `with:` params in our workflow (checkout `submodules`/`fetch-depth`, upload `path`) are stable across these majors.

## Fix

Bump all four to the verified latest majors in `.github/workflows/hugo.yml`. Confirm the next deploy run is green with no Node 20 deprecation warning.

## Success criteria

- Workflow pins all four Pages actions at node24-targeting majors.
- A deploy run completes green with no "Node.js 20 is deprecated" warning.

## Outcome

- (S27) **Done.** Bumped checkout@v4 -> v7, configure-pages@v5 -> v6, upload-pages-artifact@v3 -> v5, deploy-pages@v4 -> v5. Verified next deploy: TBD.
