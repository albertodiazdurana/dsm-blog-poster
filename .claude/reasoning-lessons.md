# Reasoning Lessons

Entries tagged `[STAA]` are from Session Transcript Analysis. Format: `[STAA] S{N} [{scope}]: {lesson}`
Scope: `ecosystem` (any DSM project), `pattern` (same project type), `project` (this project only)

---

- [STAA] S8 [ecosystem]: Inbox action items must create a BL before implementation -- "implement" in triage means "approve for BL creation," not "do it now."
- [STAA] S8 [ecosystem]: Spoke-to-hub feedback must first be written to local docs/feedback/ before pushing to DSM Central _inbox/. Don't skip the intermediate step.
- [STAA] S8 [pattern]: Before migrating Hugo themes, read the target theme's README/requirements for external dependencies (e.g., Dart Sass). Don't discover requirements from build failures.
- [STAA] S8 [ecosystem]: When acting on a known protocol, slow down and verify the full step sequence before executing. "Knows the rule, skips a step" is the most common protocol violation pattern.
- [auto] S9 [ecosystem]: When DSM_3 and DSM_0.2 conflict, follow DSM_0.2 -- it is the operational layer that gets patched first. DSM_3 may lag behind.
- [auto] S9 [pattern]: When renaming a governance folder (docs/ -> dsm-docs/), grep all *.md files for references before committing. Internal cross-references break silently.
- [auto] S9 [project]: Main branch is protected -- don't attempt direct push. Go straight to branch + gh pr create + gh pr merge.
- [auto] S12 [pattern]: For data visualization, generate and review output before presenting to the user. Parallel-coordinates with 15 systems was caught as cluttered in the same thinking block that assessed it, preventing a bad recommendation.
- [auto] S12 [pattern]: When pivoting from a composite encoding (Z as bubble size) to separate 2D plots per axis pair, the composite encoding becomes redundant. Catch and remove it in the same step rather than carrying forward dead weight.
- [auto] S12 [pattern]: For data-driven blog posts, finalize and approve all plots before writing prose. Plot revisions ripple into the narrative; prose written first gets partially invalidated by later plot changes.
- [auto] S12 [project]: After replacing plots, proactively remove the old image files. Orphaned assets in a Hugo leaf bundle do not break the build but accumulate silently.
- [auto] S13 [ecosystem]: When a skill (like /humanizer) should apply persistently, enforce it in two layers: CLAUDE.md (loaded every session) for the rule, feedback memory for the why. Either alone is insufficient.
- [auto] S13 [pattern]: When humanizing blog posts, the "Everything Else" / personal sections are often already clean. Focus humanizer effort on professional/promotional sections where AI patterns concentrate.
- [auto] S13 [pattern]: Blog materials from source projects are raw inputs, not drafts. Read voice-calibration pages (about-me, about) before adapting tone, not after.
- [auto] S13 [project]: Two PRs from the same session branch fail on GitHub (one PR per branch). Either split work to separate branches upfront, or accept one combined PR.
- [auto] S14 [pattern]: When a Hugo feature appears configured in front matter but does not render on the live site, check the theme template for the actual parameter name before assuming the front matter is correct. PaperMod uses `showToc:`, Anatole uses `toc:`. Migrating themes silently breaks any front matter that was theme-specific.
- [auto] S14 [pattern]: When writing new governance rules in CLAUDE.md, expect 2-3 iterations as edge cases surface during the next action that uses the rule. Better to write a v1, use it once, and revise than to try to specify completely upfront. The reconstruction-trail rule and Hub naming rule both followed this shape this session.
- [auto] S14 [ecosystem]: Cross-repo paths in MEMORY.md decay quickly. The Advanced-DS-and-AI-Portfolio-Projects spoke was renamed to efficientnet-flower-classification-transfer-learning, and the inbox notification still pointed at the old path. Verify ecosystem paths exist before reading them; fall back to the inbox summary if the source file is unreachable.
- [auto] S14 [project]: When committing logically separate changes, avoid wildcard `git add content/blog/*` if a new untracked bundle sits in that tree. The wildcard will sweep the new bundle into the wrong commit. Use explicit file lists or commit the new bundle first.