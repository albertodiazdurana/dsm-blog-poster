### [2026-08-05] /dsm-align: alignment updated (v1.19.0 -> v1.20.0)

**Type:** Notification
**Priority:** Medium
**Source:** /dsm-align

Run mode: post-change
Full report: `.claude/last-align-report.md`

Summary:
- Created: none
- Fixed: `.claude/hooks/validate-cross-repo-write.sh` updated from Central
  (BL-484 extends the guard to Bash file operations);
  `.claude/settings.json` gained `PreToolUse` / `Bash` ->
  `validate-cross-repo-write.sh`
- Warnings: 3 (see persistent report for full text)
  1. `2026-08-05_local-state-files-assumed-gitignored-are-tracked.md` unpushed;
     needs voice-attribution approval before the send. Its predecessor (the
     ugrep report) HAS landed, and both defects it named are fixed upstream in
     v1.20.0 as BL-482 and BL-483.
  2. Four v1.20.0 BLs ask for `scripts/sync-commands.sh --deploy` in DSM
     Central; BL-485 asks for a review of DSM_0.2 §19.1. `--check` is reliable
     again per BL-479, reversing the v1.19.0 instruction.
  3. `/dsm-align` Step 10e's command-only idempotency rule makes BL-484's Bash
     matcher un-installable in any spoke, because the same script appears under
     three matchers in `settings-hooks.json`. This run used `(matcher, command)`
     instead. Candidate feedback entry.
- Collisions: 0
