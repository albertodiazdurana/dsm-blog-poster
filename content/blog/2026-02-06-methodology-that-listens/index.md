---
title: "A Methodology That Listens: How Our First Spoke Project Rewrote the Playbook"
date: 2026-02-06
draft: false
description: "What happened when the first spoke project in a hub-and-spoke data science methodology completed its feedback cycle -- 22 scored entries, 14 proposals, and 7 accepted improvements."
tags: ["Methodology", "Data Science", "Feedback", "DSM", "Process Improvement"]
categories: ["Methodology"]
author: "Alberto Diaz Durana"
showToc: true
ShowReadingTime: true
slug: "methodology-that-listens"
---

Most data science methodologies are written once and left to age. Someone drafts a process document, the team follows it for a while, and then reality drifts. The document stays frozen while the work evolves. By the time anyone revisits the methodology, it describes how things used to be done, not how they should be.

I built DSM (Data Science Methodology) to avoid that trap. The idea was straightforward: every project that uses the methodology must score the sections it touches and propose improvements. Not as a nice-to-have, not as an optional retrospective, but as a required deliverable baked into the sprint boundary checklist. The methodology requires projects to grade it.

This is the story of what happened when the first real spoke project completed and handed its feedback back.

## The Architecture: Hub and Spoke

DSM is a hub-and-spoke system [1]. The central repository ("DSM Central") contains the methodology, templates, project management guidelines, and a backlog of proposed improvements. Spoke projects, each in their own repository, reference DSM Central through their configuration files and follow its workflow during execution.

```
                +---------------------------+
                |     DSM Central (Hub)     |
                |  Methodology + Backlogs   |
                +-----------+---------------+
                            |
            +---------------+---------------+
            |               |               |
     +------+------+  +----+----+  +--------+-------+
     | sql-query   |  | graph   |  | jupyter-book   |
     | agent       |  | explorer|  | (planned)      |
     +------+------+  +---------+  +----------------+
            |
            v
     Feedback files:
     - methodology.md (scored entries)
     - backlogs.md (improvement proposals)
```

The feedback loop is the critical piece. At sprint boundaries, spoke projects update two files in `docs/feedback/`: a methodology file with per-section scores (1-5 scale, four dimensions: clarity, applicability, completeness, efficiency) and a backlogs file with structured improvement proposals. At project completion, these files are handed off to DSM Central for integration.

The theory was clean. What I did not know was whether the practice would produce anything useful or just generate bureaucratic noise.

## The First Spoke Project: sql-query-agent

The sql-query-agent project built a natural language to SQL agent using local LLMs (Ollama) over two sprints in three days [2]. It was a good test case for DSM: it touched notebook work (Sprint 1 exploration), software engineering (Sprint 2 Streamlit app), experiment design (model comparison evaluation), and blog writing (three published posts). Nearly every part of the methodology was exercised.

When the project completed, its feedback files contained:

| Metric | Value |
|--------|-------|
| Methodology entries scored | 22 |
| Average score | 3.3 / 5.0 |
| Gaps identified | 12 |
| Pain points | 3 |
| Successes | 7 |
| Backlog proposals | 14 |

An average of 3.3 out of 5 is not flattering. But the purpose of scoring is not to produce a good number; it is to find the sections that need work. The distribution mattered more than the average.

## What the Scores Revealed

The scores clustered into three bands:

**High (4.0-5.0): Sections that worked as intended**

DSM_0 (the getting-started guide) scored 4.0 during project setup. The PM Guidelines templates scored 4.0 for sprint planning. The experiment framework, once discovered, scored 3.75 for applicability. The blog workflow scored 3.5-4.0 after the first post established the pattern. Sprint 2's explicit collaboration workflow scored 4.75 after being refined during execution. These sections delivered value without friction.

**Middle (3.0-3.5): Sections with minor gaps**

The checkpoint template scored 3.5, losing half a point because `docs/checkpoints/` was not in the project structure template. The feedback file naming (validation tracker vs. feedback files) scored 3.0 due to overlap confusion. The sprint boundary checklist scored 3.0 because it missed the README as a deliverable. These were real gaps but not blocking ones.

