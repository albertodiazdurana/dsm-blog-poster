---
title: "Process Mining for AI Agentic Workflows, Part 3: Engineering and the Agent"
date: 2026-06-24
draft: false
description: "Automating a process with an agent is two engineering disciplines wearing one project name: a mature, deterministic data pipeline and a young, stochastic agent. Where they overlap, and where they split."
tags: ["Data Engineering", "LLMOps", "MLOps", "AI Agents", "Take AI Bite"]
categories: ["Engineering"]
author: "Alberto Diaz Durana"
toc: true
slug: "pm-agentic-part-3"
---

*Part 3 of 4 in the series Process Mining for AI Agentic Workflows. Previous: [Part 2, Discovery and Value](/blog/pm-agentic-part-2/). Next: [Part 4, In Production](/blog/pm-agentic-part-4/).*

Part 2 closed on a warning worth repeating: the data you mined to understand a process and the data your agent runs on in production are not the same plumbing. That single confusion is where a lot of agentic projects quietly lose a quarter and a budget.

Discovery told you what to build and where the value is. It did not build anything. Now comes the build, and with it a tempting assumption: because the analytics pipeline and the agent pull from some of the same data, one team and one stack can surely handle both. Sometimes they can. But that has to be a deliberate choice, not the default everyone drifts into.

The honest framing is that automating a process with an agent is two engineering disciplines wearing one project name. One is mature and largely deterministic. The other is young, stochastic, and operationally unforgiving. This part is about telling them apart before you staff and budget them as if they were one.

## What actually overlaps

There is real overlap, and ignoring it would waste work you have already done. So start there.

The first overlap is the data. The event logs you mined to understand the process usually come from the same systems the agent will read from and write to. The connections you built to pull that data, into the ERP, the ticketing tool, the case system, are connections the agent needs too. If discovery left you with clean data and working integrations, that is a real head start.

The second overlap is how you work. Process mining only trusts what the data shows: you measure a baseline before you claim an improvement. An agent needs the same habit, just pointed forward: you measure what it does before you let it do more. Same idea, later stage. A team that learned to measure before trusting already has the mindset the agent will need.

But look at what carries over and what does not. The data, the connections, and the way of working carry over. How each system is built, tested, and run day to day does not. That is where the two split apart, and where most of the cost and the surprises show up.

## The analytics pipeline is a data-engineering problem

The pipeline that produced your process view, and that keeps producing the metrics you track, is mostly a data-engineering job. You pull data out of the source systems, turn raw events into a clean log, check that the data is right, run it on a schedule, store the results, and keep the whole thing alive when a feed breaks at 2 a.m. None of that is new. The failure modes are well known: a source system renames a field, a feed runs late, data quality drifts. There are mature tools and patterns for all of it.

When the work includes a model, predicting a delay, scoring a case, flagging an anomaly, a second layer comes in. Now you also track experiments, version the model, retrain it when the data shifts, and watch its accuracy over time. Even here, the model is the small part. A [2015 paper from a Google team](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) made the point that has held up since: in a real machine learning system, the model is only a small fraction of the code, and the rest is data handling and infrastructure.

This is familiar ground. Deploying machine learning models into production for cement manufacturing was, in practice, mostly this: reliable data pipelines, monitoring, dashboards, and alerts, so the models had clean inputs and someone knew the moment they did not. It is demanding work, but it is well understood. The tools are stable, the skills are established, and a competent data and platform team has seen these problems before.

## The agent in production is an LLMOps problem

The agent is the part that is not well-trodden. It behaves differently from a data pipeline, in ways that change how you build it, test it, and run it.

Start with the obvious one: it is not deterministic. The same input can produce a different answer twice in a row, so you cannot test it once and call it correct. And a right-looking answer can hide a wrong path, the agent reached a reasonable conclusion through a tool call it should never have made. So you do not only check the output, you check the whole path: which tools it called, with what, and whether the answer was actually grounded in the data it retrieved.

That makes evaluation continuous, not a one-time gate. You trace every step in production: the reasoning, the tool calls, the retrieved data, the cost and delay of each. Then you sample those traces, score them, often with [another model acting as the judge](https://arxiv.org/abs/2306.05685), feed the failures back into your test set, adjust the prompts, and check again. Prompts become versioned artifacts, because a small change in wording shifts behavior. Cost and speed become first-order concerns, because every call has a price and a delay that a scheduled pipeline job does not.

Then there is security, which is genuinely new. An agent reads content you do not control and can take actions, so a hidden instruction inside a document can hijack it. Prompt injection sits at the [top of the OWASP risk list for LLM applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) for exactly this reason. The defenses are part of the build, not an afterthought: give the agent only the tools it needs, filter what goes in and out, and keep a human approving anything that moves money or changes records.

None of this is mature the way data engineering is. The tools are young, the patterns are still forming, and the people who can run it well are harder to find.

## Where the stacks diverge, and why it is often two teams

Put the two side by side and the split is clear. It is in the operational core, not at the edges.

Testing works differently. A data pipeline has deterministic tests: the same input gives the same output, so a check either passes or fails, and once it is green you trust it. An agent is never simply green. You judge it on samples, with a mix of automated checks and human review, and the work does not end, because the model, the data, and the prompts all keep moving.

What you watch differs too. For the pipeline you watch freshness, completeness, and whether a schema changed overnight. For the agent you watch cost per call, response time under load, and whether the quality of the answers is slipping. A pipeline tends to fail loudly: a feed stops and an alert fires. An agent tends to [fail quietly](https://arxiv.org/abs/2204.10227): it keeps answering, just a little worse, and you only notice if you are sampling.

And the skills differ. One side is data engineering and platform work. The other is evaluation, prompt and agent behavior, and a feel for how these systems drift. The instinct you want on call at 3 a.m. is not the same on each side.

So in practice this is often two teams, or at least two distinct skill sets. The common mistake is to assume the team that built the data pipeline can also run the agent, or that the AI team will keep the data flowing. In a small shop one group may do both, but treat that as a decision you made, with the gap budgeted, not an accident you discover later.

Once both sides are built and staffed, you have a system that runs. That is not the same as a system that pays off. A pipeline that updates and an agent that answers are still just machinery until someone confirms the value showed up: the cycle time fell, the rework dropped, the cost moved the right way. And the closer the agent comes to acting on its own, the more the real question shifts from whether it can, to how the people around it stay in control of what it does.

Part 4 is about exactly that: running the system in production, proving the value against the baseline you set in discovery, and keeping a human meaningfully in the loop once the thing is live.

*Next in the series: [Part 4, In Production](/blog/pm-agentic-part-4/).*

---

## Sources

- D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems," NeurIPS 2015 (in a real ML system the model is only a small fraction of the code; the rest is data and infrastructure): https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
- OWASP Top 10 for LLM Applications (prompt injection ranked the top risk): https://owasp.org/www-project-top-10-for-large-language-model-applications/
- L. Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," arXiv 2306.05685, 2023 (a strong LLM can score outputs at roughly human-level agreement; basis for automated evaluation at scale): https://arxiv.org/abs/2306.05685
- "The Silent Problem: Machine Learning Model Failure," arXiv 2204.10227 (ML systems tend to degrade silently rather than crash, so the failure is caught by monitoring, not by an error): https://arxiv.org/abs/2204.10227
