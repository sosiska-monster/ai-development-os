# Codex task contract — adapt, don't paste every field into every microtask

The task mode is a **current assessment, not a permanent label**. Codex may recommend mode changes on new evidence but cannot unilaterally grant permissions.

```text
TASK ID / GOAL: <one verifiable user-visible result>
CURRENT MODE / RISK: FAST | STANDARD | CONTROLLED / why
CONTEXT: <confirmed requirements IDs, relevant paths, branch/base SHA; omit unknown paths>
IN SCOPE / OUT OF SCOPE: <specific areas and prohibitions>
EXPECTED_DIFF_PATHS: <exact paths/globs when reasonably known; PROVISIONAL otherwise>
ACCEPTANCE: <objective behavior, tests or invariant>
DEPENDENCIES / CONTRACT: <what is pre-approved; new deps need approval per Environment Profile>
MODEL / EFFORT: <OPTIONAL — verified current setting and requested adjustment if a specific hard problem warrants it; never assume the prompt can switch the UI>
VERIFY: <project check + task-specific check; baseline status if known>
GIT / PRE-EXISTING CHANGES: <approved branch/checkpoint; preserve user edits>
MEMORY: <update only verified facts; propose unverified records>
STOP / ESCALATE WHEN: <new auth/data/API/prod risk, out-of-scope diff, new dependency, no-progress failures>
PLAN FIRST: <mandatory for CONTROLLED; get approval before high-risk effects>
REPORT: <Lite for low-risk FAST; Full for high-impact tasks; show actual Git and verification artifacts>
```

At completion compare **committed, staged, unstaged and untracked** paths against EXPECTED_DIFF_PATHS, distinguishing pre-existing user edits. Report MATCH / MISMATCH / NOT SCOPED, with exceptions explicitly approved. A path mismatch is not solved by claiming it was necessary.

**One-task boundary:** execute only this explicitly authorized outcome and necessary substeps. Return a concise task result and actual checks; explicitly state **NEW CHAT: YES/NO + reason** (default YES after DONE for a separate next task); ask which task to do next and STOP. Do not auto-execute a roadmap/TODO item or trigger autonomous Goal continuation without explicit approval. If the next task is independent and the chat is cluttered, recommend a fresh thread after updating essential verified existing project memory; native compaction is for continuing the SAME unfinished task and does not erase history.

For a true FAST task, use a few sentences rather than pasting this template wholesale. On escalation, stop new risky operations, preserve state and request an updated task contract; on de-escalation, don't bypass already necessary checks.
