# Session branch must be recreated after `gh pr merge --delete-branch`

**Date:** 2026-04-09
**Project:** dsm-blog-poster
**Session:** 17
**Severity:** Workflow gap (avoidable overhead, not data loss)
**Suggested target:** DSM_0.2 Three-Level Branching Strategy section, or `/dsm-go` / wrap-up workflow guidance

## Summary

After running `gh pr merge {N} --merge --delete-branch`, the local working copy lands back on `main` because the session branch it was on was just deleted. Any subsequent `git commit` will go directly to `main`, silently violating the Three-Level Branching Strategy (sessions must never commit directly to main). The agent does not get a clear signal that the branch context has changed.

## Concrete incident

In Session 17 of dsm-blog-poster, the sequence was:

1. Work on `session-17/2026-04-08`, commit BL-004 (Principle 1.9 blog post), push, open PR #23
2. `gh pr merge 23 --merge --delete-branch` , succeeded, working copy now on `main`
3. User asked to record LinkedIn Post 7 URL (small follow-on edit)
4. Agent edited `linkedin-posts.md`, ran `git add` + `git commit`, **commit landed on main**
5. Agent only noticed during the next status check
6. Recovery required:
   - `git branch session-17/2026-04-09-post7` (create safety net at current HEAD)
   - `git update-ref refs/heads/main refs/remotes/origin/main` (rewind main without `--hard`, since the harness blocks `git reset --hard` without per-call approval)
   - `git checkout session-17/2026-04-09-post7`
   - Push, PR #24, merge

No work was lost, but the recovery cost ~5 minutes and one extra PR. The slip is easy to repeat across any project that uses the merge-and-delete pattern, which is most of them.

## Root cause

DSM_0.2 has clear rules about which branch to commit on (Step 0 of `/dsm-go` enforces session branch creation at session start). It does not have rules about what happens to the branch context **after** an in-session PR merge. The agent treats the merge as "the previous unit of work is done" and the next task starts on whatever branch the working copy is on, which is `main` after `--delete-branch`.

The deeper issue: in the agent's mental model, "session branch" is something created at session start, not something that needs re-creating after every intra-session merge. There is no protocol step that says "after a merge, create a new branch before the next commit."

## Proposed fixes

### Option A , `/dsm-go` and wrap-up rule: explicit post-merge branch creation

Add a rule to DSM_0.2's Three-Level Branching Strategy section (and reinforce in `/dsm-go` Step 0 documentation):

> **After any in-session PR merge that deletes the source branch**, immediately create a new session-level branch before doing any further edits or commits. The cleanest pattern is to chain it in the same shell call:
> ```
> gh pr merge {N} --merge --delete-branch && git checkout -b session-{N}/{YYYY-MM-DD}-{next-purpose}
> ```
> If forgotten and a commit lands on main: create the recovery branch first (`git branch ...`), then rewind main with `git update-ref refs/heads/main refs/remotes/origin/main`. Do not use `git reset --hard` from the harness, it requires per-call approval.

### Option B , Hook-based guard

Add a pre-commit hook (or Claude Code hook) that refuses any commit on `main` and reports: "Refusing to commit on main. Create a session branch first." This is more robust but requires hook infrastructure on every spoke. Recommend Option A as the primary fix and Option B as opt-in for projects that want belt-and-suspenders.

### Option C , Naming convention for follow-on branches in the same session

DSM_0.2 already has `session-{N}/{YYYY-MM-DD}` format. For multiple merge cycles within one calendar session, suggest a `-{purpose}` suffix:
- `session-17/2026-04-08` (initial)
- `session-17/2026-04-09-post7` (follow-on after merge)
- `session-17/2026-04-09-bl015` (next task)

This avoids branch name collisions and makes the session boundary clearer in `git log`.

## Recommendation

Adopt Option A as a DSM_0.2 protocol amendment (Three-Level Branching Strategy section), and Option C as a soft naming convention. Option B is optional infrastructure for projects that want it.

The fix is cheap (one rule, one shell pattern) and the cost of the bug is moderate (one wasted PR + recovery overhead per slip). Worth fixing across the ecosystem before more spokes hit it.

## Related

- DSM_0.2 Three-Level Branching Strategy
- `/dsm-go` Step 0 (session branch setup)
- Cross-Repo Write Safety protocol (separate concern but same family of "the agent does not notice context changes" gaps)
