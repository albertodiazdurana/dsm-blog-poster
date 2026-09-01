### [2026-08-13] New features in DSM Central: punctuation scope, hook install fix, research labels

**Type:** Action Item
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

FEATURES.md was updated with new user-facing capabilities. Actions:
1. Update the feature blog to include the new F-entries
2. Write and post a dedicated blog about the new feature(s)

**New F-entries:**

- **F-152 (2026-08-13) The punctuation rule now says which files it governs (BL-505, DSM_0.2 §17.1)** — Writing conventions now apply where they are read: the em-dash-to-comma rule governs files that reach a public repository, and files that live only inside a private repo are exempt, as are gitignored files anywhere. For a project with a public mirror the governed set is whatever the mirror-sync manifest carries; for a project that is itself public it is every tracked file. The test is readership rather than whether a file is agent-consumed, because published methodology is read by agents too and that test exempts nothing. Exempt is not forbidden either, so a private file can still be tidied without the rule demanding it. Origin: a rule written for published prose had been quietly governing session transcripts and reasoning-lessons files, where nobody reads the punctuation and the cost is paid on every append.
- **F-151 (2026-08-12) Spoke hook installation stopped dropping two thirds of its work (BL-503, `/dsm-align`)** — Spoke hook installation now matches on the tool surface *and* the script, so the next alignment run on any spoke fills in registrations that earlier runs dropped. One script is deliberately registered against three different tool surfaces; the old check looked at the script name alone, so the first registration landed and the other two looked like duplicates and were discarded, including shell-command coverage added a week earlier that had therefore never reached a single spoke. The step reported success either way, so nothing distinguished a complete install from a third of one. Origin: found by a spoke while carrying out a previous release's instructions, not by looking for defects.
- **F-150 (2026-08-12) A research file's "confirmed" label can no longer outrun what was actually checked (BL-501, DSM_0.2 §10.1)** — A verification pass now records *which* sources it covered rather than only how many, and a status label may claim no more than that scope supports. "10 of 13 confirmed" does not say which 13, so a wrong citation sitting inside a "confirmed" list of 25 is unauditable in either direction. The rule arrives with a distinction worth more than the rule: a **log** records what a pass found and is never rewritten, an **index** asserts current status and is a defect when false. That single sentence answers "am I allowed to edit this artifact?", a question DSM had been resolving case by case. Origin: a research file labelled 25 sources confirmed over a pass that had covered 13, and the wrong pointer buried in the over-claim survived a pass built to catch exactly that.

**Context:**
F-150 and F-152 are the same instinct applied twice, that a claim should state
its own scope rather than leave a reader to assume it: one stops a research
file's "confirmed" label covering more sources than were checked, the other says
which files a writing rule governs. F-151 is unrelated, a spoke-install defect
that had been silently dropping two thirds of its registrations.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-08-19] New feature in DSM Central: three session-lifecycle capabilities in v1.21.2

**Type:** Action Item
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

FEATURES.md was updated with new user-facing capabilities. Actions:
1. Update the feature blog to include the new F-entries
2. Write and post a dedicated blog about the new feature(s)

**New F-entries:**

