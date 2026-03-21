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

---

## Entry 3: DSM_3 6.4.3 says "delete" but DSM_0.2 says "move to done/"

**Date:** 2026-03-20
**Session:** 9
**Section:** DSM_3 6.4.3 (Inbox Lifecycle) vs DSM_0.2 (Session-Start Inbox Check)
**Score:** 4/5

**Gap:** DSM_3 Section 6.4.3 step 4 says: "Remove: Delete processed entries from the inbox file." DSM_0.2 Session-Start Inbox Check says: "After processing, **move** the entry to `_inbox/done/`. Do not mark entries as 'Status: Processed'... Processed entries in `done/` preserve communication history and traceability; entries left in the inbox root cause stale re-processing in future sessions (observed: dsm-blog-poster S3-S4)."

These two documents contradict each other. DSM_0.2 was updated with the correct behavior (move to done/) and includes a rationale citing a real incident, but DSM_3 6.4.3 was not updated to match. Agents and project CLAUDE.md files that reference DSM_3 inherit the outdated "delete" instruction.

**Evidence:** This project's CLAUDE.md stated "Inbox entries are transient: DELETE after processing" -- derived from DSM_3 language. Agent planned to delete inbox entries. User corrected: "Do not delete, move to _inbox/done/."

**Root Cause:** DSM_0.2 was patched to fix the inbox lifecycle (citing dsm-blog-poster S3-S4 observation), but the corresponding DSM_3 Section 6.4.3 text was not updated in the same change. Spoke projects referencing DSM_3 inherit the stale instruction.

**Proposed Change:** Update DSM_3 Section 6.4.3 step 4 from "Remove: Delete processed entries from the inbox file" to "Archive: Move processed entries to `_inbox/done/`." Add the traceability rationale from DSM_0.2. This brings DSM_3 in sync with DSM_0.2 and prevents spoke projects from inheriting the outdated delete behavior.