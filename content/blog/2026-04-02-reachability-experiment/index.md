---
title: "Can your AI agent find everything you wrote?"
date: 2026-04-02
draft: true
description: "We built a tool to check whether an AI agent can reach every section in a 35-document methodology. The results changed how we think about documentation."
tags: ["Deliberate Systematic Methodology", "DSM", "Graph Explorer", "Documentation", "Experiments", "Take AI Bite"]
categories: ["Experiments"]
author: "Alberto Diaz Durana"
toc: true
---

You write documentation for your AI agent. Protocols, templates, decision frameworks. 35 files. 1,310 sections. A dispatch table. Cross-references. Module files.

Then you ask: can the agent actually find all of it?

Not "is it well-written?" or "is it complete?" A more basic question: starting from the one file the agent loads automatically, can it follow references to reach every section in every document?

We built a tool to find out.

---

## The problem

DSM is a methodology for human-AI collaboration, written as interconnected markdown files. The agent enters through one file (DSM_0.2, loaded via an `@` reference in every project's configuration). From there, it discovers everything else by following references: dispatch tables, markdown links, prose mentions, section pointers.

During Session 39 of a spoke project, an agent failed to find experiment templates that existed in the documentation but were never directly referenced. The templates were architecturally invisible: they existed on disk but not in the agent's navigation path.

That moment stayed with me. If the agent can't find the rules I wrote, they may as well not exist. So I developed the Graph Explorer.

## Graph Explorer

The documentation had grown to 20,000 lines across 35 files with hundreds of cross-references. Reading through them to check for gaps was no longer realistic. So I built [Graph Explorer](https://github.com/albertodiazdurana/dsm-graph-explorer), a validation tool that treats documentation the way a compiler treats source code.

What it does:

- Parses every heading and cross-reference across all files
- Builds a directed reference graph (files as nodes, references as edges)
- Runs BFS from the agent's entry point to measure reachability
- Detects semantic drift (TF-IDF similarity between a reference and its target)
- Compares reference graphs across git commits to track how the structure changes over time
- Resolves cross-repository entity references for distributed documentation

547 tests, 95% coverage. The methodology built the tooling to validate itself.

After completing a four-phase audit of all 35 documents (domain-neutrality checks, structural compliance, modularization), I pointed Graph Explorer at the result and asked: is everything reachable?

## The experiment

Graph Explorer's BFS traversal starting from DSM_0.2:

1. Inventory every heading (## and ###) across all 35 files
2. Parse six types of references: markdown links, @ references, module dispatch table entries, prose mentions ("See DSM_X.Y"), section references (§N), and file-name mentions
3. Build the directed reference graph (286 edges)
4. Run BFS from the entry point
5. Report hop distances and unreachable sections

Pre-registered success criterion: every section reachable within 3 hops or fewer.

## The results

100% file reachability. All 35 files, all 1,310 sections, reachable from the entry point. Nothing orphaned, nothing invisible.

Hop distribution:

| Hops | Files | What lives there |
|------|-------|-----------------|
| 0 | 1 | Entry point (DSM_0.2) |
| 1 | 6 | Core modules, file naming, AI principles |
| 2 | 12 | Methodology cores, PM, documentation adaptation |
| 3 | 5 | Implementation guide, software engineering, PM extension |
| 4 | 7 | START_HERE guide, implementation guide modules (A-F) |
| 5 | 4 | Systems Prompt Engineering chapter and modules |

## The surprise

11 files exceed the 3-hop threshold. All of them are modules.

The 3-hop criterion was defined before we modularized the documents. The modularization effort (Sessions 146-151) split large files into core + module patterns to reduce per-file context cost. A 1,500-line file became a 350-line core with four 300-line modules.

Each module level adds one hop. DSM_3.0.A (a module of DSM_3.0) is always one hop deeper than DSM_3.0 itself. And DSM_6.1.A (a module of DSM_6.1, which is a sub-chapter of DSM_6.0) is two hops deeper than DSM_6.0.

The threshold failed, but the architecture held. These files were reachable; they just required more hops than the pre-registered criterion allowed. The criterion was wrong, not the structure.

## Modularity vs. discoverability

When you modularize documentation for AI consumption, you are making a trade-off.

Modularity reduces context cost. The agent loads a 300-line module instead of a 1,500-line monolith. When your context window is finite and every loaded file competes for space, smaller is better.

Discoverability decreases with depth. Each module boundary adds a hop. A file at hop 5 requires the agent to traverse 5 intermediate files to find it. In practice, the agent loads modules on demand (triggered by a dispatch table or cross-reference), so hop count reflects navigation complexity, not loading time.

The revised threshold accounts for this: core files must be within 3 hops, modules must be within 1 hop of their core. Under this model, everything passes.

## What we learned

Content that exists but can't be found through reference chains is functionally absent. Graph Explorer caught this in Session 39. The reachability experiment confirmed the fix worked.

Flat hop thresholds penalize modular architectures. A two-tier model (core files vs. their modules) is more honest about what the numbers mean.

The entry point matters more than the content. All 35 files were well-organized. The question was whether the reference chain from the agent's starting point could reach them. An infrastructure question, not a content quality question.

The file system shows files in a flat directory. The reference graph shows how an agent actually navigates them. Graph Explorer makes that second structure visible.

## What Graph Explorer does beyond reachability

The reachability experiment is one use case. Graph Explorer also:

- Detects semantic drift: when a cross-reference points to a section whose content has changed enough that the reference may be misleading
- Tracks structural evolution: compare reference graphs across git commits to see how documentation architecture changes over time
- Resolves cross-repo references: for documentation spread across multiple repositories, match entities by ID, heading, or fuzzy TF-IDF similarity
- Measures protocol usage: compare what the methodology prescribes against what agents actually consult during sessions
- Lints conventions: enforce style rules (emoji in docs, line endings, metadata format) as automated checks

547 tests to make sure the validator itself is correct.

## Key numbers

| Metric | Value |
|--------|-------|
| DSM files | 35 |
| Sections (## and ###) | 1,310 |
| Reference edges | 286 |
| File reachability | 100% |
| Max hop distance | 5 |
| Files within 3 hops | 24/35 (68.6%) |
| Files within revised threshold | 35/35 (100%) |
| Graph Explorer tests | 547 |
| Test coverage | 95% |

---

*Source: EXP-001 (BL-230), Session 162. Graph Explorer is open source at [github.com/albertodiazdurana/dsm-graph-explorer](https://github.com/albertodiazdurana/dsm-graph-explorer). Full experiment results and reference graph available in the [Take-AI-Bite repository](https://github.com/albertodiazdurana/take-ai-bite).*