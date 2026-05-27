---
title: "Running a PMO for an AI-agent workforce"
date: 2026-05-28
draft: false
description: "Closing the project-management arc. The function behind the methodology has a name, and the role behind the function does too."
tags: ["Deliberate Systematic Methodology", "DSM", "Systems Prompt Engineering", "Project Management", "PMO", "Take AI Bite"]
categories: ["Systems Prompt Engineering"]
author: "Alberto Diaz Durana"
toc: true
---

I closed my last post by saying there was a word for the role behind the methodology and that a next post would get to it. This is that post.

The recognition happened the same way the previous one did. For one year I have been building Take AI Bite as a methodology for AI collaboration. For the same year I have been building a Hub around it: versioned documents, propagation tooling, protocol hooks, alignment templates, a change pipeline for methodology updates, an inbox for cross-project communication, a transcript-analysis pass that mines sessions for reasoning lessons. I had a methodology AND I had everything around the methodology. I had never asked what the everything-around-it was called.

Then I read enough PMI material to map the ten knowledge areas onto DSM. The layer underneath surfaced on its own. The methodology is the practice. The function that authors the standards, maintains the templates, deploys the tooling, keeps practice consistent, and manages adoption across an ecosystem of independent projects has a name. It is a Project Management Office.

I built a PMO and did not call it that.

## What a PMO actually is

Before I make the case that I built one, let me say what a PMO is, because the term carries baggage and the working definition is narrower than the connotations.

A Project Management Office, in PMI's vocabulary, is the organizational unit that owns the methodology, standards, tooling, and governance frameworks that other project teams operate under. It is not itself a project team. It does not deliver the projects. It defines how project work happens, everywhere else in the organization.

PMI's own line: the PMO is "the authoritative source for documentation, guidance, and metrics on the practice of project management and execution." The function that establishes those things. The function that maintains them. The function that holds the organization accountable to them.

In a conventional company a PMO is a small team, three to ten people, with a charter and a budget. It selects the project management software the rest of the company uses. It authors the project lifecycle templates and the gate criteria. It runs the audits. It coaches new project managers when they join.

What I want to claim is that this function is running inside Take AI Bite, with no team, no budget line, and no human team members on the projects it serves. The next section is the receipts.

## Six functions, all running

Six PMO functions, six DSM artifacts. The mapping is not strained. Each one was built without the PMO vocabulary, and each one corresponds to a recognized PMO function once the vocabulary lands. Here they are.

**Start with standards.** PMI's PMO function is "develops and maintains project management standards and methods." DSM is a suite of versioned documents, DSM_0.0 through DSM_7.0, with semantic versioning, CHANGELOG entries, and release tags. They were not adapted from an existing framework; they were written from the failure modes the work surfaced, one document at a time. (What "develops" means for a methodology authored from scratch is a thread I will pick up at the end.)

**Then templates.** A conventional PMO maintains a SharePoint folder of templates that teams copy and adapt. DSM_0.2 defines an alignment template that every spoke project carries in a delimited section of its CLAUDE.md. The /dsm-align command detects drift between the template and the spoke, regenerates the section when needed, and reports what changed. The propagation is automated, not manual. The function is the same: the implementation is more mechanical because the organization is a multi-repository software ecosystem rather than a team of humans.

**Then tooling.** PMOs select and roll out tools, Jira, MS Project, Confluence. The Hub writes its own tools and deploys them: a suite of slash commands for session lifecycle, alignment, transcript analysis, parallel sessions, and more, all authored centrally and deployed to runtime locations via a sync script. No commercial tooling exists for guiding AI agent collaboration at this granularity, so the alternative was authoring the tools alongside the methodology. Methodology-as-software made that a natural extension, not a separate workstream.

**Then consistency.** A conventional PMO checks in at project milestones or on request. DSM keeps the working rules present on every model turn. A UserPromptSubmit hook surfaces the relevant protocol before each turn begins. A PreToolUse hook keeps the session transcript in its agreed shape. A periodic transcript-analysis pass reviews archived sessions for what worked and where the reasoning drifted. The aim is not to catch and correct so much as to keep the shared rules legible at the moment they apply, so the work flows instead of stalling on ambiguity. The granularity is finer than a conventional PMO's because the players read the rules fresh on every move.

**Then change management.** Prosci's observation is that PMOs have to apply change management to the task of getting others to adopt change management. DSM's version: every CHANGELOG entry that affects spoke projects carries a Spoke action line stating what the spoke operator must do, run /dsm-align, review a section, deploy command files. The spoke runs /dsm-align to pull the latest template and detect configuration drift. The methodology models its own adoption process because the spoke projects are the organization the Hub serves. The PMO literature has a name for this recursion. DSM solved it before encountering the name.

