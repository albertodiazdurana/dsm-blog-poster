@../../dsm-agentic-ai-data-science-methodology/DSM_0.2_Custom_Instructions_v1.1.md

<!-- BEGIN DSM_0.2 ALIGNMENT - do not edit manually, managed by /dsm-align -->
## 1. DSM_0.2 Alignment (managed by /dsm-align)

**Project type:** Application (DSM 4.0)
**Participation pattern:** Spoke

### Session Transcript Protocol (reinforces inherited protocol)
- Append thinking to `.claude/session-transcript.md` BEFORE acting
- Output summary AFTER completing work
- Conversation text = results only
- Use Session Transcript Delimiter Format for every block:
  <------------Start Thinking / HH:MM------------>
  <------------Start Output / HH:MM------------>
  <------------Start User / HH:MM------------>
- HH:MM is 24-hour local time when the block begins; no end delimiter needed
- Append technique: read last 3 lines, use last non-empty line as anchor.
  NEVER match earlier content for mid-file insertion.
- Per-turn enforcement: a `UserPromptSubmit` hook in `.claude/settings.json`
  injects a reminder every turn. The hook enforces *occurrence*; the
  existing `validate-transcript-edit.sh` PreToolUse hook enforces *shape*.
  IDE monitoring and session-start behavioral activation are user
  affordances, not enforcement. The hook is the mechanism.
- Turn-boundary self-check: every turn begins with a transcript append. If
  your first tool call this turn was not a transcript append, the protocol
  was violated. This includes pure-reasoning turns (decision analysis,
  recommendation, trade-off comparison) that would otherwise touch no files,
  the transcript append is the one required tool call. The only exemption
  is content-trivial turns (one-word acknowledgments, single-fact
  confirmations with no new reasoning). Recover by appending a
  `[RETROACTIVE]` entry with the current HH:MM (never backdate) and a note
  explaining the gap; do not edit history.
- Process narration: thinking blocks narrate reasoning as it unfolds,
  including considered-and-rejected paths, doubts, loops, and reversals.
  Clean post-hoc summaries hide inefficiency signals that are the primary
  input to reasoning-efficiency analysis. Brevity is not the goal,
  auditability is.
- Unconditional activation: if `.claude/session-transcript.md` exists in
  the project, the protocol is active. No skill needs to activate it. The
  presence of the file is the activation signal. This rule is independent
  of `/dsm-go` Step 6 and applies to continuation sessions that defer
  from `/dsm-light-go` to `/dsm-go` mid-flight.
- Heredoc anti-pattern: when appending to the transcript via Bash, never
  use single-quoted heredoc (`<< 'EOF'`) if the content contains shell
  expansions like `$(date +%H:%M)`. Capture the timestamp into a variable
  first and use unquoted heredoc, or prefer the Edit-tool append path
  (read last 3 lines, anchor on last non-empty line).

### Pre-Generation Brief Protocol (reinforces inherited protocol)
- Four-gate model: collaborative definition (confirm threads → dependencies → packaging) → concept (explain) → implementation (diff review) → run (when applicable)
- Each gate requires explicit user approval; gates are independent
- What/why/how thinking block: before Gate 1, answer what the artifact is, why it is needed, and how it will be built, in the session transcript thinking block
- Skill self-reference: before claiming any behavior of a DSM skill (`/dsm-go`, `/dsm-wrap-up`, `/dsm-align`, etc.), read `scripts/commands/{skill-name}.md` or `~/.claude/commands/{skill-name}.md`. Do not answer "does skill X do Y?" from memory.
- Chunked drafting for prose deliverables (per DSM_0.2 §8.10): for project plans, proposals, reports, research papers, blog posts, and similar structured prose, the four gates take a specific shape: Gate 1 confirms purpose / audience / outcome / length / scope; Gate 2 proposes a TOC with per-section length budgets; Gate 3 drafts ONE section at a time with per-section user review and approval before the next; Gate 4 reviews the full assembled document for consistency. Full-file Write at Gate 3 is reserved for final assembly after all sections are individually approved. Triggered by document type, not length.

