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