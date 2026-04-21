---
title: "114 features across three dimensions"
date: 2026-03-20
draft: false
description: "DSM's 114 features mapped across human oversight, knowledge provenance, and experience accumulation."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Features", "Take AI Bite"]
categories: ["Features"]
author: "Alberto Diaz Durana"
toc: true
---

Most AI coding tools are built to reduce human involvement. DSM is built to make human involvement worth the time: the human and the AI produce better work together than either would alone, and what they learn carries forward.

This post maps DSM's 114 features across three dimensions: human oversight, knowledge provenance, and experience accumulation. For the full chronological list, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md).

---

## Human oversight

Where most tools give you a slider between "approve everything" and "let the AI run," DSM builds oversight into the structure of every interaction.

### Per-turn artifact review

Every artifact passes through a three-gate approval model: concept (do you understand what will be created?), implementation (does the diff look right?), and run (should this execute?). The AI cannot proceed without the human engaging with the work. Before the three gates, there is a fourth conversation: Gate 0, where the human and the agent define the work together before any plan is drafted. Presenting a pre-formed plan for approval reduces the human from collaborator to approver; Gate 0 keeps the definition itself shared.

This extends to collections. Multiple edits to a single file need separate explanations. Notebook cells are generated one at a time, with output verified before the next cell is created. Cells that produce plots save the figure to disk so the agent can read it back and check what it actually drew before moving on.

Enforcement is structural. A per-turn hook appends reasoning to a live transcript as the first tool call of every turn, so the record of thinking cannot be skipped by an eager agent. When a protocol violation is detected mid-output, the output itself is a stop condition: the agent halts, names the violation, and waits for confirmation before resuming. Before a Gate 2 approval, the agent is required to surface the strongest counter-evidence to its own recommendation, shifting the burden of critical evaluation from user vigilance to protocol.

### Session lifecycle

Sessions are not "start coding, stop coding." Each session starts by checking inbox messages, validating project state, comparing versions, and loading context. Each session ends by saving memory, committing work, and creating continuity documents. If a session ends unexpectedly, the next session detects the gap and offers recovery.

Lightweight sessions handle quick follow-ups. Session baselines track what changed. Configuration recommendations match settings to the planned work scope. A wrap-up type marker lets the next session-start command know whether the previous session ended light or full, so the two ends of the lifecycle stay aligned. Before suggesting wrap-up, the agent now re-reads the sprint plan and checks completed deliverables against actual evidence, so "sprint complete" cannot be declared while gates are still open.

### Safety guardrails

Destructive commands (force push, hard reset, recursive delete) require explicit human request. Sensitive files (.env, credentials) are blocked from commits. Feature branches must be tested before merging. The first write to any path outside the current repository in a session requires explicit user confirmation, so an agent working in a spoke project cannot quietly write into the Hub.

The guardrails extend to publication. Merging a pull request against `main` is treated as equivalent in outcome to pushing to `main`, and both require specific confirmation. At session start, the agent resolves the remote default branch and hard-halts if it differs from the local main line, so a stale session branch left as the repo default cannot quietly redirect a merge. Small checks, but the kind of thing that eats 45 minutes when it goes wrong.

These are structural constraints, not opt-in features. They cannot be bypassed without the human explicitly choosing to do so.

---

## Knowledge provenance

Most AI tools start with a blank slate: a generic model, maybe a config file. DSM starts with a versioned, human-authored knowledge base that the AI inherits and contributes to.

### Methodology documents

DSM is a suite of versioned documents: data science workflows (1.0), project management (2.0), cross-project governance (3.0), software engineering (4.0), documentation standards (5.0), collaboration principles (6.0), and most recently the AI platform collaboration guide (7.0) which centralizes platform-specific knowledge so the rest of the suite can stay platform-agnostic. Each is maintained with semantic versioning and a formal update workflow.

Project-specific instructions reference the methodology via a configuration chain, so every project inherits the full protocol suite but can override specific rules. A per-artifact configuration recommendation runs inside Gate 1, so mechanical edits and architectural decisions do not both execute at the same session baseline. Picking the right tool configuration for the work is itself part of the record.

### Protocol inheritance

