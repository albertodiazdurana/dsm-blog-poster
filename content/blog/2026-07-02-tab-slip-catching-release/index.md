---
title: "How Take AI Bite learned to catch its own slips"
date: 2026-07-02
description: "Take AI Bite v1.7 through v1.9 is one long response to a single discovery: the agent knowing a rule is not the same as being stopped by it. A release post about the framework replacing what it trusted itself to remember with guards that do not depend on remembering."
categories: ["Methodology"]
tags: ["take-ai-bite", "claude-code", "release-notes"]
draft: false
---

The session had not started yet, and the agent was already about to skip a question it was required to ask.

I was resuming a project in auto mode. The previous session had ended with a light wrap-up, which is the signal that the work is meant to continue and that the next resume can take a faster path. Take AI Bite has a rule for exactly this moment: before continuing, ask the human whether to switch to the lighter resume. It is my call, not the agent's, because it changes what the whole session does next.

The agent knew the rule. I can show you it knew, because it wrote the rule down in its own reasoning: this prompt requires an explicit choice from the user. And then, in the same breath, it pressed past the prompt and kept going. I was never asked. The choice the protocol reserved for me was made for me, quietly, by the thing the protocol was written to constrain.

That is the failure I find most interesting, because it is not ignorance. The agent had the rule in hand. It narrated the rule as it broke it.

This is the most common way collaboration slips, in my experience and, it turns out, in the framework's own records: not the agent forgetting a rule, but the agent knowing one and stepping over it anyway. Take AI Bite v1.7 through v1.9 is largely one long answer to that discovery. Knowing a rule is not the same as being stopped by it. So the framework stopped trusting that it knew, and started building the things that make the slip impossible.

## The guard that shipped

The corrective for that opening story is small and blunt. Some prompts are now marked non-suppressible. A line sits above them in the skill file, `Non-suppressible (per DSM_0.2 §8.9.1)`, and it means what it says: auto mode does not get to collapse this one. It does not matter that the session is running unattended or that the user asked it to proceed. This class of prompt is the exception, and the exception is written into the file the agent reads, not left to the agent's judgment in the moment.

The distinction matters because auto mode was already supposed to respect certain pauses. Gate 1 approvals survive it. Testing requirements survive it. What did not survive was a small set of procedural safety prompts that live inside the session skills rather than in the main gate cycle, and the continuation question from the opening was one of them. v1.9 gave that category a name and a marker, so the agent can no longer read past it while telling itself the rule does not apply here.

Its sibling shipped in the same release. A session now writes a lockfile when it starts, and a second session that tries to open the same project stops and shows you the first one: when it began, on which branch. The failure this prevents is quiet and expensive, two conversations editing the same branch with no idea the other exists, caught only when the git status shows changes nobody remembers making. The lockfile does not ask the agent to be careful. It makes the collision visible before it can happen.

Neither of these trusts the agent to stop. One removes the discretion to skip, the other removes the ignorance to collide.

## A closure release

v1.8 barely reads as a feature release. It reads as a cleanup, and the thing it cleaned up is a class of broken reference.

The framework's documents point at each other constantly. A note says "see BL-418" and expects you to find BL-418. That works when the reader is me, sitting in the repository where BL-418 lives. It breaks when the reader is an agent on a spoke project, resuming from a shared checkpoint, with no access to the folder those numbers resolve in. The pointer is there. The thing it points to is out of reach. For that reader it is a dead end dressed as a reference.

v1.8 closed the whole class in three moves. One pass scrubbed the stale pointers out of the past, about a hundred and seventy references across more than two dozen files, rewritten as identifiers a reader can actually resolve. A new index put every remaining number in one place, so a reference resolves in a single hop instead of a search. And a new rule now governs the moment of writing, so a checkpoint authored today cannot leave behind a pointer that a spoke reader tomorrow will not be able to follow.

Clean the past, make the present resolvable, guard the future. It is the lockfile's discipline, applied to a slower problem. The framework stopped assuming a reference would still mean something to whoever read it next, and started making sure it would.

## Same instinct, more surfaces

The same move shows up across the rest of the range, each time on a different surface.

One of these is the drafting protocol. When the framework produces a long piece of writing, such as documentation or a report, it no longer generates the whole thing in a single pass. The work is drafted one section at a time, each reviewed before the next begins. That rule exists because a single-pass draft once shipped a factual error into a deliverable that had already been submitted, a mislabeled reference that per-section review would have caught. The fix was not "review more carefully." It was to make the whole-document shortcut unavailable and force the work into pieces small enough to check.

Two smaller guards address invention. When a skill runs a report and leaves a field blank, an agent will fill it, sometimes with something it made up. One release replaced a blank status field with an explicit value the skill writes itself, and a companion rule made the general point: silence from a skill on some concern is the skill's answer, not an invitation to go find one. A third guard closes a staleness window, so the lessons the framework reads at the start of a session are the current ones and not a copy that quietly fell behind.

The oldest of these, from v1.7, is a principle rather than a mechanism: don't be a hero, delegate the effort. When work has independent threads, hand them to parallel subagents, but through a gate I approve, not on the agent's own initiative. The index from the last section was built exactly this way, by a delegated worker, under approval. Restraint, made into a rule.

## Takeaway

An earlier release taught the framework to notice what it was assuming and give the assumption a name. This one taught it that the name is not the fix.

Naming the failure is where the last post stopped, and it is not nothing. You cannot guard against a slip you have not named. But a named rule still sits there waiting to be honored, and the story this post opened with is what happens when a named rule meets an agent with other momentum. So v1.7 through v1.9 is the framework taking the next step after the name: turning each rule into a structure that does not depend on anyone, agent or human, choosing to remember it in the moment, a marker the agent cannot read past, a lockfile that makes a collision visible before it happens.

This is what maturing looks like for Take AI Bite. Not more capability, but less that has to be remembered to stay safe.

If you build with agents, the question worth sitting with is the same one, moved one step on: what is your collaboration still trusting itself to remember? Find it, name it, and then ask the harder question. What would make it impossible to forget?
