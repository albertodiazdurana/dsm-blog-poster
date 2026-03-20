# DSM Methodology Feedback

## Entry 1: Inbox Action Items should require BL before implementation

**Date:** 2026-03-17
**Session:** 8
**Section:** DSM_3 6.4.3 (Inbox Lifecycle)
**Score:** 3/5

**Gap:** Section 6.4.3 lists three processing paths for inbox entries: Backlog Proposal (create BACKLOG item), Methodology Observation (assess), and Action Item (implement, defer, or reject). The "Action Item: implement" path allows direct implementation without requiring a backlog item. This bypasses the BL planning workflow (plan -> branch -> PR -> merge) that provides traceability and user approval before code/content changes.

**Evidence:** An inbox entry from dsm-data-science-portfolio-working-folder requested publishing an About page. The agent classified it as an Action Item and implemented it directly (created content/about-me.md, updated hugo.toml, committed) without first creating a BL item. The user expected BL-based workflow.

**Proposed Change:** Clarify Section 6.4.3 so that "Action Item: implement" requires creating a BL/BACKLOG item when the action involves code, content, or configuration changes. Direct implementation should be reserved for trivial actions (e.g., acknowledging a notification, updating a config value).

---

## Entry 2: Feedback must draft in docs/feedback/ before pushing to DSM Central inbox

**Date:** 2026-03-17
**Session:** 8
**Section:** DSM_3 6.4.4 (Spoke-to-Hub Flow)
**Score:** 2/5

**Gap:** The agent attempted to push feedback directly to DSM Central's `_inbox/` directory, skipping the intermediate step of drafting in the spoke project's `docs/feedback/methodology.md`. Section 6.4.4 clearly defines the flow: draft in `docs/feedback/`, push notification to hub inbox when ripe, hub reads spoke's `docs/feedback/` for full context. The anti-patterns section explicitly states: "Do not use the inbox as a drafting space; draft in docs/feedback/, push when ripe."

**Evidence:** When asked to send feedback to DSM Central about Entry 1, the agent proposed writing directly to `~/dsm-agentic-ai-data-science-methodology/_inbox/`. The user had to correct the flow.

**Root Cause:** The agent recalled the inbox as the destination for cross-project communication but did not recall the intermediate docs/feedback/ drafting step defined in Section 6.4.4. The spoke-to-hub flow has two stages (draft -> push) but the agent collapsed them into one.

**Proposed Change:** No DSM text change needed -- the protocol is already clear. This is an agent behavioral failure. Saved as feedback memory for future sessions.