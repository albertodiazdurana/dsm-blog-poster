# BL-034: DSM v1.26.4 to v1.26.6 release coverage

**Status:** OPEN
**Priority:** Medium
**Date Opened:** 2026-10-02
**Author:** Alberto (S39)
**Origin:** S39 Stage 0. `/dsm-go` Step 1.8 reported last-align 1.26.3 against CHANGELOG 1.26.6 at boot; `/dsm-align` ran 1.26.3 → 1.26.6. Three inbox notifications from Central (2026-09-30 v1.26.4, 2026-10-01 v1.26.5, 2026-10-02 v1.26.6) were processed S39.

## Scope, and why it starts at v1.26.4

**BL-033 owns v1.20.0 through v1.26.3** (closed S38). **BL-029 owns v1.18.0 to v1.19.0 and is still open**, blocked at Gate 1 on the thesis, not on drafting. This BL covers only the unowned range and does not absorb either neighbour.

Range: **v1.26.4 (2026-09-30) through v1.26.6 (2026-10-02)**, three releases, four F-entries.

## Problem, with deltas measured 2026-10-02

| Artifact | Claims | Gate | Delta |
|---|---|---|---|
| `content/blog/2026-03-20-dsm-features-three-dimensions/index.md` | 176 features | `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` = **180** | **4 behind** |
| `content/about.md` | The Fourteen Principles | `grep -cE '^### 1\.[0-9]+'` = **14** | none |

**The principle check was run on heading TEXT, not just the count.** None of F-176..F-179 is a new DSM_6.0 §1.x principle (F-176 is DSM_0.2.C §5.7 methodology; F-177 touches DSM_0.2.A §8; F-178/F-179 are memory/wrap-up tooling). about.md's "The Fourteen Principles" heading + 14 numbered items still match. Front C is a no-op this cycle. Recording the method so the next cycle does not re-establish that the check was real.

**The counting convention (S37, carried):** the canonical gate `grep -cE '^- \*\*F-[0-9]+' FEATURES.md` EQUALS FEATURES.md's own `**Current count:**` line (both 180 on 2026-10-02). No +1 F-000 discrepancy. The post tracks the gate; re-run it at edit time since it moves whenever Central ships.

## The four F-entries (verbatim-sourced from the Central notifications)

- **F-176 (v1.26.4, 2026-09-30)** , No project name reaches the public mirror, and the rule that guarantees it is now methodology (BACKLOG-560, DSM_0.2.C §5.7). The public methodology carried specific project/client/spoke names in its provenance lines , a confidentiality exposure, and to an outside reader a pointer that resolves to nothing. Every such name is reworded to a project-agnostic form that keeps the session and backlog id. The standing rule (no specific project name reaches the public mirror; removal + prevention; a slug smuggled back as a generic descriptor still counts as a violation) is written into the methodology. Framed honestly: the scanner is a backstop and operator review is the last gate , bounded to the public surface, not a claim of technical impossibility.

- **F-177 (v1.26.5, 2026-10-01)** , The reasoning-lessons primer gains a flow control so its two size targets can both hold (BACKLOG-495, DSM_0.2.A §8). The curated lessons an agent is primed with had a target entry count and a target byte size that contradicted each other at the length entries were actually written. The missing piece was a per-entry length limit: each entry now targets ~600 characters (where count and byte targets align), and an over-length entry is shortened or split rather than dropped. A long-standing practice becomes a rule: ecosystem-wide lessons at the hub go to the shared aggregation file, not also into the always-loaded primer.

- **F-178 (v1.26.5, 2026-10-01)** , Session memory ages itself down a three-tier chain so the always-loaded file stays small (BACKLOG-544, `/dsm-memory-decommission`, `/dsm-memory-archive`). Two move-only skills age the file read in full every turn: the oldest session's notes move from the always-loaded file to an on-demand long-term file once the session zone passes a size threshold, and from there to a deepest archive once the long-term file passes its own. They run at wrap-up, move a whole session's notes at a time, never touch the permanent zone, back up before writing, and verify nothing was lost. The threshold watches the session zone, not the whole file.

