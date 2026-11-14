# Codex task contract — adapt, don't paste every field into every microtask

The task mode is a **current assessment, not a permanent label**. Codex may recommend mode changes on new evidence but cannot unilaterally grant permissions.

```text
PROJECT INTAKE: <NEW / EXISTING, real repo and task-scoped AS-IS facts; for EXISTING do not initialize or rebuild>
AUDIT/REMEDIATION MODE: <READ-ONLY INVENTORY with WRITE ALLOWLIST NONE and no mutating tests / APPROVED SAFE CHANGE with baseline and rollback; choose one>
EXISTING BEHAVIOR TO PRESERVE: <validated user journeys, interfaces, data/checkpoint formats, existing dirty worktree; UNKNOWN explicitly where not verified>
REFACTOR JUSTIFICATION (if applicable): <confirmed issue + code/runtime evidence + goal impact + smallest adequate fix + before/after check>
TASK ID / GOAL: <ONE atomic, verifiable result; no second task in the same prompt>
GOAL GRAPH TRACE: <G0 customer outcome → parent outcome → THIS task ID; linked requirement IDs, prerequisite IDs and acceptance; omit speculative file mapping>
APPROVED EXPERIENCE (when UI/UX is consequential): <approved design/wireframe/version + confirmed content, responsive behavior, interactions and user approval source; if still PROPOSED/DESIGN_REVIEW, do not implement>
DESTINATION CHAT (if handing off): <existing chat; only name a distinct destination if actually known, otherwise PROPOSED>
WORKSPACE / BRANCH: <verified product repo, intended Git branch and worktree; for an experimental write task require isolated experiment/<slug>, never main>
CURRENT MODE / RISK: FAST | STANDARD | CONTROLLED / why
CONTEXT: <confirmed requirements IDs, relevant paths, branch/base SHA; omit unknown paths>
READ CONTEXT: <relevant known files; Codex may inspect nearby code to establish actual feature dependencies, respecting secrets>
APPROVED WRITE SCOPE: <FAST/STANDARD: goal and affected feature/component, including necessary implementation files and direct tests; CONTROLLED: exact paths/operations when warranted; NONE for read-only audit>
DO NOT MODIFY: <unrelated features, critical configs/CI, dependencies/lockfiles, auth/security, data/migrations, approved product semantics; ordinary related tests are in scope for FAST/STANDARD>
EXPECTED DIFF: <optional path hints; after task list all real changed files and verify each belongs to the approved feature/scope, including staged/unstaged/untracked>
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
STOP / ESCALATE WHEN: <new critical decision, another feature, auth/data/API/production effect, CI/tests weakening, dependency/lockfile, no progress; no next independent goal>
IN-TASK REPAIR: <Codex may locate/edit necessary adjacent code and direct tests within approved component, fix safe failures and rerun; STOP on critical boundary>
PLAN FIRST: <mandatory for CONTROLLED; get approval before high-risk effects>
EVIDENCE HANDOFF: <exact existing source paths/ref and destination Web chat; if files genuinely needed, approved local .ai-handoff/<TASK_ID>/ or explicitly approved shared evidence path; no implicit write scope>
REPORT: <Lite for low-risk FAST; Full for high-impact tasks; show actual Git and verification artifacts>
```

**Critical decision stop:** If `DECISION LOCK` is missing or disagrees with actual data for a consequential choice, return `BLOCKED — CRITICAL DECISION MISSING` before split creation/training/export or other side effects. Do not select ML train/validation/test proportions, sample weights, leakage boundary, validation metric or production semantics yourself. A conventional ratio is a proposal, not approval. If allowed to implement an approved split, report actual counts/ratios, disjoint groups/records, dataset version and reproducibility; do not silently edit/decrease tests or overwrite existing artifacts.

For an **experiment with side effects**, before any writes/installations verify actual working directory, branch, HEAD and dirty state. If not in the approved isolated `experiment/<slug>` worktree/repo, STOP as BLOCKED. Never switch into or modify `main` to run a trial, auto-merge, push, globally install/uninstall models or delete failed trial data without separately approved scoped instructions. A successful trial needs a later explicit integration task; a failed one stays isolated, with safe cleanup proposed rather than executed automatically.

For FAST/STANDARD, **the approved feature/component is the boundary**: Codex may discover and change necessary implementation files and directly related tests without another approval, even if their paths were not known upfront. A separate read-only reconnaissance task is optional, not automatic. For CONTROLLED, an explicit file/operation allowlist may be required. **STOP before** leaving that feature, changing public contracts, dependencies/lockfiles, CI checks, protected config, auth, private data, migrations, critical ML/business decisions or production operations. Do not weaken tests or falsify a PASS. These are behavioral boundaries, NOT OS-enforced filesystem restrictions.

At completion inspect **committed, staged, unstaged and untracked** changes, distinguishing pre-existing user edits. Report whether each task-introduced change belongs to the approved feature/component and whether protected boundaries were respected. For CONTROLLED, also check exact approved paths. Never label an unrelated file as in scope merely because it was convenient.

**In-task bounded repair:** within THIS approved result, fix implementation and related tests within the component, rerun checks and report attempts. No new dependencies, changed acceptance/DECISION LOCK, weakened assertions, unauthorized push/merge, production effects or second task. Escalate at these boundaries or repeated no-progress failures. `DONE` is not product acceptance.

**One-task boundary:** complete only this approved outcome and its technical substeps; report actual diff/checks and STOP before starting another task. Continue the current Codex chat by default. Recommend a fresh chat only if context is unusable, an independent review is needed, or the user chooses; never auto-reset or delete history.

For a true FAST task, use a few sentences rather than pasting this template wholesale. On escalation, stop new risky operations, preserve state and request an updated task contract; on de-escalation, don't bypass already necessary checks.
