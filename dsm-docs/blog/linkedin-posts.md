# LinkedIn posts

Reference file for published LinkedIn posts and their humanized versions.

## Post 1: Blog launch (2026-03-07)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_take-ai-bite-activity-7436142360511717376-lWF7
**Status:** Clean, no changes needed

## Post 2: Take AI Bite company (2026-03-20)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_aiagents-humanintheloop-productmanagement-share-7439832315725246465-R69v
**Status:** Humanized replacement ready

**Replacement text:**

I spent the last eight months running data science projects with AI coding agents. Not experimenting, running: 15+ repositories, 200+ backlog items, thousands of review cycles.

The pattern was always the same. The AI generates fast. The human becomes a bottleneck. And the moment you stop engaging with the output, you lose control of what you're building.

Take AI Bite started as my notes on how to fix that. It became 9 principles, a versioned methodology, and a framework I use every day to keep human judgment at the center of AI collaboration.

The idea is to size the work so every delivery earns real understanding, not just approval. Small, reviewable increments where the human reads, questions, and decides.

I have directed the construction of a 531-test application through this process without writing its code. I run multiple projects simultaneously, reviewing one while another generates output. The bottleneck is judgment, not speed, and that is exactly where it should be.

Take AI Bite is now live as a company. The principles are open, the blog is running, and I am looking for organizations serious about adopting AI systematically.

## Post 3: 84 features (2026-03-20)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_ai-humanaicollaboration-methodology-share-7440867361764585472-FPMQ
**Status:** Humanized replacement ready

**Replacement text:**

I mapped 84 features of DSM across three dimensions to see where it actually sits compared to other AI coding tools.

Human Oversight: structural gates the AI cannot bypass without genuine human engagement. Every artifact passes through approval before it exists.

Knowledge Provenance: a versioned methodology that every project inherits and extends. Not a blank slate with a config file.

Experience Accumulation: insights from one project improve the methodology for every future session. The system retains what you learn across projects, not just within them.

No single feature here is new. Memory systems, feedback loops, review gates, they exist elsewhere in various forms. What is different is that 84 features work together, and the methodology improves through use.

Full post: https://take-ai-bite.com/blog/2026-03-20-dsm-features-three-dimensions/

#AI #HumanAICollaboration #Methodology #DataScience #SoftwareEngineering

## Post 4: The Trainer and the Agents (2026-04-02)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_ai-humanaicollaboration-dsm-activity-7445316791947395074-J8Dj
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-02-trainer-and-agents/

**Text:**

I did not plan to become a trainer. But after 15+ projects with AI agents I built from scratch, I realized I had seen this story before.

Pokemon: a trainer collects creatures and commands them. The relationship is vertical.

Big Hero 6: a builder creates a companion that asks "are you satisfied with my care?" The creation carries meaning, but the builder designs and the creature executes.

How to Train Your Dragon: an outcast earns trust through patience. He builds a prosthetic so the dragon can fly, but it only works when they fly together. Neither can do it alone.

That last one is the closest to what I built. A methodology where every project feeds back into the system. Where the agents grade the trainer: one project scored 22 sections of my methodology and averaged 3.3 out of 5. The lowest scores revealed blind spots I did not know I had.

The creatures are training the trainer.

#AI #HumanAICollaboration #DSM #TakeAIBite

## Post 5: Protocol existence is not protocol visibility (2026-04-07)

**URL:** TBD
**Status:** Draft
**Blog post:** https://take-ai-bite.com/blog/2026-04-07-dsm-v1.4.5-protocol-visibility/

**Text:**

Two failures in a single session. A spoke agent wrote a feedback file directly into the Hub without showing me first. The same agent answered a question about a skill from its one-line description, and only then asked permission to read the full definition.

Both rules already existed in DSM. Both had existed for months. The agent broke them anyway.

I went looking for the gap, and the gap was not the rules. It was where the rules lived.

Spoke agents inherit a long chain of methodology documents, but at session start they actually read one specific surface: the alignment template that gets written into the project's CLAUDE.md. Protocols sitting upstream are technically inherited and behaviorally invisible. The agent never lands on them at the moment of decision.

DSM v1.4.5 fixes this by relocation, not invention. Two rules moved from upstream documents into the alignment template, where the agent reads them every turn. The Destructive Action Protocol becomes a three-line "Cross-Repo Write Safety" section. Earn Your Assertions becomes a one-line "read the source before answering." Same rules, new placement.

Two more features in the same release follow the same shape: sprint boundaries got a structured retrospective, and the wrap-up type marker closes a session-lifecycle gap that had been quietly costing me overhead for weeks.

What this release taught me: more documentation is not the answer to agents not following documentation. Proximity is. So is reframing principles into templated instructions shaped for the moment they apply.

Full post: https://take-ai-bite.com/blog/2026-04-07-dsm-v1.4.5-protocol-visibility/

#AI #HumanAICollaboration #DSM #TakeAIBite