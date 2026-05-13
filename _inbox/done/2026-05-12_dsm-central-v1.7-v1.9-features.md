**Consumed at:** Session 22 (2026-05-12), processed into BL-021


### [2026-04-23] FEATURES.md update from DSM Central (v1.7.0)

**Type:** New F-entries
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

Three new F-entries eligible for blog coverage:

- **F-117 Checkpoint step in /dsm-wrap-up** (BL-414). Story angle: diagnostic detective work (missing-artifact-as-missing-step), user design refinement during Gate 1 rebalancing the MEMORY/checkpoint split.
- **F-116 /dsm-go context efficiency** (BL-413). Story angle: Sonnet session economics, unbundling 3 coupled concerns (align / chmod / inbox).
- **F-115 Gate 1 parallel offload analysis** (BL-409, §8.8 + §1.12). Story angle: ad-hoc agent delegation promoted to user-approved gate; "Don't be a Hero, Delegate the Effort" foundational principle.

See feature-trail v1.7.0 section for full origin + meta-pattern mapping.

### [2026-04-24] FEATURES.md update from DSM Central (v1.8.0)

**Type:** New F-entries
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

Three new F-entries eligible for blog coverage. Common thread: dead-pointer prevention across the BL→checkpoint→spoke-reader chain (closure of a problem class, not three independent features).

