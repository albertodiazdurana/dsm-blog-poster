### [2026-06-01] FEATURES update from agentic-ai-data-science-methodology (v1.13.0)

**Type:** FEATURES timeline update
**Priority:** Medium
**Source:** agentic-ai-data-science-methodology (DSM Central)

1 new F-entry shipped in v1.13.0 (S215):

- **F-134 (2026-06-01) User-Reframes-Proposal Handling sub-rule (BL-453, DSM_0.2 §8.0.1)** — Gate 0 (Collaborative Definition) gains a named operational sub-rule for one recurring move: when the user responds to a proposal by reframing it (re-decomposing, re-shaping the structure) rather than answering yes/no, the agent re-decomposes instead of defending the original framing. Two sub-rules: loose framing ("formalize this", "address these") triggers "what threads do you see?" before any decomposition is proposed; a reframe that doubles as "this also explains why the original problem existed" is a diagnostic that the first framing missed a structural coupling. Four distinct sibling patterns (user-factual-question, pointer-as-implicit-correction, "why does this matter?" drop-signal, deliverable-portability scope-expansion) are cross-referenced, not absorbed. §8.0 already stated the principle ("the conversation IS the collaboration") but agents defended their framing across six recurrences (S180/S183/S200/S201/S203/S204) over four-plus months, so §8.0.1 names the behavior the principle implies. Origin: pattern promotion from `.claude/reasoning-lessons.md`, filed S214, implemented S215.

**Context:** This is a strong blog-candidate feature — it captures a subtle human-AI collaboration dynamic (the difference between answering a proposal and reframing it) that most people experience but few name. The "principle existed for four months but the behavior still failed six times" framing is a good hook for a post about why naming operational behaviors matters even when the underlying principle is already stated.

---

### [2026-06-01] FEATURES update from agentic-ai-data-science-methodology (DSM Central)

**Type:** Feature Timeline Update
**Priority:** Medium
**Source:** agentic-ai-data-science-methodology (DSM Central)

1 new F-entry shipped in v1.14.0 (S216):

- **F-135 (2026-06-01) Introduce Once, Then Deepen writing principle (BL-454, DSM_6.0 §1.13)** — Structured prose with a summary-then-body shape (project plans, proposals, reports, CVs, public-facing copy, research files) now has a named information-architecture discipline: introduce each concept, metric, or claim once and let the body deepen it, rather than restating it verbatim between summary and body. Two facets come with it: lead with the descriptive phrase before the acronym in introductions ("a Deliberate Systematic Methodology" before "DSM"), and when a deliverable needs both a no-repetition refactor and a humanizer pass, run the repetition refactor first and the humanizer second (the reverse wastes humanizer effort on prose about to be cut, and repetition is not an AI tell the humanizer catches). The principle lives in DSM_6.0 §1.13; DSM_0.2 §8.10 Gate 4 operationalizes it as the cross-section repetition check plus the ordering rule, so prose produced through the chunked-drafting protocol surfaces it. Scope is the summary+body shape, not document length; short-form text, tables, code, and checklists are out of scope. Origin: pattern stabilized across CV summaries, public-facing copy, and hiring deliverables in the portfolio spoke (S85/S86/S87), promoted when it cleared the "multiple deliverable types" bar S86 set.

**Context:** A blog-candidate feature about information architecture in writing. The core idea ("introduce once, deepen in the body, don't restate the summary in the body") is a concrete, relatable writing-quality rule, and the refactor-before-humanize ordering is a nice operational detail (you cannot humanize prose you are about to cut). Origin story is strong: the pattern was discovered the hard way across CV summaries, public-facing copy, and hiring deliverables in a portfolio project before it was promoted to a DSM principle, so it carries lived evidence rather than abstract prescription.

> **Note (added S30, 2026-07-12):** F-135 above named "Introduce Once, Then Deepen" a DSM_6.0 §1.13 principle. As of TAB v1.18.0 it was relocated to DSM_0.2 §8.10 and renamed "Present Once, Then Deepen", it is now a writing discipline, not a principle. The DSM_6.0 §1.13 slot is now the new principle "Forward the Why" (F-142, BL-473). This notification is preserved as the accurate v1.14-era record.