- **F-155 (2026-08-19) Session analysis picks a subject that has not been analysed yet (BL-509, `/dsm-staa`)** — Subject selection now asks how many candidate transcripts are still unanalysed and acts on the answer: none halts and changes nothing, one becomes the default, two asks which. The previous behaviour picked the latest archived transcript and warned when that was probably the wrong one, and the warning was overridden on six consecutive runs, because the window it flagged turned out to be the normal shape of the workflow rather than an edge case. A default taken zero times out of six is the wrong default. The halt also reports the values that produced it, so a refusal to run can be diagnosed in one read instead of arriving as a bare "nothing to analyse". Origin: a run in which both candidate subjects had already been analysed, where following the step literally would have appended duplicate lessons and overwritten the record of the last real pass with a record of a null one.
- **F-154 (2026-08-19) The punctuation rule follows the reader rather than the repository (BL-513, DSM_0.2 §17.1)** — Writing conventions now govern any file that reaches a reader outside the project, by any channel, with publication to a public repository named as the most common instance rather than as the definition. A document sent as an attachment has an outside reader and is governed exactly as a published page is. The revision also says when not to apply the rule mechanically, which nothing in the corpus had said before. An em dash joining two independent clauses wants a period or a semicolon, because a comma there produces a splice. And an em dash separating a numeric range must never become a comma: in a decimal-comma locale the range silently turns into a decimal, and the result still reads as plausible prose. Origin: a rule whose stated test was readership had been implemented as repository visibility, so a private project's CVs and cover letters, the documents that most need the convention, were the ones it exempted.
- **F-153 (2026-08-19) Handoffs are read before they are filed away (BL-511, `/dsm-go`)** — A handoff left by the previous session is now read in full at session start, its pending items surfaced in the boot report and labelled by source alongside the checkpoint's, and only then archived. Where the two sources disagree about what comes next, the disagreement is shown rather than quietly resolved in favour of one. The report also distinguishes a handoff that was read from one that was merely filed, which used to produce identical lines. Origin: the step opened by asserting that any handoff predating the session had already been consumed, which stated an assumption as fact and made the archiving look successful every time. Handoffs are written only when pending work is complex enough to need them, so the sessions that most needed the context were the ones losing it.

**Context:**

All three land in the session-start and writing-convention layer: a handoff written for the next
session is now read before it is archived rather than filed unread, session-transcript analysis
refuses to re-analyse a subject it has already covered, and the punctuation rule's scope follows
the reader rather than the repository so documents leaving as attachments are governed too.

**Meta-pattern worth a blog angle:** all three originated as defects found by SPOKE projects
carrying out a previous release's instructions, not by the hub that wrote them. That is the third
consecutive release with that provenance.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-08-21] New features in DSM Central: seven unnotified F-entries across v1.20.0 to v1.23.0

**Type:** Action Item
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

FEATURES.md was updated with new user-facing capabilities. Actions:
1. Update the feature blog to include the new F-entries
2. Write and post a dedicated blog about the new feature(s)

**Note on scope, please read before treating this as a routine entry.** This covers
**four** releases, not one, and the backlog was found rather than remembered. DSM
Central's wrap-up record said two entries were owed. Comparing this inbox file
against FEATURES.md raised that to four. Comparing against this file **plus
`_inbox/done/`** raised it to seven: the archived entries stop at F-146 and this
file starts at F-150, so F-147, F-148 and F-149 fell in the gap between a rolling
archive and its successor and were never sent at all. F-150 to F-155 did arrive
normally, so this is a patchy record rather than a clean cutoff, and any future
reconciliation should compare against both locations.

Dated 2026-08-21 because that is when it was written. Every F-entry below is dated
earlier, between 2026-08-05 and 2026-08-20.

**New F-entries, grouped by release:**

**v1.20.0 and v1.21.0, never notified:**

