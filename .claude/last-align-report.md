# /dsm-align persistent report

**Timestamp:** 2026-09-01T23:02+02:00
**DSM version:** 1.25.0 (from ~/dsm-agentic-ai-data-science-methodology/CHANGELOG.md latest heading)
**Run mode:** post-change
**Project:** dsm-blog-poster
**Project type:** Application (DSM 4.0) , no override section present; detection signals are ambiguous (no primary runtime marker; `public/` build output + `scripts/` + a `hugo.yml` deploy workflow), and the recorded type was retained per the §17 do-not-silently-reclassify rule

---

## Report

/dsm-align post-change report:
- Project type: Application (DSM 4.0)
- Created: dsm-docs/blog/README.md (Blog Publication Tracker stub, per v1.24.0 / BL-517)
- Already correct: 8/8 dsm-docs folders, 6/6 done/ subfolders, 6/7 template files, _inbox/ + done/ + README.md, .gitattributes (LF enforced), .claude/session-transcript.md, .claude/dsm-ecosystem.md (4/4 paths validated on disk), .claude/reasoning-lessons.md, settings.json hook entries (6/6 template entries present including all three validate-cross-repo-write.sh matchers)
- Fixed: 2 hook scripts updated from Central (validate-cross-repo-write.sh 8944 -> 11857 B per BL-532; validate-transcript-edit.sh 4304 -> 7243 B per BL-518); all 8 hooks re-chmod +x; CLAUDE.md alignment block gained the BL-519 PROJECT-PLAN.md routing bullet under Actionable Work Items
- Collisions: 1 (dsm-docs/inbox/ ghost folder)
- Warnings: 2 (see full text below)
- CLAUDE.md alignment: Drift partially resolved , BL-519 routing line applied; the punctuation-scope drift is HELD pending a user decision (see Warning 1)
- CLAUDE.md content: OK (Application project; no Notebook Development Protocol present)
- CLAUDE.md redundancy: OK
- CLAUDE.md paths: OK (28 candidate paths checked; 5 flagged and all 5 are false positives , 2 GitHub repo slugs, 2 YYYY-MM-DD/vX.Y filename patterns the `{}` placeholder filter does not catch, and dsm-docs/blog/feature-trail.md which is a DSM Central path and verified present there)
- .gitattributes: OK
- Command sync: N/A (not DSM Central)
- Feedback pushed: none pending (no per-session files, no technical.md)
- EC governance scaffold: N/A (not EC)

## Warnings (full text)

1. **The §17.1 template has lost the Punctuation rule but kept its Scope block. Verbatim regeneration would delete a live project convention.**

   `DSM_0.2.T_Alignment_Templates.md` carries three paragraphs beginning "**Scope.** The rule governs files that reach a reader outside the project, by any channel." sitting between `### Actionable Work Items` and `### Code Output Standards` with **no heading and no antecedent for "The rule"**. The `### Punctuation` heading and its rule sentence appear nowhere in the template, nowhere in `DSM_0.2_Custom_Instructions_v1.1.md`, and nowhere in any `DSM_0.2.*` module; `grep -rn 'When an em dash'` over DSM Central returns hits only inside two closed backlog files (BACKLOG-469, BACKLOG-505). The BL-513 deliberate-application caveat the v1.21.2 CHANGELOG describes as shipping in the same revision (comma splice, numeric range separator) is also absent from the template.

   CHANGELOG v1.21.1 (BL-505) and v1.21.2 (BL-513) both carry **Spoke action: Run `/dsm-align` to pick up the revised §17.1 alignment block**, so the intent is clearly that spokes gain the Scope block *attached to the punctuation rule*, not that they lose the rule.

   This spoke currently holds the rule text without the Scope block. Regenerating verbatim from the template would produce the inverse: Scope paragraphs orphaned under an unrelated heading, and no punctuation rule , in a project whose prose convention depends on it (the comma-for-em-dash form is applied throughout this repo's content and is named in project MEMORY).

   Held for a user decision rather than applied. Proposed resolution is to keep `### Punctuation` and append the three Scope paragraphs beneath it, which is what both BLs describe, and to report the template defect upstream.

2. **Ghost folder `dsm-docs/inbox/` is present and git-tracked (contains only an empty `.gitkeep`).**

   `/dsm-go` Step 0.5 names this project by name as the measured instance: the folder was created to satisfy a nine-entry canonical list that no specification actually defines, inflating the scaffold count to a false 9/9. The canonical inbox is `_inbox/` at project root, which exists and is correct. Reported, not auto-removed, per Step 3b.

## Collisions (full text)

`dsm-docs/inbox/` collides with the canonical `_inbox/` at project root. Tracked file: `dsm-docs/inbox/.gitkeep` (0 bytes). See Warning 2.

## Already correct

- All 8 canonical `dsm-docs/` subfolders: blog, checkpoints, decisions, feedback-to-dsm, guides, handoffs, plans, research
- All 6 required `done/` subfolders
- Template files present: blog/journal.md, checkpoints/README.md, feedback-to-dsm/README.md, handoffs/README.md, plans/README.md, research/README.md
- `_inbox/`, `_inbox/done/`, `_inbox/README.md`
- `.gitattributes` present and enforcing `* text=auto eol=lf`
- CLAUDE.md `@` reference valid: `@../../dsm-agentic-ai-data-science-methodology/DSM_0.2_Custom_Instructions_v1.1.md`
- Alignment delimiters present at lines 3 and 96
- `.claude/dsm-ecosystem.md` present; all 4 registered paths exist on disk (dsm-central, take-ai-bite, portfolio, graph-explorer)
- `settings.json` hooks: all 6 template `(matcher, command)` pairs already present, including the three `validate-cross-repo-write.sh` matchers (Write / Edit / Bash). BL-503's multi-matcher fix has landed here; the S34 report that Bash coverage never reached this spoke is now resolved.
- No sprint-plan files matching `^#\s+Sprint\s+\d+\b` in dsm-docs/plans/ or done/, so step 3a had no candidates
- No consumed handoffs outside `done/`

## Steps skipped

- Step 11 skipped: not DSM Central
- Step 11b skipped: not DSM Central
- Step 11c skipped: `dsm-docs/blog/feature-trail.md` is a hub-only artifact and is absent here
- Step 3-EC skipped: not an External Contribution
- Step 6 produced no push: no per-session feedback files and no `technical.md`
