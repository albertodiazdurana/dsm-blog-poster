---
title: "Where DSM Sits: Mapping the AI Collaboration Landscape"
date: 2026-03-21
draft: true
description: "We scored 15 AI development tools on three axes, scored competitors first, challenged our own scores, and found that DSM occupies a position no other tool approaches."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Competitive Positioning", "Take AI Bite"]
categories: ["Positioning"]
author: "Alberto Diaz Durana"
showToc: true
ShowReadingTime: true
---

Every AI tool and framework answers the same question: *how should humans and AI work together?*

The answers fall into two camps.

**Camp 1: Make AI faster.** Most tools optimize for throughput. Give the AI more autonomy, skip permissions, run agents in parallel, let the machine handle it. The human sets goals and reviews results. GSD (27K+ stars) recommends skipping permissions. Devin runs autonomously. autoresearch experiments overnight without human oversight.

**Camp 2: Make collaboration deliberate.** Take-AI-Bite's DSM is the only framework that treats human oversight as a *design goal*, not a limitation to overcome. The human approves every artifact before it exists. The session captures reasoning. Experience accumulates across projects and feeds back into the methodology itself, making every future session better.

The difference is not speed vs. quality. It is *who learns*. In Camp 1, the AI executes and the human reviews. In Camp 2, the human and the AI build understanding together, and that understanding compounds over time.

That is a strong claim. Here is the data behind it.

---

## Three Axes

To move beyond assertion, we defined a positioning framework with three measurable dimensions. Each axis has a 5-level rubric with observable indicators, defined *before* any system was scored.

| Axis | What it measures | Scale |
|------|-----------------|-------|
| **Human Oversight** | How much human control per unit of work | 1 (per-turn gating) to 5 (full autonomy) |
| **Knowledge Provenance** | Who authored the agent's operating knowledge | 1 (pretrained only) to 5 (comprehensive curated ecosystem) |
| **Experience Accumulation** | Whether the system learns from collaboration | 0 (stateless) to 5 (distributed methodology evolution) |

We then scored 15 systems: 12 competitors scored first (alphabetically), DSM scored last. This ordering prevents unconsciously calibrating the scale around our own strengths.

After initial scoring, we ran a devil's advocate pass: systematically challenging every DSM score and asking where competitors could score higher. No scores were adjusted, but the reasoning is documented. The full rubric, scoring matrix, and audit trail are available in the [positioning map source](https://github.com/albertodiazdurana/take-ai-bite).

---

## The Maps

Three 2D views, one for each dimension pair. Together they show where DSM sits relative to the field.

### Human Oversight vs. Knowledge Provenance

{{< figure src="/images/blog/competitive-positioning/oversight-vs-provenance.png" alt="Scatter plot showing Human Oversight vs Knowledge Provenance for 15 AI tools. DSM is isolated in the top-left corner at maximum provenance and maximum oversight." caption="DSM alone in the top-left: maximum human oversight, maximum knowledge provenance. The nearest system (Kilo Code at X=2, Y=3.5) is one full step more autonomous and 1.5 steps less provenance-rich." >}}

Most tools cluster in the middle band (X=2-4, Y=3-3.5): similar provenance depth (project-scoped rules), varying oversight models. The bottom-right corner (Devin, OpenHands) represents the Camp 1 extreme: minimal knowledge, maximum autonomy.

DSM occupies the top-left corner alone. No other system combines comprehensive human-curated knowledge with per-turn gating.

### Human Oversight vs. Experience Accumulation

{{< figure src="/images/blog/competitive-positioning/oversight-vs-experience.png" alt="Scatter plot showing Human Oversight vs Experience Accumulation for 15 AI tools. DSM is isolated in the top-left corner, two full levels above any competitor on the experience axis." caption="DSM at (1, 5): maximum oversight and the only Level 5 experience accumulation system. The gap to Picobot (Level 3) is two full levels, with Level 4 entirely empty." >}}

This is the most striking view. Level 4 on the experience axis (cross-session, human-curated) is empty: no system has that capability without also having distributed methodology evolution. This suggests DSM's Level 4 mechanisms (versioned memory, reasoning lessons, session transcript analysis) are architectural prerequisites for Level 5, not a standalone category that other tools are approaching from below.

