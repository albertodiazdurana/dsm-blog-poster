# Six `.claude/` local-state files that the specs call gitignored are tracked in spokes, and public in this one

**Date:** 2026-08-05
**Project:** dsm-blog-poster
**Session:** Found by the `/dsm-staa` run analyzing S33 (2026-08-05), while verifying the skill's own claim that its output files are not committed.
**Severity:** Spec-versus-reality defect with a real disclosure consequence. Six files that `/dsm-staa`, `/dsm-align` and `DSM_0.2.A` all describe as gitignored local state are tracked in this repository and present at `origin/main` on a **public** GitHub repo. No credentials are involved; the exposed content is internal session reasoning and project state. Nothing is lost, but a file the specs promise is local-only has been published since 2026-03 without the owner ever deciding that.
**Suggested targets:** `scripts/commands/dsm-staa.md` lines 55 and 60; `scripts/commands/dsm-align.md` line 499; `DSM_0.2.A_Session_Lifecycle.md` lines 818 and 901. Plus one new install/verify step, see Proposed fixes.

**Relationship to the prior report:** this is a third instance of the pattern filed in
`done/2026-07-30_ugrep-shim-breaks-dsm-go-baseline-checksums.md`, but it widens that
report's pattern statement rather than fitting inside it. See "How this relates to
Instances 1 and 2" below, which states the widening explicitly instead of asserting a
match.

---

## Summary

Four separate specs assert that DSM's per-session local-state files are gitignored:

- `dsm-staa.md:60` , "All three are gitignored local-only artifacts; none is committed."
- `dsm-staa.md:55` , "The marker is gitignored and local-only."
- `dsm-align.md:499` , "The file is gitignored via the existing `.claude/` rule; no `.gitignore` change required."
- `DSM_0.2.A:818` and `:901` , "`.claude/reasoning-lessons.md` (gitignored, project-local)" and "The compact mirror file is gitignored (same as the live file)".

In this repository none of that is true. `.gitignore` carries six `.claude/` rules and
none of them covers these files:

```
$ grep -n '^\.claude' .gitignore
18:.claude/session-baseline.txt
19:.claude/session-transcript.md
20:.claude/transcripts/
21:.claude/plans/
22:.claude/session.lock
23:.claude/cross-repo-writes-session.txt

$ git check-ignore -v .claude/reasoning-lessons.md .claude/reasoning-lessons-compact.md .claude/last-staa.txt
(no output, exit 1 , none is ignored)
```

Six local-state files are tracked, and every one of them is present on the public
remote:

```
$ for f in last-align-report.md last-align.txt last-staa.txt last-wrap-up.txt \
           reasoning-lessons.md reasoning-lessons-compact.md; do
    git cat-file -e origin/main:.claude/$f && echo "PUBLIC: .claude/$f"
  done
PUBLIC: .claude/last-align-report.md
PUBLIC: .claude/last-align.txt
PUBLIC: .claude/last-staa.txt
PUBLIC: .claude/last-wrap-up.txt
PUBLIC: .claude/reasoning-lessons.md
PUBLIC: .claude/reasoning-lessons-compact.md

$ gh repo view --json visibility -q .visibility
PUBLIC
```

