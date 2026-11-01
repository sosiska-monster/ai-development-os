# Environment — project-specific Codex harness

**When:** design Codex setup after sufficiently clear requirements/architecture, or inspect an existing codebase without implementing changes.

## Discovery before design

For brownfield repos send Codex a **read-only** recon task: branch/HEAD/status, pre-existing dirty worktree, root instructions and nested AGENTS, stack/package manager, module map, entrypoints/contracts, existing verify/tests/CI, lockfiles, secret boundaries and known blockers. Exclude vendor dirs, generated artifacts and secrets. Return actual paths and command outputs; inspect relevant diff before trusting conclusions.

## Environment Profile (proposed → implemented → verified)

Document project-specific: language/versions and deployment; Codex Desktop/CLI/Cloud actual interaction mode; git/worktree strategy; instruction paths; user approvals; dependency policy; quick `verify` + optional `verify-full`, baseline HEAD and last verified result; memory paths/permissions; scopes, privacy/secret boundaries and production isolation; session handoff; optional Skills/MCP/subagents and why needed. State deliberately omitted mechanisms.

A profile is **READY FOR BOOTSTRAP** when requirements/architecture sufficient and intended setup approved; it is **VERIFIED FOR FEATURE WORK** only after Codex actually establishes the baseline checks and validates the intended controls (or records explicit justified exceptions). For a greenfield repo, setup may create the first check before any feature; don't pretend it already passed.

## Mechanical controls rather than promises

**For each proposed control, specify:** threat, enforcement point, exact configuration or command appropriate to installed Codex/project version, test stimulus, observed outcome, and fallback. Do not assume a rule, permission profile, network denial, hook, CI or worktree exists or operates solely because documentation mentions it.

- Keep worktree outside automatic access to production credentials; redact sensitive output and verify actual limits with safe dummy secrets, never real ones.
- Risky Git/push/history-rewrite/clean and production operations require explicit authorization and appropriate permission barriers; safe local commits when permitted. Protect pre-existing edits. Never automatically `git checkout -- .` or delete branches as a circuit breaker.
- A project `verify` should be fast and deterministic, returning nonzero on failures. Add focused checks for suspicious changes to tests, typing/lint configs, dependencies, lockfiles, unsafe shortcuts; **review flagged changes rather than automatically banning legitimate updates**.
- Independently inspect changed files vs intended scope; include committed, staged, unstaged and untracked paths. Consider CI on PRs for material projects. Neither a generated evidence block nor CI alone proves behavior is correct.
- Install third-party Skills, MCP or packages only for identified need; review provenance, scripts, network requests, licence/version and access boundary before approval.
- Record whether the current tool surface actually supports sandbox, rule, hook, review or worktree mechanisms; do not require unavailable features.

## Minimal project memory

Keep root `AGENTS.md` short and durable; route to `PROJECT.md`, current `TODO.md`, `REQUIREMENTS.md` for confirmed behavior, `Decision.md`, `Bugs.md`, `Gotchas.md` only as relevant. A tiny project may combine compatible files when it preserves authority and status. Personal `WordStyle.md` lives outside customer repos by default.

## Environment Gate C

- PLANNED: scope and controls approved, ready to draft project Bootstrap on **separate user request**.
- IMPLEMENTED: real files/config and commands created without erasing existing work.
- VERIFIED: project-specific smoke tests, baseline command, protective barriers and evidence observed where applicable.

Do not confuse PLANNED with VERIFIED; high-risk feature work requires appropriate verified baseline and approvals.