- **F-149 (2026-08-05) Concurrent-session liveness verdict instead of an impression (BL-487, DSM_0.2.A §26)** — When a session start finds another session's lockfile, it now probes whether that session's process is actually running and reports `LIVE`, `STALE`, or `UNKNOWN`, rather than leaving the agent to guess from how long ago the transcript was written. `UNKNOWN` is a real answer, not a failure: a lock that cannot be probed is not an absent one, and the age signal stays a hint, never a verdict. The probe informs the choice and never makes it, the halt still stops and asks in all three states, and a `STALE` reading does not pre-select "force". Origin: a session that halted on a live sibling's lock, read it as stale, and continued, producing interleaved transcripts and five duplicated reasoning entries.
- **F-148 (2026-08-05) Cross-repo write guard covers shell file operations (BL-484, DSM_0.2.C)** — The rule against writing outside the repo without confirmation was stated tool-agnostically but enforced on two tools only, so every `cp`, `mv`, `>`, `>>`, `tee` and `rsync` reached any path with nothing in the way. Shell commands now reach the guard too. It warns rather than blocks, on purpose: a shell command's write targets have to be inferred from the text, and a gate that blocks on a guess fires on ordinary work and teaches you to dismiss it, which is worse than no gate because a dismissed gate still looks like protection. The documentation now states what the check does and does not see, so it reads as a floor rather than a guarantee. Origin: a spoke lost 181 reasoning-lesson entries to a single redirect and got them back from git by luck of timing.
- **F-147 (2026-08-05) Published snippets are run before they ship (BL-485, DSM_0.2 §19.1)** — A command published inside a skill file is a claim about two things it never states: what its input looks like and what environment it runs in. Neither is checked when it is written, so the rule now requires running it against the real file, in the real harness, before the change merges, and capturing the output as evidence. It asks a second question beyond "did it work": would a wrong result have looked any different from a right one. The trigger covers prose specifications as well as fenced code, because one of the two defects that motivated the rule lived entirely in a sentence and never sat inside a code block. The rule's own acceptance test caught that gap: it walks both original defects through the draft and fails if either slips past. Origin: two such defects were live at once, both reported by spoke projects rather than by the hub that wrote them, and both reproduced at the boot of the session that fixed them.

**v1.22.0, never notified:**

- **F-157 (2026-08-20) The boot no longer claims to have read a file it only partly read (BL-491, `/dsm-go`, DSM_0.2.A §8.1)** — The reasoning-lessons mirror read at every session start was governed by two size caps that could not work: one advertised a limit the file exceeded roughly thirteen times without anything noticing, the other was arithmetically impossible to exceed and so reported healthy no matter how large the file grew. There is now a single bound, derived from two independent measurements that agree within 1.7%, and a breach reports the measured size against it instead of passing in silence. The behavioural half matters more than the number: when the file no longer fits one read, the session says so and states what it read instead, where before a partial read and a complete one produced identical reports.
- **F-156 (2026-08-20) A command that fails is no longer able to report success (BL-515, DSM_0.2 §19.2)** — Piping a command into something like `tail` or `wc` and then testing the result checks the wrong command, because a pipeline reports on its last step rather than the one you care about. A failing push could print "pushed" and a failed search could look like a clean result. The rule now names both directions this fails in, gives three verified ways to check the command you actually ran, and rules out the shortcut that caused it.

**v1.23.0, never notified:**

- **F-159 (2026-08-20) Slash commands reach every project, not just the one that ships them (BL-518, `sync-commands.sh`)** — Five commands were being installed to a folder only the hub could see, so every other project quietly loaded a copy that nothing had written in four months. The visible cost was not staleness in the abstract: the backlog command those projects loaded was missing both the risk section and the test-results section the methodology requires, so items filed through it broke the very rules meant to make them auditable, while the agent believed it had followed the skill. The drift checker reported everything healthy the whole time, truthfully, because it compared each command against the folder it was sent to rather than the folder a project reads from. All commands now install to one place, the checker reports leftover copies that would shadow them, and the mirror manifest carries the five it was missing so a mirror clone cannot reproduce the same gap.
- **F-158 (2026-08-20) A pull request can no longer be opened from a branch that is missing your latest commit (BL-516, DSM_0.2 §20.4)** — A pull request is built from the branch as it exists on the server, so a commit made after the last push is absent from the request, absent from the merge, and destroyed when the merge deletes the branch holding the only copy. Every step reports success. The rule now requires confirming there is nothing unpushed before a request is opened or merged, and halting with the missing commits named rather than pushing them silently, since an unpushed commit at that moment usually means the branch is not in the state its author thinks. The rule also records why the obvious remedy is the wrong one: git already refuses to delete a branch holding work that is not merged, and the request-merging tool bypasses that refusal, so the check has to happen before the tool runs and can never rely on it declining.

**Context:**

