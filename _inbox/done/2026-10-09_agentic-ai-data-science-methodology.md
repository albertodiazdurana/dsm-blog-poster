### [2026-10-05] FEATURES update from DSM Central (v1.26.7)

**Type:** Notification
**Priority:** Low
**Source:** agentic-ai-data-science-methodology

1 new F-entry shipped in v1.26.7:

- **F-180 (2026-10-05) Session start now checks the FEATURES and README feature counts against the real number of entries, so a stale total can't slip onto the public page (BACKLOG-569, `/dsm-go`)** — The feature timeline and the README both carry a running total that is kept current by hand, and a release that added entries without updating it left both numbers wrong until someone happened to notice. Session start now recomputes the real count and compares it against both stated totals, flagging a mismatch with both the claimed and the measured number and staying quiet when they agree, so the drift is caught at the next boot instead of sitting on the public timeline. It is the counting-side companion to the existing check that already watched the related downstream notification, which had a guard while the count had none.

**Context:** v1.26.7 adds a boot-time count-equality assertion (`/dsm-go` Step 2f, BACKLOG-569) — the prevent half of the S269 §22 count-drift fix. Sibling to the existing Step 2e downstream-notification reconciliation: the notification half of FEATURES maintenance had a guard, the count half had none.

### [2026-10-05] FEATURES update from DSM Central (v1.26.8) — 2 new entries

**Type:** Notification
**Priority:** Low
**Source:** DSM Central (S271)

Two internal session-lifecycle correctness fixes shipped in v1.26.8; new F-entries (verbatim):

- **F-182 (2026-10-05) Wrap-up stops dropping a project's inbox by mistaking every project for the public mirror (BACKLOG-566, `/dsm-wrap-up`, `/dsm-quick-wrap-up`)** — Session wrap-up carried a guard meant to keep the read-only public mirror from committing its own inbox entries. It identified the mirror by the absence of a single file that lives only at the hub, but every ordinary project also lacks that file, so the guard treated every project as the mirror and quietly left each one's own inbox changes out of the wrap-up commit, logging the omission as if it were the intended protection. The guard now identifies the public mirror positively, by the absence of every role signal a real project carries, so the hub, a clone of it, and any spoke all commit their own inbox normally while the genuine mirror is still held back. The same corrected check now lives in both the full and the quick wrap-up.

- **F-181 (2026-10-05) Session start stops silently skipping a merged branch it could not delete, and the rule it followed is corrected (BACKLOG-565, `/dsm-go`, DSM_0.2 §20.4)** — The boot-time cleanup that deletes branches already merged into the main line ran the safe delete and, when that delete refused, moved on without a word. The refusal it swallowed is the one that matters: the safe delete checks a branch against its own remote copy, not against the main line, so a branch genuinely merged to main whose remote copy has fallen behind refuses to delete and was left to accumulate, unseen, across sessions. The cleanup now reports such a branch as a leftover needing attention instead of skipping it, and it never reaches for the force-delete that would hide the distinction. The methodology text that had described the delete's criterion as the main line rather than the branch's own remote copy is corrected to match what the command actually tests.

### [2026-10-07] FEATURES update from DSM Central (v1.27.0)

**Type:** FEATURES notification
**Priority:** Medium
**Source:** agentic-ai-data-science-methodology

New F-entries in v1.27.0 (verbatim):

- **F-185 (2026-10-06) Setting up a fresh public-mirror fork is smoother and less misleading (BACKLOG-573/574/575/577, Cloned-Mirror Kick-off)** — Initializing a fresh fork surfaced several rough edges, now addressed together. Kick-off prints the exact one-line ignore rule a fresh fork needs (without editing the local git exclude file itself) when generated files would otherwise clutter `git status`; the drift check no longer labels a mirror's load-bearing command copies as orphaned-and-deletable; Kick-off ends with a readiness checklist of the environment tools the boot gates depend on; and a cross-repo-write guard that had shipped non-executable on the mirror is corrected so it actually runs.
- **F-184 (2026-10-06) The session-analysis agent no longer carries personal names into durable, propagating lessons (BACKLOG-572, `/dsm-staa`)** — The analysis command reads a whole session transcript, which on a sensitive project can hold personal names, and appended its findings to a lessons file that propagates to the hub and into every future session's startup context. It now carries an explicit instruction to keep every quoted excerpt and every saved lesson name-free (role, not name), states that propagation chain so it is visible from inside the command, and recommends scrubbing names before analysis on projects that declare a privacy policy.
- **F-183 (2026-10-06) Scanning for leaked personal data no longer risks leaking it (BACKLOG-571, DSM_0.2.C §5.8)** — When a project that handles sensitive data scans its transcript, memory, or reasoning-lessons for stray personal names before they can cross to the hub, the scan must now report only generically ("clean", or line numbers) and never echo a matched name, or a search pattern containing one, back into those same append-only files. A new core rule stops the control from becoming the leak itself, and an always-loaded pointer keeps the rule visible where the transcript is written.

