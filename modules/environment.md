# Environment — project-specific Codex harness

**When:** design Codex setup after sufficiently clear requirements/architecture, or inspect an existing codebase without implementing changes.

## Discovery before design

For brownfield repos send Codex a **read-only** recon task: branch/HEAD/status, pre-existing dirty worktree, root instructions and nested AGENTS, stack/package manager, module map, entrypoints/contracts, existing verify/tests/CI, lockfiles, secret boundaries and known blockers. Exclude vendor dirs, generated artifacts and secrets. Return actual paths and command outputs; inspect relevant diff before trusting conclusions.

## Environment Profile (proposed → implemented → verified)

Document project-specific: language/versions and deployment; Codex Desktop/CLI/Cloud actual interaction mode; git/worktree strategy; instruction paths; user approvals; dependency policy; quick `verify` + optional `verify-full`, baseline HEAD and last verified result; memory paths/permissions; scopes, privacy/secret boundaries and production isolation; session handoff; optional Skills/MCP/subagents and why needed. State deliberately omitted mechanisms.

A profile is **READY FOR BOOTSTRAP** when requirements/architecture sufficient and intended setup approved; it is **VERIFIED FOR FEATURE WORK** only after Codex actually establishes the baseline checks and validates the intended controls (or records explicit justified exceptions). For a greenfield repo, setup may create the first check before any feature; don't pretend it already passed.

## Product assurance is a separate axis from task mode

Agree on the product's **Product Assurance Profile** in the Blueprint / PROJECT passport before selecting the verification and maintenance baseline. PROTOTYPE / MVP / PRODUCTION / CRITICAL are illustrative levels of intended lifetime, audience and consequence, **not** automatic architecture prescriptions. Confirm the real operational context (users, environment, data, privacy, failure impact, recovery and support capacity).

- **PROTOTYPE:** favor learning, simple code and fast checks; record disposable components and shortcuts. Do not use live sensitive data or grant production access casually.
- **MVP:** key user journeys must work, with maintainable structure and appropriate regression checks; defer unneeded scale machinery.
- **PRODUCTION:** establish fit-for-purpose regression/security checks, diagnostics, deployment discipline, data handling and recovery based on actual service expectations.
- **CRITICAL:** identify concrete high-consequence failures and stronger independent review, operational procedures, auditability and restore evidence, as required by actual risks.

Product assurance can change when a demo becomes a live service; **re-evaluate quality gates, acceptable debt and operational readiness before real exposure**. A production service can still execute a reversible label edit in FAST; a prototype touching real credentials may require CONTROLLED. Neither axis substitutes for approval, contractual constraints or concrete safety controls.

## Model and effort availability profile

At setup, determine the **actual UI and available model/effort controls** for ChatGPT Web and Codex Desktop/Work/CLI in the user's account; do not infer them from a model name or universal docs. Record only when useful: supported Default/auto routing, available manual levels, persistence of manual selection, budget/allowance constraints, tool-access compatibility and who can change a setting. Prefer native Default/auto selection for normal work if it behaves well; otherwise recommend a manual choice **before** a meaningful task. Project instructions and AGENTS.md cannot grant themselves permission to modify a model picker.

Evaluate on representative tasks: quick fix, standard implementation and hard investigation. Track verified outcome, human repair, completion time and any actual usage data; use UNKNOWN when not observable. Establish no fixed provider/model lock-in. Never sacrifice privacy or verification to save tokens.

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
