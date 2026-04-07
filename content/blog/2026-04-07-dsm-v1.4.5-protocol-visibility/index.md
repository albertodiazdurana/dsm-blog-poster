---
title: "Protocol existence is not protocol visibility: DSM v1.4.5"
date: 2026-04-07
draft: false
description: "Two spoke agent violations in one session traced back to the same root cause, and how DSM v1.4.5 fixes it by relocating rules to where agents actually read them."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Release Notes", "Take AI Bite"]
categories: ["Releases"]
author: "Alberto Diaz Durana"
toc: true
---

Session 8 of the efficientnet-flower-classification-transfer-learning project. A spoke agent wrote a feedback file directly into the Hub's repo. It did not show me the content first, did not ask, did not pause. The write just happened.

A few hours later in the same session, I asked the same agent what `/dsm-finalize-project` does. It gave me a partial answer from the skill's one-line description, and then politely asked if it could read the full definition. After answering. That order was wrong, and we both knew it.

Two failures. Both already covered by rules that DSM has had for months. The Destructive Action Protocol in Module C is explicit about cross-repo writes needing confirmation. Earn Your Assertions, principle 1.3 in DSM_6.0, says investigate before you claim. The rules were there when the agent broke them.

So I went looking for the gap, and the gap was not the rules.

## Where the agent actually reads

Spoke agents inherit a long chain of methodology documents through a configuration reference. So technically, every protocol in that chain is "active". In practice, what an agent actually sees at session start is one specific surface: the §17.1 alignment template that gets written into each project's CLAUDE.md. That template is short. It is loaded every turn. It is where the operating instructions live as far as the agent is concerned.

Module C and DSM_6.0 §1.3 sit upstream of that template. The agent inherits them through the @ chain, but never lands on them during the moment of decision. They might as well not be there.

The documentation was fine. The placement was the problem.

A reasoning lesson from the session that diagnosed this caught it in a single line: "Protocol existence is not protocol visibility. The §17.1 template is the behavioral surface for spoke agents." That sentence sat on my screen for a while. It explained more than just these two violations.

## The fix

v1.4.5 puts both rules on the surface where the agent reads.

A new section called "Cross-Repo Write Safety" goes into the §17.1 template. Three lines. The first write to any path outside the current repository in a session requires explicit user confirmation, with content and target path shown beforehand. Same rule the Destructive Action Protocol always carried. It now arrives at session start, in front of the agent, in language the agent can act on without translating.

Code Output Standards in the same template gets one extra line: "Read the relevant source before answering questions about it; do not answer from partial knowledge." Earn Your Assertions, made concrete at the exact spot where the agent is about to answer.

Nothing was invented for this release. Two rules got moved.

## The same move, in two other corners

Once I started looking, the pattern showed up in two other places that shipped in the same release.

Sprint boundaries used to have a checklist. Close open items, push branches, update memory. Mechanically correct and analytically empty. Phase 4 of BACKLOG-310 added a structured retrospective at the boundary itself, across six dimensions: themes, principles, evolution, collaboration, learning, maturity. The checklist still runs, but it now sits next to actual analysis. That is F-090, Sprint Retrospective Intelligence, and it is the Think Ahead principle (1.9) finally showing up in the place where the agent decides what the next sprint should focus on, instead of sitting in a principles document one inheritance level removed.

The wrap-up type marker (F-088) is the same kind of plumbing fix. Light wrap-up exists for short continuation sessions. Full wrap-up exists for everything else. The next session-start command had no way to know which one had run, so I would sometimes run heavy `/dsm-go` over a light context and pay overhead for nothing, or run `/dsm-light-go` after a full wrap-up and quietly skip checks I needed. A `.claude/last-wrap-up.txt` marker now records the type at wrap-up and gets read at session-start. The two ends of the lifecycle agree on what happened. It is a small thing. Small things matter when you run a lot of sessions.

Neither of these features added a new concept. The concepts were already there. They just were not where the agent could act on them.

## What this release taught me

After three sessions sitting with this, here is what I keep coming back to. DSM does not really evolve by writing more rules. It evolves by two related moves.

One is relocation. You take a rule that lives upstream in the inheritance chain and you put it on the behavioral surface, the place the agent actually reads when it is about to act. The closer the rule is to the decision, the more often it gets followed. That sounds obvious when you write it down. It is much less obvious when you are looking at a violation and your first instinct is to add another paragraph somewhere.

The other is reframing. You take a principle, written in the kind of language that principles are written in, and you translate it into a templated instruction shaped for the moment it applies. "Earn Your Assertions" is a fine principle, but the agent should not have to reason from there to "read the source file before answering questions about it." The translated form should arrive already done, at the spot it is needed. Templates do that work, and they take a real load off the agent's understanding.

There is a tempting answer to "agents not following documentation," and that answer is "more documentation." It is wrong almost every time. The right answers are proximity and reframing. Move the rule closer. Translate it into something the agent can act on without going back to first principles every turn.

I expect most future DSM releases to look like this one. A bit less new vocabulary. More rules quietly moving closer to where they have to do their work.

---

*v1.4.4 and v1.4.5 shipped on the same day and are treated as one release in this post. For the full feature timeline, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md). For the changelog entries, see [CHANGELOG.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/CHANGELOG.md). The features discussed here ship as F-087, F-088, F-089, and F-090, implementing BACKLOG-310, BACKLOG-314, and BACKLOG-315.*