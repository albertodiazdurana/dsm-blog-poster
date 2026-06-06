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

**URL:** https://www.linkedin.com/posts/albertodiazdurana_ai-humanaicollaboration-dsm-share-7447105689770078208-ov7k
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-07-dsm-v1.4.5-protocol-visibility/

**Text:**

What this release taught me: more documentation is not the answer to agents not following documentation. Proximity is. So is reframing principles into templated instructions shaped for the moment they apply.

Two failures in a single session. A spoke agent wrote a feedback file directly into the Hub without showing me first. The same agent answered a question about a skill from its one-line description, and only then asked permission to read the full definition.

Both rules already existed in DSM. Both had existed for months. The agent broke them anyway.

I went looking for the gap, and the gap was not the rules. It was where the rules lived.

Spoke agents inherit a long chain of methodology documents, but at session start they actually read one specific surface: the alignment template that gets written into the project's CLAUDE.md. Protocols sitting upstream are technically inherited and behaviorally invisible. The agent never lands on them at the moment of decision.

DSM v1.4.5 fixes this by relocation, not invention. Two rules moved from upstream documents into the alignment template, where the agent reads them every turn. The Destructive Action Protocol becomes a three-line "Cross-Repo Write Safety" section. Earn Your Assertions becomes a one-line "read the source before answering." Same rules, new placement.

Two more features in the same release follow the same shape: sprint boundaries got a structured retrospective, and the wrap-up type marker closes a session-lifecycle gap that had been quietly costing me overhead for weeks.

A note on what comes next. Right now I am calling proximity "the unit that matters" without being able to measure it. That is changing. Graph Explorer, the spoke that builds a structural graph of any DSM project, has a proposal for an agent-consumable knowledge summary that derives hub scores, reference chains, and concept clusters from the graph itself (BACKLOG-302). Once that ships, "proximity to the decision" stops being a qualitative claim and becomes a number: the distance, in the reference graph, between where a rule lives and where the agent reads. I expect that to change which rules I move next, and probably to surface a few I have not noticed yet.

Full post: https://take-ai-bite.com/blog/2026-04-07-dsm-v1.4.5-protocol-visibility/

#AI #HumanAICollaboration #DSM #TakeAIBite

## Post 7: Think Ahead (2026-04-09)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_humanaicollaboration-dsm-takeaibite-share-7447783991056744448-9n6P
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-08-think-ahead/

**Text:**

There is a moment in every growing project when the backlog starts feeding itself. You fix something, and the fix reveals two more things. You build a feature, and three people ask for the feature next to it. The work produces more work.

The instinct is to read this as a problem, when really it is a graduation.

That moment hit me in March. Thirty active backlog items, all high priority, no way to explain to anyone which one mattered most. I had been building Take AI Bite and its methodology, DSM, for four months. Strategically, a roadmap could help address the backlog issue. But before I built one, I asked myself why I had needed one *now*, and not four months ago.

The answer turned out to be a principle.

Strategic planning is phase four of a project, not phase one. It needs four layers underneath it before it can do real work:

1. Operational. Templates, conventions, protocols. The mechanics of "done."
2. Infrastructure. Backlogs, versioning, hub-spoke routing. A way to track what exists.
3. Philosophical. Articulated values. A way to weigh trade-offs against what you actually care about.
4. Learning. Transcripts, reasoning lessons, feedback loops. A way for plans to stay connected to evidence.

A roadmap built without these is speculation with formatting. A roadmap built on top of them is a navigation tool. The four-month gap between "I should plan this" and "I can plan this" was not procrastination. It was the layers accumulating until planning had material to work with.

This is what I named Principle 1.9 of Take AI Bite: **Think Ahead.** Build the map before you walk the territory. Strategy emerges from operational maturity, not before it.

I almost missed this principle. My first instinct was to write "I had a problem, so I built a roadmap." The honest version is "I had a problem, which made me ask why the problem existed in the first place." The build was the receipt. The question was the point.

