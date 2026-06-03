---
title: "How Take AI Bite learned to bootstrap itself"
date: 2026-06-03
description: "Take AI Bite v1.5 and v1.6 added a hard gate for the default branch, a principle for reading the manual before assuming, and a self-bootstrapping protocol for fresh clones. A release post about the framework naming the assumptions it just paid for."
categories: ["Methodology"]
tags: ["take-ai-bite", "claude-code", "release-notes"]
draft: false
---

It is curious how AI, in this case Claude Code, will embark on a quest with topics not entirely explored. That would write the fate for an explorer in counted minutes. However, we humans sometimes think that AIs suggest acting on something based on their own training, as if training is equivalent to knowledge. Try entering the Amazon jungle without knowledge and see if you walk out at all.

I have a few examples that took me to realize an important pattern that was fixed with a new principle to the framework: Read the User's Manual (DSM_6.0 §1.11).

My favorite example and the one that surprised me the most is Claude Code actively suggesting to create Skills and Hooks without entirely knowing how these are defined by Anthropic. It's like saying "hey! I'm a surgeon, let's operate because I know I can fix this... but... I don't know how to deal with an artery." The agent treats Skills and Hooks as concepts it knows from training, then proposes shapes that do not match the actual Anthropic spec, then ships them with confidence. The mess shows up later, in the form of a hook that does not fire, a skill that does not register, or a frontmatter field that gets silently ignored.

There is a smaller version of the same story in tooling. The agent ran `gh pr create` against a repo whose default branch had been silently pointed at a session branch that no longer existed. The API returned 404, again and again. Forty-five minutes went into investigating what looked like a GitHub outage and turned out to be a single `gh repo view` call we had not thought to make. The default branch was main. The agent assumed it was. Nobody had checked.

And a third version, with the platform itself. The agent treated Claude Code like generic Claude: same prompt shape, same tool-use conventions, same defaults. Claude Code has its own harness, its own file-tracking, its own slash-command flow. Treating them as the same kept producing edits that landed in the wrong place and skill calls that did not behave as expected.

Three rooms, one question: what is actually here, before I act on what I think is here.

## The gate

The default-branch story has a corrective that shipped in Take AI Bite v1.6. At session start, the agent calls `gh repo view --json defaultBranchRef --jq .defaultBranchRef.name` and compares the result against the local main line read from `.claude/CLAUDE.md`. If they disagree, the session halts with a critical warning that names both values and the fix command (`gh repo edit --default-branch {local}`). No session work proceeds until the user fixes the configuration or types `defer` to bypass for this session only. The check runs once per session, one `gh` call. The whole gate is a few dozen lines of skill spec (BL-386). The forty-five minutes do not happen again.

The principle has more reach than the gate. The gate fixes one symptom on one surface. The principle names the failure mode wherever it shows up: a skill whose description does not match its behavior, a platform whose conventions do not match the generic case, an external library whose API has changed since the example you remember.

## Same pattern, more surfaces

Four other features in v1.5 and v1.6 follow the same pattern, each on a different surface.

**Cloned-Mirror Kick-off Protocol.** A fresh clone of a public mirror now bootstraps itself into a working session on the first `/dsm-go`. The Kick-off Protocol (Take AI Bite v1.5) detects fresh-clone state, auto-derives runtime values from the repo, copies the five `.claude/*.template` files into runtime paths, self-registers the clone in the ecosystem registry, deploys the project commands, and sets the kickoff-done marker. All of it happens at session start without prompting. A reader who clones the public mirror to look around can run `/dsm-go` and be in a working session, with alignment block populated and skills installed, in one step.

**DSM_7.0 AI Platform Collaboration Guide.** DSM_7.0 is the file the project now reads to know what each AI platform actually does. §2.1 holds the filled instance for Claude Code, the harness this site is built on: file-tracking conventions, slash-command flow, hook surfaces, the bits that are not portable from a generic Claude API call. §3 is the template for the next platform someone fills in. The Read-the-Manual principle has somewhere to point: an agent that needs to know what the platform supports reads one file and knows. The manual exists so it can be read.

**Gate 1 token-minimizing config recommendation (DSM_0.2 §8.7).** Gate 1 of the four-gate Pre-Generation Brief now names the right configuration for the artifact being proposed. A quick edit gets "Sonnet, low effort, thinking off." A multi-file refactor gets "Opus, high effort, thinking on." The recommendation draws from the user's `claude-subscription.md` and is not enforcement, the user can override. The work scope and the configuration conversation happen at the same moment, when both are clearest.

**Project type detection broadened.** Take AI Bite's project-type detector now recognizes Node (`package.json`), Rust (`Cargo.toml`), Go (`go.mod`), and shell-script (executable `.sh` in `src/`) signals as Application markers, alongside the existing Python ones. Any application clone, in any of those languages, gets the right CLAUDE.md scaffold and the right session-start checks from the first `/dsm-go`. The type label drives a lot of downstream behavior, which session-start protocols run, which sprint cadence applies, which deliverables get checklists. Application-type recognition catches up to the polyglot reality of what people actually build.

Four files, four surfaces, the framework learning the same lesson in four places.

## How Take AI Bite grows

What v1.5 and v1.6 reveal about Take AI Bite is the shape of how it actually grows: it names the assumption it just paid for, and turns the name into a thing the project can rely on next time.

The 45-minute 404 became a hard gate at session start. The implicit "the agent will figure out what this platform does" became a principle with a section number (DSM_6.0 §1.11) and a file the agent reads (DSM_7.0). The undocumented manual-setup ritual on fresh mirror clones became a Kick-off Protocol that runs without prompting. In each case, a thing that used to depend on the agent or me happening to do the right thing now depends on a check the project carries on its own.

This is the through-line I am most interested in publishing here. Take AI Bite grows by collecting the receipts of its own work. Each release adds an artifact that did not exist before, drawn from a moment when the artifact's absence cost something concrete. The framework is not just a list of clever ideas. It is a list of corrections that earned their place by being needed.

For a reader using AI agents in their own work: the question to keep asking is what your collaboration is currently depending on you to remember. Whatever you find, that is the next thing to name.
