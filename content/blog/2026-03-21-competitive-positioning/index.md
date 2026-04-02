---
title: "Where DSM sits: mapping 15 AI collaboration tools on three axes"
date: 2026-03-21
draft: true
description: "We scored 15 AI development tools on three axes, scored competitors before ourselves, challenged our own numbers, and found a gap we did not expect."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Competitive Positioning", "Take AI Bite"]
categories: ["Positioning"]
author: "Alberto Diaz Durana"
showToc: true
ShowReadingTime: true
---

Every AI tool answers the same question: how should humans and AI work together?

The answers tend to split into two camps.

**Camp 1: make AI faster.** Most tools optimize for throughput. Give the AI more autonomy, skip permissions, run agents in parallel, let the machine handle it. The human sets goals and reviews results. GSD (27K+ stars) recommends skipping permissions. Devin runs autonomously. autoresearch experiments overnight without human oversight.

**Camp 2: make collaboration deliberate.** DSM treats human oversight as a design goal. The human approves every artifact before it exists. Sessions capture reasoning. Experience accumulates across projects and feeds back into the methodology itself.

The difference is not speed vs. quality. It is who learns. In Camp 1, the AI executes and the human reviews. In Camp 2, the human and the AI build understanding together, and that understanding compounds over time.

That is a strong claim. We tried to test it.

---

## Three axes

To move beyond assertion, we defined three measurable dimensions. Each axis has a 5-level rubric with observable indicators, defined before any system was scored.

| Axis | What it measures | Scale |
|------|-----------------|-------|
| Human Oversight | How much human control per unit of work | 1 (per-turn gating) to 5 (full autonomy) |
| Knowledge Provenance | Who authored the agent's operating knowledge | 1 (pretrained only) to 5 (curated ecosystem) |
| Experience Accumulation | Whether the system learns from collaboration | 0 (stateless) to 5 (distributed methodology evolution) |

We scored 15 systems: 12 competitors first (alphabetically), DSM last. This ordering prevents unconsciously calibrating the scale around our own strengths.

After initial scoring, we ran a devil's advocate pass, systematically challenging every DSM score and asking where competitors could score higher. No scores changed, but the reasoning is documented. The full rubric, scoring matrix, and audit trail are in the [positioning map source](https://github.com/albertodiazdurana/take-ai-bite).

---

## The maps

Three 2D views, one for each dimension pair.

### Human oversight vs. knowledge provenance

{{< figure src="/images/blog/competitive-positioning/oversight-vs-provenance.png" alt="Scatter plot showing Human Oversight vs Knowledge Provenance for 15 AI tools. DSM is isolated in the top-left corner at maximum provenance and maximum oversight." caption="DSM in the top-left: maximum human oversight, maximum knowledge provenance. The nearest system (Kilo Code at X=2, Y=3.5) is one full step more autonomous and 1.5 steps lower on provenance." >}}

Most tools cluster in the middle band (X=2-4, Y=3-3.5): similar provenance depth (project-scoped rules), varying oversight models. The bottom-right corner (Devin, OpenHands) is the Camp 1 extreme: minimal knowledge, maximum autonomy.

DSM sits in the top-left corner alone. No other system combines human-curated knowledge at that depth with per-turn gating.

### Human oversight vs. experience accumulation

{{< figure src="/images/blog/competitive-positioning/oversight-vs-experience.png" alt="Scatter plot showing Human Oversight vs Experience Accumulation for 15 AI tools. DSM is isolated in the top-left corner, two full levels above any competitor on the experience axis." caption="DSM at (1, 5): maximum oversight and the only Level 5 on experience accumulation. The gap to Picobot (Level 3) is two full levels, with Level 4 empty." >}}

This was the view we did not expect. Level 4 on the experience axis (cross-session, human-curated) is empty: no system has that capability without also having distributed methodology evolution. It looks like DSM's Level 4 mechanisms (versioned memory, reasoning lessons, session transcript analysis) are prerequisites for Level 5, not a standalone category that other tools are approaching from below.

### Knowledge provenance vs. experience accumulation

{{< figure src="/images/blog/competitive-positioning/provenance-vs-experience.png" alt="Scatter plot showing Knowledge Provenance vs Experience Accumulation for 15 AI tools. DSM is isolated in the top-right corner." caption="DSM at (5, 5): both deep curated knowledge and distributed experience accumulation. All competitors cluster in the bottom-left quadrant." >}}

This view removes the oversight axis entirely. Even setting aside per-turn gating, DSM still sits alone: no other system pairs deep human-authored knowledge with a functioning experience accumulation architecture.

---

## Experience accumulation: the widest gap

The experience axis is where the distance to the nearest competitor is largest, two full levels.

{{< figure src="/images/blog/competitive-positioning/experience-accumulation-bars.png" alt="Horizontal bar chart showing Experience Accumulation scores for all 15 systems. DSM at Level 5, Picobot at Level 3, then a cluster of systems at Level 0-2.5." caption="Experience accumulation by system. DSM at Level 5; Picobot at Level 3 is next. Most systems are stateless or session-scoped." >}}

The five levels:

| Level | What it means | Systems |
|-------|--------------|---------|
| 0: Stateless | Each session starts identically | Devin, OpenHands |
| 1: Session-scoped | Experience persists within a session, resets at end | GSD, BMAD, Cline, claude-sci-skills |
| 2: Project-scoped | Experience persists across sessions, scoped to one project | Kilo Code, Kiro, Paperclip |
| 3: Cross-project (agent) | Experience propagates across projects via agent mechanisms | Picobot |
| 4: Cross-session (human-curated) | *Empty: no system occupies this level* | -- |
| 5: Distributed evolution | Experience propagates outward to improve the methodology for all future sessions | DSM |

Level 4 being empty matters. It means no tool is one feature away from what DSM does. The gap is architectural.

---

## Neutrality: how we tried to keep ourselves honest

Positioning analyses are inherently biased. The author wants to look good. We know this about ourselves, so we built in five safeguards:

### The single-practitioner limitation

One genuine weakness: DSM's Level 5 claim on experience accumulation is architecturally valid (the hub-spoke feedback mechanism works and has been field-tested across 15+ projects) but all evidence comes from one practitioner. The mechanism supports multi-practitioner evolution; the data does not yet prove it. A skeptical reader could argue this drops DSM to Level 4, which would still leave it alone at the top.

---

## What this means

If you have automated tests and want maximum throughput, Camp 1 tools like GSD are a reasonable choice. If your work involves judgment calls and you care about retaining what you learn across projects, DSM is the only option we found that was built for that.

We went in expecting to find competitors closer to DSM's position. We did not. Whether that gap stays open is a different question, and one we plan to keep tracking.

---

*The full scoring rubric, devil's advocate analysis, and gap analysis are published in the [Take-AI-Bite repository](https://github.com/albertodiazdurana/take-ai-bite). The competitive analysis is a living document, updated as new tools emerge.*
