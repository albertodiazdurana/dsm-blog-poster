# BL-031: Adapt the GE Epoch-5 multi-agent post for Take AI Bite

**Status:** Complete
**Priority:** Medium
**Date Opened:** 2026-08-05
**Date Completed:** 2026-08-06
**Target:** Review and publish in S34 (owner decision, 2026-08-05)
**Origin:** `_inbox/2026-07-06_dsm-graph-explorer_epoch5-multi-agent-blog-post.md`, pushed by the dsm-graph-explorer spoke on 2026-07-06. Routed to its own BL per `BL-029:116`, which classified it as an unrelated content thread that needed one.
**Author:** dsm-blog-poster S34

## Problem

A finished blog draft has been sitting in the inbox for a month with no work item
attached to it, which is the state that makes work invisible to `/dsm-go` and to
MEMORY at the same time. The draft exists at
`~/dsm-graph-explorer/dsm-docs/blog/epoch-5/2026-07-06-multi-agent-red-card.md`
(11,192 bytes, roughly 1,975 words, 7 sections) and has never been published
here: `content/blog/` contains no `multi-agent` or `red-card` bundle.

S33 already identified the routing (`BL-029:116`) and did not execute it, so the
notification survived a session boundary without becoming actionable. This BL is
the execution of that decision.

## What the post is

Working title: **How a Fleet of Agents Red-Carded My Own Decision**

Multi-agent orchestration used as a decision instrument, to make and then unmake
an engineering decision. GE's Sprint 17 committed to migrating its Intrinsic
table of contents (a "README for LLMs") from Markdown to TOON to save roughly 10%
of the tokens every agent pays to read it. A multi-agent adversarial assessment
(EXP-010: Fable-5 plus 9 Haiku gatherers, Opus-adjudicated) found the migration
pessimized tokens rather than saving them, and surfaced the deeper error, that
the north-star metric was a token proxy rather than agent navigation performance.
A pre-registered multi-agent A/B (EXP-011: 24 blind isolated subagents) then
validated the table of contents and red-carded TOON. Framed around the 2026 World
Cup.

Angle: methodology-as-instrument. Named beats: the metric-selection root error,
delegation economics, transcript-based verification (VAR), pre-registration, a
"why not RAG?" reflection, a Sprint-18 Leiden teaser, and honest caveats.

Supporting material in GE: `dsm-docs/blog/epoch-5/materials.md` (fact sheet and
source pointers) and `journal.md`.

## Approach

This is a **conversion**, not fresh drafting. The draft arrives already written
and reviewed upstream, so the four-gate chunked-drafting protocol collapses to
the shape S26 used for the portfolio series: confirm scope (Gate 1), convert one
pattern-setter section and get a convention check, batch the rest, then run a
full consistency pass. Re-running per-section drafting on already-approved prose
is wasted effort.

**Draft completeness is an open verification item, not a settled premise.** The
owner assesses the draft as "quite complete" (2026-08-05). That assessment has
not yet been checked against the full file, only against its opening and the
notification's summary. Verify it on the first complete read and say so plainly
if the draft turns out to need more than conversion.

## Checklist

- [x] Read the full GE draft plus `materials.md`; confirm or correct the
      completeness assessment before committing to a conversion-shaped plan
- [x] Decide the publication date (see Open decisions)
- [x] Create `content/blog/{date}-multi-agent-red-card/index.md` as a leaf bundle
- [x] Apply the TAB/DSM reader-facing convention: TAB owns the version and the
      brand; DSM survives only as file references. Grep the converted text for
      DSM as a standalone noun
- [x] Apply the "an AI" singular typography rule; grep for `AIs`
- [x] Punctuation rule: em dashes become `, ` (no space before the comma)
- [x] Check any figures or charts for internal labels that need a reader-facing
      bridge (S25 lesson; applies to visual assets, not only prose)
- [x] Repetition and dedup pass BEFORE `/humanizer` (BL-454 order; the humanizer
      never flags repetition, so running it first spends the pass on prose about
      to be cut)
- [x] `/humanizer` pre-publish gate. For already-humanized upstream prose this is
      an evidence-based grep audit rather than a rewrite; report the actual greps
- [x] Build locally WITHOUT `--buildFuture` and confirm the post's path is in the
      built output before merging
- [x] Publish, then verify the live page by grepping the rendered HTML for a
      specific new string, cache-busted with `?cb=$RANDOM`
- [x] Notify dsm-graph-explorer so it can move its `dsm-docs/blog/` source file
      to `done/` (cross-repo write; needs confirmation)
- [x] LinkedIn cross-post as the next Post N in `dsm-docs/blog/linkedin-posts.md`,
      leading with a DIFFERENT asset than the blog post's opener (S31 lesson)

## Open decisions

