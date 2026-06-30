
### [2026-06-18] FEATURES update from DSM Central (v1.17.0) , 1 new F-entry

**Type:** Feature Notification
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

New F-entry in v1.17.0:

- **F-141 (2026-06-18) Subchapter/paragraph bite + file-first editable delivery for chunked drafting (BL-465, DSM_0.2 §8.10 Gate 3)** — Structured-prose deliverables (plans, proposals, reports, research files, blog posts) are now drafted one subchapter at a time, or one paragraph when the subchapter is long, and each bite is written to an editable draft file rather than pasted into the conversation, so the user edits the draft in place between bites instead of relaying changes back through chat. Explicitly modeled on the Notebook Collaboration Protocol (one cell at a time, user returns review before the next). Incremental per-bite file writes are the delivery; generating the whole document in one write stays prohibited, and Gate 4 remains the cross-section consistency pass. Origin: Data Science Portfolio S106, validated live on a 4-part blog series.

**Blog angle:** the document-co-development model (file-first editable delivery, Notebook-protocol analogy) , plus the recursive irony that the same session's EXP-005 design was itself drafted with the OLD chat-block model this BL replaces, which is what surfaced the need.