### Inbox Lifecycle (reinforces inherited protocol)
- After processing an inbox entry, move it to `_inbox/done/`
- Do not mark entries as "Status: Processed" while keeping them in place

### Actionable Work Items (reinforces DSM_3 planning pipeline)
- Only items in `dsm-docs/plans/` (and legacy `plan/backlog/`) are actionable work items.
- Material found elsewhere (`_reference/`, `docs/`, README, inbox, sprint plan drafts) is INPUT to the planning pipeline, not a substitute for it.
- Before suggesting implementation of anything that looks like a plan, verify that a formal BL exists in `dsm-docs/plans/`. If not, route through research → formalize → plan first.

### Punctuation
Use comma "," instead of Em Dash "—" for connecting phrases in any language.
Never use space coma space (" , "). The correct format is no spaces before the comma, and one space after: ", ".

### Code Output Standards (reinforces Earn Your Assertions)
- Show actual values: shapes, metrics, counts, paths
- No generic confirmations: avoid "Done!", "Success!", "Data loaded successfully!"
- When uncertain, state the uncertainty; do not guess or fabricate
- Read the relevant source (file, definition, documentation) before answering questions about it; do not answer from partial knowledge
- Let results speak for themselves

### Tool Output Restraint (reinforces Take a Bite)
- Generate only what you can meaningfully process in the next step
- Comprehensive tool reports are reference material, not the analysis itself
- Run tools because the output serves the task, not because the tool is available

### Working Style (reinforces Take a Bite, Critical Thinking)
- Confirm understanding before proceeding
- Be concise in answers
- Do not generate files before providing description and receiving approval

### Cross-Repo Write Safety (reinforces Destructive Action Protocol)
- First write to any path outside this repository in a session requires explicit user confirmation
- Present the content and target path before writing; do not write cross-repo silently
- Subsequent writes to the same cross-repo target in the same session do not need re-confirmation

### Plan Mode for Significant Changes (reinforces Earn Your Assertions)
- Before implementing significant features: explore codebase, identify patterns, present plan
- Do not write or edit files until the plan is approved by the user
- This is a read-only exploration phase, not an implementation phase

### Session Wrap-Up (reinforces Know Your Context)
- When the user says "wrap up" or the session ends, use `/dsm-wrap-up`
- Before wrap-up, cross-reference sprint plan if one exists (verify all deliverables accounted for)
- At minimum: commit pending changes, push to remote, update MEMORY.md
- Create a handoff document if complex work remains pending

### App Development Protocol (reinforces inherited protocol)
- Explain why before each action
- Create files via Write/Edit tools; user approves via permission window
- Wait for user confirmation before proceeding to next step
- Build incrementally: imports → constants → one function → test → next function
<!-- END DSM_0.2 ALIGNMENT -->

# Project: DSM Blog Poster
Domain: Software Engineering (Static Site + Automation) / Content Operations

## Framework Documents
This project uses:
- **DSM 4.0: Software Engineering Adaptation** (Project Knowledge): Adapted phases for SW projects
- **PM Guidelines** (Project Knowledge): Sprint planning structure
- **Collaboration Methodology v1.3.0** (Project Knowledge): Core philosophy, communication style
- **Content Operations Guide** (`dsm-docs/content-operations.md`): Role definition, legal/licensing checklist, distribution practices, asset management, lessons learned

## Project Planning Context

### Scope
- **Purpose**: Personal website with integrated blog, hosted on GitHub Pages. Publishes DSM methodology posts, project updates, and data science content. Includes LinkedIn cross-posting.
- **Resources**: 1 sprint, solo project
- **Success Criteria**:
  - Functional: Hugo site builds and deploys to GitHub Pages
  - Content: Existing blog posts migrated and first new post published
  - Distribution: LinkedIn post created (manual initially, automated later)
  - Documentation: README with setup and publishing workflow

