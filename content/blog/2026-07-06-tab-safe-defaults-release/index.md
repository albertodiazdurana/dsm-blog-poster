---
title: "How Take AI Bite learned to build its own guardrails"
date: 2026-07-06
description: "Take AI Bite v1.10 through v1.12 add guardrails: changes that make an unsafe operation impossible or blocked, rather than asking the agent to remember to avoid it. A short walk through what each one prevents."
categories: ["Methodology"]
tags: ["take-ai-bite", "claude-code", "release-notes"]
draft: false
---

Take AI Bite versions 1.10 through 1.12 are a batch of guardrails. They target ways a working session could quietly damage its own files: a log that grew until it was unusable, an archive overwritten by a routine move, a commit landing in the wrong repository.

There is something fractal about the set. A fractal repeats its whole shape at smaller and smaller scale, and each of these guardrails is a small copy of the one idea the framework runs on, to make the safe path the one you get by default, set down at the scale of a single edit, file, or repository.

None of the failures were carelessness. Each was an ordinary operation whose default behavior happened to be destructive in one specific situation. Telling the agent to be more careful does not close that gap; changing what the operation does closes it.

Here is what each guardrail prevents, and how Take AI Bite propagates each fix so the same failure does not recur across the ecosystem.

## Guardrails built into the workflow

The first two change how a routine file operation behaves, so the damaging version of it can no longer happen.

When a session finishes processing an item from its inbox, it moves the file into a `done/` archive. The old convention named the archived file after its source, so a second entry from the same source moved on top of the first and replaced it. That is exactly what happened once: a move overwrote a rolling archive and 323 lines vanished, caught only before the commit. The fix is a filename. Archived entries now carry the date in their name, so two of them never collide and the move has nothing to overwrite. Nothing has to detect the collision or clean up after it. With two filenames that cannot coincide, it simply cannot happen.

The second guardrail draws a line around git. Take AI Bite projects often sit in a hub-and-spoke layout, and a session in one repository sometimes needs to drop a file into another, a notification or a piece of feedback. The write itself is fine. The problem was that a session would also run git commands in that other repository, and once a background session committed on another project's active branch and swept that project's staged work into the commit. The rule now is narrow: a session may write files into a repository it does not own, but may not run git there. The repository that owns the code owns its history. The stray commit is no longer a mistake to avoid, it is an action the session does not take.

## Guardrails at the moment of action

The other two sit at the point where an action happens and decide whether it goes through.

One is a check that refuses a single kind of edit. The runaway log came from a find-and-replace with "replace every match" turned on, run against text that appeared more than once, so each match pasted the same block and the file grew at every step. One such edit reached 95 megabytes before anyone noticed. Replacing every match is a normal thing to want, so the guardrail is specific rather than broad: a check refuses that one kind of edit on the session log in particular, before it runs, and names the safe way to make the same change. It is not advice the agent can read and then override. The edit does not happen.

The other is a correction to a guardrail that had started firing too often. Writing a file into another repository asks for confirmation, which is the right default. But during the end-of-session routine the same confirmation came up again and again for destinations the protocol already knows are safe, the project's own memory, a sibling project's inbox. A check that interrupts you on safe actions trains you to wave it through, and that habit is exactly how the dangerous one slips past. So the routine now confirms those known destinations once, up front, and the check keeps its force for the writes that actually warrant a look.

## The same shape at every scale

That is the fractal shape from the opening, seen whole. Blocking one edit on one file, dating one archive name, drawing a line around git in one repository: each is the same move as the framework it belongs to, the safe path made into the default. Zoom in on the smallest check and you find the idea the whole methodology runs on. Zoom out to the methodology and it is that check again, repeated wherever a failure has shown the default was unsafe.

It is also how Take AI Bite grows, and it does not grow in only one place. The guardrails are not planned in advance; each is added at the scale where something went wrong. But a fix made on one project does not stay there. Take AI Bite runs as a hub and its spokes, and an improvement proven on one spoke returns through the hub to all of them. That movement has a name here, propagation, and it is the concrete counterpart to the abstract picture: fractal in shape, propagation in reach. A single overwritten archive on one project becomes, a version later, a guardrail every project already has.
