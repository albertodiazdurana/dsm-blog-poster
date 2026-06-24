# Harness Engineering, Context Engineering, and the Human-AI Collaboration Trend (2021 to 2026)

**Type:** Research capture (DSM_0.2 §10 web research)
**Created:** 2026-06-07
**Session:** parallel-24.1 (QA, read-only + this file)
**Purpose:** Refresh the evidence base for BL-005 (competitive positioning blog post). Establish the chronology of how the human engineer's role evolved alongside AI coding tools, and validate whether Take AI Bite's "understanding over speed / human-AI collaboration" posture aligns with the 2026 trend.
**Target outcome:** Input to BL-005 repositioning. This is an internal research note, not reader-facing prose. The /humanizer gate and the TAB/DSM reader-facing vocabulary rules apply later, when this material is adapted into the blog post, not here.
**Status:** Draft (open for revision)

---

## 0. Scope and method

Trigger: a keynote by Dexter Horthy (HumanLayer), "Everything We Got Wrong About Research-Plan-Implement," at the Coding Agents conference (Computer History Museum, 2026-03-03). The original BL-005 research (Session 9, 2026-03) framed two camps, "speed" versus "understanding," with the key message "understanding over speed." Since then the field's vocabulary has shifted, and the question is whether that shift validates or undercuts Take AI Bite's posture.

This note was built from two passes:

1. A first pass anchored on Horthy and Birgitta Böckeler (the harness-engineering definition).
2. A second, broader pass run as four parallel read-only research agents, each owning one axis: (a) dated chronology, (b) independent practitioner voices, (c) lab and vendor framing, (d) empirical data on speed and quality. Each agent returned findings with verbatim quotes where possible and an explicit verified-versus-secondary flag.

Verification discipline: every figure below carries a primary-or-secondary tag. Claims that could not be traced to a primary source are quarantined in §10, not presented as fact. The point of this note is not to claim who arrived first. It is to map the evolution and locate Take AI Bite within it.

---

## 1. Headline finding

The center of gravity in AI-assisted software engineering has moved back toward the human engineer, with the AI used for leverage and speed rather than as a substitute for judgment. The most vivid signal is a reversal by the people who pushed automation hardest: Horthy and HumanLayer "initially advocated against reading AI-generated code," then "reversed this position entirely" after having to "rip out and replace large parts of systems built without proper code review." The new rule is blunt, "read and own the code. No exceptions."

Three caveats keep this honest:

- The re-centering applies most cleanly to experienced engineers. Junior hiring is genuinely squeezed, so "the engineer is back" is really "the senior engineer is back."
- The "speed" half is contested. A controlled study (METR) found experienced developers were 19% slower with early-2025 tools on repositories they knew well, while believing they were faster.
- There are two coexisting 2026 postures, not one settled consensus: minimize human code-reading by building a strong harness (OpenAI, parts of Böckeler) versus preserve human comprehension as the last line of defense (Pragmatic Engineer, Stack Overflow, Thoughtworks). Take AI Bite sits with the second camp, while the harness discipline supplies the tooling that makes the second camp practical.

---

## 2. Chronology (2021 to 2026)

The throughline is the human's role: author, then director, then architect and owner. Dates are the publication or first-appearance date of the source, oldest first.

