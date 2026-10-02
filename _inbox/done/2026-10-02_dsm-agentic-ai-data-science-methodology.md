### [2026-10-02] FEATURES update from DSM Central (v1.26.6)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 269

FEATURES.md was updated with a new user-facing capability in v1.26.6. Actions:
1. Update the feature blog to include the new F-entry
2. Write and post a dedicated blog about the new feature(s)

**New F-entries:**

- **F-179 (2026-10-02) The always-loaded memory file's permanent zone now gets a size-review flag so it stops growing unchecked (BACKLOG-568, `/dsm-wrap-up`)** — The memory file an agent reads in full on every turn is split into a permanent zone that never ages and a session zone that does. Machinery added earlier keeps the session zone small by ageing its oldest notes out of the file, and once that runs the permanent zone is the larger half and the only one still growing, with nothing watching it. Wrap-up now measures the permanent zone and, when it passes a soft size target, raises a non-blocking flag recommending a review: trim lines that are resolved, or move durable-but-not-boot-critical lines somewhere less costly to load and then remove them — moved before removed, never silently dropped. The flag only recommends; a person or the deeper analysis pass does the trimming, because the permanent zone holds high-value context that should not be aged automatically the way the session zone is.

**Context:**
v1.26.6 adds an evergreen-zone review flag to wrap-up, the companion to v1.26.5's session-zone tiering (F-178): once tiering drains the session zone, the permanent (evergreen) zone becomes the larger and only-growing half of the always-loaded cost, so wrap-up now measures it and flags when it exceeds a soft ~6 KB target.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`
