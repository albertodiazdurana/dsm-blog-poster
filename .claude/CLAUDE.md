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

### Pre-Generation Brief Protocol (reinforces inherited protocol)
- Three-gate model: concept (explain) → implementation (diff review) → run (when applicable)
- Each gate requires explicit user approval; gates are independent

### Inbox Lifecycle (reinforces inherited protocol)
- After processing an inbox entry, move it to `_inbox/done/`
- Do not mark entries as "Status: Processed" while keeping them in place

### Punctuation
Use "," instead of "—" for connecting phrases in any language.

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

### Existing Content to Migrate

| # | Date | Title | Source |
|---|------|-------|--------|
| 1 | 2026-01-30 | From TF-IDF to Transformers: What Classifying Disaster Tweets Taught Me About How We Got to LLMs | `~/dsm-disaster-tweets/docs/blog-post-draft.md` |
| 2 | 2026-02-01 | SQL Query Agent Part 1: From Notebook Exploration to Structured Evaluation | `~/sql-query-agent-ollama/docs/blog/blog-s01.md` |
| 3 | 2026-02-03 | SQL Query Agent Part 2: The Value of Human Review in AI-Generated Code | `~/sql-query-agent-ollama/docs/blog/blog-s02-collaboration-value.md` |
| 4 | 2026-02-03 | SQL Query Agent Part 3: Why Zero-Shot Beat Few-Shot | `~/sql-query-agent-ollama/docs/blog/blog-s02-ablation.md` |
| 5 | 2026-02-05 | Validating 7,400 Lines of Documentation with Compiler Architecture | `~/dsm-graph-explorer/docs/blog/epoch-1/blog-draft.md` |
| 6 | 2026-02-05 | From Windows to WSL: Migrating an AI-Assisted Documentation Ecosystem | `~/dsm-graph-explorer/docs/blog/epoch-2/wsl-migration-post.md` |
| 7 | 2026-02-06 | A Methodology That Listens: How Our First Spoke Project Rewrote the Playbook | `~/dsm-agentic-ai-data-science-methodology/docs/blog/2026-02-06_blog-feedback-loop.md` |

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
- Run `/humanizer` on all material produced and posted by this project: blog posts, page content, descriptions, any reader-facing prose
- This is a pre-publish gate, not optional