| Date | Milestone | What changed in the human's role | Primary anchor |
|------|-----------|----------------------------------|----------------|
| 2021-06-29 | GitHub Copilot launches as "your AI pair programmer" | Human stays the line-by-line author; the AI suggests, the human accepts or rejects and owns every line | github.blog |
| 2025-02-02 | Karpathy coins "vibe coding" | Role inverts: human becomes a vibes-director, "forget that the code even exists." Karpathy scoped it to throwaway projects, not production | x.com (text confirmed via Wikipedia, CodeRabbit) |
| 2025-04 (approx) | Horthy, "12-Factor Agents" | Pushback begins: reliable agents are "mostly just software," builders must "own your control flow" and own the context window | github.com/humanlayer/12-factor-agents |
| 2025-06-19 | Tobi Lütke endorses "context engineering," Karpathy amplifies | Human re-enters as a context architect, curating what the model sees | dbreunig.com |
| 2025-06-23 | LangChain (Harrison Chase), "The rise of context engineering" | Reliability located in the human-built system around the model, not the model's mind-reading | langchain.com |
| 2025-07-09, 2025-08-05 | Böckeler, "I still care about the code" / "pushing AI autonomy" | The canonical "we still need to care about the code" position; "keep the AI on a leash" | martinfowler.com |
| 2025-09-02 | GitHub open-sources Spec Kit (spec-driven development) | Human moves upstream to author and refine specs; positioned as the antidote to piecemeal vibe coding | github.blog |
| 2025-11 | Thoughtworks Technology Radar Vol. 33: "Complacency with AI-generated code" on Hold | Institutional warning against review fatigue and automation bias | thoughtworks.com |
| 2026-01-06 | Orosz (Pragmatic Engineer), "When AI writes almost all code" | Engineers "more valuable than before" as validators and architects; the key skill is "knowing when not to trust the code" | pragmaticengineer.com |
| 2026-02-05 | Hashimoto, "My AI Adoption Journey" ("Engineer the Harness") | Names the discipline: when an agent makes a mistake, engineer the environment so it never repeats it | mitchellh.com |
| 2026-02-11 | OpenAI, "Harness engineering: leveraging Codex in an agent-first world" | Human builds and steers the harness (repo, CI, instructions, feedback) rather than typing code | openai.com (date and detail via InfoQ) |
| 2026-02-17 | Böckeler, "Harness Engineering, first thoughts" (memo) | Harness should "direct human input to where our input is most important," not eliminate it | martinfowler.com |
| 2026-03-03 | Horthy keynote, "Everything We Got Wrong About Research-Plan-Implement" | The public reversal: read and own the code; decompose oversized prompts; add alignment checkpoints | youtube.com (keynote) |
| 2026-03-25 | Anthropic, "How we built Claude Code auto mode" | Data on autopilot risk: users approve 93% of permission prompts; auto mode "is not a drop-in replacement for careful human review on high-stakes infrastructure" | anthropic.com |
| 2026-04-02 | Böckeler, "Harness engineering for coding agent users" (full article) | Formalizes the discipline: guides (feedforward) and sensors (feedback); "the human's job is to steer the agent by iterating on the harness" | martinfowler.com |
| 2026-05-07 | GitHub, "Agent pull requests are everywhere. Here's how to review them." | "Judgment is the bottleneck, and that's fine"; "human accountability remains the foundation of code quality in the agent era" | github.blog |
| 2026-05-22 | Faros AI, "Harness Engineering: Making AI Coding Agents Work in 2026" | Popularizes the three-era framing and the "Agent = Model + Harness" distillation | faros.ai |

Key shifts in one breath: author (2021) became director (vibe coding, early 2025), then the pendulum swung back through context engineering and spec-driven development (mid to late 2025) to architect and owner (harness engineering plus read-and-own-the-code, 2026).

---

## 3. The three eras: prompt, then context, then harness engineering

The industry now describes a layered progression, each era wrapping the previous rather than replacing it:

- **Prompt engineering** (roughly 2022 to 2023): asking the model the right question.
- **Context engineering** (2024 to 2025): building systems that feed the model the right information and tools. The clean primary anchor is Harrison Chase / LangChain (2025-06-23): "Context engineering is building dynamic systems to provide the right information and tools in the right format such that the LLM can plausibly accomplish the task." Horthy's "12-Factor Agents" (April 2025) is widely cited as the first deep dive on the idea, and he is credited with popularizing the term.
- **Harness engineering** (2026): engineering the full environment the agent runs in. Böckeler's definition: the harness is "everything in an AI agent except the model itself," and building one "is a specific form of context engineering." She splits it into guides (steer before the agent acts) and sensors (observe after, self-correct), each either computational (tests, linters) or inferential (LLM-based). Faros frames five layers: tool orchestration, verification loops, context and memory, guardrails, observability.

Attribution caveats (see §10): the named practice "engineer the harness" traces to Mitchell Hashimoto (2026-02-05). The equation "Agent = Model + Harness" is a downstream distillation (Faros and others), not Hashimoto's own phrasing. The neat "three eras with dates" packaging is mostly third-party narrative; only the two endpoints (context, harness) have clean primary anchors.

