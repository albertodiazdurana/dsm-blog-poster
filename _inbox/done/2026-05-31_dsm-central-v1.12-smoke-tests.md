### [2026-05-31] FEATURES update from DSM Central (v1.12.0)

**Type:** FEATURES Notification
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology (DSM Central)

1 new F-entry shipped in v1.12.0 (S213, BL-452).

**F-133 (2026-05-31) Smoke tests as a named DSM artifact (BL-452, DSM_4.0.A §7 + DSM_4.0 §4.1 + DSM_2.0.C)** — The per-item smoke-test practice (a small, fast check run after each file is built, with the command and result written down) now has a canonical home in DSM. DSM_4.0.A §7 names the artifact, gives it a canonical spoke location (`dsm-docs/guides/smoke-tests.md`, created lazily and appended to as the build progresses), specifies the structure (per-file sections, command/Expected/Result, optional dated log), and distinguishes it from `/verify` and unit tests. It is framed as the industry-standard smoke-test practice (McConnell *Code Complete*; Microsoft daily-build) given a repo home, not a DSM coinage. A pointer sits in DSM_4.0 §4.1 and a soft N/A-able check in the Sprint Boundary Checklist. Origin: traveline-ds-project-skeleton S1, where ~80 lines of validation commands the user ran lived only in transcript context with no place to persist.

**Context for a blog angle:** this feature is a clean "name the industry-standard practice, give it a repo home, don't coin a term" story. Two sub-threads worth surfacing: (1) the practice was discovered live during a real interview-prep build (~4 hours before a pairing interview), and (2) Gate-1 grounding reshaped the proposal before any edit landed (the proposed DSM_0.1 canonical-list edit was dropped once the agent read that §10 is a folder-only table). Feature-trail row: `dsm-docs/blog/feature-trail.md` F-133.