- **F-179 (v1.26.6, 2026-10-02)** , The always-loaded memory file's permanent zone now gets a size-review flag so it stops growing unchecked (BACKLOG-568, `/dsm-wrap-up`). Once tiering (F-178) drains the session zone, the permanent (evergreen) zone is the larger and only-growing half of the always-loaded cost. Wrap-up now measures it and, when it passes a soft ~6 KB target, raises a non-blocking flag recommending a review (trim resolved lines, or move durable-but-not-boot-critical lines somewhere less costly and remove them , moved before removed, never silently dropped). The flag only recommends; a person or the deeper analysis pass does the trimming.

**Narrative clustering (for Stage 3):** F-177 / F-178 / F-179 form one coherent cluster , "keep the always-loaded context lean" (lessons primer ceiling, session-zone tiering, evergreen-zone flag), a story about DSM managing its own context-window cost. F-176 is a separate confidentiality theme (project-agnostic public mirror by construction). Decide at Stage 3 Gate 1 whether F-176 is a bonus beat or omitted from the release post.

**Dogfooding note:** F-178 and F-179 directly target this project's own flagged state (MEMORY.md 20.6 KB; reasoning-lessons mirror 1.46x over the §8.1 bound, BL-030). The tooling lands via the owed mirror sync + `sync-commands.sh --deploy`.

## Stage checklist (per CLAUDE.md DSM Version Release Coverage)

- [x] **Stage 0 , Detect.** Range named, deltas measured, notifications located and read (S39).
- [x] **Stage 1 , Open the BL.** This file. Deltas recorded above.
- [x] **Stage 2 , Factual updates** (shipped S39). **Front B PUBLISHED live** 2026-10-02 at https://take-ai-bite.com/blog/2026-03-20-dsm-features-three-dimensions/ via PR #72 (merge commit), deploy run 37060927815 success (build 12s, deploy 9s, healthy baseline); verified live cache-busted: "180 features" x11, 0 stale "176", age:0, all 4 weave phrases serving.
  - [x] Front B , features post 176 → 180. **Drafted + Gate 4 clean** (S39). Wove F-176 into Knowledge provenance (public mirror project-agnostic by construction, §5.7, backstop-not-proof framing); F-178+F-179 into Experience accumulation / Memory and context (the always-loaded file ages itself: session-zone tier-down + evergreen-zone review flag); F-177 into Experience accumulation / Reasoning extraction (per-entry ~600-char ceiling resolving the count-vs-byte contradiction). Count updated in all 4 places. Gate 4: dedup pass (3 fixes: "read in full" echo, F-177 cap re-naming, "pointer to nothing"->"dead end") then /humanizer (artifact grep clean, 6 earned contrast constructions within the author's established range per lesson #101, 1 grammar fix). Local Hugo build verified (180 serves x11, 0 stale 176). +~230 words (4392->~4620). PUBLISH status recorded at Stage 2 close below.
  - [x] Front C , About page. **No change needed, verified S39** on heading TEXT not count: DSM_6.0 has 14 §1.x headings; `content/about.md` heading "The Fourteen Principles" + 14 numbered items match. None of F-176..F-179 is a new §1.x principle (F-176 §5.7, F-177 §8, F-178/F-179 memory/wrap-up tooling). No same-slot swap. Recorded, not edited.
  - [x] Front F , portfolio inbox notification sent S39 to `~/dsm-data-science-portfolio-working-folder/_inbox/2026-10-02_dsm-blog-poster_dsm-v1.26.6-release.md` (Low priority, informational: 176->180 features, 14 principles unchanged).
- [ ] **Stage 3 , Release post (Front A).** Pending. Candidate theme: the context-lean cluster (F-177/178/179); F-176 decision at Gate 1. Must differ from BL-033's "structural fix" frame and BL-029's pending thesis.
- [ ] **Stage 4 , LinkedIn cross-post (Front E) + record (Front D).** Pending.
- [ ] **Stage 5 , Close.** Pending.

## Acceptance criteria

- [x] All three inbox notifications read and moved to `_inbox/done/YYYY-MM-DD_{source}.md` per the dated-archive convention (S39)
- [x] Features post count reconciled against the gate at the time of the edit (gate = 180 at edit time, 2026-10-02; matches FEATURES.md Current count line)
- [ ] Stage gates marked complete or deferred in this file
