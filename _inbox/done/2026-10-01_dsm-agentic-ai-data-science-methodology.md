### [2026-10-01] FEATURES update from DSM Central (v1.26.5)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 268

FEATURES.md was updated with new user-facing capabilities in v1.26.5. Actions:
1. Update the feature blog to include the new F-entries
2. Write and post a dedicated blog about the new feature(s)

**New F-entries:**

- **F-178 (2026-10-01) Session memory ages itself down a three-tier chain so the always-loaded file stays small (BACKLOG-544, `/dsm-memory-decommission`, `/dsm-memory-archive`)** — The file an agent reads in full on every turn had been growing with every session it recorded, because the one-time split that separated permanent context from session notes left nothing to stop the session half from re-filling. Two move-only skills now age it. The oldest session's notes move from the always-loaded file to an on-demand long-term file once the session zone passes a size threshold, and from there to a deepest archive once the long-term file passes its own. They run at wrap-up, move a whole session's notes at a time, never touch the permanent zone, back up before writing, and check that nothing was lost. The threshold watches the session zone rather than the whole file, because the permanent zone on its own can be larger than a naive whole-file target would allow, which would have made the trigger fire on every wrap-up and never clear.

- **F-177 (2026-10-01) The reasoning-lessons primer gains a flow control, so its two size targets can both hold (BACKLOG-495, DSM_0.2.A §8)** — The curated lessons an agent is primed with at session start had a target entry count and a target byte size that quietly contradicted each other: at the length entries were actually written, meeting one broke the other. The missing piece was a limit on per-entry length, not on how many entries accumulate. Each entry now targets roughly six hundred characters, the figure at which the count target and the byte target line up, and an over-length entry is shortened or split rather than dropped. Alongside it, a long-standing practice becomes a written rule: ecosystem-wide lessons at the hub go to the shared aggregation file that already redistributes them, instead of also sitting in the always-loaded primer. A measurement set the direction. The intake rate was already below the per-session cap the item was filed to add, so a cap would have controlled nothing, and the real lever was entry length.

**Context:**
Both entries are boot-context flow controls shipped together in v1.26.5: F-178 keeps the always-loaded MEMORY.md small by ageing old session notes down a tier chain; F-177 adds a per-entry size ceiling to the reasoning-lessons primer so its count and byte targets stop contradicting each other.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`
