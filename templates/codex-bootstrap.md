# Project-specific Codex Bootstrap — TEMPLATE ONLY

**Not an executable generic bootstrap.** ChatGPT Web must first agree on product requirements, architecture, Environment Profile, and then receive a **separate explicit user request**. The result is adapted to actual Codex interface/version and real repo. Read-only recon of a brownfield repo may happen earlier.

```text
You are Codex working in the real APPROVED product repository. Do not implement features yet.

APPROVED REQUIREMENTS / customer authority: <source, active REQ IDs, privacy rules>
APPROVED ARCHITECTURE / expected invariants: <...>
APPROVED ENVIRONMENT PROFILE / method version SHA: <...>
CURRENT REPO FACTS (if discovered): <branch/base SHA, dirty worktree, tests and instructions>

1. Perform read-only inventory of repository, git status, existing AGENTS and nested rules,
   actual stack/versions, installed checks, CI, sensitive files, branch/worktree mode.
   Respect any pre-existing user changes. Report conflicts before modifying anything.
2. Propose the MINIMAL project setup; include planned paths, test baseline, git policy,
   memory names/authority, requirement ledger need, security boundary, and costs.
3. Configure ONLY approved setup. No business features, no unapproved dependencies,
   no dangerous permission escalation, no push or production action.
4. Establish fast deterministic verify where practical; show executable command,
   baseline SHA and exact result. Add applicable checks/CI/permission controls
   according to the installed surface, and test them using safe fixtures.
   Mark each as PLANNED / IMPLEMENTED / VERIFIED with actual evidence.
4a. For user-facing products, define an actual acceptance path: preview/staging URL or
    CLI/API/inference example, minimal runtime check, target viewports where applicable,
    authorized browser runner or NO TOOL. Run a safe smoke test and record evidence
    or mark NOT RUN. Do not install Playwright or any service without separate scope.
4b. For ML/LLM products, record the user-approved Model Evaluation Contract:
    dataset/cases version, baseline model, split/group leakage policy, seeds,
    metric thresholds and error slices, environment reproducibility, no test tuning.
    First compare on safe fixtures; no production model promotion.
4c. If GitHub bridge is requested: inspect real remote/branch, propose exact
    push/PR permissions; check protected main and CI in actual GitHub settings;
    verify Web can access *this* repo's non-default branch and full PR diff/CI.
    A local commit is not remote. Never auto-push, merge or expose secrets.
4d. Test installed Codex sandbox/permissions against harmless out-of-scope canaries
    and verify failures. Log CONFIGURED vs OBSERVED and an explicit fallback;
    do not confuse allowed roots with file-specific denies.
5. Create short project AGENTS.md routing to active project docs, not a giant manifesto.
   Include ONE TASK → concise Russian result/checks → STOP for user direction.
   Continue the current Codex chat while useful; offer a new one only for unusable
   context, independent review or user choice. Never delete chat histories.
   Protect secrets and prompt-injection boundaries, use dynamic risk mode policy.
6. Record initial project state and required docs. For meaningful client requirements
   create docs/ai/REQUIREMENTS.md with authorized statuses, no invented confirmations.
7. Produce a REAL Git status, scoped diff, checks with exit codes, baseline/checkpoint
   and next SMALL vertical product task. Preserve dirty changes and STOP for new risks.
```

Never claim installed hooks, sandbox, CI or deny policies work without evidence. No product work until environment review and user approval of the next task.
