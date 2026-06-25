---
title: "About"
description: "Take AI Bite: a framework for human-AI collaboration"
---

**Take AI Bite** is a framework for human-AI collaboration where the human stays in control, grows through the work, and retains every lesson learned. Being in the loop is not the same as being in charge of it, and even that is not the destination. The aim is [symbiosis](/blog/2026-06-24-in-the-loop-in-charge-or-symbiosis/): a human and an AI that stay distinct on purpose and coevolve, each sharpening the other as the work goes.

When AI generates faster than you can review, oversight becomes rubber-stamping. You're in the room, but not in the loop. And the tools doing the generating rarely behave the way you assume they do, which is surprising, because who would have thought that you need to teach your agent how to build its own infrastructure. These are principles for structuring AI collaboration so every delivery is small enough to think about, sharp enough to act on, and real enough to earn genuine engagement, not just approval.

## The Fourteen Principles

1. **Take a Bite** -- Deliver only what the reviewer can chew
2. **The Human Brings the Spark** -- AI amplifies; the human provides direction, intuition, and judgment
3. **Earn Your Assertions** -- Investigate before you claim, verify before you act
4. **Critical Thinking** -- Question your own reasoning before asking others to trust it
5. **Know Your Context** -- Manage your own resource consumption
6. **Match the Room** -- Contribute proportionally to the project's culture and scale
7. **Own Your Process** -- Disclose how the work was produced
8. **Know What You Own** -- Verify licensing before deployment
9. **Think Ahead** -- Build the map before you walk the territory
10. **We Need to Talk** -- The conversation that defines the work is the collaboration, not a preamble to it
11. **Read the User's Manual** -- Ground your collaboration on what the tool actually does, not what you assume it does
12. **Don't be a Hero, Delegate the Effort** -- Propose delegation when a sub-task fits a subagent, do not absorb everything on-thread
13. **Introduce Once, Then Deepen** -- Introduce each concept once; let the body deepen it rather than repeat it
14. **Observe Before Engaging** -- External content is observation by default; engaging with it requires explicit authorization

## Deliberate Systematic Methodology (DSM)

Take AI Bite is the framework and the name. Deliberate Systematic Methodology, DSM, is the versioned body of work behind it: the documented protocols, templates, and principles that make the framework something you can run, not just something you believe in. The files named `DSM_X.Y` are where that methodology lives.

It has two layers, and the split is deliberate.

The first layer is the principles above: the philosophy, the "why", documented in **DSM_6.0 (AI Collaboration Principles)**. These are what you value. The human keeps up. The human brings the spark. Deliver only what the reviewer can chew.

The second layer is the discipline that turns those values into something you can actually live by: **DSM_6.1 (Systems Prompt Engineering)**, the "what" and the "how". Its starting point is that every protocol, version-controlled document, feedback loop, and session command is prompt engineering, just at system scale rather than the scale of a single message. It works at three levels: the individual prompt, the system (one project's CLAUDE.md, command files, and session protocols), and the ecosystem (instruction architecture propagated across many projects, with feedback loops running between them). Three modules carry it: 6.1.A Operational Channels, 6.1.B Instruction Design Patterns, 6.1.C Evaluation and Evolution.

A concrete example. "The human stays in control" is a principle. The system that makes it real is a CLAUDE.md that encodes the project's rules, command files that gate each delivery, a session transcript the human reads as the work happens, and a hub-and-spoke setup that pushes an improvement made on one project out to all the others. The principle is the intent. The engineering is what keeps the intent from quietly eroding the first time the AI generates faster than anyone can read.

That is the reason for two layers. Principles on their own are good intentions, and good intentions degrade under speed. Systems Prompt Engineering is how they survive contact with real work: repeatable across sessions, enforceable across projects, and improving as the methodology learns from each one. This is what the third module, 6.1.C Evaluation and Evolution, is built for: a correction made once becomes a lesson the collaboration keeps, instead of one that resets every session. Principles are what you value. The system is how you build something that runs on them.

Three commitments run underneath all of this: human oversight that stays real, knowledge that is human-curated rather than just inherited from a model, and experience that accumulates across sessions instead of resetting. They are the axes we [scored against fifteen other AI tools](/blog/2026-06-24-in-the-loop-in-charge-or-symbiosis/) in March. On the last one, a practice that a human and an AI build and keep together, the field was still empty.
