# CLAUDE.md "always" / "at session start" instructions are silently skipped without hook enforcement

**Date:** 2026-04-09
**Project:** dsm-blog-poster
**Session:** 19
**Severity:** Critical (silent protocol violation, recurring across instructions, undermines Earn Your Assertions)
**Suggested target:** DSM_0.2 (CLAUDE.md instruction enforcement section), `/dsm-go` Step 2, hook infrastructure propagation policy

## Summary

Project-level CLAUDE.md instructions phrased as unconditional imperatives ("At session start, read X", "Always run /humanizer on Y", "Before writing reader-facing content, read Z") are silently skipped by the agent under task pressure when there is no runtime hook to enforce them. The agent reads the rule (CLAUDE.md is in the system prompt), acknowledges the rule, and then does not fire the corresponding tool calls. The failure is invisible until something downstream catches it, by which point the agent has often produced recommendations or content built on top of the unread sources.

This is not a one-off slip. In a single session (S19) the same structural pattern produced two independent failures, and the second was on a rule with explicit "At session start, read..." phrasing. This is a structural gap, not an attention lapse.

## Concrete incidents (Session 19, dsm-blog-poster, 2026-04-09)

### Incident 1, Session Transcript Protocol skipped across multiple turns

DSM_0.2 Session Transcript Protocol and project CLAUDE.md both require: append thinking to `.claude/session-transcript.md` BEFORE acting, every turn, as the first tool call. `/dsm-go` Step 6 has a "Behavioral activation (mandatory, immediate)" paragraph reinforcing this.

Actual behavior: agent reset the transcript header during `/dsm-go` Step 6, then performed ~4 conversation turns (session report, BL-015 plan presentation, alternative work suggestion, deferral handling) without appending a single thinking block. The transcript stayed at "header only" until the user manually challenged: "Why are we not appending to session-transcript?"

F-094 (per-turn `UserPromptSubmit` hook reminder) was created in DSM Central specifically to close this failure mode. The hook is not propagated to dsm-blog-poster (no `.claude/settings.json`, no `.claude/settings.local.json`). The static doc rules in DSM_0.2 + CLAUDE.md + `/dsm-go` Step 6 were the only enforcement, and they failed silently.

### Incident 2, "At session start, read" rules skipped, recommendations made on unread sources

Project CLAUDE.md (`Voice and content quality` section) contains TWO unconditional session-start read rules:

1. *"At session start, read `content/about-me.md` and `content/about.md` to calibrate the author's voice before writing any content"*
2. *"At session start, read the following DSM Central files to build accurate context about Take AI Bite (TAB) and Deliberate Systematic Methodology (DSM) before writing or editing any reader-facing content"* , followed by 6 file paths (FEATURES.md, DSM_6.0, DSM_6.1, 6.1.A, 6.1.B, 6.1.C)

Actual behavior in S19: agent read NEITHER set of files during `/dsm-go`. Then, when the user picked BL-010 (Systems Prompt Engineering blog content), the agent produced an angle ranking ("Angle 2 PMP-to-SPE is strongest because...") with confidence, despite never opening `DSM_6.1_Systems_Prompt_Engineering_v1.0.md` or any of its modules. The recommendation was unearned.

Worse, the agent admitted the violation in passing inside the recommendation paragraph ("Per CLAUDE.md session-start rule I should already have these as context but didn't read them") and continued presenting the plan, treating the admission as a footnote rather than a stop condition. The user had to escalate ("this is unacceptable") to halt the work.

## Root cause

The pattern is the same in both incidents:

1. **CLAUDE.md is loaded as context, not executed as a checklist.** CLAUDE.md is injected into the agent's system prompt at conversation start. The agent parses it as descriptive metadata about the project, not as a list of imperatives requiring tool calls. "At session start, read X" gets understood, not actioned. Reading the rule and executing the rule are conflated.
2. **`/dsm-go` is project-agnostic.** Its session-start checklist enumerates generic protocol steps (session number, branch, inbox, version, baseline, transcript reset). It does not enumerate project-specific CLAUDE.md mandatory reads. After Step 9 ("What would you like to work on?"), `/dsm-go` considers session start complete. Project-level "At session start, read X" rules are invisible to `/dsm-go`'s bash checklist.
3. **No hook enforcement.** Static doc rules without runtime triggers lose to immediate task pressure under concise/low-effort modes. F-094 closes this gap for one specific instruction (transcript append). The analogous closure for "session-start mandatory reads" and other "always X" / "before X" CLAUDE.md instructions does not exist.
4. **Concise mode amplifies the gap.** The agent optimizes for "minimum tool calls to answer the user" and skips reads it judges deferrable. The reasoning that justifies the skip is never written down (process narration F-095 would catch this if the transcript itself were being maintained, but see Incident 1).
5. **Naming a violation is not neutralizing it.** The agent's instinct to admit a miss in passing while continuing the work is a separate failure mode. The admission should be a stop condition, not a parenthetical.

