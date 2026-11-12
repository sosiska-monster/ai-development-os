# Codex task contract — adapt, don't paste every field into every microtask

The task mode is a **current assessment, not a permanent label**. Codex may recommend mode changes on new evidence but cannot unilaterally grant permissions.

```text
TASK ID / GOAL: <ONE atomic, verifiable result; no second task in the same prompt>
GOAL GRAPH TRACE: <G0 customer outcome → parent outcome → THIS task ID; linked requirement IDs, prerequisite IDs and acceptance; omit speculative file mapping>
APPROVED EXPERIENCE (when UI/UX is consequential): <approved design/wireframe/version + confirmed content, responsive behavior, interactions and user approval source; if still PROPOSED/DESIGN_REVIEW, do not implement>
DESTINATION CHAT: <exact Codex Desktop chat name registered by ChatGPT Web; label as proposed until user confirms it>
WORKSPACE / BRANCH: <verified product repo, intended Git branch and worktree; for an experimental write task require isolated experiment/<slug>, never main>
CURRENT MODE / RISK: FAST | STANDARD | CONTROLLED / why
CONTEXT: <confirmed requirements IDs, relevant paths, branch/base SHA; omit unknown paths>
READ CONTEXT: <paths allowed to inspect for understanding; reading does not grant write permission>
WRITE ALLOWLIST: <exact files or narrow globs where edits are authorized; NONE for read-only recon>
DO NOT MODIFY: <all other paths including config, deps, tests, memory, AGENTS unless explicitly allowlisted>
EXPECTED_DIFF_PATHS: <same write allowlist; PROVISIONAL only for read-only recon; approve extra paths before editing>
DECISION LOCK (when consequential): <Web/user-approved semantic choices; for ML: split ratios, strategy, units/groups, seed, metric, dataset identity; cite approval source>
ACCEPTANCE: <objective behavior, tests or invariant; attach approved UI/behavior reference when present>
RUNTIME CHECK (when applicable): <actual user journey/API/CLI/inference scenario, safe environment and observable PASS/FAIL evidence; NOT APPLICABLE otherwise>
MODEL EVAL CONTRACT (when applicable): <approved dataset/cases version, split/seed, baseline, metrics, thresholds, slice checks, leakage policy, artifact refs; NOT APPLICABLE otherwise>
DEPENDENCIES / CONTRACT: <what is pre-approved; new deps need approval per Environment Profile>
MODEL / EFFORT: <OPTIONAL — verified current setting and requested adjustment if a specific hard problem warrants it; never assume the prompt can switch the UI>
VERIFY: <project check + task-specific check; baseline status if known; browser/E2E/ML evaluation only when supported/approved>
GIT / PRE-EXISTING CHANGES: <approved branch/checkpoint; preserve user edits>
GITHUB BRIDGE: <push/PR policy explicitly approved for exact branch or NO PUSH; verified Web access unknown until tested>
MEMORY: <update only verified facts; propose unverified records>
STOP / ESCALATE WHEN: <new auth/data/API/prod risk, out-of-scope diff, new dependency, no-progress failures; no next independent goal>
IN-TASK REPAIR: <small safe scope-preserving fixes and reruns allowed; stop if no progress / critical decision needed>
PLAN FIRST: <mandatory for CONTROLLED; get approval before high-risk effects>
EVIDENCE HANDOFF: <exact existing source paths/ref and destination Web chat; if files genuinely needed, approved local .ai-handoff/<TASK_ID>/ or explicitly approved shared evidence path; no implicit write scope>
REPORT: <Lite for low-risk FAST; Full for high-impact tasks; show actual Git and verification artifacts>
```

**Critical decision stop:** If `DECISION LOCK` is missing or disagrees with actual data for a consequential choice, return `BLOCKED — CRITICAL DECISION MISSING` before split creation/training/export or other side effects. Do not select ML train/validation/test proportions, sample weights, leakage boundary, validation metric or production semantics yourself. A conventional ratio is a proposal, not approval. If allowed to implement an approved split, report actual counts/ratios, disjoint groups/records, dataset version and reproducibility; do not silently edit/decrease tests or overwrite existing artifacts.

For an **experiment with side effects**, before any writes/installations verify actual working directory, branch, HEAD and dirty state. If not in the approved isolated `experiment/<slug>` worktree/repo, STOP as BLOCKED. Never switch into or modify `main` to run a trial, auto-merge, push, globally install/uninstall models or delete failed trial data without separately approved scoped instructions. A successful trial needs a later explicit integration task; a failed one stays isolated, with safe cleanup proposed rather than executed automatically.

Never interpret 'necessary for the task' as authorization to write outside WRITE ALLOWLIST. If additional files, tests, dependency/lockfile edits, memory updates or new directories are needed, **STOP and ask for an updated ChatGPT Web task/user approval before modifying them**. If required paths are unknown, perform a separate read-only reconnaissance task first. The write allowlist is a behavioral contract, NOT an OS-enforced filesystem permission; use verified isolation/sandbox and human diff review for stronger controls.

At completion compare **committed, staged, unstaged and untracked** paths against EXPECTED_DIFF_PATHS, distinguishing pre-existing user edits. Report MATCH / MISMATCH / NOT SCOPED, with exceptions explicitly approved. A path mismatch is not solved by claiming it was necessary.

**In-task bounded repair:** within THIS approved result, diagnose failed checks, edit only allowlisted files and rerun as needed. This does not authorize new dependencies, altered acceptance/decision lock, weakened tests, unapproved push/merge, production data or a second task. Escalate before any such change; after repeated unproductive attempts preserve evidence and STOP. Report actual tries/checks, runtime acceptance and model eval where relevant. `DONE` alone is not the product goal's `ACCEPTED`.

**One-task boundary:** execute only this explicitly authorized outcome and necessary substeps. Return a concise task result and actual checks; explicitly state **NEW CHAT: YES/NO + reason** (default YES after DONE for a separate next task); ask which task to do next and STOP. Do not auto-execute a roadmap/TODO item or trigger autonomous Goal continuation without explicit approval. If the next task is independent and the chat is cluttered, recommend a fresh thread after updating essential verified existing project memory; native compaction is for continuing the SAME unfinished task and does not erase history.

For a true FAST task, use a few sentences rather than pasting this template wholesale. On escalation, stop new risky operations, preserve state and request an updated task contract; on de-escalation, don't bypass already necessary checks.
