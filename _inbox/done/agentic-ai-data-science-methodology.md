### [2026-04-11] FEATURES.md update (v1.4.15) — blog material

**Type:** Notification
**Priority:** Medium
**Source:** DSM Central S183

One new F-entry in v1.4.15 worth considering for blog coverage:

- **F-100 (2026-04-11) `/dsm-align` External Contribution governance scaffold**

### Story arc candidates

1. **"Fix the code, not the data" meta-pattern.** The BL-348 tier-1 detection originally read only the Project type field. During a mid-session audit of IronCalc, the agent's first instinct was to recommend that IronCalc rewrite its CLAUDE.md to put "External Contribution" in the Project type field (a valid-sounding convention fix). The user pushed back with a factual question ("isn't this already defined in lines 6-7?"), which surfaced the real problem: the data was correct, the detector was the bug. 3-line patch landed. Generalizable meta-pattern for human-AI collaboration: detectors that fail on legitimate data must be fixed, not the data; asking the data to conform to the detector compounds over time.

2. **Two-tier detection as a robustness pattern.** BL-348's EC detection is metadata first (read CLAUDE.md alignment section), filesystem fallback second (check for upstream project markers + absence of `dsm-docs/` and `scripts/commands/`), with a user confirmation gate on the fallback path. Both tiers handle a different lifecycle stage (configured vs first-run) and both fail gracefully. Parallel to fail-safe defaults in safety-critical code.

3. **Cross-repo write gate as "necessary, not a problem".** BL-348 writes to a governance folder in a separate repo during scaffold creation. Tension: /dsm-go Step 1.8 runs /dsm-align unconditionally, which could imply "no interruptions". Resolution in S183: the cross-repo confirmation IS the safety mechanism, not friction. First session gets the prompt, subsequent sessions skip via idempotent pass-through. Reusable insight for agent-triggered workflows that occasionally need explicit consent.

### Cross-references

- BL-348 (implemented S183): `dsm-docs/plans/done/BACKLOG-348_dsm-align-external-contribution-governance-scaffold.md`
- BL-347 (prerequisite rename): `dsm-docs/plans/done/BACKLOG-347_rename-collaboration-storage-to-external-contribution-storage.md`
- BL-349 (spawned, /dsm-go EC governance inbox): `dsm-docs/plans/BACKLOG-349_dsm-go-ec-governance-inbox-check.md`
- CHANGELOG v1.4.15 entry
- feature-trail.md F-100 row
- IronCalc audit inbox: `~/dsm-external-contribution-storage/IronCalc/_inbox/2026-04-11_dsm-central-s183_audit-recommendations.md`

### [2026-04-13] Blog journal: "The Architecture You Didn't Design" — planned emergence observation

**Type:** Notification
**Priority:** High
**Source:** DSM Central S188

New blog journal entry in `dsm-docs/blog/journal.md` with a meta-observation
about DSM's own evolution that showcases TAB's core philosophy.

**Core narrative:** A Feb 2026 research folder proposed a deliberate multi-agent
architecture (Research Agent, Graph Explorer as structural arm, gateway reviews,
file-based communication). The same architecture emerged bottom-up from solving
methodology problems: `/dsm-align` became the scaffold generator, `_inbox/`
became the message bus, mirror sync became propagation, the `@` chain became
config distribution. The protocols ARE the architecture.

**Key angle:** Sequel to ["The Trainer and the Agents"](https://take-ai-bite.com/blog/2026-04-02-trainer-and-agents/).
That post introduced the metaphor (Dragon = bidirectional partnership). This
observation provides empirical evidence: the Feb research is the "dragon's
first flight plan," the realized architecture is what happened when trainer
and dragon flew together.

**6 differentiator points included** (TAB is not boilerplate, not average,
addresses unmet need, magnifies uniqueness, solves complex problems iteratively,
methodology is a training mechanism). Point 6 was the agent's suggestion,
itself evidence of bidirectional training.

**Screenshot for blog:** `C:\Users\adiaz\OneDrive\Bilder\Screenshots\2026-04-13 203523 - bonding.png`
Captures the live transcript moment (lines 363-373) where the agent produced
the "methodology as training mechanism" insight and the human recognized it as
evidence of the bond. Visual proof of the claim being made.

**Closing tease:** "You're not configuring a tool. You're training YOUR agent."
(Connects to HTTYA vision without revealing it.)

**Principle decision (final):** BL-357 "Contribution, Not Protocol, Not Output"
filed as DSM_6.0 §1.10 restructure. Three-part principle:
- §1.10 "Contribution, Not Protocol, Not Output" (parent, philosophical anchor)
- §1.10.1 "We Need to Talk" (human→agent: structured delivery)
- §1.10.2 "The Methodology is the Training Ground" (bidirectional: practice shapes both)

**The naming journey IS blog material.** The S188 transcript documents:
the philosophical reflection on why vocabulary fails (emotional terms vs
technical reductions), the ChatGPT zero-context contrast (50 correct but
weightless names), and the resolution through contrast ("after so much lyric
philosophy, a cutting form builds a nice contrast").

**Source material:**
- **S188 session transcript (full reasoning chain):** `~/dsm-agentic-ai-data-science-methodology/.claude/transcripts/2026-04-13T18:22-ST.md` (582 lines). Read this file for the complete conversation including critical analysis, philosophical reflection, proposed-vs-realized mapping, ChatGPT contrast, naming journey, and principle formulation.
- Blog journal entry: `~/dsm-agentic-ai-data-science-methodology/dsm-docs/blog/journal.md` (2026-04-13 entry)
- Original research: `~/dsm-agentic-ai-data-science-methodology/dsm-docs/research/done/Multi-Agent-Architecture/` (2 files)
- Published predecessor: https://take-ai-bite.com/blog/2026-04-02-trainer-and-agents/
- BL-357: `~/dsm-agentic-ai-data-science-methodology/dsm-docs/plans/BACKLOG-357_contribution-not-protocol-not-output-principle.md`
- Screenshot (bonding moment): `C:\Users\adiaz\OneDrive\Bilder\Screenshots\2026-04-13 203523 - bonding.png`