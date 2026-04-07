---
title: "Take AI Bite: a framework for human-AI collaboration"
date: 2026-03-12
draft: false
description: "A collaboration framework where the human stays in control and retains every lesson learned."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Principles Series", "Take AI Bite"]
categories: ["Principles"]
author: "Alberto Diaz Durana"
toc: true
---

AI tools generate faster than humans can review. When the output exceeds what a person can meaningfully engage with, the collaboration quietly breaks: the human stops reading and starts clicking "approve." The human in the loop becomes decorative, and what they actually bring, direction, judgment, style, goes missing from the work.

Take AI Bite is a set of principles for keeping the human genuinely present in AI-assisted work. The idea is not to slow the AI down. It is to structure collaboration so that every delivery is sized for real engagement.

It also goes further than review sizing. Take AI Bite builds an agent system that retains your memory, experience, and decisions across sessions and projects. Over time it becomes an extension of your professional self: it remembers what you learned and carries your expertise into every new collaboration.

## The principles

Nine principles govern how humans and AI agents work together. Each addresses a specific failure mode in human-AI collaboration.

| Principle | Core idea |
|-----------|-----------|
| **Take a Bite** | Deliver only what the reviewer can chew. If they can't redirect it, it was too much. |
| **The Human Brings the Spark** | AI amplifies. The human provides direction, intuition, and aesthetic judgment. |
| **Earn Your Assertions** | Investigate before you claim. Verify before you act. Neither side gets to assume. |
| **Critical Thinking** | Understand first, review second, decide third. Then challenge your own reasoning: what did I miss? What am I assuming? |
| **Know Your Context** | The agent manages its own resource consumption. Don't charge ahead until overflow. |
| **Match the Room** | Contribute proportionally to the project's culture and scale. |
| **Own Your Process** | Disclose how the work was produced. Transparency about method is a professional obligation. |
| **Know What You Own** | Verify licensing before deployment. Free tier does not mean free use. |
| **Think Ahead** | Build the map before you walk the territory. Strategy emerges from operational maturity. |

## The engine: Deliberate Systematic Methodology (DSM)

These principles run on DSM, a versioned methodology for the full lifecycle of human-AI collaboration: research, implementation, governance, disclosure. Take AI Bite is documented in two layers, and you need both.

### DSM_6.0, the principles

The nine principles above are **DSM_6.0: AI Collaboration Principles**. This is the philosophy layer, the "why". It says what humans bring to the work that AI cannot generate on its own, direction, judgment, the spark, and the rules that keep that contribution present instead of decorative.

### DSM_6.1, Systems Prompt Engineering

Principles on their own do not survive contact with months of sessions across multiple projects. To live by them you need an instruction system: documents, templates, feedback loops, and session protocols that shape AI behavior without being rewritten each time. **DSM_6.1: Systems Prompt Engineering** names that discipline, the "what" and "how". It treats every protocol, template, and command as an instruction artifact, designed and versioned the way software is.

DSM_6.1 has three modules:

- 6.1.A Operational Channels and Context Management. The nine `dsm-docs/` folders mapped to communication functions. Session lifecycle commands (`/dsm-go`, `/dsm-wrap-up`, parallel sessions) as context-management operations. A five-layer memory architecture from session transcript to versioned git history.
- 6.1.B Instruction Design Patterns. The three-layer CLAUDE.md architecture (inherited protocols, alignment block, project-specific overrides). Command files as reusable prompt templates. Protocol templates with anti-patterns as negative instructions. The hub-spoke feedback loop as instruction iteration.
- 6.1.C Evaluation and Evolution. Git history as audit trail. Automated cross-reference validation through Graph Explorer, a 547-test CI for instruction documents. Retrospective session analysis (STAA). The learning loop that closes evaluation findings back into the next protocol revision.

Most prompt engineering writing stops at the first layer. Individual prompts you can write by feel. Instruction systems you cannot. DSM_6.1's central claim is context engineering at ecosystem scale: not how to give one model the right context for one task, but how to manage context across many agents, many projects, and months of sessions.

### How the two layers work together

DSM is not static. It evolves through a hub-spoke feedback loop where every session and every project feeds back into the methodology. Protocols get tested and refined, then spread across projects. What one project discovers improves every future one.

The principles tell you what is worth caring about. The discipline gives you the materials to build a system that actually cares about those things across time. Without the second layer, the first one is a poster on the wall with a list of good intentions.

This is what makes the long-term memory possible. Session transcripts capture reasoning. Checkpoints preserve milestones. Memory files carry context across sessions. Feedback flows from projects to the central methodology and back. The result is a system that keeps your expertise, not just your files.

## Start here

Read [Take a Bite](/blog/2026-03-07-take-a-bite/) for the short version of the founding principle. It takes two minutes. The core idea: someone offers you a bite of a cookie, you take a bite the size you will enjoy. Too small and you won't taste it; too much and it causes problems.

## Field-tested

These principles emerged from daily practice with AI agents across real projects: data science pipelines, production software, open source contributions in unfamiliar stacks (Android/Kotlin, all merged upstream), documentation systems with thousands of cross-referenced lines, research synthesis, and financial compliance work.

They are not theoretical. Practitioners working on complex multi-session tasks independently recreate DSM patterns, checkpoint directories, session handoffs, decision logs, before encountering the framework. DSM formalizes behavior that shows up naturally when people work deliberately.

## What's coming

This is the philosophical foundation. The full framework is being prepared for publication:

- Methodology tracks for data science, software engineering, documentation, and project management, with templates and setup scripts
- A queryable knowledge graph that compiles human-authored methodology into a navigable structure, searchable across projects and sessions
- Competitive positioning research mapping human-AI collaboration approaches across three dimensions: human control, knowledge provenance, and experience accumulation

---

*Part of the [Principles Series](https://github.com/albertodiazdurana/take-ai-bite) -- Take AI Bite, powered by Deliberate Systematic Methodology (DSM).*