Context: v1.27.0 resolved three issues filed on the public mirror — an egress leak-scan safety rule (§5.8), a /dsm-staa PII/egress safeguard, and a cluster of Cloned-Mirror Kick-off / fork-init fixes. Blog-worthy angle: "the leak-scan must not become the leak" (a control that was its own vector).

### [2026-10-08] FEATURES update from DSM Central (v1.27.2)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 275

FEATURES.md gained one new user-facing capability in v1.27.2. Actions:
1. Update the feature blog to include the new F-entry
2. Consider a dedicated blog about the new feature

**New F-entries:**

- **F-186 (2026-10-08) Two `/dsm-align` audits that catch a backlog item going invisible or a finished design left marked unfinished (BL-557 + BL-580, `/dsm-align` Steps 11d/11e)** — The active backlog index is what every planning pass and session-start report reads to decide what to work on, and nothing ever checked that it matches the files on disk: an item filed without its index row was invisible, and two sat that way for roughly five months, outside the process rather than merely delayed. A separate gap let a design item whose decision was already written stay listed as open work, carried forward in every checkpoint, because its status lived in one place and the evidence it was done lived in another. Two report-only audits now run in the hub's alignment pass: one set-differences the active index against the files both ways, telling an unlisted file apart from a row whose file has moved; the other cross-references decision records marked complete against items still listed active. Both report rather than fixing, since placing or closing an item needs a human judgement, and both stay silent when the index is clean so they do not become warnings people learn to ignore. With the existing done-index audit they make three axes of one question: does the record of what there is to do still match reality.

Context: v1.27.2 is an internal-governance release — two report-only audits in the hub's own /dsm-align pass. Blog-worthy angle: "an index nobody audits is a place work goes to disappear" (a filed item sat invisible for five months because nothing checked the index against the files).

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-10-09] FEATURES update from DSM Central (v1.28.0)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 276

FEATURES.md gained one new user-facing capability in v1.28.0. Actions:
1. Update the feature blog to include the new F-entry
2. Consider a dedicated blog about the new feature

**New F-entries:**

- **F-187 (2026-10-09) The cross-project lessons file now has a size bound and a prune, so it stops growing without limit (BACKLOG-567, DSM_0.2.A §8.3, `/dsm-staa` Step 7b)** — The hub's aggregation of reasoning lessons from every project had rules for attribution and deduplication but nothing capping its size or removing stale entries, so it grew past the boot-primed file it feeds and its signal thinned as already-codified lessons piled up. It now carries a soft review-cost size bound, a per-entry length ceiling, and a prune that the session-analysis agent runs when the file is over bound: archiving lessons since codified into protocols, consolidating duplicates reported by several projects, and retiring lessons from projects that no longer exist, each leaving a tombstone so nothing is dropped silently. The bound is an honest long-term target — the first prune confirmed the file is mostly irreducible cross-project value, so it is approached gradually as lessons get codified rather than by compressing valuable prose, and the prune is a no-op on spoke projects, which have no such aggregation file.

Context: v1.28.0 is an internal-governance release — bounding the hub's own cross-project lessons aggregation. Blog-worthy angle: "a bound you cannot reach yet is still worth setting" (the file is mostly irreducible value, so the bound is an honest long-term target approached as lessons get codified, not a number forced by compression).

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-10-09] FEATURES update from DSM Central (v1.29.0)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 277

FEATURES.md gained one new user-facing capability in v1.29.0. Actions:
1. Update the feature blog to include the new F-entry
2. Consider a dedicated blog about the new feature

**New F-entries:**

- **F-188 (2026-10-09) A fresh directory can be set up as a new spoke with one command (BACKLOG-578, DSM_0.2.A §25.7, `/dsm-new-spoke`)** — Turning an uninitialized directory into a DSM spoke had no clean path: the only setup command on offer assumed a cloned mirror and would register the directory as its own hub, so a new spoke had to be hand-assembled and was easy to get wrong. The new `/dsm-new-spoke <hub-path>` command scaffolds the directory as a spoke of an existing hub — pointing it at the real hub, building the standard folders, and running the spoke alignment — and session start now recognizes the mistaken case and routes the user to the command instead of failing on it.

