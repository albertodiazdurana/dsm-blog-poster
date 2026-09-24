### [2026-09-01] /dsm-align: alignment updated, warnings present

**Type:** Notification
**Priority:** Medium
**Source:** /dsm-align

Run mode: post-change
Full report: `.claude/last-align-report.md`

Summary:
- Created: `dsm-docs/blog/README.md`
- Fixed: 2 hook scripts updated from Central (BL-532 cross-repo guard, BL-518 transcript validator); all hooks re-chmod +x; CLAUDE.md gained the BL-519 PROJECT-PLAN.md routing bullet
- Warnings: 2 (see persistent report for full text)
- Collisions: 1 (see persistent report for full text)

DSM version moved 1.20.0 -> 1.25.0. `.claude/last-align.txt` is deliberately
HELD at 1.20.0 because one template drift was found and NOT fixed: the §17.1
template has lost the `### Punctuation` heading and rule while keeping its
Scope paragraphs. Advancing the marker would hide the unresolved item from the
next boot gate.