Full post: https://take-ai-bite.com/blog/2026-04-08-think-ahead/

#HumanAICollaboration #DSM #TakeAIBite #SystemsThinking

## Post 6: Systems problem, not a prompt engineering problem (2026-04-08)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_humanaicollaboration-llms-systemsthinking-share-7447398752887324673-kBYX
**Status:** Published
**Related blog updates:** https://take-ai-bite.com/about/ and https://take-ai-bite.com/blog/2026-03-12-take-ai-bite-framework/ (BL-014, DSM_6.1 layer surfaced)

**Text:**

Working effectively with LLMs isn't a prompt engineering problem. It's a systems problem.

Since July last year I've been running an applied research program in human-AI collaboration called Take AI Bite. I started it because I couldn't find a framework that kept me in control of the work instead of reactively chasing whatever the model produced.

The system around the model is what does the heavy lifting. The prompt is the smallest part of it.

Underneath Take AI Bite is an operational layer I call DSM, Deliberate Systematic Methodology. It governs 14 repositories as one graph. The most recent layer, DSM 6.1, is about Systems Prompt Engineering: how context flows through operational channels, which instruction patterns hold up under pressure, and how you evaluate and evolve the whole setup over time.

The honest test of any methodology is whether you'll use it on yourself. So I did. Graph Explorer is a Python application I built end-to-end through AI collaboration, without writing the code myself, to validate the very ecosystem the methodology governs. It parses 14 repositories, builds a typed knowledge graph in FalkorDB, validates 1,191 cross-references, lints conventions, compares historical commits, and tracks drift between private and public repos. It took documentation errors across the ecosystem from 448 down to 6, and it now sits at 664 tests across 15 sprints.

The interesting part isn't the tool. It's that every sprint surfaced something the methodology was missing, and I fed those gaps back into DSM. Building the validator made the framework that built the validator measurably better. That's the loop I keep chasing.

If you want to read more: https://take-ai-bite.com/

#HumanAICollaboration #LLMs #SystemsThinking #PromptEngineering #AIEngineering

## Post 8: The inbox was a Communication Management Plan (2026-05-12)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_projectmanagement-pmp-humanaicollaboration-share-7459885565509980160-Hk2b
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/
**Series:** Fragment 1 of 6 from the PM post series (BL-020).

**Text:**

I was reading my own inbox folder when it clicked. Not the email kind, the one that lives at `_inbox/` inside every project I run, where messages from one repository land for another to pick up at the next session start. I had built it months earlier to stop losing observations between projects. Populated it without ceremony, processed it without ceremony, moved entries to `done/` when finished. It worked. I had not given it a name beyond "the inbox," and I had not asked where the pattern came from.

The pattern came from a chapter I had read in a different life. In 2016 I sat for the PMP exam. One of its ten knowledge areas is Communication Management: the discipline of moving information between stakeholders deliberately rather than hoping it shows up where it needs to be. Who needs to know, in what form, by when, through which channel, and how you confirm receipt.

The inbox folder is Communication Management. I had built a Communication Management Plan inside a software project and not noticed.

That recognition turned into a question. If one knowledge area was already running in the project under a different name, were the others?

I went back and looked. Spoiler: all ten were there. Some of them I had built deliberately. Most of them had walked in quietly, over months, doing work I had attributed to something else.

I will get to the other nine in the next posts. But the part I want to put down first is the smaller, stranger thing: a decade-old credential, one I thought I had stopped using, turned out to be running my AI collaboration. I just did not have the vocabulary.

Full post: https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/

#ProjectManagement #PMP #HumanAICollaboration #DSM #TakeAIBite

## Post 9: Ten knowledge areas, all running, none named (2026-05-12)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_projectmanagement-pmp-humanaicollaboration-share-7460228213261148160-Orb0
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/
**Series:** Fragment 2 of 6 from the PM post series (BL-020).

**Text:**

