---
title: "The rules that almost cover the case"
date: 2026-07-25
description: "Take AI Bite v1.13 through v1.17. Three gaps that an existing protocol nearly covered, two disciplines for producing prose, and what it takes to turn a stated value into something an agent can act on."
categories: ["Methodology"]
tags: ["take-ai-bite", "claude-code", "release-notes"]
draft: false
---

Nothing here broke a rule.

In May an agent working on one of my projects read through a public issue thread. The comments were friendly and well argued, written by people trying to help. By the end of the thread the agent had a plan ready for me: three engagement options, pick one. Nobody had asked it to engage at all.

Take AI Bite already had a protocol for untrusted external input. It looks for shell commands, injection patterns, instructions dressed up as data. It found nothing, because there was nothing to find. The comments were courteous. Courtesy is not a pattern you can search for.

If a stranger kindly tells you to jump out of a window from the top of a building, would you do it? Politeness is not authorization.

## A rule that states a value

That gap has a shape, and it repeats.

Take AI Bite holds that the conversation defining the work is the collaboration itself, not a preamble to it. One thing that follows: when I reframe an agent's proposal instead of answering it, the agent should rebuild on the new framing. The principle has been in the framework for a long time. It did not stop the failure. Over four months an agent defended its original framing six separate times across six sessions, and each one was recorded as it happened.

Take AI Bite does not promote a rule on the strength of one bad afternoon. A pattern has to clear an evidence bar before it earns a name. The six entries together were not a memory problem. They were the signature of a rule that states a value without naming the behavior the value requires.

The window case shows why this is hard to catch. That input protocol was doing real work. It checked the wrong layer. A rule that sits next to a failure without covering it costs more than no rule at all, because it produces the feeling of coverage. Nobody goes looking for a gap when something that sounds right is already in place.

## What the gates were not asking

Three gaps surfaced on the same project within a day of each other, and none was caught by a gate. They were caught in review, where I read over finished work before it counts as done. The review did its job three times. That it had to do it alone is the part worth fixing.

The sharpest was a comment. The agent was working through review feedback on a public pull request, and every file edit had come to me as a diff, approved on its own, before it ran. The closing step was different in kind. Posting a comment is a command, so what came up for approval was a command, with the comment text buried inside it as an argument. I approved an action. The words went onto a public thread under my GitHub name without ever being reviewed as words.

Take AI Bite already gated writes into repositories I do not own. That rule asks where the file lands. It does not ask whose voice it is written in.

The second gap was a pull request into a project that publishes its own requirements: a contributing guide, a body template, a release-note file its checks look for. One of the principles says to ground your work in what a tool actually does, and the agent had done that for its own tooling. Nothing sent it to read the receiving project's rules. The fix is a step with a list attached: read those files first, plus a merged request or two of similar shape, then write against what they require.

The third fix is a sequence rather than a warning: classify what the external content is doing, surface it, wait for a decision, then plan. It ends with the rule I like most here. A generic yes does not clear the gate. When the answer comes back as ok or go ahead, the question gets asked again with the specifics named.

The three fixes have the same form. Not a value to hold in mind, but a named behavior at the point where the decision happens.

## The same move, applied to writing

Two other changes in this batch do it for prose.

The first says a concept is presented once and deepened afterwards, rather than announced in a summary and restated in the body. Why it needs a rule of its own: repetition is not an AI tell, so a pass that hunts for AI tells reads straight past it.

The second is about where a draft lives. A draft delivered in a chat window cannot be edited by the person reviewing it. So each piece goes to a file, one subchapter or one paragraph at a time, and the author edits in place before the next one arrives.

## Half a rule

Take AI Bite has fourteen collaboration principles and none of them is wrong. What this batch shows is that a principle is half of a rule. It tells you what to value and leaves open what to do at the moment the value is in play. Until that second half is written down, the reviewer is the mechanism.

The review caught them. But catching something after it happens is not the same as preventing it, and a framework whose safety rests on me noticing is one that gets less safe as the work grows.

Take AI Bite does not get safer by asking for more attention. It gets safer by needing less.