The hub-spoke architecture means protocols are authored once in the central repository and inherited by all projects. When a protocol improves, every project picks it up. Project type detection activates the right methodology track. Participation patterns adjust rules based on whether a project is a standard spoke, an external contribution, or a private repo.

A path registry maps cross-repository relationships. Mirror repos receive methodology updates automatically. A fresh clone of a public mirror now bootstraps itself into a working session on first run: the clone detects that it is unconfigured, scaffolds the folder structure, copies the template files, self-registers as its own local hub, deploys the slash commands, and writes a marker so subsequent sessions skip the setup. Zero user prompts, zero manual scaffolding.

### Versioned knowledge

Every change to the methodology is tracked in a changelog, tagged with semantic versions, and checkpointed. Design decisions are numbered and documented with rationale and alternatives. Research findings are preserved with sources and dates.

The point is preventing knowledge loss. When a protocol decision was made six months ago, the rationale is recoverable. When research informed a design choice, the original evidence is still there. The same standard applies in the moment: before answering a question about a file, a definition, or a piece of documentation, the agent reads the source. No partial knowledge passing as understanding.

A recent principle extends this outward, to the tools themselves. "Read the User's Manual" treats external-tool understanding as a prerequisite to collaboration design, not an optional afterthought. Before building a pattern on a platform feature, the agent reads the platform's own documentation and verifies the understanding against it, not against memory or experiential knowledge. The motivating incident was a per-turn enforcement hook that sat broken for two and a half months because an assumption about git's index mode never got checked. Methodology knowledge is versioned; tool knowledge has to be grounded the same way.

---

## Experience accumulation

This is where the distance to other tools is largest. Most tools treat each session as independent. Some persist project-level memory. DSM propagates experience from individual sessions outward to improve the methodology for all future work.

### Memory and context

MEMORY.md provides persistent, typed memory across conversations: user preferences, project decisions, feedback patterns, reference pointers. The session transcript captures reasoning in real time, a record of why decisions were made, not just what was done. Context budget management treats the AI's context window as a finite resource.

Handoffs ensure pending work survives session boundaries. Checkpoints snapshot project state. When a session ends unexpectedly, transcript-based recovery reconstructs the missing wrap-up. When the normal boot chain itself is broken, a minimal read-only entry point starts a session with no side effects, just enough context to diagnose what went wrong without making it worse.

### Feedback loops

Spoke projects generate backlog proposals and methodology observations for the central repository. At session end, feedback is pushed to the central inbox. The inbox system routes notifications between projects with a processed/done lifecycle.

One spoke project generated 42 backlog proposals and 53 methodology observations. That is not a theoretical capability; those are real numbers from a real project, producing concrete improvements to the shared methodology.

### Reasoning extraction

Session transcripts get mined for reasoning patterns that become formal guidance for future sessions. The experiment framework ensures capability tests are reproducible and feed back into the methodology. Stress testing compares guided vs. unguided collaboration to measure the actual impact of structured protocols.

External observations generate backlog items automatically. The "Earn Your Assertions" principle means claims are verified before acting. "Critical Thinking" requires the AI to challenge its own outputs. These run as active protocols in every session.

Sprint boundaries are not just packing-up moments. At each boundary, the agent runs a structured retrospective across six dimensions: themes, principles, evolution, collaboration, learning, and maturity. Mechanical compliance is necessary; the analysis is what makes the boundary useful for the next sprint.

---

## The compound effect

No single feature here is new. Pre-generation briefs, memory systems, feedback loops, they exist in various forms elsewhere. What is different is that 114 features work together as a system, and the system learns. The count keeps moving because the methodology is in active use; the shape of what it covers, though, has stayed recognizable across every version.

A feedback observation from a spoke project becomes a backlog item in the central repository. That item becomes a protocol change. That change propagates to every project. The next session in any project benefits from an insight that started in a completely different context.

The methodology improves through use.

---

*For the full chronological feature timeline, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md). For the competitive positioning analysis behind these three dimensions, see the [3D positioning map](https://github.com/albertodiazdurana/take-ai-bite/blob/main/dsm-docs/research/DSM-Rebranding/2026-03-18_competitive-positioning-map.md).*