### Knowledge Provenance vs. Experience Accumulation

{{< figure src="/images/blog/competitive-positioning/provenance-vs-experience.png" alt="Scatter plot showing Knowledge Provenance vs Experience Accumulation for 15 AI tools. DSM is isolated in the top-right corner." caption="DSM at (5, 5): the only system with both comprehensive curated knowledge and distributed experience accumulation. All competitors cluster in the bottom-left quadrant." >}}

This view removes the oversight axis entirely. Even ignoring DSM's per-turn gating model, it still occupies a unique position: the only system where deep human-authored knowledge combines with a functioning experience accumulation architecture.

---

## Experience Accumulation: The Deepest Gap

The experience axis deserves special attention. It represents DSM's most distinctive contribution and the dimension where the gap to competitors is largest.

{{< figure src="/images/blog/competitive-positioning/experience-accumulation-bars.png" alt="Horizontal bar chart showing Experience Accumulation scores for all 15 systems. DSM at Level 5, Picobot at Level 3, then a cluster of systems at Level 0-2.5." caption="Experience accumulation depth by system. DSM is the only Level 5; Picobot at Level 3 is the next highest. Most systems are stateless or session-scoped." >}}

The five levels of experience accumulation:

| Level | What it means | Systems |
|-------|--------------|---------|
| **0: Stateless** | Each session starts identically | Devin, OpenHands |
| **1: Session-scoped** | Experience persists within a session, resets at end | GSD, BMAD, Cline, claude-sci-skills |
| **2: Project-scoped** | Experience persists across sessions, scoped to one project | Kilo Code, Kiro, Paperclip |
| **3: Cross-project (agent)** | Experience propagates across projects via agent mechanisms | Picobot |
| **4: Cross-session (human-curated)** | *Empty: no system occupies this level* | — |
| **5: Distributed evolution** | Experience propagates outward to improve the methodology for all future sessions | DSM |

The empty Level 4 is significant. It means no tool is "almost there," one feature away from what DSM does. The gap is architectural, not incremental.

---

## Neutrality: How We Kept Ourselves Honest

Positioning analyses are inherently biased. The author wants to look good. We addressed this with five safeguards:

1. **Rubric before scoring.** All score levels with observable indicators were defined before any system was evaluated.
2. **Competitors first.** The 12 competitors were scored alphabetically before DSM was scored. This prevents calibrating the scale around DSM's strengths.
3. **Devil's advocate pass.** Every DSM score was challenged: "Where could we score lower? Where could competitors score higher?" Reasoning documented.
4. **Dimension selection audit.** We asked: "Did we choose these three axes because DSM wins on them?" The answer: axes were defined in prior research sessions, and we acknowledge alternative axes (community scale, speed) where DSM would score low.
5. **External reproducibility.** The rubric is self-contained. A third party can independently score the same systems using the published rubric and compare results.

### The Single-Practitioner Limitation

We flag one genuine risk: DSM's Level 5 claim on the experience axis is architecturally valid (the hub-spoke feedback mechanism functions and is field-tested across 15+ projects) but has been validated with one practitioner. The mechanism supports multi-practitioner methodology evolution; the evidence is single-practitioner. A skeptical reader could argue this reduces DSM to Level 4, which would still leave it alone at the top of the landscape.

---

## What This Means

The competitive landscape validates a specific positioning: DSM is the only AI collaboration framework where the human stays in the loop by design, the methodology evolves from every session, and the principles transfer to any domain.

This is not the right approach for everything. If you have automated tests and want maximum throughput, Camp 1 tools like GSD are a valid choice. If your work requires subjective judgment, context-dependent decisions, and accumulating expertise over time, DSM offers something no other tool does.

Every AI tool optimizes for speed. We optimize for understanding. Here is the data.

---

*The full scoring rubric, devil's advocate analysis, and feature gap analysis are published in the [Take-AI-Bite repository](https://github.com/albertodiazdurana/take-ai-bite). The competitive landscape is a living document, updated as new tools emerge.*
