### [2026-08-05] Feedback file pending push to DSM Central: six `.claude/` local-state files assumed gitignored are tracked and public

**Type:** Action Item
**Priority:** High
**Source:** STAA run analyzing S33 (this project)

A DSM feedback file was written but NOT pushed. The STAA run that produced it
does not push feedback (that is `/dsm-wrap-up` Step 6's job) and performs no
commits, so this needs a main session to carry it.

**File:** `dsm-docs/feedback-to-dsm/2026-08-05_local-state-files-assumed-gitignored-are-tracked.md`

This is a third instance of the pattern filed in
`dsm-docs/feedback-to-dsm/done/2026-07-30_ugrep-shim-breaks-dsm-go-baseline-checksums.md`,
and the report widens that file's pattern statement rather than claiming a match:
Instances 1 and 2 are published *snippets* that fail against real input, this one is a
published *property claim* that was never installed downstream and therefore has no
failure mode at all until someone checks it.

**Action for the next main session:**

1. Commit the file (it is uncommitted, along with this inbox entry, `BL-030`, the
   `plans/README.md` edit, and the three modified tracked `.claude/` files).
2. At wrap-up, let Step 6 push it to DSM Central and send the accompanying inbox
   notification.
3. Move this entry to `_inbox/done/2026-08-05_staa-s33.md` once the push lands.

**Why Priority High.** Four specs (`dsm-staa.md:55` and `:60`, `dsm-align.md:499`,
`DSM_0.2.A:818` and `:901`) state that DSM's per-session local-state files are
gitignored. In this repository six of them are tracked and all six are present at
`origin/main` on a **public** repo, `.claude/reasoning-lessons.md` since commit
`6d676d1` (S9 wrap-up, roughly five months). An ecosystem sweep of five repositories
found the claim true only in DSM Central, where the specs were written: dsm-take-ai-bite
has a partial rule, and dsm-blog-poster, dsm-data-science-portfolio-working-folder and
dsm-graph-explorer have no rule at all. dsm-graph-explorer is public with the files
committed locally but not yet pushed, so it leaks on its next `git push`.

The root cause is that `dsm-align.md:499` assumes an "existing `.claude/` rule" that
cannot exist in a spoke: `.claude/` is a mixed directory whose tracked half
(`CLAUDE.md`, seven hooks, `dsm-ecosystem.md`, `settings.json`) is load-bearing, so only
per-file rules work. Central uses six explicit lines; no spoke has them, and no skill
installs or verifies them at any point except `/dsm-finalize-project` Step 4, which runs
at end of project life.

**Separate from the spec fix, and the owner's call:** adding the ignore rules plus
`git rm --cached` stops the bleeding but does not remove what is already on the public
remote. The report says so explicitly and does not recommend a history rewrite.

**Two decisions this project may want independent of Central's fix:**

1. Whether to add the seven per-file `.gitignore` rules here now rather than waiting for
   a Central-side `/dsm-align` step.
2. Whether the already-published content matters enough to act on. The exposed material
   is internal session reasoning and project state, no credentials, and much of the
   adjacent context is already public via the tracked `CLAUDE.md`.