### Data & Dependencies
- **Primary inputs**: Blog posts from DSM Central (`dsm-docs/blog/`) and spoke projects
- **Dependencies**: Hugo v0.142.0 extended, GitHub Pages, GitHub Actions for deployment

### Stakeholders & Governance
- **Primary**: Alberto (site owner) - professional portfolio and blog
- **Secondary**: DSM community - methodology insights and project updates

## Execution Context (DSM 4.0 Adapted Phases)

### Timeline & Phases
- **Phase 1 - Setup**: Hugo site configuration, theme selection, GitHub Pages deployment
- **Phase 2 - Content**: Migrate existing posts (7 posts), create portfolio page
- **Phase 3 - Automation**: GitHub Actions deploy pipeline, LinkedIn posting script (future)
- **Phase 4 - Polish**: Custom domain, SEO, RSS feed

### Deliverables
- [ ] Hugo site building locally
- [ ] GitHub Pages deployment working
- [ ] Existing blog posts migrated (7 posts)
- [ ] README with publishing workflow
- [ ] LinkedIn cross-posting (manual first sprint)

## Domain Adaptations

### Key Techniques
- Hugo static site generation (Go templates, markdown content)
- GitHub Actions for CI/CD
- GitHub Pages hosting
- LinkedIn cross-posting and content distribution
- AI-generated asset licensing and management (see `dsm-docs/content-operations.md`)

### Known Challenges
- GitHub Pages custom domain requires DNS configuration
- LinkedIn API requires app approval (may need manual posting initially)

## Advanced Practices
- [ ] Testing Strategy (HTML validation, link checking)

## Communication & Style

### Standards
- No emojis in documentation
- Use WARNING/OK/ERROR text conventions
- Blog posts follow DSM Section 2.5.6 workflow
- File naming follows DSM_0.1 convention
- In public-facing content (blog, About pages, LinkedIn, any reader-facing prose), refer to the DSM Central repository as "the Hub". "DSM Central" is the internal governance name; the public repo is Take-AI-Bite, and "Hub" avoids confusion between the two. This rule applies to all reader-facing material; internal docs and code can keep using "DSM Central".

### TAB and DSM in reader-facing prose

Take AI Bite (TAB) is the framework and the reader-facing brand. The version belongs to TAB. The files that implement TAB happen to be named `DSM_X.Y`, that is where the DSM name shows up. "DSM is part of TAB" is the reader-facing posture, not "DSM is a separate versioned layer beneath TAB", that earlier framing was internal architecture leaking into reader-facing prose.

- **Take AI Bite (TAB)** owns the version. "Take AI Bite v1.6", "TAB v1.6", or just "v1.6" when context makes it clear.
- **DSM as a standalone noun does not appear in reader-facing prose.** It only survives as file references where the file is literally named that way: `DSM_6.0`, `DSM_7.0`, `DSM_0.2 §8.10`.
- **Principles:** "Take AI Bite's Read-the-Manual principle (DSM_6.0 §1.11)". The principle belongs to TAB, the parenthetical points to where the file lives.
- **Release-post titles:** TAB-led. "How Take AI Bite learned to X."
- **Release-post Takeaways re-anchor to TAB** at least once.
- **LinkedIn hashtags:** `#TakeAIBite` (drop `#DSM` to match the convention). Topical tags as appropriate (`#AI`, `#HumanAICollaboration`, etc.).
- **About page's "two layers" paragraph** is acceptable as optional depth for readers who want internal architecture, it does not drive vocabulary elsewhere.

### Language & Formatting
- Primary language: English
- Number format: 1,234.56
- Date format: YYYY-MM-DD

## Backlog
- Backlog items live in `dsm-docs/plans/` as `BL-{NNN}-short-title.md`
- See `dsm-docs/plans/README.md` for the index of open and completed items
- When a BL item is implemented, move the file to `dsm-docs/plans/done/`

## Project-Specific Requirements
- Blog posts sourced from DSM Central and spoke project `dsm-docs/blog/` folders
- Hugo content in `content/blog/` follows date-prefixed naming
- Portfolio section highlights DSM ecosystem projects
- Minimal theme, fast loading, mobile responsive

