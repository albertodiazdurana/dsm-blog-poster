---
title: "What Makes DSM Different: 84 Features Across Three Dimensions"
date: 2026-03-20
draft: false
description: "Most AI tools optimize for speed. DSM optimizes for collaboration quality. Here are 84 features mapped across three dimensions that define its position."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Features", "Take AI Bite"]
categories: ["Features"]
author: "Alberto Diaz Durana"
showToc: true
ShowReadingTime: true
---

Most AI coding tools optimize for speed: get to the answer faster, automate more, reduce human involvement. Take-AI-Bite's DSM takes a different position entirely. It optimizes for *collaboration quality*: ensuring that the human and the AI produce better work together than either could alone, and that the quality compounds over time.

This post maps DSM's 84 features across the three dimensions that define its competitive position: human oversight depth, knowledge provenance, and experience accumulation. Each dimension represents a design choice that most tools either ignore or address superficially.

For the full chronological feature list, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md).

---

## Dimension 1: Human Oversight -- Collaboration, Not Automation

Where most tools give you a slider between "approve everything" and "let the AI run," DSM builds oversight into the structure of every interaction. The human is not a bottleneck to be optimized away; the human is the quality signal that makes everything else work.

### Per-Turn Artifact Review

Every artifact the AI creates passes through a three-gate approval model: concept approval (do you understand what will be created?), implementation approval (does the diff look right?), and run approval (should this execute?). Each gate is an explicit stop. The AI cannot proceed without the human engaging with the work.

This extends to collections: when producing multiple items, each gets individual attention. Multiple edits to a single file require separate explanations. Notebook cells are generated one at a time, with actual output verified before the next cell is created.

### Session Lifecycle Management

Sessions are not just "start coding, stop coding." Each session has a structured start that checks inbox messages, validates the project state, compares versions, and loads accumulated context. Each session ends with a structured wrap-up that saves memory, commits work, and creates continuity documents. If a session ends unexpectedly, the next session detects the gap and offers recovery.

Lightweight sessions preserve continuity for quick follow-ups. Session baselines track exactly what changed. Configuration recommendations match the AI's settings to the planned work scope.

### Safety Guardrails

Destructive commands are never auto-approved: force push, hard reset, recursive delete each require explicit human request. Sensitive files (.env, credentials) are automatically blocked from commits. External inputs are sanitized before processing. Feature branches must be tested before merging.

These are not "opt-in safety features." They are structural constraints that cannot be bypassed without the human explicitly choosing to do so.

---

## Dimension 2: Knowledge Provenance -- Human-Curated, Not Pre-Trained

Most AI tools start with a blank slate for every project: a generic model with maybe a project-specific config file. DSM starts with a versioned, human-authored knowledge ecosystem that the AI inherits, follows, and contributes to.

### Methodology Document Ecosystem

DSM is not a single instruction file. It is a suite of versioned documents covering data science workflows (DSM 1.0), project management (DSM 2.0), cross-project governance (DSM 3.0), software engineering (DSM 4.0), documentation standards (DSM 5.0), and AI collaboration principles (DSM 6.0). Each document is maintained with semantic versioning and a formal update workflow.

Project-specific instructions reference the methodology via a configuration chain, so every project inherits the full protocol suite while retaining the ability to override specific rules.

### Cross-Project Protocol Inheritance

The hub-spoke architecture means protocols are authored once in the central repository and inherited by all projects automatically. When a protocol improves, every project benefits. Project type detection activates the right methodology track for each project. Participation patterns adjust communication and isolation rules based on whether a project is a standard spoke, an external contribution, or a private project.

The ecosystem path registry maps cross-repository relationships, enabling automated synchronization. Mirror repos receive methodology updates automatically.

### Versioned Knowledge Architecture

Every change to the methodology is tracked in a changelog, tagged with semantic versions, and checkpointed with detailed context. Design decisions are numbered and documented with rationale and alternatives. Research findings are preserved with source URLs and date stamps.

This is not documentation for documentation's sake. It is the mechanism that prevents knowledge loss. When a protocol decision was made six months ago, the rationale is recoverable. When research informed a design choice, the original evidence is traceable.

---

## Dimension 3: Experience Accumulation -- Learning Across Sessions

This is DSM's strongest differentiator. Most tools treat each session as independent. Some persist project-level memory. DSM builds a learning system where experience from individual sessions propagates outward to improve the methodology for all future sessions across the entire ecosystem.

### Memory and Context Persistence

MEMORY.md provides persistent, typed memory across conversations: user preferences, project decisions, feedback patterns, and reference pointers. The session transcript captures reasoning in real time, creating a complete record of *why* decisions were made, not just what was done. Context budget management treats the AI's context window as a finite resource with explicit controls.

Handoffs ensure complex pending work survives session boundaries. Checkpoints snapshot project state at milestones. Session baselines enable precise diff tracking. When a session ends unexpectedly, transcript-based recovery reconstructs the missing wrap-up artifacts.

### Feedback Loops Across Projects

Spoke projects generate backlog proposals and methodology observations for the central repository, creating a systematic learning loop. At session end, feedback is automatically pushed to the central inbox. The inbox system routes notifications between projects with a processed/done lifecycle.

A single spoke project generated 42 backlog proposals and 53 methodology observations, demonstrating that this is not a theoretical capability: it operates at scale, producing concrete improvements to the shared methodology.

### Reasoning Pattern Extraction

Session transcripts are not just logs. They are mined for reasoning patterns that become formal guidance for future sessions. The experiment framework ensures capability tests are reproducible and their results feed back into the methodology. Stress testing compares guided vs unguided AI collaboration to measure the actual impact of structured protocols.

External observations generate backlog items automatically. The "Earn Your Assertions" principle ensures claims are verified, not assumed. "Critical Thinking" requires the AI to challenge its own outputs. These are not passive values: they are active protocols that shape every interaction.

---

## The Compound Effect

No single feature in this list is revolutionary on its own. Pre-generation briefs, memory systems, and feedback loops exist in various forms elsewhere. What makes DSM different is that all 84 features work together as a system, and that system *learns*.

A feedback observation from a spoke project becomes a backlog item in the central repository. That backlog item becomes a protocol change. That protocol change propagates to every project via the hub-spoke architecture. The next session in any project benefits from an insight that originated in a completely different context.

This is the compound effect that no individual feature can replicate: the methodology improves itself through use.

---

*For the full chronological feature timeline, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md). For the competitive positioning analysis behind these three dimensions, see the [3D Positioning Map](https://github.com/albertodiazdurana/take-ai-bite/blob/main/dsm-docs/research/DSM-Rebranding/2026-03-18_competitive-positioning-map.md).*