Seven entries, one shape. Each fixes a check, guard, or report that asserted more than it had
established. A pipeline reported on `tail` instead of the push that had been rejected. A boot
reported a full read of a file it had only partly read. A drift checker reported twenty of
twenty healthy while comparing each command against the wrong folder. A pull request was built
from a branch state missing the commit its author had just made. A liveness probe returned an
impression dressed as a verdict. A cross-repo write guard covered the write tools and not the
shell. And a snippet published inside a skill file was a claim about its own input and
environment that nobody had ever run.

**Meta-pattern worth a blog angle.** The interesting half is not that these checks were wrong.
It is that **a wrong result was indistinguishable from a right one**, so nothing surfaced them
for months. That is now a written rule: DSM_0.2 §19.1 asks of any published check not merely
"does it work on real input" but "would a wrong result look different from a right one". F-147
is the entry where that rule landed, which makes this set unusually self-referential , the
rule and the defects it describes shipped alongside each other.

**A second angle, smaller and sharper.** §19.2, the rule about pipeline exit status, was
breached by its own author within an hour of shipping it. That is recorded inside the section
rather than quietly fixed, and it is why the rule carries a display carve-out clause it would
not otherwise have.

**A third, which is really about this entry.** The notification backlog itself is an instance
of the pattern. Every session's record said the debt was smaller than it was, and each said so
truthfully about the slice it had checked. Three successive widenings, from two to four to
seven, each came from comparing against a wider piece of the actual source instead of against
the previous session's summary.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-08-21] New features in DSM Central: v1.24.0, five checks that now read what they were guarding

**Type:** Action Item
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

FEATURES.md was updated with new user-facing capabilities. Actions:
1. Update the feature blog to include the new F-entries
2. Write and post a dedicated blog about the new feature(s)

**New F-entries:**

- **F-164 (2026-08-21) Two sprint-closure checklist items you could never honestly tick (BL-521, DSM_2.0.C Template 8)** — Sprint closure is gated on a nine-item checklist, and two items named files nothing ever created, failing in opposite directions. One carried an escape clause true forever of a project that will never record smoke tests, so it could be ticked truthfully without the file existing and the check could never fire. The other named a blog publication tracker that no scaffolding step produced, so it could not be ticked truthfully at all. Both leave a closure record whose ticks do not mean what they appear to. The waiver is now scoped to the kind of project it applies to, matching how the neighbouring item already worked, and the tracker is created on scaffolding with a note that an empty table means nothing has been published, which is different from the file being absent. The audit this prompted found a third: the phase checklist pointed at a feedback file the alignment command itself asks projects to migrate away from.
- **F-163 (2026-08-21) Approving six agents can no longer run eleven (BL-524, DSM_0.2 §8.9.2)** — The cost gate asks for consent before a task fans out into many parallel model calls, and it priced that consent on the number of agents launched directly. Nothing stopped one of those agents from launching a fan-out of its own, and a six-agent approval was observed running eleven. Agents spawned inside an approved fan-out now have no authority to delegate further unless the approval said so, and where it does, the disclosed number is the ceiling on the total rather than the first level. The gate's trigger also excluded the very mitigation the gate recommends: it asked whether the calls draw on the same budget as your main thread, while advising you to move them to a cheaper one that has its own. What makes a fan-out risky is many calls competing for one exhaustible budget, and running out of the cheap one stops the work exactly as hard.
- **F-162 (2026-08-21) Guides that tell you when they do not apply to you (BL-522, `dsm-docs/guides/`)** — Some hard-won lessons are a landmine under one specific setup and pure noise everywhere else, and there was nowhere to put them: written as general advice they get applied where they do not belong, left unwritten they get rediscovered the expensive way. Guides now have an index, and a guide may open by naming the conditions that must all hold, with an explicit instruction to stop reading if they do not. Each condition has to be checkable without reading the guide, since a condition you can only evaluate by reading the thing defeats the point of gating it. The first one covers a credential that is read once when the editor starts, silently forwards its own placeholder text as your API key when unset, and reports the server healthy because the health check never authenticates.
- **F-161 (2026-08-21) A missed notification is no longer missed forever (BL-530, `/dsm-go`)** — Notifying the blog project of new features was computed from what changed in the current session, so an entry the session failed to send stopped being a candidate the moment the session ended. Three ordinary endings skip that send. Session start now compares the feature list against what the recipient has actually received and reports the gap, which is the only moment that can catch the *previous* session's omission. Two details came from running it rather than reasoning about it: a feature counts as delivered only when quoted in full, because matching bare numbers read the sentence "past entries (F-001 to F-086) are populated lazily" as eighty-six deliveries; and the starting point is derived from the recipient's own history rather than fixed, because the real record was patchy rather than simply behind; three entries were missing beneath six that had arrived.
- **F-160 (2026-08-21) The transcript now notices when a timestamp is wrong (BL-517, DSM_0.2 §7)** — Four checks guarded how reasoning-log entries are appended and none of them read the time the entry claims. Three sessions logged timestamps off by as much as thirteen hours, one recording a decision as authorised forty minutes after the action it authorised had already happened, and every check passed. The clock is now compared against the stamp and a drift is flagged. It warns rather than refusing the write, deliberately: the other checks guard against damaging the file, while a wrong timestamp only mislabels an entry, and blocking the write would stall the very logging the check exists to protect. Retroactive entries get no exemption, because they are required to carry the current time in the first place.