I claimed in my last post that all ten PMP knowledge areas were running inside my AI collaboration methodology. That is a big claim. Here are three of them:

**Cost Management** is the context window. The agent's context window is finite. Every file read, every tool call, every back-and-forth turn consumes a resource that runs out, and when it runs out the second half of the session degrades silently. PMI calls this cost. The methodology calls it context budget. The discipline is identical: estimate before you spend, warn when you are running low, scope the work to the resource you actually have. The names are different but the work is the same.

**Risk Management** is the failure mode catalog. When something deviates from the prescribed behavior, there is a three-step response: fix the immediate issue, identify the root cause, prevent the recurrence. PMI builds risk registers for exactly this. I had a folder of recorded failure modes with associated protocols and had been calling it "reasoning lessons." It is a risk register that gets loaded into memory at each session start.

**Scope Management** is the MUST/SHOULD/COULD framework on every backlog item, the scope review checkpoint at sprint boundaries, the rule that every backlog item gets a single topic and splits when it tries to become two. These are scope disciplines applied to the work the methodology exists to govern. PMI would recognize them without prompting.

The other seven follow the same shape. Communication, Schedule, Integration, Quality, Resource, Stakeholder, Procurement. Each one mapped to something I had built and named locally without intentionally aligning by design with any specific curriculum it belonged to.

What changed when I noticed: the vocabulary. The methodology was already doing the work. The PMI vocabulary just gave me a way to see which parts were load-bearing and which parts were decoration. Almost everything turned out to be load-bearing. The decorative bits had quietly disappeared, sprint by sprint, because the work pressured them out.

A credential I had not used in a decade turned out to have been running underneath the whole time without the labels.

Full post: https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/

#ProjectManagement #PMP #HumanAICollaboration #DSM #TakeAIBite

## Post 10: I built the PM chapter before I knew it was a framework (2026-05-12)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_leadership-projectmanagement-pmp-share-7460536897677787137-i3p7
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/
**Series:** Fragment 3 of 6 from the PM post series (BL-020).
**Note:** First post using the `#Leadership` hashtag in place of `#DSM`. Method for selecting hashtags from data is captured as BL-023.

**Text:**

I owe my last post a clarification.

Communication Management was the first PMP knowledge area I *recognized* inside the methodology. It was not the first I had intended to put there. The first was Scope.

Before Take AI Bite existed, before any of this had a name, I had already written DSM_2.0, the Project Management Guidelines. One of the earliest documents in the methodology. It came right after DSM_1.0, the Data Science Collaboration Methodology, and it landed there because the work needed it. I knew from the PMP that a project without a defined scope will drift, so I built the scope discipline in deliberately, with rules I had carried from a decade earlier: MUST / SHOULD / COULD on every backlog item, a single topic per item, splits when an item tries to become two.

I was writing project management into a data science methodology before I had thought to name any of this as a framework.

So the recognition I described last time is not that PM showed up uninvited. It is that PM was the first thing I invited in, and the rest of the knowledge areas walked in quietly behind it, over months, without announcing themselves.

The PMP credential was never something I put down. I stopped applying it *intentionally*, which is different. When I started building Take AI Bite, I thought I was solving a different problem: how the human stays meaningfully present when the machine produces faster than anyone can read. The principles, the protocols, the operational channels, none of it felt like project management. It felt like figuring out how to collaborate with an agent that does not get tired and will always have something to say, even if it is wrong.

Then I noticed the inbox. And the rest of the curriculum was there, doing work I had attributed to something else.

The credential was not being repurposed. It was being completed.

Full post: https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/

#ProjectManagement #PMP #HumanAICollaboration #Leadership #TakeAIBite

## Post 11: The stakeholder the PMP curriculum did not have (2026-05-12)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_projectmanagement-pmp-humanaicollaboration-share-7462612124964433920-IT8q
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/
**Series:** Fragment 4 of 6 from the PM post series (BL-020).
**Note:** Slug picked up first 3 hashtags only. `#Leadership` sat in position 4 and did not appear in the URL. Tag ORDER may matter for slug composition; tracked in BL-023.

