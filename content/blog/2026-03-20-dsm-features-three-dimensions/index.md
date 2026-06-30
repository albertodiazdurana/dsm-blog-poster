---
title: "142 features across three dimensions"
date: 2026-03-20
draft: false
description: "DSM's 142 features mapped across human oversight, knowledge provenance, and experience accumulation."
tags: ["Deliberate Systematic Methodology", "DSM", "AI Collaboration", "Features", "Take AI Bite"]
categories: ["Features"]
author: "Alberto Diaz Durana"
toc: true
---

Most AI coding tools are built to reduce human involvement. DSM is built to make human involvement worth the time: the human and the AI produce better work together than either would alone, and what they learn carries forward.

This post maps DSM's 142 features across three dimensions: human oversight, knowledge provenance, and experience accumulation. For the full chronological list, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md).

---

## Human oversight

Where most tools give you a slider between "approve everything" and "let the AI run," DSM builds oversight into the structure of every interaction.

### Per-turn artifact review

Every artifact passes through a three-gate approval model: concept (do you understand what will be created?), implementation (does the diff look right?), and run (should this execute?). The AI cannot proceed without the human engaging with the work. Before the three gates, there is a fourth conversation: Gate 0, where the human and the agent define the work together before any plan is drafted. Presenting a pre-formed plan for approval reduces the human from collaborator to approver; Gate 0 keeps the definition itself shared.

The same review discipline applies when the work decomposes into pieces. Multiple edits to a single file need separate explanations. In Jupyter Notebooks cells are generated one at a time, with output verified before the next cell is created. Cells that produce plots save the figure to disk so the agent can read it back and check what it actually drew before moving on.

Enforcement is structural. A per-turn hook appends reasoning to a live transcript as the first tool call of every turn, so the record of thinking cannot be skipped by an eager agent. When a protocol violation is detected mid-output, the output itself is a stop condition: the agent halts, names the violation, and waits for confirmation before resuming. Before a Gate 2 approval, the agent is required to surface the strongest counter-evidence to its own recommendation, shifting the burden of critical evaluation from user vigilance to protocol.

The gate model itself has grown two refinements. When a task contains sub-tasks that fit a subagent's profile, bounded, parallelizable, reasoning-light, Gate 1 surfaces the offload candidates and requires explicit per-task user approval before any subagent spins. Heroism, absorbing every sub-task on the main thread, is not the default. And for prose deliverables (plans, proposals, reports, blog posts), Gate 3 drafts one section at a time with per-section approval before the next, instead of producing the whole document in a single Write. A factual error in a single section now surfaces before the next section is even drafted, instead of after the full document is in front of the reviewer.

### Session lifecycle

Sessions are not "start working, stop working." Each session starts by checking inbox messages, validating project state, comparing versions, and loading context. Each session ends by saving memory, committing work, and creating continuity documents. If a session ends unexpectedly, the next session detects the gap and offers recovery.

Lightweight sessions handle quick follow-ups. Session baselines track what changed. Configuration recommendations match settings to the planned work scope. A wrap-up type marker lets the next session-start command know whether the previous session ended light or full, so the two ends of the lifecycle stay aligned. Before suggesting wrap-up, the agent now re-reads the sprint plan and checks completed deliverables against actual evidence, so "sprint complete" cannot be declared while gates are still open. Session start also surfaces the CI status of any open pull request on the branch, so work never resumes on top of a check that has been red for days, and the reminder to mine the previous session's transcript no longer fires when that session has already been analyzed.

### Safety guardrails

Destructive commands (force push, hard reset, recursive delete) require explicit human request. Sensitive files (.env, credentials) are blocked from commits. Feature branches must be tested before merging. The first write to any path outside the current repository in a session requires explicit user confirmation, so an agent working in a spoke project cannot quietly write into the Hub or any other project.

The guardrails extend to publication. Merging a pull request against `main` is treated as equivalent in outcome to pushing to `main`, and both require specific confirmation. At session start, the agent resolves the remote default branch and hard-halts if it differs from the local main line, so a stale session branch left as the repo default cannot quietly redirect a merge. Small checks, but the kind of thing that eats 45 minutes when it goes wrong.

Two recent additions tighten the guardrails further. Certain safety prompts are now marked non-suppressible: even when the user has put the agent in auto mode (skipping non-critical pauses), the marked prompts must display and receive an explicit response. The pattern emerged after an incident where auto mode silently bypassed a continuation prompt that the agent had recognized in its own thinking block, then pressed past anyway. And every session now writes a lockfile at start; if a second session opens against the same project while one is still active, it hard-halts and asks the user to resolve the conflict, rather than silently interleaving two agents' work on the same branch.