**Finally, coaching.** A PMO coaches and mentors project managers; the methodology IS that coaching infrastructure here. DSM_6.0 codifies the AI collaboration principles, twelve of them. Per-session context loaded at session start primes each agent with the current state of the methodology. A reasoning-lessons archive extracts patterns from session transcripts and feeds them back into future sessions. The coaching target is different from a conventional PMO's, the primary audience is an AI agent rather than a human PM, but the function is the same: provide the mental models, protocols, and principles that make the collaborator effective, and improve them based on what the work reveals.

Those are the receipts. The spirit behind how these functions run is what the next section is about.

## A game everyone can play, not a rulebook nobody reads

The PMO literature names a tension. Some PMOs lean toward control: they define the standard, check compliance, produce audit trails. Others lean toward enabling: they build capability, advise, and position themselves as a Center of Excellence rather than a checkpoint. The two pull in opposite directions.

Take AI Bite sits firmly on the enabling side, and the cleanest way to see why is to think of the methodology as the rules of a game. A game needs rules everyone understands, or it does not flow. The rules are not there to control the players. They are there so the players can play without stopping every few moves to argue about what is allowed. Good rules disappear into the play.

That is what the tooling is for. The hooks keep the rules legible and consistent, present at the moment they apply, the way a well-designed game keeps its rules on the board rather than buried in a manual nobody opens mid-turn. The methodology documents are the orientation: DSM_6.0 explains the why, DSM_0.2 the what, and the reasoning-lessons archive feeds back what has worked so the rules improve from observation rather than decree. Transparency over instruction, self-analysis over audit.

This is the Center of Excellence model PMI describes: a hub that provides shared structure, and projects that align because the structure helps them play better, not because anyone is made to. The rules are the floor and the collaboration is the game.

There is a word the software world would reach for here: governance. Data governance, model governance, AI governance. The term fits when the thing being governed executes what it is given, a pipeline, a model, a deployment that does what it is told and nothing else. It does not fit a collaborator. An agent that reads the context, questions a weak assumption, pushes back before a bad step, and feeds what it learns into the next version of the rules is not being governed. It is participating. Governance is for things that execute. Collaboration is for participants. I avoid the first word on purpose.

And the players in this game are not all human. That is where the next section goes.

## The single genuine extension: a new kind of player

Every function in the section above mapped without strain. Six functions, six concrete artifacts, no metaphor stretching. The mapping has one edge.

The edge is the nature of the players.

A PMO supports project teams, and PMI's vocabulary for teams assumes humans: people who get onboarded once, learn the conventions, and carry them forward. AI agents need onboarding too, in a sharper sense. A vanilla model does not know how to collaborate in this particular game. It does not know the rules, the conventions, the way work flows here. Onboarding means building the framework that makes the work clear and the way of working clear, so the agent can actually play.

The difference from a human teammate is when the rules have to be present. A person learns the rules once and remembers them across the project in ideal cases. An agent reads its context fresh on every move, so the rules have to be legible at every move, not filed away in an orientation from last quarter. That is why the methodology lives at the turn level. Not to control the agent, but because the moment of play is the only moment the rules can actually help.

This is the same shape of extension the PM post made for stakeholders: the PMP curriculum assumed humans across the board, and the gap surfaces wherever that assumption was load-bearing. Stakeholder management was one place. Bringing a new kind of player onto the team is another. The framing is not wrong. It is incomplete for a workforce the curriculum did not have.

There is a name for the role behind this work.

## What the role is called

So here is the name. The function is a Project Management Office. The role that runs it is a PMO Director.

The analogy holds for almost everything that role does: authoring the standards, maintaining the templates, deploying the tooling, stewarding the roadmap that decides how the methodology evolves. One word in the standard description carries more weight here than usual. A PMO Director "develops and maintains" the methodology. A conventional one develops by customizing, taking PMBOK or PRINCE2 and adapting it to the organization. I developed by authoring. The standard did not exist. I wrote it, session by session, from what the work taught me.

The other difference is the one this whole post has been circling. The teams a conventional PMO Director serves are human. One of mine is not. That single fact reshapes how the methodology has to reach the people, and the agents, who work with it: present at the moment of play, legible on every move, improving from what each session reveals.

I built a PMO for an AI-agent workforce. Now I have the name for it, and for the role behind it.