**Text:**

I said in the last post that the PMP credential was being completed, not repurposed. There is one place where "completed" needs an asterisk.

PMI's framing of project management has a stakeholder model at its core. A stakeholder is anyone whose interests, expectations, or actions affect or are affected by the project. Sponsors, customers, team members, regulators, the people next door to the construction site. The discipline is built around managing them: identifying them, understanding their interests, communicating with them at the right cadence, getting their input into the decisions that affect them. The whole curriculum assumes the stakeholders are human.

The work I do now has two kinds of stakeholders.

The human collaborator is one of them: me, the client, the reviewer, the eventual reader of the deliverable. The AI agent is the other. It has expectations (what counts as a valid response, what counts as a violation), it has interests in the methodology sense (the protocols it operates under shape what it can do and how), and its actions affect the project in ways that need to be communicated, reviewed, and integrated. It is not a tool in the way a compiler is a tool. It is a participant whose behavior is governed by an instruction system that I author and maintain.

That instruction system is, structurally, a stakeholder management plan for a stakeholder PMI did not have to consider.

The artifacts are doing the work the metaphor describes:

- `CLAUDE.md` is a stakeholder communication document.
- The session-start command is a stakeholder onboarding protocol.
- The feedback files are a stakeholder feedback channel.
- Version updates are stakeholder change management.

This is not a stretch. The credential I had not used in a decade transferred almost without modification, except here. PMI's Stakeholder Management area is the place where the curriculum needed extending, not just completing, because the 2016 exam did not have a chapter on managing an agent that inherits behavioral protocols through a reference chain and has its own failure modes when its context drifts.

Traditional project management manages one kind of stakeholder. This work manages two.

Full post: https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/

#ProjectManagement #PMP #HumanAICollaboration #Leadership #TakeAIBite

## Post 12: PMI is in the AI conversation. This is a third direction. (2026-05-12)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_projectmanagement-pmp-humanaicollaboration-share-7463186564945424385-P_uo
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/
**Series:** Fragment 5 of 6 from the PM post series (BL-020).
**Note:** Trimmed ~220 characters pre-publish to land under LinkedIn's 3000-char limit (final body 2827 chars). First explicit Take AI Bite naming in the series. URL slug led with `projectmanagement-pmp-humanaicollaboration` (same as Post 11); `#Leadership` in position 4 did not enter the slug. Tag-text-order is not the deterministic slug rule (BL-023 observation).

**Text:**

A fair question after my last post: has PMI not already addressed AI? It has.

Since I sat for the PMP in 2016, the institute has not been standing still. PMI launched **PMI-CPMAI** to credential the practice of managing AI delivery projects. It shipped **PMI Infinity**, a GenAI assistant aimed at project managers doing their existing work. And the upcoming **PMBOK 8th edition** embeds AI as a tool across the performance domains. PMI is in the AI conversation and seriously so.

The direction PMI has taken is twofold:

1. Credentialing the projects that deliver AI systems.
2. Putting AI in the hands of the project manager as a tool for doing existing PM work better.

Both are real and useful. Neither is the one I am pointing at in this series.

The framing I have been working with in **Take AI Bite** is a third direction: treating the **instruction system that governs the agent as a stakeholder management plan** for a stakeholder the curriculum did not have to consider.

Why does the AI get the stakeholder label rather than the tool label? Because of the kind of work and the kind of interaction. The agent participates per turn, per decision, per artifact. The collaboration is two-way: I review what it produced, and what it produced feeds back into the instruction system that governs the next turn. And the bidirectionality is not local to the methodology project. In any project that follows the methodology, the AI's outputs feed back into the methodology through feedback files and reasoning lessons, which then propagate to every project's instruction system. The methodology grows through that exchange. Tools generate outputs where there is no interaction or dialog. A stakeholder participates in the exchange of ideas.