**Low (2.25-2.75): Sections with structural problems**

This is where the interesting findings were. The five lowest scores:

| Section | Score | Core Issue |
|---------|-------|-----------|
| Custom Instructions + C.1.3 (Decision Traceability) | 2.25 | No guidance for documenting implementation-level decisions within experiments |
| PM Guidelines (Intra-Sprint Documentation) | 2.50 | DSM silent on documentation at phase boundaries within sprints |
| Custom Instructions (Notebook-to-Script Transition) | 2.50 | No guidance on when to stop using notebooks and extract to scripts |
| Custom Instructions + 6.2.5 (Notebook Protocol) | 2.50 | Agent wrote .ipynb directly; protocol existed but was not surfaced |
| Section 6.4.5 (Blog Materials Location) | 2.75 | Blog tracker grouped with DSM feedback files instead of project output |

The pattern was clear: the lowest scores did not come from missing sections. They came from missing connections between sections that existed independently. The experiment framework (Appendix C.1) was well-designed, but nothing in the standard workflow pointed to it. The notebook protocol existed in Section 6.2.5, but the Custom Instructions template did not reinforce it. Intra-sprint documentation was expected at sprint boundaries, but sprints with multiple phases had no trigger to pause and document at phase transitions.

In other words, DSM had the right pieces but had not wired them together into the paths that real projects actually walk.

## The Triage: 14 Proposals In, 7 Backlog Items Out

The backlogs file contained 14 structured proposals. Each one included a Problem statement, Proposed Solution, and Evidence section describing what actually happened in the project. This structure, which DSM requires through its feedback template, turned out to be the most valuable part of the process. Abstract improvement suggestions ("make it better") are useless. Proposals grounded in "here is what we tried, here is where it failed, here is what would have prevented it" are immediately actionable.

I triaged every proposal against DSM's existing backlog (including items already implemented in previous sessions). The results:

**Rejected (5 proposals, already addressed):**

| Proposal | Existing Solution |
|----------|-------------------|
| Add research/literature review step | BACKLOG-039: Phase 0.5 Research Grounding (implemented) |
| Add sprint-level plan template | BACKLOG-044: Sprint Plan Template 8 (implemented) |
| Clarify validation tracker vs. feedback files | BACKLOG-041: Consolidated into single feedback system (implemented) |
| Add notebook collaboration protocol | BACKLOG-045 + 047: Protocol created and reinforcement added (implemented) |
| Add docs/checkpoints/ to project structure | Already present in DSM_0 daily workflow |

Five of fourteen proposals had already been fixed. This was surprising. The sql-query-agent project was set up using DSM v1.3.0, but by the time feedback was processed, DSM had advanced to v1.3.21 through other maintenance work. The methodology had evolved during the project's lifetime, addressing some of the exact gaps the project encountered.

This validates the continuous improvement cycle, but it also reveals a versioning gap: spoke projects start with a DSM snapshot and may not benefit from improvements made after setup. Whether spoke projects should periodically pull DSM updates during execution is an open question.

**Accepted (9 proposals, grouped into 7 backlog items):**

| BACKLOG | Title | Priority |
|---------|-------|----------|
| 061 | Surface Experiment Framework in Standard Workflow | Medium |
| 062 | Decision Traceability and Citations in Experiments | Medium |
| 063 | Intra-Sprint Documentation Cadence | Medium |
| 064 | Notebook-to-Script Transition Guidance | Medium |
| 065 | Add README Update to Sprint Boundary Checklist | Low |
| 066 | Blog Workflow Refinements (separation, naming, style guide) | Low |
| 067 | IDE Permission Configuration for Human-in-the-Loop | Low |

The three blog-related proposals (separate blog from feedback, artifact naming convention, style guide) were combined into a single backlog item. All other proposals became individual items.

## Lessons from the Feedback Loop

