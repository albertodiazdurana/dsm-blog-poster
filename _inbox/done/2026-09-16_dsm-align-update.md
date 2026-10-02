### [2026-09-16] /dsm-align: alignment updated (v1.20.0 -> v1.26.3)

**Type:** Notification
**Priority:** Medium
**Source:** /dsm-align

Run mode: post-change
Full report: `.claude/last-align-report.md`

Summary:
- Created: none
- Fixed: CLAUDE.md §17.1 managed block regenerated (removed retired `### Punctuation`
  section per F-175/v1.26.1; renamed transcript delimiter + Pre-Gen-Brief label
  thinking->plan per F-174/v1.26.0); 3 hooks updated from Central; `settings.json`
  merged (BL-484 Bash matcher for `validate-cross-repo-write.sh`, first landing on
  this spoke)
- Warnings: 3 (see persistent report for full text)
  1. Pre-existing S36 broken edit: humanizer bullet has an unbalanced `(` after the
     `blader/humanizer` clause was removed. Not introduced by this run.
  2. Ghost `dsm-docs/inbox/` folder (F-173 phantom). Owned by BL-033.
  3. `scripts/sync-commands.sh --deploy` still owed (many v1.20-v1.26 entries):
     /dsm-* command copies ~4 months stale (stale /dsm-backlog, /dsm-checkpoint).
- Collisions: 2 (non-canonical `dsm-docs/assets/` and `dsm-docs/inbox/`; reported, not auto-fixed)

Marker advanced 1.20.0 -> 1.26.3.
