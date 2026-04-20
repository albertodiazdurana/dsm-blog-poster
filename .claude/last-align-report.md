# /dsm-align persistent report

**Timestamp:** 2026-04-13T21:00:00+02:00
**DSM version:** v1.4.18
**Run mode:** check-only
**Project:** DSM Blog Poster
**Project type:** Application (DSM 4.0)

---

## Report

/dsm-align check-only report:
- Project type: Application (DSM 4.0)
- Created: none
- Already correct: 15 (9 dsm-docs folders, _inbox, .gitattributes, reasoning-lessons, ecosystem registry, session-transcript, hooks)
- Fixed: none
- Collisions: none
- Warnings: 7 stale CLAUDE.md path references (migration table sources)
- CLAUDE.md alignment: OK (up to date)
- CLAUDE.md content: OK
- CLAUDE.md redundancy: OK
- CLAUDE.md paths: 7 stale path(s) found (all in Existing Content to Migrate table, cross-repo references)
- .gitattributes: OK
- Command sync: N/A (not DSM Central)
- Feedback pushed: none pending
- EC governance scaffold: N/A (not EC)
- Transcript hooks: 0 installed / 0 updated / 2 ok · settings.json: already ok

## Warnings (full text)

1. CLAUDE.md references `~/dsm-disaster-tweets/docs/blog-post-draft.md` which does not exist. (Line 101, Existing Content to Migrate table)
2. CLAUDE.md references `~/sql-query-agent-ollama/docs/blog/blog-s01.md` which does not exist. (Line 102)
3. CLAUDE.md references `~/sql-query-agent-ollama/docs/blog/blog-s02-collaboration-value.md` which does not exist. (Line 103)
4. CLAUDE.md references `~/sql-query-agent-ollama/docs/blog/blog-s02-ablation.md` which does not exist. (Line 104)
5. CLAUDE.md references `~/dsm-graph-explorer/docs/blog/epoch-1/blog-draft.md` which does not exist. (Line 105)
6. CLAUDE.md references `~/dsm-graph-explorer/docs/blog/epoch-2/wsl-migration-post.md` which does not exist. (Line 106)
7. CLAUDE.md references `~/dsm-agentic-ai-data-science-methodology/docs/blog/2026-02-06_blog-feedback-loop.md` which does not exist. (Line 107)

Note: All 7 stale paths are in the "Existing Content to Migrate" table documenting original source locations for blog posts. These posts may have been moved, renamed, or their source repos reorganized. The table is historical documentation; consider updating or removing stale rows.

## Collisions (full text)

None.

## Already correct

- `_inbox/` exists with `done/` and `README.md`
- All 9 `dsm-docs/` subdirectories present with correct `done/` subfolders
- Template files present: journal.md, checkpoints/README.md, feedback-to-dsm/README.md, handoffs/README.md, plans/README.md, research/README.md
- `.claude/CLAUDE.md` `@` reference valid
- CLAUDE.md alignment section matches current template
- `.gitattributes` enforces LF line endings
- `.claude/dsm-ecosystem.md` exists with 4 validated paths
- `.claude/reasoning-lessons.md` exists with header
- `.claude/session-transcript.md` exists
- BL-319 hooks: 2 scripts present, executable, byte-identical to source
- `.claude/settings.json` hooks entries match template

## Steps skipped

- Step 11 skipped: not DSM Central
- Step 3-EC skipped: not External Contribution