Horthy's "dumb zone" finding from the context-engineering era still holds and motivates the harness era: quality degrades past roughly 40% context-window utilization, "you always get better results if you use less of them."

---

## 4. Independent practitioner voices ("read and own the code")

These are individuals, not vendors, which is what makes the convergence notable.

- **Simon Willison** (2025 to 2026). The golden rule: "I won't commit any code to my repository if I couldn't explain exactly what it does to somebody else." His line between vibe coding and engineering: "If an LLM wrote the code for you, and you then reviewed it, tested it thoroughly and made sure you could explain how it works to someone else that's not vibe coding, it's software development." His "vibe engineering" framing has experienced engineers "amplify their existing expertise" while remaining "decision-makers and quality gatekeepers."
- **Addy Osmani** (2024-12-04 and after). The "70% problem": AI delivers 70% fast, the final 30% (edge cases, security, production-readiness) still needs human engineering. "Use AI to accelerate, not replace, your judgment." (The phrasing "understand every line" is a paraphrase, see §10.)
- **Kent Beck** (2025-06-25). Coins "augmented coding" as the disciplined counterpart to vibe coding: "In augmented coding you care about the code, its complexity, the tests, and their coverage." The engineer makes "more consequential programming decisions per hour" while keeping the same value system as hand-coding.
- **Gergely Orosz / The Pragmatic Engineer** (2025 to 2026). "The hard parts of software development, understanding requirements, designing maintainable systems, handling edge cases, ensuring security and performance, still require human judgment." And: "AI isn't making our software dramatically better because software quality was never primarily limited by coding speed." (Some quotes overlap with Osmani's syndication, see §10.)
- **Birgitta Böckeler / Thoughtworks** (2025-07-09 and after). "I personally think we very much should still care about the code." Minimum bar: "the minimum I want to still care about and be on top of is the test code." Autonomy limit: "we have to keep the AI on a leash."
- **Thoughtworks Technology Radar Vol. 33** (2025-11), institutional. Placed "Complacency with AI-generated code" on Hold: "it's all too tempting to be less vigilant when reviewing AI suggestions after a few positive experiences." Calls for "sustained human judgment, oversight and healthy skepticism."
- **Paula Muldoon** (2026-03-10). Direct "engineers back to center" evidence: senior engineers must get hands-on again because timelines collapsed. "You have deep technical and product expertise. You can use these tools to accelerate yourself to ship fast."

Empirical support for the judgment-matters thesis: the METR study (2025-07-10) found experienced open-source developers 19% slower with early-2025 AI tools on mature repositories they knew well, while believing they were 20% faster. This is the strongest single caution against treating "AI equals speed" as automatic.

Even the loudest maximalist lands on human control. Steve Yegge (the "IDE is dead by 2026," very high output claims) is explicitly skeptical of full autonomy, calling the idea that agents will do all the heavy lifting "smoking some serious crack." So the honest counter-position is not "AI replaces the engineer," it is "the engineer orchestrates, the AI executes."

---

## 5. Lab and vendor framing of human-in-the-loop

The tool builders, who have every incentive to claim full autonomy, instead architect the human back into the loop:

- **Anthropic (Claude Code)**: "Without a check it can run, 'looks done' is the only signal available, and you become the verification loop." Plan mode separates exploration from execution so the human reviews a plan before edits. Auto-mode post (2026-03-25): users approve 93% of permission prompts, and auto mode "is not a drop-in replacement for careful human review on high-stakes infrastructure."
- **OpenAI (Codex)**: approvals are "the human-in-the-loop path for tool calls," the run "pauses until you approve or reject it." The long-horizon framing is "less babysitting, more delegation with guardrails," steering at milestones.
- **GitHub (Copilot coding agent)**: the agent always produces a PR for human review and structurally cannot self-approve or run CI without a human. "Human accountability remains the foundation of code quality in the agent era," and "judgment is the bottleneck, and that's fine."
- **LangChain**: "Models are not mind readers. If you do not give them the right context, they won't know it exists." Reliability comes from the human-built context system.
- **Cursor**: by default, sensitive actions and terminal commands "require your manual approval" (page partially verified, see §10).
- **Cognition (Devin)**: "Human review is still necessary, because code quality is not straightforwardly verifiable." Devin "can't independently tackle an ambiguous coding project end-to-end like a senior engineer could."

The pattern across competitors who would benefit from claiming otherwise: the human is the verification loop, the approver, the accountable owner. That convergence is the strongest evidence in this note.

---

## 6. The empirical picture: speed versus quality

Adoption and self-reported speed are high; trust and verified quality lag, which is exactly the gap that re-centers the human.

**Speed and adoption (primary):**
- 2025 DORA report: AI adoption among developers reached 90% (up 14 points YoY); over 80% report a productivity boost; AI now correlates with higher delivery throughput (a reversal from 2024).
- 2025 Stack Overflow Developer Survey: 84% use or plan to use AI tools; 51% of professional developers use AI daily.
- HumanLayer: "ship 2-3x faster" while maintaining quality that "passes expert review" (vendor self-report, see §10; the phrase "near-human code quality" is a paraphrase, not their wording).

**Quality, security, governance (primary):**
- "Debt Behind the AI Boom" (arXiv:2603.28592, 2026-03-30): 105,364 surviving AI-introduced issues at HEAD (22.7% of 464,900 tracked), across 302,600 AI-authored commits in 6,299 repos; 89.3% are code smells. (Note: the round figure "110,000+" that circulates is a slight overstatement, the precise number is 105,364.)
- "Agent Skills in the Wild" (arXiv:2601.10338, 2026-01-15): 26.1% of 31,132 agent skills contained at least one security vulnerability; 5.2% high-severity. Skills bundling executable scripts are 2.12x more likely to be vulnerable.
- Deloitte, State of AI in the Enterprise 2026: "Only one in five companies has a mature model for governance of autonomous AI agents."
- Stack Overflow 2025 trust collapse: only 3.1% "highly trust" AI output; the top frustration is "AI solutions that are almost right, but not quite" (66%); 45.2% say debugging AI-generated code is more time-consuming. Experienced developers are the least trusting.
- DORA "trust paradox": 24% trust AI "a great deal," 30% trust it "a little or not at all," adopted as a tool, not a substitute for judgment.

**Counter-evidence worth carrying for balance (primary):** "Will It Survive?" (arXiv:2601.16809) found agent-authored code had a lower line-modification rate than human code (53.9% versus 69.3%) in its sample, complicating a one-sided "AI code is disposable" narrative.

The synthesis the data supports: speed is real but contested and uneven, quality and trust are the binding constraints, and the binding constraint is precisely where human judgment and code ownership live.

---

## 7. The genuine tensions (do not oversimplify)

For credibility in the blog post, name these rather than flatten them:

1. **Harness-minimizes-reading versus read-and-own.** OpenAI's "0 lines of manually-written code" experiment and Böckeler's "direct human input to where it matters most" pull toward less line-by-line reading. Orosz, Stack Overflow, and Thoughtworks pull toward preserving human comprehension. Both are 2026 positions. They are reconciled only partially by the harness idea (let tooling absorb the routine so human attention concentrates on what matters).
2. **Senior versus junior.** The re-centering is a senior-engineer story. Entry-level hiring is genuinely disrupted (directional, secondary data only, see §10). A blog post claiming "engineers are back" should specify which engineers.
3. **Speed is not automatic.** METR's slowdown finding means "AI for speed" is a claim to qualify, not assert. This actually strengthens the "understanding over speed" message: the measurable win is comprehension and reliability, not raw velocity.

---

## 8. Take AI Bite alignment

Take AI Bite has, from the outset, structured human-AI collaboration so that the human keeps comprehension and ownership while the AI accelerates. Its principles (human oversight, Read-the-Manual, Earn Your Assertions, Take a Bite for incremental work, understanding over speed) describe the same posture the 2026 trend has converged on from the opposite direction.

The honest framing, and the one the project's conventions require, is not "Take AI Bite was first." It is that the industry's 2026 vocabulary, harness engineering, the human as verification loop, "judgment is the bottleneck," "read and own the code," now names what Take AI Bite already practiced as principle. The 2025 "vibe coding" detour (outsource the thinking) was the antithesis of the collaboration stance; the correction that followed (context, then spec, then harness, each re-centering the human) is what the trend has been doing ever since.

Mapping, trend to Take AI Bite:
- "Read and own the code. No exceptions." maps to human oversight and Read-the-Manual.
- "You become the verification loop" (Anthropic) maps to Earn Your Assertions.
- Harness engineering (guides and sensors, validation loops) is the tooling expression of structured, accountable collaboration.
- "Understanding over speed" is reinforced, not threatened, by the data: speed is contested, comprehension and trust are the binding constraints.

---

## 9. Implications for BL-005 (repositioning angle)

1. **Refresh the two-camps map.** The original "speed versus understanding" axis still works, but the news is that the speed camp's own leaders moved toward understanding: Horthy's reversal, OpenAI and GitHub architecting human review back in, even Yegge conceding human control. The map should show that migration, not a static standoff.
2. **Reframe the axis as "where the human's judgment sits."** Author (2021), director (vibe coding), architect and owner (2026). Take AI Bite occupies the "human keeps comprehension and ownership" position, which is now the consensus direction of travel.
3. **Use Horthy's reversal as the narrative hook.** It is external, dated, and quotable validation, framed as "the field caught up," not self-congratulation.
4. **Lead with comprehension, not speed.** Given METR and the trust data, anchor the post on understanding and reliability. "Understanding over speed" is the durable claim.
5. **Be precise about who.** Specify experienced engineers; acknowledge the junior-tier disruption rather than papering over it.
6. **Cite primaries, carry the caveats.** Use the corrected figures (105,364, not 110,000), attribute "Agent = Model + Harness" to downstream commentary not Hashimoto, and treat the unverified items in §10 as off-limits for the published post unless re-verified.

---

## 10. Accuracy ledger (corrections and unverified claims)

- **"Agent = Model + Harness" attribution.** Mitchell Hashimoto coined "engineer the harness" (2026-02-05) but did not write the equation. The equation is a downstream distillation (Faros AI and others). Do not attribute it to Hashimoto.
- **"110,000+ surviving issues" overstated.** The primary paper reports 105,364 (Figure 9: "over 100k by February 2026"). Cite "over 100,000 (105,364)."
- **"65% of agent failures trace to harness defects" dropped.** This appeared in an early search snippet but is not in the Faros article that was fetched, and no primary source was found. Do not use.
- **HumanLayer "near-human code quality" is a paraphrase.** Their own writing says quality that "passes expert review" and explicitly rejects "10x" hype. The "2-3x" figure is a vendor self-report (YC page plus their GitHub doc), not an independent study.
- **QRSPI versus CRISPY naming unresolved.** Secondary write-ups disagree on the successor to RPI: QRSPI (Questions, Research, Structure, Plan, Implement) and CRISPY (Context, Research, Iterate, Structure, Plan, sYnthesize) both circulate, with stage counts from 5 to 8. The keynote's own title is just "Everything We Got Wrong About Research-Plan-Implement." Do not assert one canonical acronym.
- **Junior-developer hiring percentages are secondary.** The ~46% figures circulate in blog and Medium sources, not traced to primary labor statistics. Use as directional signal only.
- **Code-churn figures (3.3% to 5.7 to 7.1%) are secondary.** Seen only in aggregator content this pass; the usual primary-ish source is GitClear, not confirmed here.
- **Two pages could not be fetched directly** (Karpathy's tweet, x.com 402; the OpenAI harness page, 403; Cursor docs, 403). Their content is corroborated via independent secondary sources but is partially verified, as noted inline.
- **The "three eras with dates" packaging is partly narrative.** Only the context era (LangChain, 2025-06-23) and the harness era (Hashimoto, 2026-02-05) have clean primary anchors.

---

## 11. Sources (complete, deduplicated)

### Chronology and framing
- [Introducing GitHub Copilot: your AI pair programmer (GitHub Blog, 2021-06-29)](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)
- [GitHub Copilot (Wikipedia)](https://en.wikipedia.org/wiki/GitHub_Copilot)
- [Andrej Karpathy "vibe coding" tweet (2025-02-02)](https://x.com/karpathy/status/1886192184808149383)
- [Vibe coding (Wikipedia)](https://en.wikipedia.org/wiki/Vibe_coding)
- [A semantic history of vibe coding (CodeRabbit)](https://www.coderabbit.ai/blog/a-semantic-history-how-the-term-vibe-coding-went-from-a-tweet-to-prod)
- [12-Factor Agents (Dexter Horthy / HumanLayer, GitHub)](https://github.com/humanlayer/12-factor-agents)
- [Why "Context Engineering" Matters (Drew Breunig)](https://www.dbreunig.com/2025/07/24/why-the-term-context-engineering-matters.html)
- [From vibe coding to context engineering: 2025 in software development (MIT Technology Review)](https://www.technologyreview.com/2025/11/05/1127477/from-vibe-coding-to-context-engineering-2025-in-software-development/)
- [Spec-driven development with AI: new open source toolkit (GitHub Blog, 2025-09-02)](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- [github/spec-kit (GitHub)](https://github.com/github/spec-kit)
- [GitHub Spec Kit Takes Off as Antidote to Piecemeal Vibe Coding (Visual Studio Magazine)](https://visualstudiomagazine.com/articles/2026/05/12/github-spec-kit-takes-off-as-antidote-to-piecemeal-vibe-coding.aspx)

### The RPI keynote and its evolution
- [Everything We Got Wrong About Research-Plan-Implement, Dexter Horthy (YouTube)](https://www.youtube.com/watch?v=YwZR6tc7qYg)
- [From RPI to QRSPI (Alex Lavaee)](https://alexlavaee.me/blog/from-rpi-to-qrspi/)
- [HumanLayer: RPI to CRISPY (ZenML LLMOps Database)](https://www.zenml.io/llmops-database/evolving-ai-coding-agent-workflows-from-research-plan-implement-to-crispy)
- [HumanLayer: Advanced Context Engineering for Coding Agents (ace-fca.md)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
- [HumanLayer (YC company page)](https://www.ycombinator.com/companies/humanlayer)
- [The Humans in the Loop: Making Agents Mainstream with Dexter Horthy](https://thehumansintheloop.substack.com/p/making-agents-mainstream-for-dev-with-dexter-horthy)
- [12-Factor Agents talk (MLOps Community)](https://home.mlops.community/public/videos/12-factor-agents-patterns-of-reliable-llm-applications-dexter-horthy-agents-in-production-2025-2025-08-06)

### Harness and context engineering definitions
- [Harness engineering for coding agent users, Birgitta Böckeler (martinfowler.com, 2026-04-02)](https://martinfowler.com/articles/harness-engineering.html)
- [Harness Engineering, first thoughts (memo), Böckeler (martinfowler.com, 2026-02-17)](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html)
- [I still care about the code, Böckeler (martinfowler.com)](https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html)
- [How far can we push AI autonomy in code generation?, Böckeler (martinfowler.com)](https://martinfowler.com/articles/pushing-ai-autonomy.html)
- [My AI Adoption Journey, Mitchell Hashimoto (2026-02-05)](https://mitchellh.com/writing/my-ai-adoption-journey)
- [Harness Engineering: Making AI Coding Agents Work in 2026, Faros AI](https://www.faros.ai/blog/harness-engineering)
- [Harness engineering: leveraging Codex in an agent-first world (OpenAI, 2026-02-11)](https://openai.com/index/harness-engineering/)
- [OpenAI Introduces Harness Engineering (InfoQ)](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/)
- [The rise of context engineering, Harrison Chase (LangChain, 2025-06-23)](https://www.langchain.com/blog/the-rise-of-context-engineering)

### Practitioner voices
- [Not all AI-assisted programming is vibe coding, Simon Willison](https://simonw.substack.com/p/not-all-ai-assisted-programming-is)
- [Agentic Engineering Patterns, Simon Willison](https://simonw.substack.com/p/agentic-engineering-patterns)
- [The 70% problem: Hard truths about AI-assisted coding, Addy Osmani](https://addyo.substack.com/p/the-70-problem-hard-truths-about)
- [AI's 70% Problem (Zed blog mirror of Osmani)](https://zed.dev/blog/ai-70-problem-addy-osmani)
- [Augmented Coding: Beyond the Vibes, Kent Beck](https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes)
- [When AI writes almost all code, what happens to software engineering?, Gergely Orosz](https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what)
- [How AI-assisted coding will change software engineering, Gergely Orosz](https://newsletter.pragmaticengineer.com/p/how-ai-will-change-software-engineering)
- [From IDEs to AI Agents with Steve Yegge, Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/from-ides-to-ai-agents-with-steve)
- [2026: The Year the IDE Died (Hacker News discussion)](https://news.ycombinator.com/item?id=46218922)
- [Complacency with AI-generated code, Thoughtworks Technology Radar Vol. 33](https://www.thoughtworks.com/en-us/radar/techniques/complacency-with-ai-generated-code)
- [2026: Staff Engineers Need to Get Hands-On Again, Paula Muldoon](https://paulamuldoon.com/2026/03/10/2026-staff-engineers-need-to-get-hands-on-again/)
- [The best engineers in 2026 aren't the best coders (Hitechies)](https://www.hitechies.com/ai-coding-agents-developer-skills-code-review-2026/)
- [Building shared coding guidelines for AI (and people too), Stack Overflow Blog](https://stackoverflow.blog/2026/03/26/coding-guidelines-for-ai-agents-and-people-too/)

### Lab and vendor framing
- [Best practices for Claude Code (Anthropic docs)](https://code.claude.com/docs/en/best-practices)
- [How we built Claude Code auto mode (Anthropic Engineering, 2026-03-25)](https://www.anthropic.com/engineering/claude-code-auto-mode)
- [Guardrails and human review (OpenAI Agents SDK docs)](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)
- [Run long horizon tasks with Codex (OpenAI Developers blog, 2026-02-23)](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- [GitHub Copilot: Meet the new coding agent (GitHub Blog, 2025-05-19)](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/)
- [Agent pull requests are everywhere. Here's how to review them. (GitHub Blog, 2026-05-07)](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)
- [Agent Security (Cursor docs)](https://cursor.com/docs/agent/security)
- [Devin's 2025 Performance Review (Cognition blog, 2025-11-14)](https://cognition.ai/blog/devin-annual-performance-review-2025)

### Empirical data
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (METR, 2025-07-10)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [2025 DORA Report (Google announcement)](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/)
- [Announcing the 2025 DORA Report (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- [DORA State of AI-assisted Software Development 2025 (report hub)](https://dora.dev/dora-report-2025/)
- [2025 Stack Overflow Developer Survey, AI section](https://survey.stackoverflow.co/2025/ai/)
- [Debt Behind the AI Boom (arXiv:2603.28592)](https://arxiv.org/abs/2603.28592)
- [Agent Skills in the Wild (arXiv:2601.10338)](https://arxiv.org/abs/2601.10338)
- [Will It Survive? Deciphering the Fate of AI-Generated Code (arXiv:2601.16809), counter-evidence](https://arxiv.org/html/2601.16809v1)
- [Deloitte, The State of AI in the Enterprise 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)
- [AI Coding Benchmarks 2026 (larridin.com, secondary, code-churn figures)](https://larridin.com/developer-productivity-hub/ai-coding-benchmarks-2026)
- [Assess AI Code Quality 2025 (exceeds.ai, secondary, code-churn figures)](https://blog.exceeds.ai/assess-ai-code-quality-2025/)

### Secondary labor-market (directional only)
- [Junior Developer Jobs Vanished in 2026 (Engineering Playbook, Medium)](https://medium.com/engineering-playbook/junior-developer-jobs-vanished-in-2026-the-bootcamp-to-job-pipeline-is-dead-heres-the-new-path-395c18fa0c96)
- [Why Companies Are Quietly Rehiring Software Engineers in the Age of AI (Frank's World)](https://www.franksworld.com/2026/04/15/why-companies-are-quietly-rehiring-software-engineers-in-the-age-of-ai/)
