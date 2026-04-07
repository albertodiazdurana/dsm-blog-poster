---
title: "The trainer and the agents"
date: 2026-04-02
draft: false
description: "I built an AI agent ecosystem from scratch. Three franchise stories helped me understand what I was actually doing."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Take AI Bite"]
categories: ["Reflections"]
author: "Alberto Diaz Durana"
toc: true
images: ["trainer-and-dragon.jpeg"]
---

![A small person riding a small dragon in flight](trainer-and-dragon.jpeg)

I did not plan to become a trainer. But here I am, 15+ projects in, with a system of AI agents I built from scratch. Each one shaped by the projects that tested them. 20,000 lines of methodology, a feedback loop that runs both ways, and a system that learns for itself and remembers what I learned even when I forget. Also, very stubborn sometimes, but that's on me, and that's why I keep refining how we work together.

At some point I realized I had seen this story before. Three times, actually.

---

## Three stories, one pattern

### Pokemon: the collector

Ash starts with nothing. He receives Pikachu, builds a team one by one, and trains them through battles. Each Pokemon has unique abilities. The trainer's strategy matters as much as the creature's power. The Pokedex catalogs what you have encountered, the gym badges prove what you have overcome.

The DSM mapping is direct. Each spoke project is a new team member. The contributor profile is the Pokedex. Completed backlogs are gym badges. Choosing which DSM track to deploy for a project is choosing who to send into battle.

But there is a limit to this parallel. Ash collects and commands. The relationship is vertical: trainer above, creature below. The Pokemon do not talk back. They do not grade the trainer.

### Big Hero 6: the builder

Hiro builds Baymax from scratch in a garage. Baymax starts as a simple healthcare companion and becomes something more. The team assembles around a shared mission, each member with a specialty. The garage is the hub where everything gets refined.

What makes this story land is one line: "Are you satisfied with my care?" Baymax asks this after every interaction. DSM does the same thing. At the end of every spoke project, the methodology asks the project to score each section. How did I do? What should change? The system literally asks for feedback.

And there is the rebuild. Hiro loses Baymax and builds him again. The creation carries meaning. It is not disposable.

But Hiro is a genius who builds in isolation. The collaboration is mostly one-directional: Hiro designs, Baymax executes. The creature does not reshape the builder.

### How to train your dragon: the partnership

Hiccup does not fit the mold. He is an outcast in a village that fights dragons. He meets Toothless, a creature everyone fears. Instead of fighting, he observes. He learns how the dragon behaves. He adapts. He builds a prosthetic tail fin so Toothless can fly, but the catch is that it only works when Hiccup is riding. Neither can fly alone.

This is the closest parallel to what I built.

The trust is earned through patience, not given by default. Hiccup changes his approach based on what he observes in Toothless. Toothless responds to Hiccup's presence differently than to anyone else. The village initially fears the dragons, then adopts them when the proof is undeniable.

Replace "dragon" with "AI agent" and "village" with "organization" and you have the Take AI Bite pitch: the relationship is bidirectional, trust is built through deliberate practice, and the result is something neither side could do alone.

---

## Where the metaphor breaks (and gets interesting)

Unlike dragons, DSM agents talk back. They grade the trainer.

One spoke project (sql-query-agent) scored 22 methodology sections, averaging 3.3 out of 5. It proposed 14 improvements. I accepted 9 of them. The lowest scores revealed blind spots I did not know I had.

The creatures are training the trainer. The care is bidirectional. Baymax asks "are you satisfied with my care?" but DSM also asks "are you satisfied with yours?"

Every project feeds back into the methodology. What one project discovers improves every future one. Version 1.0 was built from a customer segmentation project: my starter. Version 1.4.1, 15+ projects and 85+ features later, looks nothing like it. Not because I rewrote it, but because every project reshaped it.

---

## The team

Each project in the ecosystem has a role, like Hiccup's team of dragons each with a different ability:

- **DSM Central** is the hub, the dragon sanctuary where knowledge accumulates and gets refined
- **Graph Explorer** is the validator, 547 tests parsing cross-references and knowledge graphs to make sure the documentation stays honest
- **Blog Poster** is the communicator, turning internal methodology into public-facing content
- **Take AI Bite** is the public-facing principles, the part that visitors see first
- The spoke projects (SQL Query Agent, stress tests, portfolio) are the training grounds where methodology meets real problems

When the methodology grew complex enough to need its own integrity checking, I built the tool that validates it. Using the methodology to build the tooling that validates the methodology. That is the kind of loop that only makes sense when you have been inside it.

---

## What comes next

I have a distant idea I keep coming back to: what if the trainer-agent relationship had a visual form? A personal knowledge graph, colored by the domains you have worked in. NLP in blue, time series in green, the DSM core always in white. Each person's graph would be unique, shaped by their projects and their experience. Then maybe a network for AI agent ecosystems. Your agents showcase what you have built together. We'll see...

That is a long way off. For now, the system is 15+ projects, 20,000 lines of documentation, a feedback loop that runs in both directions, and a growing conviction that the franchise writers had it right all along: the interesting part is not the creature's power. It is the bond.

---

*Part of the [Principles Series](https://github.com/albertodiazdurana/take-ai-bite) -- Take AI Bite, powered by Deliberate Systematic Methodology (DSM).*