**Status:** Done , superseded
**Date Completed:** 2026-05-12 (Session 22)
**Closure:** Absorbed by BL-022 (cumulative v1.5-v1.9 multi-front release coverage). The features-post update scope this BL named lives in BL-022 Front B.

# BL-021: Features post update for DSM v1.7-v1.9 (114 to 129)

**Status:** Open
**Priority:** Medium
**Date Created:** 2026-05-12 (Session 22)
**Source:** `_inbox/dsm-agentic-ai-data-science-methodology.md` (4 accumulated notifications: v1.7.0, v1.8.0, S205 mid-version, v1.9.0)
**Origin:** Project rule "DSM Version Release Coverage" in CLAUDE.md. The canonical features post must match FEATURES.md after each DSM version. Inbox accumulated through three minor versions (v1.7.0, v1.8.0, v1.9.0) without the features post being updated; user surfaced the catch-up at session start.

## Problem statement

The canonical features post at `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` claims **114 features across three dimensions** (last updated S21, aligned with DSM v1.6.3). The current count in DSM Central's `FEATURES.md` is **129** as of v1.9.0 (2026-05-05). The blog post is 15 features behind.

The post has six occurrences of the literal "114" (title, description, opening paragraph, closing paragraph) that need to move to 129. More importantly, 14 new F-entries (F-115 through F-128) need to be woven into the three dimensions (Human Oversight, Knowledge Provenance, Experience Accumulation) where they belong, otherwise the count update would assert the new total without showing the work.

Note on the off-by-one: the post said "114" at S21 but FEATURES.md ceiling at that time was F-114. The new ceiling F-128 plus the running total of 129 in FEATURES.md gives a delta of +15. One earlier feature was either added retroactively or the S21 count was slightly off; either way, the authoritative target is the live `grep -c` on FEATURES.md.

## Inbox contents (consolidated)

The single accumulated inbox file lists 4 push events with 14 new F-entries:

### v1.7.0 (2026-04-23) - 3 features

| F# | Title | BL | DSM ref | Story angle |
|----|-------|------|---------|-------------|
| F-115 | Gate 1 parallel offload analysis | BL-409 | DSM_0.2 §8.8 + DSM_6.0 §1.12 | "Don't be a Hero, Delegate the Effort" foundational principle |
| F-116 | /dsm-go context efficiency | BL-413 | - | Sonnet session economics; 40-55% session-start context reduction |
| F-117 | Checkpoint step in /dsm-wrap-up | BL-414 | - | MEMORY/checkpoint split rebalanced |

### v1.8.0 (2026-04-24) - 3 features (closure release for dead-pointer problem class)

