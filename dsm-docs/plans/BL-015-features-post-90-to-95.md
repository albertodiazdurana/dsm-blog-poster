# BL-015: Update Features Post from 90 to 95 Features

**Priority:** Medium
**Source:** Session 16 (2026-04-07), discovered while reading FEATURES.md per the new session-start TAB/DSM context rule
**Trigger:** Same session as BL-014, or next blog session

## Description

`content/blog/2026-03-20-dsm-features-three-dimensions/index.md` (the canonical features post) currently states "90 features across three dimensions". DSM Central's `FEATURES.md` is now at **95 features across 11 capability domains**.

New features added since the post was last updated (S14):

- F-091 Planning pipeline gate in alignment template
- F-092 Runtime register context for register-sensitive skills (humanizer)
- F-093 Python virtual environment protocol
- F-094 Per-turn transcript append enforcement
- F-095 Process narration in transcript thinking blocks

Per the project rule "DSM Version Release Coverage" in CLAUDE.md, this post is the canonical features post and must be kept current as DSM ships features.

## Success criteria

1. Total count updated from 90 to 95 in title, intro, and any other reference.
2. The five new features are woven into the three-dimensions narrative in the appropriate dimension, not appended as a flat list.
3. Voice calibration + `/humanizer` pass before publishing.
4. Commit and push via standard PR flow.

## Out of scope

- Writing a dedicated release post. Latest release post (v1.4.5, protocol-visibility) is already published. If a dedicated v1.4.6+ release post is warranted, that is a separate BL via the reconstruction trail in `feature-trail.md`.
- BL-014 (TAB two-layer framing in about/framework), tracked separately.

## Notes

The five new features span April 6-7. They should be reviewed against `feature-trail.md` to confirm whether any deserve a dedicated release post in addition to the count update.