1. **Publication date and the temporal anchor. RESOLVED IN DIRECTION, 2026-08-05.**

   The owner's resolution: anchor the incident to the World Cup finals rather
   than to a relative interval. An event anchor survives a publication delay that
   "last week" cannot, so the date pressure largely disappears. This is a better
   fix than the one originally proposed here (rewrite the phrasing OR pick a date
   to make it true), because it removes the class of error instead of correcting
   one instance of it.

   **The anchor is an ADDITION, not an existing property of the draft.** Verified
   against the file rather than the notification: the draft contains **zero**
   occurrences of "World Cup". Line 7 reads "It's football season", a generic
   seasonal reference, and line 8 is the "Last week" interval. The football
   vocabulary IS pervasive and structural , the seven section headings are
   Kickoff / The bet / Scouting report / On the pitch / The verdict / On the bench
   / Injury time , but the metaphor is football-generic, not World-Cup-specific.

   The inbox notification's summary claims the post is "Framed around the 2026
   World Cup". That claim does not match the file. Recording the discrepancy
   rather than inheriting it, and flagging it as feedback-worthy to GE: a summary
   that overstates the framing would have sent a conversion straight past the one
   edit the opening actually needs.

   Work this implies, all in the opening two lines:
   - Replace "It's football season" with the World Cup finals anchor
   - Replace "Last week" with a phrase tied to that anchor rather than to now
   - Nothing downstream needs touching; lines 49 and 163 ("before the season
     starts", "Sprint 18") are metaphor-internal and version-internal respectively

   **Sub-question CLOSED 2026-08-05.** The owner released the constraint: the
   exact final date "is not important". Phrase the anchor without a hard date ,
   "during the World Cup final" or equivalent , and do not pin a calendar date in
   published prose. This also removes the need to verify the date against an
   external source, which was the only part of this decision the repo could not
   settle on its own.

   Deploy trap that still constrains the publication date whatever the anchor
   says: `hugo.toml` sets `buildFuture = false` and GitHub Actions builds in UTC,
   so a post dated the current LOCAL day is still future-dated until 00:00Z.
   Merging between local midnight and 02:00 CEST produces a green deploy of a site
   that silently omits the post.

   Relative-time drift is a known recurring class here (S24 "Last spring vs This
   spring", S25 "a year on" for a three-month gap), and both prior instances were
   caught by the author rather than the agent. This is the third, and again the
   author caught it.

2. **Front matter. RESOLVED 2026-08-05, superseding an earlier resolution the
   same day.** Category is **`Experiments`**, not GE's proposed `Technical` and
   not `Methodology`.

   The first resolution recorded here was `Methodology`, recommended and approved
   before the category listing had been checked. That listing shows `Experiments`
   already exists and holds exactly one post,
   `content/blog/2026-04-02-reachability-experiment/`, which is the OTHER
   graph-explorer experiment post (BL-013's). Shelving both GE experiment posts
   together wins on consistency, and GE's own proposed tag list already carried
   "Experiments". The owner re-decided once the fact was surfaced.

   Recording the supersession rather than overwriting it: the approval was
   downstream of a recommendation made without a fact, which is why the fact was
   re-surfaced instead of the earlier decision being left to stand.

   Remaining front matter as GE proposed it, still subject to the Gate-4 pass:
   `title: "How a Fleet of Agents Red-Carded My Own Decision"`,
   `slug: "multi-agent-red-card"`,
   `tags: ["Multi-Agent", "AI Collaboration", "Experiments", "Methodology"]`.
   The "Experiments" tag is now redundant with the category and should probably
   drop; the sibling post's tag list is worth comparing at Gate 4.

4. **Ecosystem framing. NEW, owner-supplied 2026-08-05.** The experiment was not
   GE-local curiosity. It aimed at a problem shared across **all Take AI Bite
   projects**: every session in every project needs the project map in context,
   and that map costs tokens every time it is read. TOON was chosen as an
   approach precisely because its reduced structure promised to cut that
   recurring, ecosystem-wide cost.

   This is the single most important addition to the draft, and it is not a
   copy edit. As written, the draft scopes the stakes to one repository ("Every
   agent that reads it pays for it, on every task, forever", line 32). The
   owner's framing lifts that to every project on every session, which is what
   makes the post belong on take-ai-bite rather than on a GE-internal blog. It
   also resolves the "zero mentions of Take AI Bite in 1,974 words" gap by
   supplying the actual reason the story matters here, rather than bolting a
   mention on.

   **Proposed placement (overrulable):** "The bet: buying tokens with a format",
   where the Intrinsic Table of Contents is introduced, not the Kickoff. The
   Kickoff's power is its specificity, one decision red-carded; front-loading an
   ecosystem-scale justification would dilute it. Widening on the second beat
   keeps the hook personal and makes the stakes land where the reader already
   understands what the map is.

   **Proposed degree of anchoring (overrulable):** name Take AI Bite once, at
   this point, and let the rest of the post stay in the first person about the
   project. Per the CLAUDE.md convention, "Take AI Bite" is the reader-facing
   name and DSM survives only as file references.

   **Open factual question, blocks this paragraph only:** is the project map
   currently deployed across TAB projects, or was ecosystem-wide adoption the
   goal at the time of the experiment? The paragraph must not imply the map
   already ships everywhere if it does not. This is the same
   naming-versus-shipping overclaim caught in the features post in S33 ("three
   places now carry it" for a principle that had only been named), and the
   distinction costs one clause to get right.

3. **Title claim.** "Red-Carded My Own Decision" is a metaphor rather than a
   capability claim, so the S29 "learned to X" overclaim rule does not bite. Kept
   here so the Gate-4 title-claim check has a recorded answer rather than being
   skipped.

3a. **TOON attribution. RESOLVED 2026-08-05.** The draft's "the TOON format
   silently drops the 'and 97 more' total that Markdown keeps" was queried as
   possibly describing this project's TOON generator rather than the format. The
   owner confirms it is the format's behaviour, established by the experiment's
   own results. The sentence stands as written; no hedge needed.

## Post-vs-source discrepancies found when DEC-010 was linked (2026-08-05)

Linking `DEC-010` made the post's claims about it checkable by any reader in
one click, so the record was read before the link went in. Three mismatches
between the post and the document. None is fixed; all are factual claims about
the author's own record.

1. **The artifact has two names.** The post calls it the "Intrinsic Table of
   Contents" throughout. DEC-010's title is "Migrate Knowledge-Summary Output to
   TOON". A reader who clicks lands on "Knowledge-Summary" and has to work out
   it is the same thing. Either they are the same artifact renamed between S48
   and now, in which case one sentence in the post can say so, or they are not,
   in which case the post is linking to the wrong record.

2. **The 10% figure is doing double duty.** The post uses 10% twice, once as
   the promise ("it promised to shave roughly 10% off the tokens") and once as
   the acceptance gate ("If TOON didn't cut token cost by at least 10% on a real
   corpus, the migration was off"). The record separates them: Central's research
   projected **14.6%**, and condition C3 required "≥10% measured savings (not
   projected)" as the kill switch. The gate figure is exact; the promise figure
   is not. Understating the promise is the conservative direction, but a reader
   who clicks sees 14.6% where the post said roughly 10%.

3. **"An amendment" is two.** The post says the record "now carries an amendment
   reversing it". It carries two: Amendment 1 (2026-07-03, S52) halted
   implementation after measuring **+1.74%** on the DSM Central corpus, tripping
   C3; Amendment 2 (2026-07-06, S53) formally abandoned the migration, citing
   EXP-011's finding that "markdown strictly dominates the current TOON".
   Singular is not wrong, since Amendment 2 does reverse it, but it undercounts.

Point 3 also supplies a number the post does not use: **+1.74%**. The post says
TOON "produced *more* tokens than the Markdown it replaced" without ever saying
how much more. The measured figure is available and specific.

**Link durability:** the URL is a `blob/master/...` branch link rather than a
commit permalink. Verified that `master` is the repo's actual default branch and
that the repo is PUBLIC. A branch link is the right choice here despite being
less durable than a SHA, because the record is live and carries amendments; a
permalink would freeze it at a revision that predates the reversal the post
describes.

## Outcomes

**Published:** https://take-ai-bite.com/blog/2026-07-06-multi-agent-red-card/
(`content/blog/2026-07-06-multi-agent-red-card/index.md`, category `Experiments`,
dated 2026-07-06 to DEC-010's last amendment, deployed 2026-08-05 and verified
cache-busted).

**Cross-post:** LinkedIn Post 25,
https://www.linkedin.com/posts/albertodiazdurana_multiagent-humanaicollaboration-claudecode-share-7491033806167265280-IonJ/

**GE notified (S35, 2026-08-06):**
`~/dsm-graph-explorer/_inbox/2026-08-06_dsm-blog-poster_epoch5-post-published.md`
(3,941 bytes, written against GE's own `_inbox/README.md` entry template). The
entry does two jobs rather than one: it requests the archive move, and it hands
back the three findings recorded above that GE cannot otherwise see , the World
Cup framing overstatement in GE's own outgoing summary, the three DEC-010
post-versus-source mismatches, and the unused +1.74% measurement. Sent before this
BL was closed, so a partial failure would have left the record under-claiming
rather than claiming a delivery that never happened.

**Open decision 4's factual question is resolved in the artifact.** The published
paragraph reads "the map was built here first, on its way to every project in my
Take AI Bite ecosystem, where the same briefing would be read at the start of
every session". Built here first / on its way to / would be read is intent, not
deployment, so the naming-versus-shipping overclaim the question guarded against
was avoided. Nothing was referred to GE on this point.

## Downstream Impact Map

None. This is a leaf content item: it settles no schema, vocabulary or shared
surface that a later BL builds on. Recorded explicitly rather than omitted, so
the absence reads as checked rather than forgotten.

## Related

- `BL-029` , v1.18.0-v1.19.0 release coverage. Line 116 routed this thread here.
  Independent of it; the two share only this session's time budget.
- `BL-013` , Reachability Experiment Blog Post, the other GE-sourced post, on
  hold pending technical clarifications. Different epoch, different thread.
- `BL-023` , LinkedIn hashtag research method. The cross-post from this BL is
  another slug data point.