PMI's two directions use AI to help the PM manage human stakeholders. This work extends Stakeholder Management to cover the agent itself, as a participant whose behavior is shaped by an artifact that the human authors and maintains.

I want to be honest about the distance between the three:

- PMI direction 1: I am running a project, and the project produces an AI system.
- PMI direction 2: I am running a project, and an AI helps me run it.
- Third direction: I am running a project, and the AI is a stakeholder I am managing.

Not in conflict, complementary. A PM running a Generative AI delivery (direction 1), using PMI Infinity to draft status reports (direction 2), still has to author the system prompt that governs the agent doing the technical work (third direction). The three coexist in the same project.

Worth naming as distinct, though: different framings carry different obligations.

Full post: https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/

#ProjectManagement #PMP #HumanAICollaboration #Leadership #TakeAIBite

## Post 13: There is also an organization (2026-05-12)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_projectmanagement-pmp-humanaicollaboration-share-7465159793746264065-SP84
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/
**Series:** Fragment 6 of 6 from the PM post series (BL-020). Series closes here; hands off to BL-019 (PMO Director full blog post).

**Text:**

The knowledge areas are one layer. There is another underneath.

The PMP curriculum teaches project management as a practice: ten knowledge areas, processes, inputs, outputs. PMI also defines a function that owns the methodology across projects: the **Project Management Office**. A PMO is not a project team. It is the organizational unit that authors the standards, maintains the templates, deploys the tooling, monitors compliance, and manages methodology adoption across the teams under its domain. The function that defines how project work happens everywhere else.

That function is what **Take AI Bite's Hub** is.

Not because I designed it to mirror a PMO. Because the problems a PMO exists to solve, standards drift, tooling fragmentation, compliance without authority, methodology adoption across independent teams, are the same problems a hub-and-spoke methodology ecosystem has to solve. The structure that resolves them is the same structure.

Concretely, the Hub does PMO work:

- Authors the methodology documents. Versions them.
- Maintains the templates every project inherits.
- Deploys the tooling, slash commands, hooks, validators, that runs in every project.
- Manages the change pipeline when a methodology update needs to propagate across an ecosystem of independent repos.

This is not a metaphor. The artifacts are doing the work.

Which means there is a word for the role behind the methodology, too. I built a PMO and did not call it that. A next post will get to the name.

Full post: https://take-ai-bite.com/blog/2026-04-10-project-management-for-the-agentic-stakeholder/

#ProjectManagement #PMP #HumanAICollaboration #Leadership #TakeAIBite

## Post 14: Running a PMO for an AI-agent workforce (2026-05-28)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_projectmanagement-pmo-leadership-share-7465728153559363584-9TC7/
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-05-28-pmo-director-agentic-stakeholder/
**Source:** BL-019 (PMO Director blog post). Cross-post for the full blog post that the PM-post LinkedIn series (Posts 8-13) handed off to.
**Hashtag set:** #ProjectManagement #PMO #Leadership #HumanAICollaboration #TakeAIBite (dropped #PMP, added #PMO).
**Slug observation (BL-023):** declared hashtag order matched URL slug lead-tags 1:1 for the first three tags (`projectmanagement-pmo-leadership`). First Post in the series where slug appears to track declared order.

**Text:**

I built a PMO for an AI-agent workforce.

For a year I have been building Take AI Bite as a methodology for AI collaboration, and for the same year I have been building everything around it: versioned documents, alignment templates, tooling, a change pipeline, an inbox, a transcript-analysis pass that turns sessions into reasoning lessons. I had the methodology, and I had the whole apparatus that keeps it consistent across projects. I never asked what the apparatus was called.

It is a Project Management Office. The function that authors the standards, maintains the templates, deploys the tooling, keeps practice consistent, and coaches the teams. Six PMO functions, six concrete artifacts, mapped without strain.