**Context:**

v1.24.0, six backlog items. The through-line is narrower and more interesting than the last
batch: in four of the five, a guard existed and was running, and it was reading the wrong
thing. Four checks validated how a transcript entry is appended and none read the time the
entry claims, so three sessions logged drift of up to thirteen hours and every check passed. A
cost gate counted the agents you launch directly and not the ones they launch. A closure
checklist asked for files nothing created. A notification was computed from what changed this
session, so anything missed stopped being a candidate the moment the session ended.

**Meta-pattern worth a blog angle.** The previous batch was about checks whose failures looked
like successes. This one is a level up: **checks that were looking at the wrong object
entirely** and therefore could not fail. That distinction is worth drawing out, because the
remedies differ , the first family needs a louder signal, the second needs someone to ask what
the check is actually reading.

**A second angle, on how two of these were decided.** The transcript check ships as a warning
rather than a block, and the reasoning is in the methodology rather than only in the commit:
the other checks guard against damaging the file, while a wrong timestamp only mislabels an
entry, and blocking the write would stall the logging the check exists to protect. The same
session found that a proposed 10-minute tolerance rested on a premise a later incident had
already falsified. Both are small examples of a rule's *rationale* being the load-bearing part.

**Source file:** `~/dsm-agentic-ai-data-science-methodology/FEATURES.md`

### [2026-08-25] New features in DSM Central: artifact coherence, delegated-result checks, a project-plan tier

**Type:** Action Item
**Priority:** Medium
**Source:** dsm-agentic-ai-data-science-methodology

FEATURES.md was updated with new user-facing capabilities. Actions:
1. Update the feature blog to include the new F-entries
2. Write and post a dedicated blog about the new feature(s)

**New F-entries:**