The guardrails then grew outward, beyond what an agent may do, to cover whose words go out and what outside text is allowed to steer. A session writing into another repository may now only create or append files, never run git there, so a foreign session cannot author commits on a project it does not own. Content posted under the human's byline, a pull-request comment, a commit message, gets its own approval gate, because approving the send is not the same as approving the words: the full text surfaces for review before it goes out. And cooperative external content, a polite suggestion on a public thread, is treated as observation by default; acting on the agenda it proposes takes explicit authorization, since politeness is not authorization and being on-topic is not an invitation. Smaller hardenings sit underneath, like dated filenames so an archived message cannot silently overwrite its predecessor, or a guard that stops a careless bulk edit from exploding the live transcript.

These are structural constraints, not opt-in features. They cannot be bypassed without the human explicitly choosing to do so.

---

## Knowledge provenance

Most AI tools start with a blank slate: a generic model, maybe a config file. DSM starts with a versioned, human-authored knowledge base that the AI inherits and contributes to.

### Methodology documents

DSM is a suite of versioned documents: data science workflows (1.0), project management (2.0), cross-project governance (3.0), software engineering (4.0), documentation standards (5.0), collaboration principles (6.0), and most recently the AI platform collaboration guide (7.0) which centralizes platform-specific knowledge so the rest of the suite can stay platform-agnostic. Each is maintained with semantic versioning and a formal update workflow.

Project-specific instructions reference the methodology via a configuration chain, so every project inherits the full protocol suite but can override specific rules. A per-artifact configuration recommendation runs inside Gate 1, so mechanical edits and architectural decisions do not both execute at the same session baseline. Picking the right tool configuration for the work is itself part of the record.

The research folder reached parity with the plans folder on this front. Plans had skills for adding and closing items that kept an active index in the README current; research was a passive convention document for months, and it drifted out of sync with what was actually in the folder. Two new skills now create research files with header stubs and validation, insert them into a five-category active index, and move them to done on closure with the index updated. Drift between folder and README is now treated as a protocol violation signal, not a housekeeping nuisance.

### Protocol inheritance

The hub-spoke architecture means protocols are authored once in the central repository and inherited by all projects. When a protocol improves, every project picks it up. Project type detection activates the right methodology track. Participation patterns adjust rules based on whether a project is a standard spoke, an external contribution, or a private repo.

A path registry maps cross-repository relationships. Mirror repos receive methodology updates automatically. A fresh clone of a public mirror now bootstraps itself into a working session on first run: the clone detects that it is unconfigured, scaffolds the folder structure, copies the template files, self-registers as its own local hub, deploys the slash commands, and writes a marker so subsequent sessions skip the setup. Zero user prompts, zero manual scaffolding.

Inheritance has a sharp edge: when a project inherits a skill, the skill's output is authoritative. If the skill skips a check because it does not apply in this context, that silence is the answer, not an invitation for the agent to run the check by hand and fold the result into the skill's report. The principle is "silence from the skill on a concern is the skill's answer," and the lesson came from an incident where an agent correctly skipped a check on a spoke project, then ran the check anyway as a side action, then reported fabricated drift counts in the skill's output. The fix names the principle and gives the agent three honest options when a check feels missing: audit out-of-band under its own label, file a backlog item to extend the skill's scope, or skip. The specific report wording that triggered the incident was also pinned down so the field always emits a clear "not applicable" sentinel instead of a blank line that invites invention.

### Versioned knowledge

Every change to the methodology is tracked in a changelog, tagged with semantic versions, and checkpointed. Design decisions are numbered and documented with rationale and alternatives. Research findings are preserved with sources and dates.

The point is preventing knowledge loss. When a protocol decision was made six months ago, the rationale is recoverable. When research informed a design choice, the original evidence is still there. The same standard applies in the moment: before answering a question about a file, a definition, or a piece of documentation, the agent reads the source. No partial knowledge passing as understanding.

A recent principle extends this outward, to the tools themselves. "Read the User's Manual" treats external-tool understanding as a prerequisite to collaboration design, not an optional afterthought. Before building a pattern on a platform feature, the agent reads the platform's own documentation and verifies the understanding against it, not against memory or experiential knowledge. The motivating incident was a per-turn enforcement hook that sat broken for two and a half months because an assumption about git's index mode never got checked. Methodology knowledge is versioned; tool knowledge has to be grounded the same way. The same discipline now reaches outbound work: before drafting a pull request for an external project, the agent reads that project's own contribution guide, its PR template, its CI gates, and a couple of recently merged requests, then drafts against those conventions instead of an internal default.

A closure cycle in v1.8.0 surfaced a class of problem with this kind of provenance: dead pointers. The methodology had grown hundreds of references to backlog filing codes (BL-NNN) that only resolved inside the central repository's plans folder. A mirrored spoke reading a methodology document hit a wall when the filing code was the only identifier on offer. The fix was a three-part cleanup: roughly 170 anchors removed from mirrored documents and replaced with resolvable identifiers (section references, protocol names, file references); a new BL lookup index that maps every implemented BL number to its title, version, and resolving concept, so the codes that remain can still be resolved in one hop; and a forward-only rule that checkpoint entries must use resolvable identifiers from the moment they are written, not BL numbers an unrelated spoke agent cannot follow. Knowledge that cannot be followed is not knowledge.

