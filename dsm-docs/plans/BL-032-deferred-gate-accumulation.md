# BL-032: A mandatory gate can be deferred to death by individually correct decisions

**Status:** Open
**Priority:** High
**Date Opened:** 2026-09-16
**Origin:** S36 (2026-09-01/02). LinkedIn Post 26 was published without the `/humanizer` pre-publish gate ever running. No single decision in that sequence was wrong.

## Problem

CLAUDE.md states the humanizer gate in unambiguous terms: "Run `/humanizer` on all material produced and posted by this project... This is a pre-publish gate, not optional."

It did not run before Post 26 was published. The sequence:

| Turn | Event | Deferral reason | Correct at the time? |
|---|---|---|---|
| 1 | Post 26 v1 drafted | BL-454: do not spend the pass on prose about to be rewritten | Yes |
| 2 | Author rejects the frame, v2 drafted | Same | Yes |
| 3 | Author asks for five additions, v3 drafted | Same | Yes |
| 4 | Author publishes | , | , |

BL-454's ordering rule is correct and was correctly applied three times. The gate was
never refused, never forgotten, and never argued down. It was deferred, each time on
sound grounds, until the author published and the last moment at which it could run
had passed.

**The defect is not a judgement error.** Re-running the decision at any of turns 1
through 3 with full information produces the same deferral, because at each of those
moments the prose genuinely was about to be rewritten. The defect is that nothing in
the workflow tracks that a mandatory gate has been deferred, or notices when the
deferral count crosses the point where the gate can still discharge its purpose.

**Why this is not covered by existing rules.** The flag-inefficacy lesson (S33) covers
a flag repeated without action, and its remedy is to convert the flag into an owned
work item. That does not apply: a deferral is not a flag, it carries a stated reason
and an implicit "later", and each one was discharged correctly by the next draft. The
S24 do-not-advance-the-marker lesson covers drift that was offered and not applied,
which also does not apply, because nothing was offered and declined.

## What makes this recurrent rather than a one-off

The preconditions are ordinary, not exotic:

1. A gate whose correct position is **last** (Gate 4, pre-publish, post-repetition-pass).
2. A legitimate ordering rule that says **not yet** while the artifact is in flight.
3. An artifact that stays in flight across several turns.
4. A publication trigger the agent does not control, in this case the author posting.

Condition 4 is the one that converts the other three into a miss. Every cross-post in
this project has it, because the author publishes to LinkedIn by hand. The same shape
exists for any blog post the author deploys himself.

## Candidate resolutions

Not yet decided; this BL exists to hold the decision, not to pre-empt it.

- **A. Deferral ledger.** When a mandatory gate is deferred, record it, and surface the
  open deferrals in every subsequent turn's output until discharged. Cheap, visible,
  and puts the count in front of the author as well as the agent.
- **B. Last-responsible-moment rule.** Name the trigger that closes the window (here:
  "the author is about to publish") and require the gate to run at the turn where the
  artifact is presented as final, regardless of whether further revision is expected.
- **C. Run-early-and-again.** Drop BL-454's deferral for gates that are cheap on short
  artifacts. Costs a wasted pass per revision; buys the guarantee. Probably wrong for
  long-form, possibly right for a 350-word cross-post.
- **D. Accept and detect.** Leave the ordering rule alone and add a post-publication
  check that reports the gate as missed, which is what happened here manually.

Option B is the most likely fit, because it preserves BL-454's reasoning and closes the
window at the one moment the agent can still observe.

## What was actually done in S36

The pass ran late, against the published text rather than the draft, and found nothing
actionable: 392 words, 0 em dashes, 0 "AIs" plural, 0 space-before-comma, 0 standalone
DSM, 0 boldface; two matches, both the author's own choices or platform normalisation
(a `👉` emoji marker, and curly quotes LinkedIn substituted for the source's straight
ones).

**A clean late pass is not a mitigation and must not be recorded as one.** It says the
published text happened to be clean. It says nothing about whether publishing without
the gate was safe, and a run of clean late passes would make this defect less visible
rather than less real.

## Acceptance criteria

- [ ] A resolution is chosen from the candidates above, or a better one, with the reason recorded
- [ ] The chosen mechanism is written into CLAUDE.md where the humanizer gate is stated, so the rule and its enforcement live together
- [ ] The mechanism is exercised once on a real cross-post before this BL closes, since a gate that has never fired proves nothing (the BL-535 lesson)
