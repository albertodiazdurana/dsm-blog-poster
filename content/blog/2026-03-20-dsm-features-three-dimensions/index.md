---
title: "90 features across three dimensions"
date: 2026-03-20
draft: false
description: "DSM's 90 features mapped across human oversight, knowledge provenance, and experience accumulation."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Features", "Take AI Bite"]
categories: ["Features"]
author: "Alberto Diaz Durana"
toc: true
---

Most AI coding tools are built to reduce human involvement. DSM is built to make human involvement worth the time: the human and the AI produce better work together than either would alone, and what they learn carries forward.

This post maps DSM's 90 features across three dimensions: human oversight, knowledge provenance, and experience accumulation. For the full chronological list, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md).

---

## Human oversight

Where most tools give you a slider between "approve everything" and "let the AI run," DSM builds oversight into the structure of every interaction.

### Per-turn artifact review

Every artifact passes through a three-gate approval model: concept (do you understand what will be created?), implementation (does the diff look right?), and run (should this execute?). The AI cannot proceed without the human engaging with the work.

This extends to collections. Multiple edits to a single file need separate explanations. Notebook cells are generated one at a time, with output verified before the next cell is created. Cells that produce plots save the figure to disk so the agent can read it back and check what it actually drew before moving on.

### Session lifecycle

Sessions are not "start coding, stop coding." Each session starts by checking inbox messages, validating project state, comparing versions, and loading context. Each session ends by saving memory, committing work, and creating continuity documents. If a session ends unexpectedly, the next session detects the gap and offers recovery.

Lightweight sessions handle quick follow-ups. Session baselines track what changed. Configuration recommendations match settings to the planned work scope. A wrap-up type marker lets the next session-start command know whether the previous session ended light or full, so the two ends of the lifecycle stay aligned. Before suggesting wrap-up, the agent now re-reads the sprint plan and checks completed deliverables against actual evidence, so "sprint complete" cannot be declared while gates are still open.

### Safety guardrails

Destructive commands (force push, hard reset, recursive delete) require explicit human request. Sensitive files (.env, credentials) are blocked from commits. Feature branches must be tested before merging. The first write to any path outside the current repository in a session requires explicit user confirmation, so an agent working in a spoke project cannot quietly write into the Hub.

These are structural constraints, not opt-in features. They cannot be bypassed without the human explicitly choosing to do so.

---

## Knowledge provenance

Most AI tools start with a blank slate: a generic model, maybe a config file. DSM starts with a versioned, human-authored knowledge base that the AI inherits and contributes to.

### Methodology documents

DSM is a suite of versioned documents: data science workflows (1.0), project management (2.0), cross-project governance (3.0), software engineering (4.0), documentation standards (5.0), and collaboration principles (6.0). Each is maintained with semantic versioning and a formal update workflow.

Project-specific instructions reference the methodology via a configuration chain, so every project inherits the full protocol suite but can override specific rules.

### Protocol inheritance

The hub-spoke architecture means protocols are authored once in the central repository and inherited by all projects. When a protocol improves, every project picks it up. Project type detection activates the right methodology track. Participation patterns adjust rules based on whether a project is a standard spoke, an external contribution, or a private repo.

A path registry maps cross-repository relationships. Mirror repos receive methodology updates automatically.

### Versioned knowledge

Every change to the methodology is tracked in a changelog, tagged with semantic versions, and checkpointed. Design decisions are numbered and documented with rationale and alternatives. Research findings are preserved with sources and dates.

The point is preventing knowledge loss. When a protocol decision was made six months ago, the rationale is recoverable. When research informed a design choice, the original evidence is still there. The same standard applies in the moment: before answering a question about a file, a definition, or a piece of documentation, the agent reads the source. No partial knowledge passing as understanding.

---

## Experience accumulation

This is where the distance to other tools is largest. Most tools treat each session as independent. Some persist project-level memory. DSM propagates experience from individual sessions outward to improve the methodology for all future work.

### Memory and context

MEMORY.md provides persistent, typed memory across conversations: user preferences, project decisions, feedback patterns, reference pointers. The session transcript captures reasoning in real time, a record of why decisions were made, not just what was done. Context budget management treats the AI's context window as a finite resource.

Handoffs ensure pending work survives session boundaries. Checkpoints snapshot project state. When a session ends unexpectedly, transcript-based recovery reconstructs the missing wrap-up.

### Feedback loops

Spoke projects generate backlog proposals and methodology observations for the central repository. At session end, feedback is pushed to the central inbox. The inbox system routes notifications between projects with a processed/done lifecycle.

One spoke project generated 42 backlog proposals and 53 methodology observations. That is not a theoretical capability; those are real numbers from a real project, producing concrete improvements to the shared methodology.

### Reasoning extraction

Session transcripts get mined for reasoning patterns that become formal guidance for future sessions. The experiment framework ensures capability tests are reproducible and feed back into the methodology. Stress testing compares guided vs. unguided collaboration to measure the actual impact of structured protocols.

External observations generate backlog items automatically. The "Earn Your Assertions" principle means claims are verified before acting. "Critical Thinking" requires the AI to challenge its own outputs. These run as active protocols in every session.

Sprint boundaries are not just packing-up moments. At each boundary, the agent runs a structured retrospective across six dimensions: themes, principles, evolution, collaboration, learning, and maturity. Mechanical compliance is necessary; the analysis is what makes the boundary useful for the next sprint.

---

## The compound effect

No single feature here is new. Pre-generation briefs, memory systems, feedback loops, they exist in various forms elsewhere. What is different is that 90 features work together as a system, and the system learns.

A feedback observation from a spoke project becomes a backlog item in the central repository. That item becomes a protocol change. That change propagates to every project. The next session in any project benefits from an insight that started in a completely different context.

The methodology improves through use.

---

*For the full chronological feature timeline, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md). For the competitive positioning analysis behind these three dimensions, see the [3D positioning map](https://github.com/albertodiazdurana/take-ai-bite/blob/main/dsm-docs/research/DSM-Rebranding/2026-03-18_competitive-positioning-map.md).*