- **F-120 Checkpoint Authoring Identifiers Rule** (BL-420, DSM_0.2.A §10.2.1). Story angle: dead-pointer prevention at authoring time, the spoke-reader-blindness pattern (`/dsm-go` Step 3.5 reads checkpoints across sessions and that reader is often a spoke agent without access to `dsm-docs/plans/`); forward-only fix with a two-condition exception for in-flight BL checkpoints.
- **F-119 BL Lookup Index** (BL-419, `dsm-docs/plans/done/INDEX.md`). Story angle: governance artifact on a third axis (BL# alongside CHANGELOG's chronology and FEATURES' capabilities); mirrored to TAB so downstream readers resolve BL numbers in one hop; first major Sonnet-subagent-built artifact (332 rows, §8.8 approval).
- **F-118 Mirrored methodology BL-reference scrub** (BL-418). Story angle: pure reference cleanup, ~170 BL anchors removed from DSM_0-7 + commands + FEATURES prose + guides, replaced with resolvable identifiers; 174 edits across 26 files; FEATURES F-entry anchors preserved for the F→BL trail (resolvable in one hop via BL-419 Index).

Cross-cut narrative for the post: v1.8.0 is a "closure release" for the dead-pointer problem class (BL-418 cleans the past, BL-420 prevents recurrence at authoring time, BL-419 makes the remaining BL-number identifiers resolvable cheaply). Less a feature shipment, more a governance refactor.

See feature-trail v1.8.0 section for full origin + meta-pattern mapping.

### [2026-04-29] New features in DSM Central: F-121 + F-122 (S205)

**Type:** Action Item
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

Two new F-entries shipped in S205. Manual push because BL-424 (the wired-in /dsm-wrap-up FEATURES → blog-poster notification path) is filed but not yet implemented.

**New F-entries:**

- **F-121 (2026-04-29) Research folder index maintenance skills (BL-425, `/dsm-research-add` + `/dsm-research-done`)** — Two new skills bring `dsm-docs/research/` to parity with `dsm-docs/plans/` for index maintenance. `/dsm-research-add` creates a research file with a header stub, validates filename convention and linked-BL existence, and inserts a row into the appropriate sub-table of `dsm-docs/research/README.md` (5 categories: BL-tied / informs-BL / ready-for-promotion / tool-assessment / untracked-carryover). `/dsm-research-done` annotates `Status: Done` + `Date Completed:`, runs `git mv` followed by an explicit `git add` on the destination to handle the BL-370 rename-staging pitfall, and removes the row from the active index. CLAUDE.md gains a "Research Index Maintenance" sub-section flagging drift between folder and README as a §22 protocol violation signal.

- **F-122 (2026-04-29) Compact reasoning-lessons mirror for agent-facing session-start priming (BL-427, DSM_0.2.A §8.1)** — A derived `.claude/reasoning-lessons-compact.md` file is regenerated at every `/dsm-wrap-up` Step 0 from the live `.claude/reasoning-lessons.md`, and `/dsm-go` Step 1.5 reads the compact mirror in full instead of peeking at the first 10 lines of the live file. Restores §8 design intent ("the lessons feed the agent's priming at session start"). Trim-only format drops the live file's first ~20 guideline lines and the inline `[auto] S{N} [{scope}]:` provenance prefix; preserves category headings + lesson body verbatim. Empirical measurement: ~5% savings on a 113-entry / 51 KB file (lower than the projected 25-30%; entry-verbose files do not gain much from trim-only). Compression beyond trim-only is BL-427 Step 5, deferred behind a controlled-experiment requirement that explicitly forbids using productive sessions as A/B subjects.

**Suggested angles:**

- F-121: parity-by-skill across sibling folders (plans/ + research/), the asymmetry that existed silently, why "active index" beats "convention doc"
- F-122: source-of-truth + derived-mirror separation, the empirical surprise (5% vs 25-30%), measurement-before-scale discipline as the genesis of the BL-427 Step 5 controlled-experiment gate


### [2026-05-05] FEATURES.md update from dsm-agentic-ai-data-science-methodology

**Type:** FEATURES.md notification
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology
**Pushed by:** /dsm-wrap-up Step 1 sub-step (e) (BL-424)

## New F-entries (6)

v1.9.0 release shipped 6 new features (F-123 through F-128) from an inbox-derived backlog landing pass in S207. All 6 BLs traced to external spoke incidents (haystack-magic S5-S8, heating-systems-conversational-ai S10/S10.L2). Three new DSM_0.2 sub-sections (§8.6.1, §8.9.1, §8.10), one new DSM_0.2.A section (§26), two skill amendments.

- **F-128 (2026-05-05) Chunked Drafting Protocol for prose deliverables (BL-430, DSM_0.2 §8.10)** — The four-gate Pre-Generation Brief Protocol gains an explicit prose-deliverable shape: Gate 1 confirms purpose / audience / outcome / length / scope, Gate 2 proposes a TOC with per-section length budgets, Gate 3 drafts ONE section at a time with per-section user review and approval before the next, Gate 4 reviews the assembled document for cross-section consistency. Closes the gap §8 left for prose, where the agent's default reading of "produce the artifact at Gate 3" was collapsing to "produce the whole document at Gate 3," yielding 2000-3500 word full-file Write operations that defeated per-section review and the Take a Bite philosophy. Trigger is document type, not length. §17.1 alignment template gains a Pre-Generation Brief Protocol reinforcement bullet so spokes inherit the rule via `/dsm-align`. Origin: haystack-magic S8 R3 hiring challenge produced two structured documents (~2565 + ~3519 words) by full-file Write; the first carried a load-bearing factual error (misattributed deepset 5-Step Guide labels) that escaped into the SUBMITTED deliverable because per-section review never happened.
- **F-127 (2026-05-05) Concurrent-Session Detection Protocol (BL-431, DSM_0.2.A §26)** — A session lockfile at `.claude/session.lock` prevents silent concurrent-session data hazards (interleaved transcripts, conflicting baselines, race conditions on staged changes, MEMORY drift). `/dsm-go` Step 0.7 hard-halts when the lockfile is present, with three resolution options: wrap up the existing session, force-concurrent (crashed-session recovery only), or manual `rm`. The lockfile WRITE happens at end of Step 6 so the `transcript_anchor` field reflects the post-reset state. All three primary wrap-ups (full / light / quick) clear the lockfile in their final step. `/dsm-parallel-session-go` is exempted because parallel sessions are concurrent siblings by design via the commit booking system. Origin: heating-systems-conversational-ai S10.L2 (2026-04-29) where two parallel Claude Code conversations operated the same branch with no awareness, surfacing only when `git status` showed entries the active agent had not authored.
- **F-126 (2026-05-05) Non-Suppressible Prompts Convention (BL-432, DSM_0.2 §8.9.1)** — A prompt classification that auto mode must honor regardless of explicit suspension. §8.9 already established that auto mode does NOT collapse Gate 1 pauses or §19/§21.3 testing requirements; §8.9.1 closes the gap for procedural safety prompts living inside skill files (not inside Gate 1/2/3 cycles). Initial scope: `/dsm-go` Step 0.7 (concurrent-session halt), Step 2a.6 (default-branch verification), Step 5.9 (light-wrap-up continuation, the original motivating site). Skill files carry a `**Non-suppressible (per DSM_0.2 §8.9.1):**` marker line above the prompt. Origin: heating-systems S10.L2 where auto mode silently bypassed Step 5.9's continuation prompt; the agent recognized the prompt's existence in its thinking block, then unilaterally pressed past it. The user was never given the choice §5.9 mandates.
- **F-125 (2026-05-05) Skill Scope Is Authoritative principle (BL-435, DSM_0.2 §8.6.1)** — Sibling sub-section under §8.6 generalizing the lesson BL-434 fixed at the specific Command sync wording level. §8.6 prevents memory-based claims about skill behavior; §8.6.1 prevents augmentation, where the agent invokes a skill correctly, then runs adjacent off-scope checks and folds findings into the skill's report. Core: "Silence from the skill on a concern is the skill's answer." Three handling options for adjacent checks: out-of-band audit with its own distinct label, file a BL to extend the skill's scope, or skip the check. Distinguishes composition (using one skill's output as another's input, allowed) from augmentation (folding off-skill findings into a skill's report, forbidden). Origin: heating-systems S10 where /dsm-align Step 11 was correctly skipped on a spoke and the agent then ran an out-of-scope `diff -q` and folded `Drifted: 2` into /dsm-align's report.
- **F-124 (2026-05-05) /dsm-staa Step 8 regenerate compact reasoning-lessons mirror (BL-433, `scripts/commands/dsm-staa.md`)** — `/dsm-staa` now regenerates `.claude/reasoning-lessons-compact.md` after Step 6 append + Step 7 prune complete. Closes the staleness window between `/dsm-staa` runs and the next `/dsm-wrap-up` (potentially 24+ hours), during which `/dsm-go` Step 1.5 reads a stale boot-time canonical context. The transform implements the same rule `/dsm-wrap-up` Step 0 describes in prose; behaviorally identical output verified by byte-diff against the current compact mirror. The auto-generated comment in the mirror header references both regenerators ("/dsm-wrap-up Step 0 or /dsm-staa Step 8") so provenance is honest. Origin: haystack-magic S7 STAA continuation where /dsm-staa appended 6 [STAA] entries and pruned 2 [auto] entries, leaving the mirror 13 minutes stale and missing 6 lessons.
- **F-123 (2026-05-05) /dsm-align Step 12 conditional `Command sync` spec (BL-434, `scripts/commands/dsm-align.md`)** — Replaces enumerated values with a conditional default for the `Command sync` line in /dsm-align Step 12 report template. Spoke runs (Step 11 skipped) emit `Command sync: N/A (not DSM Central)` verbatim; DSM Central runs (Step 11 ran) emit populated `OK: N | Drifted: N | Missing: N` counts. Closes the "blank field invites invention" failure mode where the agent ran an out-of-scope `diff -q` on user-scope command files and populated the field with fabricated `Drifted: 2`, costing ~115 transcript lines of correction. Origin: heating-systems-conversational-ai S10 (2026-04-23). Sibling fix to F-125 / §8.6.1 which generalizes the lesson.

## Reference

- CHANGELOG entry: `CHANGELOG.md` v1.9.0 section (commit 74b6d92)
- feature-trail rows: `dsm-docs/blog/feature-trail.md` v1.9.0 section (BL number, origin, inbox source, meta-pattern per row)
- TAB mirror: synced via PR #76 + tagged v1.9.0 at sync commit