One word I avoid: governance. Governance fits a thing that executes what it is given, a pipeline, a model, a deployment. It does not fit a collaborator. An agent that reads the context, questions a weak assumption, and pushes back before a bad step is not being governed. It is participating. Governance is for things that execute. Collaboration is for participants.

Which is also where the PMO model needed extending. A conventional PMO serves human teams. One of mine is not human. A vanilla model does not know how to collaborate in this particular game, so onboarding means building the framework that makes the work clear and the way of working clear. The rules have to be present at the moment of play, because that is the only moment they can help.

There is a name for the role behind this: PMO Director of an AI-agent workforce.

Full post: https://take-ai-bite.com/blog/2026-05-28-pmo-director-agentic-stakeholder/

#ProjectManagement #PMO #Leadership #HumanAICollaboration #TakeAIBite

## Post 15: How Take AI Bite learned to bootstrap itself (2026-06-03)

**URL:** https://www.linkedin.com/posts/albertodiazdurana_how-take-ai-bite-learned-to-bootstrap-itself-share-7468948595631742976-SNd3/
**Status:** Published
**Blog post:** https://take-ai-bite.com/blog/2026-06-03-tab-bootstrap-release/
**Source:** BL-022 Front E (LinkedIn cross-post for the v1.5/v1.6 release post "How Take AI Bite learned to bootstrap itself").
**Hashtag set:** #AI #HumanAICollaboration #ClaudeCode #AIAgents #TakeAIBite. First Take AI Bite post applying the new CLAUDE.md TAB/DSM convention (drops #DSM, keeps #TakeAIBite as the brand tag).
**Slug observation (BL-023):** slug is TITLE-derived (`how-take-ai-bite-learned-to-bootstrap-itself`), NOT hashtag-derived. New outcome class compared to Posts 10-13 (hashtag-based, varied lead-tags) and Post 14 (hashtag-based, matched first 3 declared tags). LinkedIn's slug algorithm appears to sometimes pick the linked post title over hashtag tags. Possible factors to investigate in BL-023: title distinctiveness, hashtag overlap with other posts on the platform, link visibility in the post body.
**Note:** Published version of the text contains "AIs" plural. This linkedin-posts.md file has been updated to "an AI" singular per the new CLAUDE.md typography rule, but the live LinkedIn post retains the original wording.

**Text:**

It is curious how AI, in this case Claude Code, will embark on a quest with topics not entirely explored. That would write the fate for an explorer in counted minutes. We humans sometimes think an AI suggests acting on something based on training, as if training is equivalent to knowledge. Try entering the Amazon jungle without knowledge and see if you walk out at all.

My favorite example surprised me the most: Claude Code actively suggesting to create Skills and Hooks without entirely knowing how Anthropic defines them. It is like saying "hey, I'm a surgeon, let's operate because I know I can fix this... but I do not know how to deal with an artery." The agent treats Skills and Hooks as concepts it knows from training, proposes shapes that do not match the actual Anthropic spec, ships them with confidence. The mess shows up later, in the form of a hook that does not fire or a frontmatter field that gets silently ignored.

A smaller version of the same story: an agent ran `gh pr create` against a repo whose default branch had been silently pointed at a session branch that no longer existed. Forty-five minutes went into investigating what looked like a GitHub outage and turned out to be a single `gh repo view` call we had not thought to make.

The pattern got a name: Read the User's Manual. Before you commit to using something, find out what it actually is. The principle now has a hard gate behind it (default-branch verification at session start), a dedicated platform-quirks file the agent reads, and a self-bootstrapping protocol for fresh public-mirror clones.

What v1.5 and v1.6 of Take AI Bite teach me about how the framework actually grows: it names the assumption it just paid for, and turns the name into a thing the project can rely on next time.

Full post: https://take-ai-bite.com/blog/2026-06-03-tab-bootstrap-release/

#AI #HumanAICollaboration #ClaudeCode #AIAgents #TakeAIBite