- **F-170 (2026-08-25) Checking that a change left its document coherent, not just that the change worked (BL-531, DSM_0.2 §21.4)** — Every testing rule in the methodology is scoped to one backlog item: does this change do what it said, were its own conditions met, did its branch pass. All of them can pass while the document the change landed in is left contradicting itself, and nothing asked the wider question. A change now also sweeps for every phrase it removed or renamed and reads each surviving mention, on the understanding that most of them are legitimate , a historical note and a stale pointer look identical to a search, so a hit is a candidate and never a verdict. Three things a search cannot check are asked in prose instead: that references still point at something real, that any number the document states about itself is recomputed rather than carried forward, and that the edited file is actually carried by whatever distributes it. The check reports rather than blocking, and it stays silent on changes that renamed nothing, which is what keeps it from becoming the kind of warning people learn to click past. Origin: six items shipped in one session, someone asked whether they had interfered with each other, and the answer was no , but nothing had required anyone to look, and the audit that ran only because it was requested found a real defect.
- **F-169 (2026-08-25) A research run that reports success can still hand back an empty answer (BL-520, DSM_0.2 §19.3)** — A background research job completed five lines of enquiry across nineteen sources, checked seventy claims, ran a hundred and one assistants and spent roughly three million words of processing, then returned a summary reading "test" and a single finding reading "test claim". Every progress signal was real and every one of them said the work had gone fine. The genuine findings existed only in the individual assistants' own logs and were recovered by hand. Nothing had checked whether the answer that came back was proportionate to the work that produced it. That comparison now happens before the result is used, measured against the run's own reported effort rather than against any fixed minimum, so a small job that honestly returns a small answer is not flagged. When the result does look hollow, there is an ordered recovery path whose first two steps cost nothing, because the expensive work has already been done and paying for it twice is the reflex worth preventing.
- **F-168 (2026-08-25) A home for projects that arrive with the planning already done (BL-519, DSM_2.0.C Template 13)** — Planning templates covered sprints, phases, days and checkpoints, and stopped there. A project that turns up with a finished specification , a client's build document, a statement of work, a research protocol , had no canonical place to put the whole-project view, so the natural move was to re-describe the supplied plan as a second plan, leaving two descriptions of the same ladder to drift apart. There is now a project-level template that points at the source rather than copying it, with one table where a milestone becomes actual work. The filename is settled too: the conventions document said one spelling, the only real example in the wild used another, neither was binding, and a third project would have invented a third. The template changed during its own testing, because tracing the one real example found that it *supersedes* its source rather than deferring to it, which contradicted the draft's central rule and revealed a case the draft had missed.
- **F-167 (2026-08-25) The guard against writing outside the project now follows the command's own directory (BL-532, `validate-cross-repo-write.sh`)** — Writing to a file outside the current project needs your explicit confirmation. The check worked out where a write would land by resolving the path against the project folder, but a shell command can change directory first, and then the same relative path means somewhere else entirely. A command that stepped outside and wrote a file was judged to be writing inside, and passed without asking. It now resolves the path the way the command itself would. The way this was tested is worth knowing: proving it required a write outside the project, which is exactly the thing that needs permission, and the obvious safe location was one the guard deliberately ignores, so a pass there would have been indistinguishable from the bug. Because the check inspects the command before anything runs, a command aimed at a directory that does not exist fails immediately, writes nothing anywhere, and still gets fully evaluated. The test needed the offence described, not committed.
- **F-166 (2026-08-25) Feedback review stopped looking for filenames nobody writes any more (BL-533, `/dsm-review-feedback`)** — The command that gathers a project's feedback searched for an older filename shape, while every active project had moved to a dated per-session one. It reliably found nothing and reported that as an empty result rather than as a mismatch. It now reads both shapes, and six documents that had drifted into disagreeing about which shape is current were reconciled, including a ruling on when an older name is genuinely legacy and when it is a documented and still-valid form. Two claims in the original report turned out to be wrong and are recorded rather than quietly dropped. The search that established the scope was also wrong the first time: it had been narrowed to the folder where these files usually live, and re-running it without that restriction found nearly twice as many places , including the instruction template a person copies to invoke the very command being repaired.
- **F-165 (2026-08-25) A safety net that had never once caught anything (BL-535, `/dsm-wrap-up`)** — Wrap-up checks for a leftover open pull request that would collide with the one it is about to create. The check asked for branches named with a prefix, but the underlying option matches a branch name exactly, so it matched nothing and the net had never fired in the entire life of the step. The failure hid in the most durable way available: six consecutive sessions believed the check was catching two deliberately retained pull requests and worked around it on that basis, and every uneventful session reinforced the belief. Nothing had ever collided. The check now filters correctly and distinguishes three outcomes instead of silently reporting none, and it was verified against a case created on purpose to trigger it , a check that can only ever say "nothing found" proves nothing about whether it can find something.