`.claude/reasoning-lessons.md` has been tracked since commit `6d676d1` ("Session 9
wrap-up: reasoning lessons from S8 STAA + S9 auto extraction"), so it has been public
for roughly five months. The compact mirror joined at `887f7d4` (S25) and
`last-staa.txt` at `44707f7` (S22).

## Ecosystem sweep

Checked five repositories in the ecosystem. The claim holds only where it was written.

| Repository | `.gitignore` rule | Files tracked | Remote |
|---|---|---|---|
| DSM Central | **Complete** , 6 explicit lines (116-119, 123-126) | none (ships `reasoning-lessons.md.template` only) | compliant |
| dsm-take-ai-bite | **Partial** , covers `reasoning-lessons.md` + `-archived.md`, not the compact mirror or `last-staa.txt` | none (template only) | no leak yet; would leak if STAA ran there |
| dsm-blog-poster | **None** | 6 | **PUBLIC**, all 6 at `origin/main` |
| dsm-data-science-portfolio-working-folder | **None** | 5 (incl. a `.bak` and an archive) | PRIVATE, at `origin/main` |
| dsm-graph-explorer | **None** | 3 | PUBLIC, **not yet pushed** , leaks on next push |

DSM Central, which authors the specs, is the one repository where the assertion is
true. That is the whole defect in one line.

## Root cause

`dsm-align.md:499` names the assumed mechanism: "gitignored via the existing `.claude/`
rule". **No such rule exists in a spoke, and none can.** `.claude/` in a DSM spoke is a
*mixed* directory whose tracked half is load-bearing:

```
$ git ls-files .claude/
.claude/CLAUDE.md              <- must be tracked
.claude/dsm-ecosystem.md       <- must be tracked
.claude/hooks/*.sh  (7 files)  <- must be tracked
.claude/settings.json          <- must be tracked
.claude/last-align-report.md   <- local state, should not be
.claude/last-align.txt         <- local state, should not be
.claude/last-staa.txt          <- local state, should not be
.claude/last-wrap-up.txt       <- local state, should not be
.claude/reasoning-lessons.md   <- local state, should not be
.claude/reasoning-lessons-compact.md  <- local state, should not be
```

A blanket `.claude/` exclude would drop CLAUDE.md and every hook. So the only workable
form is per-file lines, which is exactly what Central does and what no spoke has.

The belief likely came from a real but differently-scoped harness behaviour that the
specs elsewhere describe correctly. `dsm-go.md:660` states, for External Contribution
projects, that session artifacts "are hidden from git by Claude Code's
`.git/info/exclude` rule (which adds `.claude/`), not by DSM or the project's
`.gitignore`". That is accurate, and it applies to *external* repositories where
`.claude/` is wholly foreign. Spokes are the opposite case. The `.claude/` exclusion
was generalised from the one context where it holds to the one where it cannot.

`DSM_0.2.A` §26.1 already demonstrates the correct way to state this, for the session
lockfile:

> Gitignored (entry in `.gitignore` independent of any broader `.claude/` exclude rule,
> so the file is never committed even if `.claude/` exclusion drifts)

That is a *requirement with an install condition*. For the six files above, the same
property is stated as a *fact*, and nothing installs it.

## Why no existing step catches it

No skill installs or verifies these rules at any point in a project's working life.
Grepping every `dsm-*` command for a gitignore action returns exactly one, and it fires
at the wrong end of the lifecycle:

- `dsm-finalize-project.md:165` , "Gitignore verification: Check `.gitignore` excludes
  all deleted artifact types" , runs only at project *finalization*.
- `dsm-align.md` mentions gitignore five times (323, 455, 499, 542, 709) and every one
  is a descriptive assertion. None is a check.

`DSM_0.2.A:2750` records "Finding #9 (no `.gitignore` ships)" as a motivator of the
Cloned-Mirror Kick-off protocol, so the hub already knows spokes receive no
`.gitignore`. That remedy covers **new** cloned mirrors. Existing spokes , which is all
of the ones above , were never backfilled.

## Consequence

Ranked by what actually happens:

1. **Disclosure.** `reasoning-lessons.md` is 115 entries of internal session reasoning,
   cross-repo paths, incident narratives and project state, published on a public repo
   under a spec that promises it is local-only. No secrets, and much of the adjacent
   context is already public via the tracked `CLAUDE.md`; the defect is that the
   decision was never made, not that the content is dangerous.
2. **Silent future leak.** dsm-graph-explorer has the files committed locally but not
   pushed. The next `git push` publishes them, with no warning at any point.
3. **Working-tree noise.** `/dsm-staa` documents itself as leaving nothing behind, so
   its three modified tracked files show up as unexplained dirt in the next session's
   baseline, where an unscoped `git add` can sweep them into an unrelated commit.
4. **Merge friction.** Local-state files that change every session are tracked on a
   protected-branch workflow, so they collide across branches for no benefit.

## Proposed fixes

**Primary , correct the four claims.** Restate them as requirements rather than facts,
in the §26.1 form. Concretely, `dsm-staa.md:60` should read that the three files *must
be* gitignored per-file and are not committed *when the rule is installed*, and
`dsm-align.md:499` should drop "via the existing `.claude/` rule; no `.gitignore` change
required", which is the sentence that actively prevents the fix.

**Secondary , install and verify the rule.** `/dsm-align` is the natural carrier: it
already aligns spoke structure, runs on every version bump, and has a post-change
report to surface the result. A new sub-step under the scaffold checks would be:

```bash
# Per-file, never a blanket .claude/ rule: .claude/ is a mixed directory in a spoke.
for f in .claude/reasoning-lessons.md \
         .claude/reasoning-lessons-compact.md \
         .claude/reasoning-lessons-archived.md \
         .claude/last-staa.txt \
         .claude/last-align.txt \
         .claude/last-align-report.md \
         .claude/last-wrap-up.txt; do
  git check-ignore -q "$f" || echo "MISSING .gitignore rule: $f"
done
```

Report each miss, and for files already tracked, report that `git rm --cached` is
needed as well, since adding the ignore rule alone does not untrack them. That second
half matters here: five of the six are already in history, so the ignore rule fixes the
future and not the past.

**Owner's decision, not a spec fix.** Whether to purge the already-published content
from history is the repository owner's call and is out of scope for this report. Adding
the rule plus `git rm --cached` stops the bleeding; it does not remove what is already
on the remote.

## How this relates to Instances 1 and 2

The prior report's pattern is "a canonical **snippet** published in a skill that does
not match its actual input". This instance is not a snippet, so rather than assert a
match I checked what the three genuinely share and what separates them.

| | Instance 1 (ugrep) | Instance 2 (CHANGELOG) | Instance 3 (this) |
|---|---|---|---|
| What is published | a runnable snippet | a format description | a property claim |
| Mismatch is between | the snippet and the **execution environment** | the spec and its **own source file** | the claim and the **downstream environment it was never installed into** |
| True anywhere? | yes, under GNU grep | no, nowhere | yes, in DSM Central only |
| Failure signal | exit 0, silent at execution | exit 1, silent at effect | none at all; nothing ever runs |
| What catches it | reading tool output, not the exit code | comparing the spec to the file it names | running the spec's own assertion as a check |

The shared cause survives the widening, and the prior report already stated it in a
form that covers this case: **a published assertion about input or environment that is
never verified at authoring time.** What Instance 3 adds is that the assertion need not
be executable to fail. A prose claim of a property is still an assertion, and it is
strictly worse than a broken snippet, because a snippet at least fails when someone
runs it. This one had no failure mode at all until somebody thought to check it.

The prior report's suggested convention , "the snippet must be run against the real
file, in the harness the agent actually uses, before it ships" , extends cleanly:
**a property a skill claims about a project should be expressible as a check, and
shipped as one.** All three instances are then caught by the same discipline.

## Related

- `done/2026-07-30_ugrep-shim-breaks-dsm-go-baseline-checksums.md` , Instances 1 and 2
- `done/2026-05-28_staa-step8-wrapup-step0-transform-drift.md` , prior STAA-filed skill
  defect in this project, same family
- `DSM_0.2.A` §8 (reasoning lessons), §25 (Cloned-Mirror Kick-off, finding #9), §26.1
  (the lockfile's correctly-stated gitignore requirement, the model for the fix)
- `/dsm-go` Step 5.5, Step 5.7 (consumers of `last-staa.txt` and the transcript archive)
- `/dsm-finalize-project` Step 4 (the only existing gitignore verification, end-of-life)