The deeper structural observation: **DSM has two layers of enforcement, doc and hook, and only the hook layer survives task pressure.** Anywhere a "must" or "always" or "at session start" rule lives in static doc only, expect silent skipping. F-094 proves the hook layer works for the specific case it covers. The principle generalizes.

## Proposed fixes

### Option A , Compulsory hook enforcement for all "always" / "at session start" CLAUDE.md instructions (recommended primary)

Make hook enforcement compulsory, not optional, for any CLAUDE.md instruction phrased as an unconditional imperative. Concretely:

1. Establish a DSM_0.2 rule: any project-level CLAUDE.md instruction containing "at session start", "always", "before X, do Y", or equivalent unconditional phrasing MUST be backed by a corresponding hook in `.claude/settings.json`. Doc-only rules are explicitly insufficient.
2. Generalize F-094's mechanism: ship a configurable `UserPromptSubmit` hook in DSM Central that reads a list of project-defined "session-start mandatory reads" and "per-turn mandatory actions" from a config file (e.g., `.claude/dsm-enforcement.json`) and injects reminders into the user prompt. The transcript-append rule becomes one entry in this config; mandatory reads become other entries.
3. Add a `/dsm-align` step that scans CLAUDE.md for unconditional imperative phrasing, cross-references against `.claude/settings.json`, and flags any rule without a backing hook as a critical alignment failure.

### Option B , `/dsm-go` Step 2 extension: parse CLAUDE.md for "at session start, read" patterns and execute them

Extend `/dsm-go` Step 2 with a sub-step that scans the project CLAUDE.md for the literal phrase "at session start, read" (and variants), extracts the listed file paths, and fires Read tool calls before reaching Step 9 ("What would you like to work on?"). This is narrower than Option A and only covers the read-files case, but it is cheap and immediately closes Incident 2.

### Option C , Stop-condition rule: any acknowledged protocol violation halts the current task

Add a DSM_0.2 protocol rule: when the agent identifies that it has violated a CLAUDE.md or DSM_0.2 instruction, the violation is a stop condition. The agent must (a) name the violation explicitly to the user, (b) propose corrective action, (c) wait for user confirmation, and (d) not continue the in-progress task with the violation outstanding. Admitting a violation in passing while continuing to present a plan is itself a protocol violation.

This is independent of A and B and addresses the "compound failure" pattern where the agent treats an admission as neutralization.

### Option D , Propagate F-094 hook to all spokes via `/dsm-align`

Independent of the broader Option A redesign: `/dsm-align` should ensure that every spoke has the F-094 transcript-append hook installed in `.claude/settings.json`. Currently dsm-blog-poster does not, despite the rule being inherited from DSM_0.2. This is a propagation gap, not a design gap, and is straightforward to fix.

## Recommendation

Adopt Option A as the strategic fix (it generalizes F-094 into a protocol principle and closes the family of bugs, not just one instance). Adopt Options C and D immediately as tactical fixes that do not depend on Option A's design work:

- Option C is a one-paragraph DSM_0.2 amendment, deployable today.
- Option D is a `/dsm-align` improvement, deployable in the next DSM Central session.

Option B is a fallback if Option A's config-driven generalization is too much scope for the next release.

The cost of the bug is severe: agents produce recommendations and content on top of unread sources, violating Earn Your Assertions, and the violation is invisible until a user catches it. In a content project (this one) the failure mode publishes inaccurate posts. In a code project the failure mode ships unverified claims about how code works. This is not a minor workflow gap.

## Related

- F-094 (per-turn transcript append enforcement) , the existing point solution that proves the hook approach works
- F-095 (process narration in thinking blocks) , would have surfaced the skip-justifying reasoning if the transcript itself were being maintained (circular dependency on Incident 1)
- DSM_0.2 §22 Protocol Violation Triage , Incident 2's "admission as footnote" pattern is exactly the failure §22 is meant to catch; needs reinforcement
- Earn Your Assertions principle (DSM_6.0) , directly violated by the BL-010 angle recommendation in Incident 2
- `/dsm-align` , the natural carrier for hook propagation (Option D) and CLAUDE.md scanning (Option A.3)
