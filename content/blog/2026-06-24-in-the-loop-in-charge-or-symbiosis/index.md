---
title: "In the loop, in charge of it, or in symbiosis? What the human-centered turn in AI still misses"
date: 2026-06-24
draft: false
description: "The field turned back toward the human this year. But being in the loop is not the same as being in charge of it, and neither one reaches what genuine collaboration with AI could be."
tags: ["Take AI Bite", "Human-AI Collaboration", "AI Collaboration", "Competitive Positioning", "Harness Engineering"]
categories: ["Positioning"]
author: "Alberto Diaz Durana"
toc: true
---

For a while, the most confident advice in AI coding was to stop looking. Let the agent write, trust the tests, ship faster. The team at [HumanLayer](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) went further than most: early on, they advised against reading AI-generated code at all. Then they reversed it. After ripping out and rebuilding large parts of systems that had been assembled without real review, they landed on [a rule with no soft edges](https://www.youtube.com/watch?v=YwZR6tc7qYg): read and own the code. No exceptions.

They were not alone, and that is what makes it worth paying attention to. The reversal came from the people with the most to gain from full autonomy. GitHub now says [judgment is the bottleneck, and that this is fine](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/). Anthropic tells you that [you become the verification loop](https://code.claude.com/docs/en/best-practices). Cognition, which builds one of the most autonomous agents on the market, still says [human review is necessary](https://cognition.ai/blog/devin-annual-performance-review-2025), because code quality is not straightforwardly verifiable.

The center of gravity moved back toward the human. The interesting question is what we do with it now that it has.

## The role kept moving

Watch what the job has been called, and you can see the pendulum swing. In 2021, GitHub Copilot arrived as ["your AI pair programmer"](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/). The human stayed the author, accepting or rejecting each line. In February 2025, Andrej Karpathy coined ["vibe coding"](https://en.wikipedia.org/wiki/Vibe_coding), and the role inverted: you became a director of vibes, encouraged to "forget that the code even exists." He meant it for throwaway projects. The industry took it everywhere.

The correction came fast, and each step pulled the human back toward responsibility, but at a higher altitude. Through mid-2025, ["context engineering"](https://www.langchain.com/blog/the-rise-of-context-engineering) recast the human as the architect of what the model sees. By September, GitHub's [Spec Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) moved the human further upstream still, to author the spec and let the code regenerate from it. Then 2026 brought harness engineering, building the whole environment the agent runs in, alongside the blunt reminder to read and own the code. In June, [loop engineering](https://addyosmani.com/blog/loop-engineering/) named the next rung: you stop prompting the agent and start designing the system that prompts it.

Six names in five years, and one clear direction of travel. Each name moves the human up a level of abstraction, from the line, to the context, to the spec, to the harness, to the loop. More leverage at every step. Also more distance from the thing being built.

## Presence is not agency

Here is the uncomfortable part. The human came back, but mostly in name. Being in the loop is not the same as being in charge of it.

The clearest evidence comes from the tools themselves. Anthropic's data on its auto mode shows that [users approve 93% of permission prompts](https://www.anthropic.com/engineering/claude-code-auto-mode), and the company warns that auto mode is "not a drop-in replacement for careful human review on high-stakes infrastructure." A 93% yes rate is not oversight. It is a reflex. When every low-stakes action asks for the same confirmation as the one that matters, the reviewer learns to click approve, and the click stops meaning anything. There is a name for this, [approval fatigue](https://www.techtarget.com/searchcio/feature/Human-in-the-loop-shouldnt-rubber-stamp-decisions), and it is how a human in the loop quietly becomes a rubber stamp.

The trust data says the same thing from the other side. In the 2025 Stack Overflow survey, [only 3.1% of developers said they highly trust AI output](https://survey.stackoverflow.co/2025/ai/), and the top frustration was code that is "almost right, but not quite." People do not trust it, and they approve it anyway, because saying no slows everything down.

There is a sharper way to name the gap. A recent paper on AI oversight calls it the difference between [human-in-the-loop and human-with-agency](https://www.systemsintegrity.org/from-human-in-the-loop-to-human-with-agency-why-ai-oversight-fails-when-humans-are-present-but-powerless/): presence is not control. A person can be in the loop and still lack the time, the information, or the authority to actually stop the system. The authors call the result accountability without authority, you own the outcome of a decision you could not really make.

And notice what even agency assumes. It still casts the human as the supervisor and the AI as the supervised. That is a real step up from rubber-stamping. It is not yet collaboration.

## A different model: symbiosis

So what lies past oversight? Step outside software for a moment, because biology has been running this experiment for about a billion years.

[Symbiosis](https://en.wikipedia.org/wiki/Symbiosis) means, literally, living together: a close and lasting association between two organisms of different species. It comes in [three kinds](https://education.nationalgeographic.org/resource/symbiosis-art-living-together/). In parasitism, one partner benefits at the other's expense. In commensalism, one benefits and the other simply carries it, present, unaffected, contributing nothing. In mutualism, both contribute and both gain.

That vocabulary turns out to be uncomfortably good at describing AI collaboration. A rubber stamp is commensalism: the human is there, contributing nothing the work depends on. Accountability without authority is closer to parasitism: the human carries a cost for a system they cannot steer. Mutualism is the only one of the three worth wanting.

And mutualism runs on difference. A [lichen](https://courses.lumenlearning.com/wm-biology2/chapter/mutualistic-relationships/) is a fungus and an alga living as one body: the alga photosynthesizes, the fungus gathers water and shelter, and neither could colonize bare rock alone. Nearly 90% of plants trade sugar with root fungi that reach water the roots cannot. The partnership works precisely because the partners are not the same. Each brings what the other cannot.

Human and AI fit that shape. The human brings vision, scope, mission, intent, judgment, taste, a sense of what is worth doing and when something is right. The AI brings speed, breadth, recall, the capacity to generate and explore. Work together long enough and you coevolve: your thinking shifts from working with the agent, and the agent's behavior shifts from your feedback, your corrections, your accumulated context.

That feedback is the engine of the whole thing, and it is where Take AI Bite has always put its weight. Feedback here is not a byproduct of the work, it is a discipline of its own, kept in its own layer, [Evaluation and Evolution](/about/): a correction made once becomes a lesson the collaboration keeps, and the practice itself changes from what those loops return. I cannot claim the same for every other framework, and that turns out to be the most revealing difference of all.

What converges is the understanding between you, a shared frame and a shared vocabulary. What must not converge is the two of you into one. The moment the human dissolves into the agent, the difference disappears, and with it the whole source of leverage. A good symbiosis keeps its collaborators distinct on purpose.

## Where autonomy belongs

None of this is an argument against autonomy. There are whole classes of work where letting the machine run is exactly right. A retrieval pipeline answering questions over a document set, an agentic workflow that triages tickets or runs a nightly batch, a well-bounded task with a clear test for done, these do not need a human reading every token. Designed well, they should run on their own, and asking a person to babysit them would only smuggle the rubber stamp back in through another door.

But notice who built them. Someone decided what the system is for, what good output looks like, where it must stop and ask, and what counts as finished. An autonomous system does not author itself. The human understanding and the creative judgment are there from the first line of the dialog that shapes the design, through every correction along the way, to the moment a complete body of work is consolidated and called done.

That is the part the past year of hype kept skipping. The question was never whether the agent runs unattended. It was how well the collaboration that produced it was designed. Every autonomous system worth trusting is the output of a symbiosis that happened first: a human's understanding, built into something that can now run without them watching.

## Where we already stood

This is not a new idea for us, and there is a map to prove it. Back in March, we scored fifteen AI collaboration tools on three axes: how much human oversight they build in, where their operating knowledge comes from, and whether the collaboration accumulates any experience over time. We [scored the competitors first and ourselves last](https://github.com/albertodiazdurana/take-ai-bite), and challenged every one of our own numbers, because a positioning map drawn by the person being positioned deserves suspicion.

One result still surprises me. On the experience axis, the level that means cross-session and human-curated was simply empty. Most tools are stateless, or reset at the end of a session. None had built the thing where a human and an agent accumulate a shared, curated practice across projects.

{{< figure src="/images/blog/competitive-positioning/oversight-vs-experience.png" alt="Scatter plot of human oversight versus experience accumulation for 15 AI tools, with Take AI Bite alone in the top corner." caption="Maximum human oversight on one axis, the only system that accumulates curated experience on the other. The nearest tool is two full levels down, and the level just below it sits empty." >}}

Three months on, it is clear why that gap held. Experience accumulation is finally being built, but on the agent's side of the relationship. [Hermes](https://www.mindstudio.ai/blog/what-is-hermes-agent-openclaw-alternative), from Nous Research, extracts reusable skills from successful tasks and builds a model of its user that compounds across sessions. A whole crop of [agent-memory frameworks](https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-should-try-in-2026/) does similar work. This is real, and it is genuinely useful. It is also the machine remembering you, which is a different thing from the two of you curating a practice together. As one survey of the field puts it, [cross-session learning is usually a memory problem](https://vectorize.io/articles/do-ai-agents-learn-between-sessions). Feedback as a human discipline, where your judgment decides what the shared practice keeps, is the part still missing.

{{< figure src="/images/blog/competitive-positioning/experience-accumulation-bars.png" alt="Bar chart of experience accumulation scores across 15 tools, most clustered low, Take AI Bite highest." caption="Most tools are stateless or session-scoped. The distance at the top of the chart is the part almost no one else has built." >}}

The popular alternative goes the other way. [Spec-driven development](https://reenbit.com/bmad-vs-spec-kit-vs-openspec-choosing-your-spec-driven-ai-framework/), with Spec Kit and BMAD and Kiro, centers the human too, but upstream, on writing the spec and letting the code regenerate from it. That is genuine human authorship, and it moves the human further from the code rather than into a collaboration with it. Useful work, and a different axis from this one.

One honest caveat, the one we flagged on the original map: our top mark on that experience axis rests on a single practitioner's evidence. The mechanism is built for many, the proof so far is one. That keeps it a claim worth testing, not a trophy to polish.

We have [made a version of this argument before](/blog/2026-04-10-project-management-for-the-agentic-stakeholder/), when we treated the AI agent as a new kind of stakeholder, a participant with a real role rather than a tool to aim. Symbiosis is where that relationship leads over time. Managing the AI well was never about ruling it; good management elevates both sides and brings out the best in each. Keep at it long enough and the elevation runs both ways.

## The words are the easy part

The vocabulary has arrived. Human-in-the-loop, judgment is the bottleneck, read and own the code, these are consensus now, repeated by the same labs and tools that spent the year before telling you to let go of the wheel. That is real progress, and it is worth saying so.

But vocabulary is the easy part. It costs nothing to put a human in the loop and call it oversight. It costs more to give that human real agency, the authority and the comprehension to actually say no. And it costs more still to build the thing past agency, a collaboration where human and AI sharpen each other over time, where feedback is a discipline and understanding compounds instead of resetting every session.

Most of the field has reached the first step and named it the destination. Take AI Bite was built for the third, not because we got there first, plenty of these ideas were in the air, but because we treated the human and the agent as collaborators who change each other, and built the loops, protocols and tools to make that change stick. We have come to think of those as [the rules of a game](/blog/2026-05-28-pmo-director-agentic-stakeholder/), shared and legible, there so the work flows instead of stalling on what is allowed.

So when you weigh an AI tool, or a workflow, or a framework, the question worth asking is not whether a human is in the loop. It is whether the human and the AI are making each other better, and whether anything is being kept.

## The systems compared

The map scored fifteen systems. For anyone who wants to look closer, here they are, grouped roughly by what they are.

Methodologies and frameworks: [Take AI Bite](https://github.com/albertodiazdurana/take-ai-bite), [Engage-META / TRAIDA](https://engage-meta.com/), [SPARC](https://github.com/ruvnet/sparc), [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD).

Agentic tools and IDEs: [GSD (Get Shit Done)](https://github.com/gsd-build/get-shit-done), [Kilo Code](https://github.com/Kilo-Org/kilocode), [Cline](https://github.com/cline/cline), [Cursor](https://cursor.com/), [Kiro](https://kiro.dev/).

Autonomous agents and skill libraries: [Devin](https://devin.ai/), [OpenHands](https://github.com/OpenHands/OpenHands), [Paperclip](https://github.com/paperclipai/paperclip), [autoresearch](https://github.com/karpathy/autoresearch), [Picobot](https://github.com/louisho5/picobot), [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills).

*A personal note to close: Take AI Bite works wonders for me. That is a sample of one, and I know it, but it is a trophy I am happy to keep on my own shelf, jaja.*
