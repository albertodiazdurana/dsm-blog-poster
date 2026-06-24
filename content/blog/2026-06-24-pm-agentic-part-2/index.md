---
title: "Process Mining for AI Agentic Workflows, Part 2: Discovery and Value"
date: 2026-06-24
draft: false
description: "The documented process is a story a company tells about itself; the lived process is what the data records. Why agentic automation has to start by measuring the real process and where the value actually leaks."
tags: ["Process Mining", "Discovery", "Business Value", "Agentic Workflows", "Take AI Bite"]
categories: ["Engineering"]
author: "Alberto Diaz Durana"
toc: true
slug: "pm-agentic-part-2"
---

*Part 2 of 4 in the series Process Mining for AI Agentic Workflows. Previous: [Part 1, A Field Guide](/blog/pm-agentic-part-1/). Next: [Part 3, Engineering and the Agent](/blog/pm-agentic-part-3/).*

Every agentic AI project I have seen starts with a sentence that sounds reasonable and hides the whole problem: "Let's put an agent on this process." The word doing the damage is *this*. Before anyone can automate a process, someone has to answer what the process actually is, and that answer is almost never the one in the handbook.

I spent years doing process mining consulting before agentic AI was a category, and the lesson transferred intact. The documented process is a story a company tells about itself. The lived process is what the data records. Process mining is the discipline of reconstructing the second one from the evidence the business already produces.

## The process you think you have

Most enterprise systems are honest (deterministic) in a way people might miss during day-to-day work. An ERP, a ticketing tool, a case-management system, all of them stamp a record every time something happens: an event, a timestamp, an actor, an object. That exhaust is an event log, and an event log is evidence. It does not know how the process is supposed to work, so it cannot flatter it.

When you reconstruct the real flow from that log, the first thing you find is that the clean five-box diagram on the wall is a fiction. In one engagement on a high-volume back-office process, a flow that everyone described in five steps turned out to contain hundreds of distinct variants once we mined it: rework loops where cases bounced between two teams, shortcuts that skipped a control entirely, and a long tail of one-off paths nobody had ever named. None of that was visible in the interviews. All of it was visible in the data.

This is not a complaint about sloppy documentation. It is the normal condition of any process that humans run at scale. People adapt, exceptions accumulate, and the map drifts from the territory. The point of measuring first is that the drift is exactly where the cost lives, and exactly where an agent will either help or quietly make things worse.

## Why this matters more for agents, not less

You could argue that automation has always needed this discovery step, and you would be right. But an agent raises the stakes. A rule-based bot fails loudly when reality does not match its script. An agent improvises. Point one at a process you have only imagined, and it will confidently generate plausible actions for the paths you never accounted for, including the rework loops and the skipped controls. It automates the fiction, fluently.

So the discovery question for agentic work is sharper than "how does this process run." It is "what is the real distribution of paths this process takes, and which of them do I actually want a system acting on." You cannot answer that only from a workshop. You answer it from the log with hard facts and evidence, and then validate the business side in workshops if needed.

This is also why the major process intelligence vendors have spent the last two years repositioning around exactly this idea. Celonis now frames its agent tooling under the slogan ["No AI without PI"](https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence), process intelligence first. Salesforce [acquired a process mining company](https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-apromore/) specifically to give its agents a map of business operations to act on. The framing is consistent across the industry: the agent needs to know how the work really flows before it is trusted to touch it.

