---
title: "He Who Must Not Be Named"
date: 2026-09-01
draft: false
description: "A defect I could not write down, because writing it down summoned it."
tags: ["Debugging", "Context Engineering", "Human-AI Collaboration", "AI Agents", "Take AI Bite"]
categories: ["Engineering"]
author: "Alberto Diaz Durana"
toc: false
---

*A defect I could not write down, because writing it down summoned it.*

## The name you can't write

Harry Potter fans call him He Who Must Not Be Named. Lovecraft readers know The Unnamable: the cosmic horrors like Hastur or Azathoth whose true name, spoken aloud, is said to bring on madness or death. Both traditions keep the same rule. Some names you do not say, because saying them summons the very thing you were trying to avoid.

Last week I met a bug that played by those rules.

It was a safety classifier, a reasoning-extraction safeguard, and under the newest models it began refusing my session at boot. That part is ordinary. The part that was not ordinary: I could not write down what set it off. Every time I recorded the offending words by name, to document them, to fix them, the next session read them back and summoned the error all over again.

## The self-replicating curse

Here is the mechanism, because it is the whole story. My methodology runs a rich memory-management layer. Every session automatically writes what it learned into a persistent memory file, a session transcript, checkpoints, handoffs: exactly the files the next agent reads on its way in. Ninety-nine days out of a hundred, that is the feature I am proudest of.

On the hundredth day it was the curse. The moment I documented the trigger by name, the memory system did its job and copied that unnamable set of words into every one of those always-loaded files. Next boot, the agent dutifully read them, the classifier scored the accumulated context, and it refused before I could type a single character. I had, in effect, built a machine that re-summoned He Who Must Not Be Named every time I tried to write his name down. At that point the euphemism stopped being a literary joke and became an operational requirement.

## Not a keyword, a meaning

And it went deeper than a blacklist of words. The safeguard was not matching a string, it was matching meaning. Semantic, not keyword. Which meant I could not even open a backlog ticket to track the thing, because an honest definition of the problem was itself close enough, in meaning, to summon it. Describe the curse plainly and you cast it. My own discipline, the habit of writing a clean problem statement before I touch a fix, had turned into a liability. I had a bug I could not name, could not define, and could not file.

## The well-intentioned detour

So I did what I always do. I put a capable model to work on it, and I stayed in the loop on purpose. The model was Opus 4.8, and it was everything you want in a collaborator: fast, rigorous, tireless, well intentioned. It was also, and I say this with affection, not quite on point.

It formed a theory. The problem is the sheer size of the context loaded at boot, too much material tipping some threshold. So it went to work trimming. It relocated documents, it split files, and it designed a genuinely elegant memory-management system along the way. That last part still makes me smile: rules and thresholds that retire old memories to long-term storage and archive the obsolete ones, similar to how humans remember. Three rounds of reduction, each one leaner than the last. Each one, on a fresh session, summoned He Who Must Not Be Named exactly as before.

We had built something beautiful. It solved a problem we did not have.

## I had to follow the breadcrumbs, FUDGE!

In the end the fix was mine to find, and I found it the unglamorous way. I stopped theorizing and started subtracting, cutting, removing and testing. I followed the breadcrumbs of every file an agent touches on its way into a session, removing protocol sections one at a time, testing after each cut, watching for the moment the curse lifted.

It lifted on a single block. Not the largest file, not the accumulated weight of the context, one specific instruction in the always-loaded configuration. The fix was almost insultingly small: reword that one fudging instruction so it describes a routine work log, which is all it ever was, instead of something a safety classifier is trained to refuse. Same task. A euphemism, we humans love them. Different framing. The model booted clean. One more time fudge!

The lesson landed harder because the machine had been so confidently wrong. Three elegant rounds of reduction never touched the problem. One afternoon of manual ablation did. AI amplifies, it does not replace, and this bug sat exactly on that seam: the model was faster than me at nearly everything except knowing what to look at. The solution was still mine... Take that Lord Voldemort!

## Don't say its name

So here is what I would tell anyone building systems that remember. The models are getting stricter, Opus 5 and Fable 5 among them, and their safeguards read for meaning now, not spelling. Mostly that is good. It also means a single phrase in the wrong file can quietly lock you out of your own project, and a memory system diligent enough to preserve that phrase forever will keep re-arming the trap.

Before The Unnamable could take all our hopes away, we spent a day removing every trace of him, every word and every phrasing that came close to his meaning. The rule I kept is short: never write the unnamable, or anything semantically similar, into a file, least of all the ones an agent reads at the door. Name it once, in quarantine, somewhere the boot sequence never looks. Everywhere else, use the euphemism. And whenever Opus 5 complains with some very strict guardrail, watching and smirking while my work kicked the bucket, invite over Opus 4.8 to help you reword it. It is a good chap, not the sharpest knife in the drawer, but it will not summon the curse.

Say his name and you summon him. So, at least until the safeguards learn to tell a work log from a confession, we will not say it.