### 1. Structured evidence beats subjective impressions

Every accepted proposal included a "What happened" section with specific details: which cell failed, which file was placed in the wrong directory, which protocol the agent violated. This evidence is what made the proposals actionable. A vague "improve the notebook protocol" would have been ignored. "The agent wrote the .ipynb file directly, bypassing human validation, because nothing in the Custom Instructions specified the interaction mechanics" tells you exactly what to fix and where.

### 2. Gaps cluster at module boundaries

The five lowest scores all pointed to the same structural issue: DSM sections work well in isolation but the connections between them are undocumented. The experiment framework is thorough, but the sprint planning template does not reference it. The notebook protocol is complete, but the Custom Instructions template does not reinforce it. Phase boundaries within sprints are natural documentation checkpoints, but only sprint boundaries have a checklist.

This pattern suggests a specific improvement strategy: instead of writing new sections, focus on surfacing existing content at the points where projects need it. Phase-to-section mappings, workflow triggers, and cross-references matter more than additional guidance.

### 3. The rejection rate validates continuous improvement

Five of fourteen proposals were already implemented. This means DSM was evolving in response to the same kinds of issues that the spoke project encountered, even before receiving the feedback. The feedback loop is not just spoke-to-hub; it is also hub-internal, driven by the backlog review process and maintenance sessions.

A methodology that stays current enough to preempt some project feedback is working as intended.

### 4. The handover process needed standardization

Ironically, the act of processing feedback revealed a gap: there was no standard way to hand off feedback from spoke to hub. The sql-query-agent project invented its own prompt. This led to BACKLOG-060 (Standardize Feedback Handover Prompt), which was implemented during the same session, including a prompt template, a slash command, and a documented process in the methodology. The feedback loop improved itself through its own execution.

### 5. Quantitative scoring works better than qualitative assessment

The 1-5 scoring across four dimensions (clarity, applicability, completeness, efficiency) produced a clear ranking of where to focus. Without scores, I would have relied on my impression of which sections needed work. The scores surfaced issues I would not have prioritized, particularly the intra-sprint documentation cadence (2.5) and the decision traceability gap (2.25), both of which are structural improvements that are easy to overlook but affect every multi-phase sprint.

## What Changes Next

The seven accepted backlog items form a clear improvement roadmap. The medium-priority items (061-064) address the module boundary gaps: surfacing the experiment framework, adding decision traceability, defining intra-sprint documentation cadence, and providing notebook-to-script transition guidance. The low-priority items (065-067) refine the blog workflow, sprint boundary checklist, and IDE configuration.

None of these require rewriting the methodology from scratch. They are targeted additions, mostly cross-references, checklists, and workflow triggers, that wire the existing pieces together more effectively. The framework is sound; the pathways through it need improvement.

The next spoke project will start with these improvements in place. Its feedback will identify the next set of gaps. And the cycle continues.

## The Meta-Point

DSM is not a finished product. It is a system designed to learn from its own use. The feedback loop, the scoring, the structured proposals, the triage process: these are not overhead. They are the mechanism by which a methodology stays relevant.

Most teams treat process documentation as a one-time cost. Write it, ship it, move on. What I have found is that the ongoing cost of maintaining a self-improving methodology is small, a few hours per project for feedback and integration, and the payoff is that the methodology actually reflects how work gets done, not how someone imagined it would be done six months ago.

If your team uses a methodology, any methodology, consider adding a feedback requirement. Score the sections you use. Propose improvements with evidence. Process the feedback systematically. The methodology will thank you by getting better.

---

## References

[1] A. Diaz Durana, "Data Science Methodology (DSM): A Hub-and-Spoke Framework for AI-Assisted Data Science Projects," GitHub, 2026. Available: https://github.com/albertodiazdurana/agentic-ai-data-science-methodology

[2] A. Diaz Durana, "SQL Query Agent with Ollama: Building a Local NL-to-SQL Agent," GitHub, 2026. Available: https://github.com/albertodiazdurana/sql-query-agent-ollama