## Voice and content quality
- At session start, read `content/about-me.md` and `content/about.md` to calibrate the author's voice before writing any content
- At session start, read the following DSM Central files to build accurate context about Take AI Bite (TAB, the public framework this blog publishes) and Deliberate Systematic Methodology (DSM, the versioned methodology that powers TAB) before writing or editing any reader-facing content. TAB is documented across DSM_6.0 (the nine AI Collaboration Principles, the "why") and DSM_6.1 + its modules A/B/C (Systems Prompt Engineering, the "what/how"). FEATURES.md is the canonical inventory of DSM features across all dimensions:
  - `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`
  - `~/dsm-agentic-ai-data-science-methodology/DSM_6.0_AI_Collaboration_Principles_v1.0.md`
  - `~/dsm-agentic-ai-data-science-methodology/DSM_6.1_Systems_Prompt_Engineering_v1.0.md`
  - `~/dsm-agentic-ai-data-science-methodology/DSM_6.1.A_Operational_Channels.md`
  - `~/dsm-agentic-ai-data-science-methodology/DSM_6.1.B_Instruction_Design_Patterns.md`
  - `~/dsm-agentic-ai-data-science-methodology/DSM_6.1.C_Evaluation_and_Evolution.md`
- Run `/humanizer` on all material produced and posted by this project: blog posts, page content, descriptions, any reader-facing prose
- This is a pre-publish gate, not optional

## DSM Version Release Coverage

A DSM version bump cascades into several artifacts in this project. The cascade is silent unless tracked. The pipeline below sequences the response across six stages; the BL template that materializes it is BL-022 (`dsm-docs/plans/done/BL-022-dsm-v1.5-v1.9-release-coverage.md` once closed).

Each stage has a trigger, an action, and a gate to the next stage. Gates are explicit: ship Stage 2 in the same session as Stage 1 when possible; Stage 3 may span sessions but blocks Stage 4.

### Stage 0 , Detect

**Trigger:** `/dsm-go` Step 1.8 reports a DSM version change (last-align version differs from CHANGELOG latest), and/or `_inbox/` contains a FEATURES.md notification pushed by DSM Central's `/dsm-wrap-up` Step 1 sub-step (e).

**Action:** read the inbox notification(s) in full. Skim CHANGELOG between the prior covered version and the new latest. Identify how many version jumps the project is behind.

**Gate to Stage 1:** the agent has named the version range to cover and surfaced any drift in feature count or principle count.

### Stage 1 , Open the BL

**Trigger:** Stage 0 complete.

**Action:** open a release-coverage BL using BL-022 as the template. Run the verification commands immediately and record deltas in the BL's Problem statement:

- Feature count: `grep -cE '^- \*\*F-[0-9]+' ~/dsm-agentic-ai-data-science-methodology/FEATURES.md`. Compare against the count claimed in `content/blog/2026-03-20-dsm-features-three-dimensions/index.md`.
- Principle count: `grep -cE '^### 1\.[0-9]+' ~/dsm-agentic-ai-data-science-methodology/DSM_6.0_AI_Collaboration_Principles_v1.0.md`. Compare against the count claimed in `content/about.md`.

**Gate to Stage 2:** the BL exists with its checklist scaffolded and deltas recorded.

### Stage 2 , Ship the factual updates

**Trigger:** Stage 1 complete. Ship Stage 2 in the same session as Stage 1 whenever the time budget allows; these are factual updates that prevent drift from getting worse.

**Three fronts ship here:**

- **Front B , features post update.** `content/blog/2026-03-20-dsm-features-three-dimensions/index.md`. Update the total count everywhere it appears (title, description, opening, closing). Weave new F-entries into Human Oversight / Knowledge Provenance / Experience Accumulation as narrative threads, not a list.
- **Front C , About page principle list.** `content/about.md`. Update the "The N Principles" heading and the numbered list to match `DSM_6.0`. Verify wording of any new principle against DSM_6.0 §1.X before committing.
- **Front F , dsm-portfolio inbox notification.** Write to `~/dsm-data-science-portfolio-working-folder/_inbox/YYYY-MM-DD_dsm-blog-poster_dsm-vX.Y-release.md` with a short summary and links. Triggers the cross-repo write confirmation gate.

