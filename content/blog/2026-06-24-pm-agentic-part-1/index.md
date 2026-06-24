---
title: "Process Mining for AI Agentic Workflows, Part 1: A Field Guide"
date: 2026-06-24
draft: false
description: "An agent demo convinces; the production system often never arrives. A four-part field guide to building agentic workflows on the real process, with a human in control."
tags: ["Process Mining", "AI Agents", "Agentic Workflows", "Data Engineering", "Take AI Bite"]
categories: ["Engineering"]
author: "Alberto Diaz Durana"
toc: true
slug: "pm-agentic-part-1"
---

*Part 1 of 4 in the series Process Mining for AI Agentic Workflows. Next: [Part 2, Discovery and Value](/blog/pm-agentic-part-2/).*

I hear the same sentence in almost every agentic AI project, and it sounds completely reasonable: "let's put an agent on this process." The demo that follows is usually convincing. Some time later, the production system it was supposed to become often is not there.

The gap between a convincing demo and a process you actually trust an agent to run is wide, and most projects fall into it. Not because the models are weak, but because the work around the model gets skipped: knowing the real process, building it as real engineering, and running it with a human still in control.

This series is about that work. It follows one process from the first question to a live, trusted system, in the order the work actually happens. This first part is the map.

## The real process is the ground

You cannot trust an agent on a process you have only imagined. The process in the handbook and the process in the data are rarely the same thing, and the difference is where the cost, and the risk to an agent, lives.

So the work starts by reconstructing the real process from evidence, not only from interviews. The systems a business already runs leave a trail: every step stamped with a time, an actor, and an object. That trail is an event log, and process mining reads it back into the actual flow, the rework loops, the shortcuts, the long tail of paths nobody describes in a workshop. It shows the process as it is, not as people remember it.

This is not a niche opinion. The process intelligence industry has spent the last few years repositioning around exactly this idea, that an agent needs a map of how the work really flows before it is trusted to act on it. Celonis now frames its agent tooling under the line ["no AI without PI"](https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence), process intelligence first.

The point for the series is the following: evidence about the real process is the ground everything else stands on. Skip it, and you are automating a story the company tells about itself, fluently and at scale.

## The pattern this is up against

The optimism is not matched by the survival rate. Gartner expects [more than 40% of agentic AI projects to be cancelled by the end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), and by the end of 2025 [at least half of generative AI projects had been abandoned after the proof of concept](https://www.gartner.com/en/articles/genai-project-failure). The demo works. The production system does not arrive.

Read the reasons Gartner gives and a pattern shows up: poor data quality, unclear business value, escalating cost, weak risk controls. Notice what is not on the list. The model is rarely the thing that kills the project. What kills it is the work this series is about: not knowing the real process, no honest measure of value, and no path from a working prototype to a system someone trusts in production.

That is the encouraging part, if you look at it right. These projects mostly fail for reasons you can do something about. The rest of the series is the doing.

## What the series covers, and who it is for

The four parts follow one process from the first question to a system you can trust in production, in the order the work actually happens.

Part 2, Discovery and Value, is about finding the real process and where the value actually sits, measuring before you build, so the thing you automate is the thing that matters and not the thing that was easy to reach.

Part 3, Engineering and the Agent, is about the build. It makes the case that an agentic automation is two engineering disciplines, not one: the analytics pipeline that feeds it, which is mature data-engineering work, and the agent itself, which is younger, stochastic, and operated differently. Confusing the two is a common and expensive mistake.

Part 4, In Production, is about the last mile: taking the system live as a graded handover of trust, earning autonomy on evidence, proving the value against the baseline, and keeping a human in control of the decisions that carry weight.

This is for people who want to build with agents, not just demo them. Who would rather ship something narrow that works and that the client can own than something broad that impresses in a meeting and quietly fails after it. The thread through all four parts is the same: let evidence earn each step, and keep a human meaningfully in the loop. If that is the kind of system you want to build, start with Part 2.

*Next in the series: [Part 2, Discovery and Value](/blog/pm-agentic-part-2/).*

---

## Sources

- Celonis, "AgentC: Making AI Agents Work for the Enterprise with Process Intelligence" ("no AI without PI"): https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence
- Gartner, "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027" (June 2025): https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- Gartner, "Why 50% of GenAI Projects Fail" (by end of 2025, at least half of GenAI projects abandoned after proof of concept; poor data quality, weak risk controls, escalating cost, unclear value): https://www.gartner.com/en/articles/genai-project-failure