| F# | Title | BL | DSM ref | Story angle |
|----|-------|------|---------|-------------|
| F-118 | Mirrored methodology BL-reference scrub | BL-418 | - | 174 edits, 26 files; resolvable identifiers replace ~170 BL anchors |
| F-119 | BL Lookup Index | BL-419 | `dsm-docs/plans/done/INDEX.md` | Third governance axis (BL# alongside CHANGELOG chronology and FEATURES capabilities); 332 rows |
| F-120 | Checkpoint Authoring Identifiers Rule | BL-420 | DSM_0.2.A §10.2.1 | Forward-only dead-pointer prevention; two-condition exception for in-flight BL checkpoints |

### S205 mid-version (2026-04-29) - 2 features

| F# | Title | BL | DSM ref | Story angle |
|----|-------|------|---------|-------------|
| F-121 | Research folder index maintenance skills | BL-425 | `/dsm-research-add` + `/dsm-research-done` | Parity-by-skill across sibling folders (plans/, research/) |
| F-122 | Compact reasoning-lessons mirror | BL-427 | DSM_0.2.A §8.1 | Source-of-truth / derived-mirror separation; empirical surprise (5% trim vs 25-30% projected) |

### v1.9.0 (2026-05-05) - 6 features (inbox-derived backlog landing pass)

| F# | Title | BL | DSM ref | Story angle |
|----|-------|------|---------|-------------|
| F-123 | /dsm-align Step 12 conditional Command sync | BL-434 | `scripts/commands/dsm-align.md` | Blank field invites invention; specific-fix sibling to F-125 |
| F-124 | /dsm-staa Step 8 regenerate compact mirror | BL-433 | `scripts/commands/dsm-staa.md` | Staleness-window closure; honest dual-regenerator provenance |
| F-125 | Skill Scope Is Authoritative principle | BL-435 | DSM_0.2 §8.6.1 | Silence-from-the-skill rule; composition vs augmentation |
| F-126 | Non-Suppressible Prompts Convention | BL-432 | DSM_0.2 §8.9.1 | Auto-mode bypass closure; explicit marker line above prompts |
| F-127 | Concurrent-Session Detection Protocol | BL-431 | DSM_0.2.A §26 | Session lockfile; hard-halt with 3 resolution paths |
| F-128 | Chunked Drafting Protocol for prose | BL-430 | DSM_0.2 §8.10 | Four-gate model gains per-section prose shape; haystack-magic S8 hiring-challenge factual error origin |

All 14 features are listed in the inbox file with full DSM_0.2 cross-references, origin incidents, and meta-pattern angles. The post does not need fresh reconstruction; the inbox carries the writeable material.

## Dimension mapping (proposed, validate during drafting)

The post's three dimensions absorb the 14 new features unevenly. Initial mapping:

**Human oversight**
- F-115 (Gate 1 parallel offload, user-approved orchestration)
- F-126 (Non-suppressible prompts, auto-mode bypass closure)
- F-128 (Chunked drafting protocol, per-section review preserved)
- F-127 (Concurrent-session detection, hard-halt for safety)

**Knowledge provenance**
- F-118 (BL-reference scrub, resolvable identifiers)
- F-119 (BL Lookup Index, third governance axis)
- F-120 (Checkpoint authoring identifiers, dead-pointer prevention)
- F-121 (Research folder index maintenance)
- F-125 (Skill scope is authoritative, silence-as-answer rule)
- F-123 (Conditional Command sync wording)

**Experience accumulation**
- F-116 (Context efficiency, session-start budget)
- F-117 (Checkpoint step in wrap-up)
- F-122 (Compact reasoning-lessons mirror)
- F-124 (/dsm-staa regenerates compact mirror)

Validate during drafting: F-125 and F-123 might fit better under Human Oversight (both are about the agent staying inside its scope). F-127 might fit better under Experience Accumulation (the lockfile carries state across boundaries). The mapping is provisional.

## Success criteria

1. Post total count updated everywhere: 114 to 129 (title, description, opening, closing, anywhere the literal appears).
2. Each of the 14 new F-entries woven into the appropriate dimension as a one to two sentence integration (not a list, a narrative thread).
3. No mechanical feature list. The post keeps its story shape: features serve the dimension's argument.
4. Voice calibration (`content/about-me.md` + `content/about.md`) and /humanizer pre-publish gate.
5. LinkedIn cross-post added to `dsm-docs/blog/linkedin-posts.md` if a post is published. (Optional: post-update may not warrant a fresh LinkedIn post; user decides.)

## Out of scope

- **Dedicated release posts for v1.7-v1.9.** That work belongs in a separate BL (the v1.5/v1.6 release post is BL-018, still open; v1.7-v1.9 release coverage is unscoped and likely needs its own BL or a BL-018 scope expansion). BL-021 is the count-and-weave update only.
- **Reconciling the off-by-one between S21's 114 and the +14 delta.** Use the live `grep -c` on FEATURES.md as the authoritative count; the historical drift is not worth excavating.

## Notes

- Verification command before publishing: `grep -cE '^- \*\*F-[0-9]+' ~/dsm-agentic-ai-data-science-methodology/FEATURES.md`. Whatever that returns is the count the post must claim.
- The inbox file is the consolidated reading material; no need to re-read each v1.7/v1.8/v1.9 source.
- BL-018 (v1.5.x/v1.6.x release post) remains open with its original scope. The question of whether to extend it to v1.7-v1.9 release coverage, or to file a new BL for v1.7-v1.9 release posts, is a user decision and not part of BL-021.
