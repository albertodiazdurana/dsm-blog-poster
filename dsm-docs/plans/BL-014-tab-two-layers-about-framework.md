# BL-014: TAB Two Layers, About Page and Framework Post

**Priority:** High
**Source:** Session 16 (2026-04-07), user observation while reviewing live site
**Trigger:** Now (S16)

## Description

`content/about.md` (live at https://take-ai-bite.com/about/) and the framework post `content/blog/2026-03-12-take-ai-bite-framework/index.md` (live at https://take-ai-bite.com/blog/2026-03-12-take-ai-bite-framework/) both present Take AI Bite as "the nine principles only". That maps to DSM_6.0 (AI Collaboration Principles) only.

TAB is now documented across two complementary layers in DSM Central:

- **DSM_6.0, AI Collaboration Principles** (the philosophy, the "why"). Nine principles, currently at v1.6.
- **DSM_6.1, Systems Prompt Engineering** (the discipline, the "what/how"), with three modules:
  - 6.1.A Operational Channels and Context Management
  - 6.1.B Instruction Design Patterns
  - 6.1.C Evaluation and Evolution

The framework post's "engine" section already describes 6.1-style content (hub-spoke routing, memory layers, feedback loops) without attributing it to 6.1, which makes the gap silent rather than visible. The about page does not mention either layer by name.

## Success criteria

1. `content/about.md` includes a short paragraph naming the two layers (principles + Systems Prompt Engineering) without bloating the landing page.
2. Framework post adds a clear two-layer framing: principles (DSM_6.0) and the SPE discipline (DSM_6.1 + modules A/B/C). The existing concrete examples (hub-spoke, memory, feedback loop) get attributed to the right layer.
3. Voice calibration done from `content/about-me.md` + `content/about.md` before drafting.
4. `/humanizer` run on both edits before publishing.
5. No emojis. Punctuation rule: "," not "—".
6. Commit and push via standard PR flow.

## Out of scope

- Features post staleness (90 → 95). Tracked separately in BL-015.
- A dedicated SPE post (already tracked in BL-010).

## Notes

Concept-gate brief was already presented and approved in S16 before this BL was created.
