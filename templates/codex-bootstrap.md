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
5. Create short project AGENTS.md routing to active project docs, not a giant manifesto.
   Protect secrets and prompt-injection boundaries, use dynamic risk mode policy.
6. Record initial project state and required docs. For meaningful client requirements
   create docs/ai/REQUIREMENTS.md with authorized statuses, no invented confirmations.
7. Produce a REAL Git status, scoped diff, checks with exit codes, baseline/checkpoint
   and next SMALL vertical product task. Preserve dirty changes and STOP for new risks.
```

Never claim installed hooks, sandbox, CI or deny policies work without evidence. No product work until environment review and user approval of the next task.