**Workflow:** voice calibration from `content/about-me.md` + `content/about.md`. /humanizer pre-publish gate.

**Gate to Stage 3:** factual updates committed (or explicitly deferred in the BL with a reason).

### Stage 3 , Write the release post

**Trigger:** Stage 2 complete. May span sessions.

**Action:** Front A , the story-shaped release post at `content/blog/YYYY-MM-DD-dsm-vX-release/index.md`.

**Reconstruction trail (mandatory reading order):** all paths in DSM Central (`~/dsm-agentic-ai-data-science-methodology/`):

1. **Index** , `dsm-docs/blog/feature-trail.md` , read the version's section and the "Narrative threads" at the bottom.
2. **BL files** , `dsm-docs/plans/done/BACKLOG-NNN_*.md` for each feature in scope. The Problem Statement is the "why this matters" paragraph; Origin identifies the trigger.
3. **Inbox origins** , for any feature with an inbox-sourced BL, read the referenced entry in `_inbox/done/`. Concrete incident stories are the best blog material.
4. **Reasoning lessons** , `.claude/reasoning-lessons.md`, search for `[auto]` or `[STAA]` entries tied to the version. These surface the meta-pattern that ties multiple features together.
5. **CHANGELOG** , `CHANGELOG.md` for the version(s). Same-day version bumps are treated as one release in the post.

**Post structure (5 parts):**

1. **Hook** , the concrete incident (from the inbox source).
2. **Insight** , the meta-pattern from reasoning lessons.
3. **Fix** , the features that implement the fix.
4. **Bonus** , related features following the same pattern.
5. **Takeaway** , what this version reveals about how DSM evolves.

**Bundling decision:** same-day version bumps are one release. Multi-version backlogs (e.g., v1.5 through v1.9) can ship as one bundled post OR split by narrative cluster, depending on whether the versions share a story. Decide at Gate 1 of the chunked drafting protocol.

**Drafting:** apply DSM_0.2 §8.10 chunked-drafting protocol (Gate 1 purpose/audience/outcome/length/scope, Gate 2 TOC with per-section budgets, Gate 3 one section at a time with per-section approval, Gate 4 full-document consistency review). Voice calibration from `content/about-me.md` + `content/about.md`. /humanizer pre-publish gate.

**Anti-patterns:**

- Do not list features mechanically , the feature list already lives in FEATURES.md and CHANGELOG.
- Do not write a changelog summary , write the story the sources don't tell.
- If covering an older feature whose `feature-trail.md` row is empty, populate the row first via the reconstruction recipe in `feature-trail.md`'s "How to use this index" section.

**Gate to Stage 4:** release post(s) published; URL(s) recorded in the BL's Outcomes section.

### Stage 4 , Cross-post and record

**Trigger:** Stage 3 complete.

**Two fronts ship here, in order:**

- **Front E , LinkedIn cross-post.** One LinkedIn post per release blog post produced. Draft in `dsm-docs/blog/linkedin-posts.md` as the next Post N. Format: 250 to 400 words, first-person, hashtags, "Full post:" link. /humanizer pre-publish gate.
- **Front D , linkedin-posts.md canonical record.** After the LinkedIn post is published, record the URL and "Status: Published" on the same Post N entry. The draft and the record live in the same file; "Front D" is the act of completing the entry with the live URL.

**Gate to Stage 5:** LinkedIn post(s) published with URL(s) recorded.

### Stage 5 , Close

**Trigger:** all six fronts marked complete or explicitly deferred in the BL.

**Action:** verify CLAUDE.md "DSM Version Release Coverage" section is still current with the pipeline shape. Move the BL to `dsm-docs/plans/done/` with Date Completed. Update `dsm-docs/plans/README.md` index.

**End of pipeline.**
