# BL-017: "Fix the Code, Not the Data" Blog Post (combined with IronCalc content)

**Priority:** Medium
**Source:** Inbox 2026-04-11 (DSM Central S183, FEATURES.md v1.4.15)
**Trigger:** When additional IronCalc-related content arrives and can be combined

## Framing note (2026-04-14, S20)

Not to be written as a standalone post. The "fix the code, not the data" meta-pattern is strong but the single /dsm-align incident is thin for a dedicated post. More IronCalc-related material is expected from DSM Central (the External Contribution work is active), and the content will be richer when batched with those future stories. Keep this BL as a pointer to the meta-pattern until a companion narrative lands.

## Description

Blog post covering DSM v1.4.15 via the reconstruction trail (per the "DSM Version Release Coverage" rule in CLAUDE.md). Feature in scope: F-100 `/dsm-align` External Contribution governance scaffold (BL-348).

## Story arc candidates

Three narrative threads surfaced in the inbox source, any of which could be the headline:

1. **"Fix the code, not the data" meta-pattern.** During a mid-session audit of IronCalc, the BL-348 tier-1 detection originally read only the Project type field. The agent's first instinct was to recommend that IronCalc rewrite its CLAUDE.md to put "External Contribution" in the Project type field, a valid-sounding convention fix. The user pushed back with a factual question ("isn't this already defined in lines 6-7?"), which surfaced the real problem: the data was correct, the detector was the bug. Three-line patch landed. Generalizable meta-pattern for human-AI collaboration: detectors that fail on legitimate data must be fixed, not the data; asking the data to conform to the detector compounds over time.

2. **Two-tier detection as a robustness pattern.** BL-348's EC detection is metadata first (read CLAUDE.md alignment section), filesystem fallback second (check for upstream project markers + absence of `dsm-docs/` and `scripts/commands/`), with a user confirmation gate on the fallback path. Both tiers handle a different lifecycle stage (configured vs. first-run) and both fail gracefully. Parallel to fail-safe defaults in safety-critical code.

3. **Cross-repo write gate as "necessary, not a problem".** BL-348 writes to a governance folder in a separate repo during scaffold creation. Tension: `/dsm-go` Step 1.8 runs `/dsm-align` unconditionally, which could imply "no interruptions." Resolution: the cross-repo confirmation IS the safety mechanism, not friction. First session gets the prompt, subsequent sessions skip via idempotent pass-through. Reusable insight for agent-triggered workflows that occasionally need explicit consent.

## Recommended angle

Arc 1 is the strongest hook (concrete incident, memorable meta-pattern, generalizable beyond DSM). Arcs 2-3 become supporting material.

## Reconstruction trail (per CLAUDE.md rule)

1. Index: `~/dsm-agentic-ai-data-science-methodology/dsm-docs/blog/feature-trail.md` (v1.4.15 section)
2. BL file: `~/dsm-agentic-ai-data-science-methodology/dsm-docs/plans/done/BACKLOG-348_dsm-align-external-contribution-governance-scaffold.md`
3. Related BLs: BACKLOG-347 (rename prerequisite), BACKLOG-349 (follow-up for `/dsm-go` EC inbox check)
4. Inbox origin: IronCalc audit at `~/dsm-external-contribution-storage/IronCalc/_inbox/2026-04-11_dsm-central-s183_audit-recommendations.md`
5. CHANGELOG: v1.4.15 entry in DSM Central
6. Reasoning lessons: check `~/dsm-agentic-ai-data-science-methodology/.claude/reasoning-lessons.md` for S183 `[auto]` or `[STAA]` entries

## Companion task

Per the "DSM Version Release Coverage" rule, also update the canonical features post at `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` (count + weave F-100 into the appropriate dimension). This may overlap with BL-015 (features post 90->95) if v1.4.15's new features can be batched.

## Workflow

Standard blog workflow: voice calibration from `content/about-me.md` + `content/about.md`, `/humanizer` pre-publish gate.