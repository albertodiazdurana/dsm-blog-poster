---
title: "Process Mining for AI Agentic Workflows, Part 4: In Production"
date: 2026-06-24
draft: false
description: "Going live is not a switch, it is a graded handover of trust. Earning autonomy on evidence, proving value against the baseline, and keeping a human in control of the decisions that carry weight."
tags: ["AI in Production", "Human-AI Collaboration", "AI Agents", "Benefits Realization", "Take AI Bite"]
categories: ["Engineering"]
author: "Alberto Diaz Durana"
toc: true
slug: "pm-agentic-part-4"
---

*Part 4 of 4 in the series Process Mining for AI Agentic Workflows. Previous: [Part 3, Engineering and the Agent](/blog/pm-agentic-part-3/). Start at [Part 1, A Field Guide](/blog/pm-agentic-part-1/).*

Part 3 ended with a system that runs. This part is about the gap between running and trusted, which is longer than it looks.

The temptation at go-live is to treat it as a switch. The build works, the evaluation passes, so you turn it on and walk away. That is how you get the project that technically shipped and quietly never delivered, or worse, the one that acted with confidence on a case it should never have touched.

Going live is not a launch event. It is a graded handover of trust: you let the system do a little, watch what it does, and let it do more only where it has earned the room. Three things run together through that handover: the rollout that earns autonomy, the measurement that proves the value, and the human who stays in control of what the system is allowed to do. This part is about all three.

## Earn autonomy, don't grant it

So you do not flip the switch. You run a staged rollout, and at each stage the agent earns the next bit of autonomy or it does not move on.

It usually starts in shadow mode. The agent runs on real, live inputs, but it takes no action. Its decisions are recorded and compared against what the people, or the existing process, actually did. You see where it agrees, where it diverges, and why, at zero risk, because nothing it produces touches a customer or a ledger. This is also where the evaluation from the build meets reality: the traces and scores you set up now run against live data instead of a test set. Shadow and canary releases are [standard ways to de-risk a deployment](https://mikulskibartosz.name/shadow-deployment-vs-canary-release); for an agent that can act, shadow mode is where you start.

When the agreement is good enough on a slice of the work, you move that slice to assisted: the agent proposes, a person approves before anything happens. Now it acts, but only through a human gate. You watch the approval rate and the corrections, and they tell you whether the slice is really ready or just looked ready in shadow.

Only then, and only on the slice that has proven itself, do you allow supervised autonomy: the agent acts on its own, monitored, with a fast path back to human review when something looks off. The rest of the process stays gated.

The principle is the one the lede promised. Autonomy is earned scope by scope, on evidence. The agent does not graduate the whole process at once. It graduates the parts it has proven, and the parts it has not stay supervised until the evidence catches up.

## Prove the value, don't assume it

Part 2 ended with a business case, a number the project was meant to move. Part 3 delivered a system that runs. Neither is proof that the value arrived.

Confirming it is its own discipline. [Benefits realization](https://www.pmi.org/learning/thought-leadership/series/benefits-realization/benefits-realization-management-framework) means measuring what actually changed against the baseline you took in discovery, not against a hopeful estimate. You set that baseline on purpose in Part 2: the cycle time, the rework rate, the cost per case, measured before you touched anything. Now you measure the same things on the live process and see whether they moved.

This is where the loop closes. The KPIs the system already emits give you part of the answer, and the process mining that found the problem can run again on the live data to show the new shape of the process, in the same evidence that justified the build. If the bottleneck shrank, you can see it. If it did not, you can see that too, which is the more important case.

One thing makes this real rather than ceremonial: a named benefit owner on the client side, someone whose job is to confirm the value, not to assume it. Without that, "it is working" drifts into folklore and nobody checks.

A delivered system is not a demonstrated outcome until someone shows the number moved. That proof is also what earns the mandate for the next scope, which is where this is heading.

## Keep the human in the loop, on purpose

As the agent earns more autonomy, the pull is to remove the human entirely. That is where the speed is, after all. For most of the process this is fine: the deterministic, high-volume steps never needed a person. But for the decisions that carry real consequence, taking the human out is the wrong instinct, and it is the one the whole rollout was built to resist.

The human stays for a specific kind of decision: the ones that move money, change a record, or commit the organization to something it cannot easily walk back, and any case where the agent's own performance drops below a set threshold. Not because the agent cannot propose an answer, but because someone accountable should still own the call. The point is not to slow the work down. A human kept in the loop as a bottleneck, forced to approve everything, stops reading and starts clicking, and a rubber stamp is worse than no check at all.

So the design problem is to make the human a real check, not theater. That means feeding them the context to decide quickly: what the agent is proposing, why, and the evidence it used, so a person can confirm or override in seconds, on the cases that actually warrant it. Get that right and the human is faster than they would be alone and safer than the agent would be alone.

This is a choice you make on purpose, by design, by consequence and reversibility, not by whatever happens to be automatable. The agent carries the volume. The person keeps the judgment where needed. That division is the whole point of building it this way: the machine amplifies the work, it does not replace the one accountable for it.

## Operating it is never done

Going live is not the finish line. A system in production is something you operate, not something you finish.

Two things keep moving. The system drifts: the agent's quality slips quietly, the models age. And the world it runs in changes: the process evolves, a source system gets replaced, the volume doubles. So the loop from the build keeps running in production: monitor, sample, re-evaluate, adjust the prompts or retrain, and watch the same metrics that proved the value. The day you stop watching is the day the quiet failures start to cost you.

The other direction is growth. Once a slice is live and has shown its value, the obvious next move is the next slice, the next use case on the list you deferred back in discovery. Each one re-enters the same staged rollout: shadow, assisted, then supervised. The process becomes a portfolio, and the system earns its way outward one proven scope at a time.

None of this works if it depends on you. The real deliverable is a system the client can run and extend without the person who built it: a runbook, paired work so their team has done it and not just watched, and enough understanding to take on the next scope themselves. A system only its author can operate is not finished, it is fragile.

## The shape of the whole thing

Step back and the four parts are one argument. You measure the real process before you touch it, because you cannot automate what you have not seen. You build it as two disciplines, not one, because the pipeline and the agent fail in different ways and need different hands. And you take it live as a graded handover of trust, earning autonomy on evidence, proving the value against the baseline, and keeping a person on the decisions that carry weight.

The thread through all of it is the same: let evidence earn each step, and keep a human meaningfully in control of what the system is allowed to do. That is not the slow way to build with agents. It is the way that produces something worth trusting, and worth running long after the launch.

---

## Sources

- B. Mikulski, "Shadow deployment vs. canary release of machine learning models" (shadow and canary as staged, low-risk rollout strategies): https://mikulskibartosz.name/shadow-deployment-vs-canary-release
- Project Management Institute, "Benefits Realization Management Framework" (measuring whether expected benefits are actually realized and sustained): https://www.pmi.org/learning/thought-leadership/series/benefits-realization/benefits-realization-management-framework