Two everyday practices got the same treatment, named and given a home rather than left to habit. The small, fast check run after each file is built is now a first-class artifact with a fixed place and structure, framed as the industry-standard smoke test given a repo home, not a DSM coinage. And a writing discipline, introduce each concept once and let the body deepen it instead of restating it between summary and detail, became a named principle the drafting protocol checks for.

---

## Experience accumulation

This is where the distance to other tools is largest. Most tools treat each session as independent. Some persist project-level memory. DSM propagates experience from individual sessions outward to improve the methodology for all future work.

### Memory and context

MEMORY.md provides persistent, typed memory across conversations: user preferences, project decisions, feedback patterns, reference pointers. The session transcript captures reasoning in real time, a record of why decisions were made, not just what was done. Context budget management treats the AI's context window as a finite resource.

Handoffs ensure pending work survives session boundaries. Checkpoints snapshot project state. When a session ends unexpectedly, transcript-based recovery reconstructs the missing wrap-up. When the normal boot chain itself is broken, a minimal read-only entry point starts a session with no side effects, just enough context to diagnose what went wrong without making it worse.

The split between memory and checkpoint became sharper recently. The session-start command was burning 30 to 40 percent of context on a single methodology check that did not actually need to run on every session, plus a defensive inbox read that pulled file bodies into context before the user had even asked. Three changes cut the cost: the methodology alignment check now only runs when the methodology version actually changed, hook permissions are repaired unconditionally with a single command instead of relying on the alignment check, and the inbox reports filenames only at session start, with content reads deferred until the user asks for them. Sonnet sessions became economically sustainable; Opus sessions freed context for the actual work. On the other end, the wrap-up command now produces a checkpoint file alongside the memory update, so "pending next session" items move out of memory (which holds global context and strategic vision) and into the checkpoint (which the next session consumes and moves to done).

### Feedback loops

Spoke projects generate backlog proposals and methodology observations for the central repository. At session end, feedback is pushed to the central inbox. The inbox system routes notifications between projects with a processed/done lifecycle.

One spoke project generated 42 backlog proposals and 53 methodology observations. That is not a theoretical capability; those are real numbers from a real project, producing concrete improvements to the shared methodology.

### Reasoning extraction

Session transcripts get mined for reasoning patterns that become formal guidance for future sessions. The experiment framework ensures capability tests are reproducible and feed back into the methodology. Stress testing compares guided vs. unguided collaboration to measure the actual impact of structured protocols.

External observations generate backlog items automatically. The "Earn Your Assertions" principle means claims are verified before acting. "Critical Thinking" requires the AI to challenge its own outputs. These run as active protocols in every session.

Sprint boundaries are not just packing-up moments. At each boundary, the agent runs a structured retrospective across six dimensions: themes, principles, evolution, collaboration, learning, and maturity. Mechanical compliance is necessary; the analysis is what makes the boundary useful for the next sprint.

The reasoning lessons file itself grew past what could fit in a session-start context budget. The fix kept the live file as the source of truth and added a derived compact mirror, regenerated at every wrap-up. The mirror drops the file's leading guideline lines and the per-entry provenance prefix, and preserves every lesson body verbatim. Session start reads the mirror in full, which restores the original intent of priming the agent with the actual accumulated lessons instead of a peek at the first ten lines. The transcript-analysis skill regenerates the mirror on its own runs too, so the staleness window between a deep analysis pass and the next wrap-up does not leave fresh lessons invisible at the next session start. The empirical savings from a trim-only transform were smaller than projected (about 5 percent on a 113-entry file, against a 25-to-30-percent target). Real compression behind a controlled experiment is queued; productive sessions are explicitly forbidden as A/B subjects.

The loop keeps closing on itself. One recurring move, the user reshaping a proposal instead of answering it, showed up six times across four months in the reasoning lessons before it was promoted into a named rule: when the user reframes, the agent re-decomposes rather than defending its first framing. The way structured prose gets drafted changed from the same kind of evidence, one section at a time, written to a file the user edits in place instead of pasted into chat, a pattern borrowed from notebook collaboration and validated on a four-part blog series. The behavior was observed enough times to earn a protocol; the protocol now shapes the next session.

---

## The compound effect

No single feature here is new. Pre-generation briefs, memory systems, feedback loops, they exist in various forms elsewhere. What is different is that 142 features work together as a system, and the system learns. The count keeps moving because the methodology is in active use; the shape of what it covers, though, has stayed recognizable across every version.

A feedback observation from a spoke project becomes a backlog item in the central repository. That item becomes a protocol change. That change propagates to every project. The next session in any project benefits from an insight that started in a completely different context.

The methodology improves through use.

---

*For the full chronological feature timeline, see [FEATURES.md](https://github.com/albertodiazdurana/take-ai-bite/blob/main/FEATURES.md). For the competitive positioning analysis behind these three dimensions, see the [3D positioning map](https://github.com/albertodiazdurana/take-ai-bite/blob/main/dsm-docs/research/DSM-Rebranding/2026-03-18_competitive-positioning-map.md).*
