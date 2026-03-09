@../../dsm-agentic-ai-data-science-methodology/DSM_Custom_Instructions_v1.1.md

# Project: DSM Blog Poster
Domain: Software Engineering (Static Site + Automation) / Content Operations

## Framework Documents
This project uses:
- **DSM 4.0: Software Engineering Adaptation** (Project Knowledge): Adapted phases for SW projects
- **PM Guidelines** (Project Knowledge): Sprint planning structure
- **Collaboration Methodology v1.3.0** (Project Knowledge): Core philosophy, communication style
- **Content Operations Guide** (`docs/content-operations.md`): Role definition, legal/licensing checklist, distribution practices, asset management, lessons learned

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
- **Primary inputs**: Blog posts from DSM Central (`docs/blog/`) and spoke projects
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
- AI-generated asset licensing and management (see `docs/content-operations.md`)

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

## Session Transcript Protocol (reinforces inherited protocol)
- Append thinking to `.claude/session-transcript.md` BEFORE acting
- Output summary AFTER completing work
- Conversation text = results only
- Use Reasoning Delimiter Format for every thinking block:
  <------------Start Thinking / HH:MM------------>
  [reasoning content]
- HH:MM is 24-hour local time when thinking begins; no end delimiter needed
- Include **User:** and **Output:** markers per DSM_0.2 format

## Inbox Lifecycle (reinforces inherited protocol)
- Inbox entries are transient: DELETE after processing, do not mark "Status: Processed"
- If an outbound inbox entry you created was consumed (file deleted by the receiving project), that is correct behavior -- do not re-create it

## Project-Specific Requirements
- Blog posts sourced from DSM Central and spoke project `docs/blog/` folders
- Hugo content in `content/blog/` follows date-prefixed naming
- Portfolio section highlights DSM ecosystem projects
- Minimal theme, fast loading, mobile responsive