Context: v1.29.0 adds a first-class new-spoke bootstrap path (the /dsm-new-spoke skill + a /dsm-go Step 0.8 guard), resolving take-ai-bite issue #117. Blog-worthy angle: "the setup path that assumed you were cloning, not starting fresh" — a new spoke had no clean bootstrap because the only path self-registered the directory as its own hub.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-10-09] FEATURES update from DSM Central (v1.30.0)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 278

FEATURES.md gained one new user-facing capability in v1.30.0. Actions:
1. Update the feature blog to include the new F-entry
2. Consider a dedicated blog about the new feature

**New F-entries:**

- **F-189 (2026-10-09) A public-mirror fork can keep its own backlog line instead of waiting on the private hub (BACKLOG-581, DSM_0.2 §21.5, cross-ref DSM_7.0 §2.1)** — A fork of the public mirror — including one promoted to its own local hub — had no sanctioned way to develop a methodology change on its own: backlog numbers are assigned in the private hub, which a fork cannot see or safely guess, and a de-identified fork ships no active backlog bodies at all, so a fork that spotted a useful change had to push it straight upstream or track it informally with no uniform form. A fork may now maintain its own backlog line numbered from 001, independent of the hub's numbering: the fork's numbers are a local identity, the hub stays canonical and assigns the real number if it later absorbs the change (with the fork recording the mapping), fork bodies stay name-free for public safety, and an ordinary upstream sync preserves them across updates. Offering a developed item upstream stays optional but recommended, so a change that helps every fork can still reach the hub.

Context: v1.30.0 adds a sanctioned independent fork-local backlog line (DSM_0.2 §21.5), absorbed from the alberto-passerelle fork's reference PR (take-ai-bite #124/#125). Blog-worthy angle: "a fork that can't see the hub's numbers can still keep a backlog" — independent local numbering with canonical reconciliation on absorption.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-10-10] FEATURES update from DSM Central (v1.31.0)

**Type:** Feature Notification
**Source:** dsm-agentic-ai-data-science-methodology
**Session:** 279

FEATURES.md gained one new user-facing capability in v1.31.0. Actions:
1. Update the feature blog to include the new F-entry
2. Consider a dedicated blog about the new feature

**New F-entries:**

- **F-190 (2026-10-10) Projects handling personal data get a data-protection / compliance briefing by design (BACKLOG-582, DSM_0.2.C §5.9)** — A project that processes personal or confidential data had no by-design prompt for a data-protection review: the need surfaced ad hoc, usually after a PII-handling model was already running, and was recorded — if at all — in no uniform form, so it was easy to miss or discover late. DSM now requests a standard briefing for such a project: the project declares it handles such data in its own config, and DSM asks for a fixed requirements checklist and an A–G template placed with the project's decisions, adapted per project type (full for documentation and data-science work, a lightweight "not applicable, with justification" for applications on synthetic data, deferred to the upstream regime for external contributions). The briefing is a name-free hand-off to human or expert review that asserts no legal conclusions of its own, and a missing one warns at session start rather than blocking work.

Context: v1.31.0 adds DSM_0.2.C §5.9, a by-design data-protection / compliance briefing. Blog-worthy angle: "the compliance review you'd otherwise discover late, asked for up front" — a uniform, name-free hand-off to human/expert review that asserts no legal conclusions, surfaced softly at session start rather than blocking work.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-10-11] New feature in DSM Central: DP/compliance briefing surfacing check (v1.32.0)

**Type:** Notification
**Priority:** Low
**Source:** agentic-ai-data-science-methodology (DSM Central)

New F-entry in FEATURES.md (v1.32.0):

- **F-191 (2026-10-11) A project that says it handles personal data is now actually warned when its data-protection briefing is missing (BACKLOG-583, `/dsm-go` Step 2g)** — The by-design data-protection briefing added in the previous release defined when a briefing is owed and what it must contain, but the promised reminder was only a convention: nothing performed the check, so a project that declared it handles personal or confidential data and had not yet written its briefing was never actually told. Session start now performs the check — when the project declares the trigger in its own config and no briefing sits with the project's decisions, the boot report warns, and it stays silent once the briefing exists or when no such data is handled. The reminder is soft, so it never blocks work, and declarative, so it trusts the project's own declaration rather than guessing from the files present; it completes the mechanism the previous release left as a follow-up.

Context: v1.32.0 (BACKLOG-583) wired the DSM_0.2.C §5.9 data-protection/compliance briefing's surfacing check into /dsm-go Step 2g — a soft, declarative session-start reminder (warns only when a project declares it handles personal data and has no briefing yet) that completes the mechanism the previous release (v1.31.0, §5.9) left as a deferred follow-up.