I watched this convergence from the inside. The low-code automation company where I did process mining consulting, Appian, acquired the Berlin process mining specialist Lana Labs in [2021](https://appian.com/about/explore/press-releases/2021/appian-acquires-leading-process-mining-company), specifically to fold discovery into its automation platform. By 2024 the two had become one product: Appian describes Process HQ as a single place combining ["data fabric, process mining, machine learning, and generative AI"](https://appian.com/about/explore/press-releases/2024/latest-version-of-appian-platform-orchestrates-change-through-ai), with its AI agents drawing on that same process context to act. I cannot confirm that the 2021 vision was aiming to support the kind of agentic workflows the market is rushing toward in 2026, or that anyone then framed process mining as essential for agents the way they do now. What I can say is that the move aligned with a strategy grounded in tools for describing how work actually flows, process modeling notation and process mining, that have been around for roughly two decades: [BPMN has been an OMG, and later ISO, standard since 2004](https://www.omg.org/bpmn/), and [process mining was formalized as a discipline by 2011](https://www.tf-pm.org/resources/manifesto). The agent is the newest consumer of that description, not the reason it exists.

## From discovery to value

Discovery tells you what is happening. It does not tell you what is worth changing. That is a separate, and more commercial, act of judgment, and it is where the consultant earns the engagement.

The intuition, especially now, is to scan the process for places to add AI. That is the wrong question, and it is how you end up with pilots that never reach production. The right question is plainer: where do time, cost, and rework actually leak? Process mining answers it with hard numbers. It shows you the bottleneck that adds three days to a cycle, the rework loop that touches a fifth of all cases, the variant that quietly consumes a disproportionate share of effort. The value case is built from measured reality, not from a hunch about where the friction must be.

There is a discipline here that survives every shift in technology: you define what "better" means, and how you will measure it, before you choose the tool. The target metric comes first. Only then do you decide whether the answer is a rule, a piece of robotic automation, an agent, a process redesign, or simply a conversation with the team that owns the bottleneck. A 2025 [Deloitte survey of process mining users](https://www.deloitte.com/de/de/services/consulting-financial/research/global-process-mining-survey.html) found that around 80 percent say the practice delivers real value, and the unglamorous through-line among the ones who get it is that they establish a baseline before they build, so that "improvement" is a number and not an impression.

## What process mining tells you to give the agent

Once you can see the real process and you know where the value sits, the map answers the design question that teams otherwise argue about in the abstract: which parts of this should an agent even do?

The decomposition falls out of the evidence. Steps that are high-volume and rule-governed do not need an agent at all; they need deterministic automation, and dressing them up in a model only adds cost and unpredictability. Steps that genuinely require judgment under ambiguity, reading a messy free-text field, reconciling two records that almost match, deciding which exception path applies, are where a language model earns its place. And steps that carry real consequence or accountability stay with a human, with the system feeding them what they need to decide quickly.

The strongest framing I can offer for agentic scoping is this: agent the high-variance, judgment-heavy steps, automate the deterministic ones with plain code, and keep the human on the decisions that matter. It echoes the advice from teams shipping agents in production, [start with the simplest thing that works and add agentic complexity only where it pays for itself](https://www.anthropic.com/research/building-effective-agents). The process map is what tells you which step is which. Without it, that conversation is just everyone's intuition competing, and the loudest voice usually wins.

Knowing the real process and where the value sits is necessary, but it is not yet a system. Someone has to build the thing, and this is where a comfortable story tends to creep in: that the data you mined and the data your agent runs on are the same plumbing. They are not. Some upstream sources do overlap, the event data, the feature tables, the system connectors, but the operational discipline diverges. Running an analytics and process mining pipeline is largely a data engineering and DevOps problem. We could even argue that MLOps has a place also in process mining depending on the complexity of the use case and feature engineering. Running an agent in production is an LLMOps problem, with its own evaluation harnesses, prompt and version management, tracing semantics, latency and cost profiles, guardrails, and the on-call skills to match, frequently a different team. Part 3 is about that build: where the two disciplines genuinely align, and where each needs its own stack and its own people.

*Next in the series: [Part 3, Engineering and the Agent](/blog/pm-agentic-part-3/).*

---

## Sources

- Celonis, "AgentC: Making AI Agents Work for the Enterprise with Process Intelligence" ("No AI without PI"), Oct 2024: https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence
- Salesforce, "Salesforce Signs Definitive Agreement to Acquire Apromore," Oct 2025: https://www.salesforce.com/news/stories/salesforce-signs-definitive-agreement-to-acquire-apromore/
- Appian, "Appian Acquires Leading Process Mining Company" (Lana Labs), Aug 5, 2021: https://appian.com/about/explore/press-releases/2021/appian-acquires-leading-process-mining-company
- Appian, "Latest Version of Appian Platform Orchestrates Change through AI Process Automation" (Process HQ unifies data fabric, process mining, ML, generative AI), Apr 16, 2024: https://appian.com/about/explore/press-releases/2024/latest-version-of-appian-platform-orchestrates-change-through-ai
- Object Management Group, "Business Process Model and Notation (BPMN)," OMG standard since 2004 (BPMN 2.0 in 2011), also ratified as ISO 19510: https://www.omg.org/bpmn/
- IEEE Task Force on Process Mining, "Process Mining Manifesto" (led by Wil van der Aalst), 2011: https://www.tf-pm.org/resources/manifesto
- Deloitte, "Global Process Mining Survey 2025" (~80% agree process mining delivers added value): https://www.deloitte.com/de/de/services/consulting-financial/research/global-process-mining-survey.html
- Anthropic, "Building Effective Agents" (start with the simplest solution; add agentic complexity only when it improves outcomes), Dec 2024: https://www.anthropic.com/research/building-effective-agents
