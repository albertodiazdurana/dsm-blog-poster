### [2026-09-30] FEATURES update from DSM Central (v1.26.4)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 266

New F-entry this release:

- **F-176 (2026-09-30) No project name reaches the public mirror, and the rule that guarantees it is now methodology (BACKLOG-560, DSM_0.2.C §5.7)** — The public methodology carried specific project, client, and spoke names in its provenance lines — each one a confidentiality exposure and, to an outside reader with no access to the project, a pointer that resolves to nothing. Every such name is now reworded to a project-agnostic form that keeps the session and backlog id and drops the name, verified clean by a boundary-robust search run with a control that proves the search can actually match. The standing rule behind the cleanup is written into the methodology rather than left as a session practice: no name of a specific project reaches the public mirror, it covers both removing what is there and preventing what tries to enter, and it counts a slug smuggled back in as a generic descriptor as a violation. The guarantee is stated honestly for anyone who adopts it — the scanner is a backstop and operator review is the last gate, so the claim is bounded to the public surface and to what the checks can see, not to technical impossibility.

**Context / blog angle:** v1.26.4 shipped the de-identification of the public provenance corpus plus DSM_0.2.C §5.7, which codifies the standing "no project names in the public mirror" rule (removal + prevention). A blog-worthy angle: how a public methodology stays project-agnostic *by construction* — mirror allowlist + a sync-time content scanner + operator review — and why the honest framing is "backstop, not proof" rather than a claim of technical impossibility.
