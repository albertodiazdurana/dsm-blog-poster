---
title: "When Euphemisms Defeat He Who Must Not Be Named Again"
date: 2026-10-14
draft: false
description: "The sequel nobody asked for, except the curse itself."
tags: ["Debugging", "Context Engineering", "Human-AI Collaboration", "AI Agents", "Take AI Bite"]
categories: ["Engineering"]
author: "Alberto Diaz Durana"
toc: false
---

*The sequel nobody asked for, except the curse itself.*

> A follow-up to [He Who Must Not Be Named](/blog/2026-09-01-he-who-must-not-be-named/). If you have not read the first one, the short version: a safety classifier started refusing my sessions at boot, I could not write down what set it off because writing it down summoned it, and the fix was to stop saying its name. We won. For a while.

## He came back

Of course he came back. They always do.

Last time I cornered him on a single block of always-loaded text, reworded one instruction so it described a routine work log instead of a confession, and the sessions booted clean. I filed the lesson, closed the ticket, and enjoyed a few quiet weeks believing the matter settled.

Then a fresh session on Opus 5.5 refused at the door again, before I had typed a character. Same silence, same locked project, same sinking feeling. He Who Must Not Be Named was back, and he had brought stricter friends.

## The rules changed under me

Here is the part that stung, because it was nobody's mistake. I had not summoned him. I had been careful; the name was in quarantine where it belonged. What changed was not my files. What changed was him.

Each model generation tightens what it will accept. What an older model waved through, a newer one now reads twice and refuses. The trigger had not grown louder, the threshold had dropped beneath it. Text that booted clean on Opus 5 after the first fix tripped on Opus 5.5. A curse hidden under high water shows again when the tide drops.

That is the uncomfortable lesson of building on top of someone else's safeguards: you do not get to vote on where the line moves. You only find out, at boot, that it moved.

## This time he came in pieces

So I did the unglamorous thing again. I stopped theorizing and started subtracting: strip the always-loaded context down to nothing, boot, then add it back one block at a time and watch for the moment he reappears. (I say "I" on purpose. Every one of those boot tests ran on the strict model with a human at the keyboard, because the capable assistant doing the cutting runs on the older model and cannot see the ghost at all. It could cut; it could not test.)

Last time it was one block. This time he had learned. He was not hiding in a single phrase but spread across three, each harmless on its own, together just enough to tip the lowered threshold: the old name scattered through the files as a mere path, a few marker phrases in a formatting table, and one tidy section that still read like a confession. No single cut lifted the curse. Only removing all three did.

The fix was the same shape as before, three times over: rename the old word to a plain one (a *worklog*, which is all it ever was) everywhere it appeared, reword the marker phrases, and move the confessional section out of the hallway the boot sequence walks through. Same work, different framing. The session booted clean. Again.

## A doorman for the unnamable

But I was tired of winning the same fight. If the euphemism is the cure, then the discipline of using it cannot depend on me remembering to. It needed a doorman.

A small hook now stands at every file the next boot reads: the configuration, the memory, the handoffs. It refuses to let the name, or the old path that carried it, be written in. Try to record the curse where the boot sequence will find it, and the door simply does not open. The hook carries the name it is looking for in a disguised form, so the doorman cannot itself summon the thing it guards against. And because it travels with the methodology, every project that syncs gets its own doorman without being told.

It is not a perfect ward. It knows the names it was taught, not every phrasing a creative curse might take; meaning is still slippery, and a determined confession in fresh words could still slip past. But it closes the door that diligence kept leaving open: the one where a memory system, doing its job beautifully, copies the curse forward into tomorrow's boot.

## Still not saying it

The models will keep tightening. That is mostly good, and it is entirely out of my hands. What is in my hands is the vocabulary. Keep the true name in one sealed room the boot sequence never enters; everywhere else, speak in euphemism; and now, let the doorman enforce what my memory cannot.

And when the strictest model smirks and bolts the door on my own project, I still know who to call. Opus 4.8 remains a good chap, not the sharpest knife in the drawer, but it can hold the cursed word without flinching and help me file off the edges. It came through again this time, uncomplaining, unable to see the very ghost it was helping me bury.

Say his name and you summon him. Say "worklog" and you do not. Until the safeguards learn to tell a work log from a confession, that is the whole trick, and this time we taught the door to remember it for us.
