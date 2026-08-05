# BL-031: Adapt the GE Epoch-5 multi-agent post for Take AI Bite

**Status:** Open
**Priority:** Medium
**Date Opened:** 2026-08-05
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

- [ ] Read the full GE draft plus `materials.md`; confirm or correct the
      completeness assessment before committing to a conversion-shaped plan
- [ ] Decide the publication date (see Open decisions)
- [ ] Create `content/blog/{date}-multi-agent-red-card/index.md` as a leaf bundle
- [ ] Apply the TAB/DSM reader-facing convention: TAB owns the version and the
      brand; DSM survives only as file references. Grep the converted text for
      DSM as a standalone noun
- [ ] Apply the "an AI" singular typography rule; grep for `AIs`
- [ ] Punctuation rule: em dashes become `, ` (no space before the comma)
- [ ] Check any figures or charts for internal labels that need a reader-facing
      bridge (S25 lesson; applies to visual assets, not only prose)
- [ ] Repetition and dedup pass BEFORE `/humanizer` (BL-454 order; the humanizer
      never flags repetition, so running it first spends the pass on prose about
      to be cut)
- [ ] `/humanizer` pre-publish gate. For already-humanized upstream prose this is
      an evidence-based grep audit rather than a rewrite; report the actual greps
- [ ] Build locally WITHOUT `--buildFuture` and confirm the post's path is in the
      built output before merging
- [ ] Publish, then verify the live page by grepping the rendered HTML for a
      specific new string, cache-busted with `?cb=$RANDOM`
- [ ] Notify dsm-graph-explorer so it can move its `dsm-docs/blog/` source file
      to `done/` (cross-repo write; needs confirmation)
- [ ] LinkedIn cross-post as the next Post N in `dsm-docs/blog/linkedin-posts.md`,
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

   **Open sub-question:** the actual date of the 2026 World Cup final is not
   verifiable from inside this repo, and the owner's "a few weeks ago" is the only
   evidence on hand. Do not invent a date in published prose. Either phrase the
   anchor without a hard date ("during the World Cup final") or confirm the date
   before drafting.

   Deploy trap that still constrains the publication date whatever the anchor
   says: `hugo.toml` sets `buildFuture = false` and GitHub Actions builds in UTC,
   so a post dated the current LOCAL day is still future-dated until 00:00Z.
   Merging between local midnight and 02:00 CEST produces a green deploy of a site
   that silently omits the post.

   Relative-time drift is a known recurring class here (S24 "Last spring vs This
   spring", S25 "a year on" for a three-month gap), and both prior instances were
   caught by the author rather than the agent. This is the third, and again the
   author caught it.

2. **Front matter.** GE proposed `title: "How a Fleet of Agents Red-Carded My
   Own Decision"`, `slug: "multi-agent-red-card"`, `categories: ["Technical"]`,
   `tags: ["Multi-Agent", "AI Collaboration", "Experiments", "Methodology"]`.
   Recorded as PROPOSED, not locked. The category in particular is worth a look:
   the post's own angle is methodology-as-instrument, which may fit "Methodology"
   better than "Technical".

3. **Title claim.** "Red-Carded My Own Decision" is a metaphor rather than a
   capability claim, so the S29 "learned to X" overclaim rule does not bite. Kept
   here so the Gate-4 title-claim check has a recorded answer rather than being
   skipped.

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
