### [2026-07-28] FEATURES update from DSM Central (v1.19.0, 4 new F-entries)

**Type:** Feature Timeline Update
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

Context: v1.19.0 shipped the two adoptable mechanisms for the "Forward the Why"
principle that v1.18.0 named but left unimplemented, plus a consent gate for
fan-out actions and a corrected definition of a bite. The two Forward the Why
entries (F-145, F-146) are siblings and read best together; F-145's origin note
records that the mechanism's first map inside DSM was wrong in both rows and its
own reconcile step is what caught that, which is the more interesting story than
the feature itself.

New entries, verbatim from FEATURES.md:

- **F-146 (2026-07-28) Causal-forward session handoffs (BL-475, DSM_6.0 §1.13 Delegating face)** — A checkpoint's pending list now states, per item, what the continuation requires and why, what it depends on, what order the dependencies force, and what breaks if it is skipped, so the next session acts on the ordering instead of rebuilding the reasoning from task names, or re-opening a decision the previous session already settled. Applied to the three skills that author pending lists (`/dsm-wrap-up`, `/dsm-quick-wrap-up`, `/dsm-checkpoint`); the consuming side needed no change, because the *why* travels inside the format. The rule bounds its own verbosity: an item is longer by exactly the causal links the receiver would otherwise rebuild, and an item with no dependency is stated plainly rather than padded with invented rationale. Origin: the meter-to-cash spoke wrote its S6 handoff this way and its S7 session acted on the ordering without reconstructing it.
- **F-145 (2026-07-28) Downstream Impact Map for cross-BL coupling (BL-474, DSM_6.0 §1.13 Registering face)** — A backlog item that settles something later items will build on (a schema, a vocabulary, a shared surface) can now record that coupling on itself, at the moment it settles it and while the interface is still cheap to change, instead of leaving each downstream author to discover it later and record only their own partial view. The section is optional and guarded by a consumption question, so leaf items omit it rather than filling an empty table. When a consuming item is eventually built, the map is checked against what actually happened, and the useful output is the mismatch: consumed but never mapped, mapped but never consumed, or consumed differently than forecast. Origin: the meter-to-cash spoke's first module BL carried a six-row map. The mechanism's first map inside DSM itself was wrong in both rows, and the reconcile step is what caught it.
- **F-144 (2026-07-28) Informed-consent gate before high-token-cost fan-out actions (BL-476, DSM_0.2 §8.9.2)** — Before an action that turns one invocation into many independent model calls against a shared usage window, the agent must say what it will cost: the shape of the fan-out, an order-of-magnitude token estimate, the model tier, the risk that exhausting the window forces a hard stop mid-run, and cheaper alternatives offered as real options rather than a footnote. The gate cannot be bypassed by auto mode or cleared by a general "proceed", and it deliberately does not fire on ordinary expensive-looking work, because a gate that fires on everything is one the user learns to click through. Origin: a session that spent roughly 3.0M tokens across two research passes, exhausted the window, and returned a partial deliverable after the second pass died mid-run.
- **F-143 (2026-07-28) A bite is the smallest increment the reviewer can verify (BL-478, DSM_6.0 §1.1)** — The unit of collaborative work is now defined by what the reviewer can actually check, one testable function, one notebook cell producing one output, one short passage, rather than by what is convenient to produce. Test-first became a standing rule instead of a per-item preference, and the build order was corrected across the methodology and the template spokes receive. The framing that treated an IDE permission window as the collaboration gate is gone: approving a write is not approving the concept, including when writes are auto-approved. Origin: a spoke session where the weak wording turned out to live in the spoke-facing template rather than the protocol everyone assumed it came from.

---

