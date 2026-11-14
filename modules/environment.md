# Environment — project-specific Codex harness

**When:** design Codex setup after sufficiently clear requirements/architecture, or inspect an existing codebase without implementing changes.

## Discovery before design

For brownfield repos send Codex a **read-only** recon task: branch/HEAD/status, pre-existing dirty worktree, root instructions and nested AGENTS, stack/package manager, module map, entrypoints/contracts, existing verify/tests/CI, lockfiles, secret boundaries and known blockers. Exclude vendor dirs, generated artifacts and secrets. Return actual paths and command outputs; inspect relevant diff before trusting conclusions.

## Existing-project adoption: preservation-first audit (BROWNFIELD)

When the user already has an ongoing product, **adopt that repository in place**; do not propose a fresh project, a new framework, new AGENTS/PROJECT/TODO files, dependency reinstalls or repo re-initialization as routine "bootstrap". The inherited code, working behavior, data and Git history are valuable assets. Audit read-only **before any changes**, and reconcile user/customer expectations with observed behavior, rather than assuming either old docs or existing code are fully correct.

**Stage A — minimum read-only inventory:**
- Confirm actual target product repository and authorized scope; record `cwd, branch, HEAD, upstream/remotes, status`, clean/dirty/untracked **without rewriting, stashing, cleaning, resetting or deleting anything**. Identify which edits predate audit. Avoid sharing private URLs, credentials, user data or full file dumps.
- Read current instructions/nested AGENTS and existing PROJECT/TODO/requirements/Decision, where present, plus Git history for recent intent and open work. Mark contradictions and stale files `NEEDS_REVIEW`, not approved facts. Preserve working branches/experiments and unfinished tasks.
- Map real runtime/build/dependency versions, entrypoints, subsystem boundaries, data flows, public interfaces, persisted formats, deployment and key user workflows. Map at sufficient depth to find risky coupling; don't index vendor/virtualenv/generated dirs or full logs.
- **Non-invasive observation first**: identify existing tests, CI, packaging and real runtime checks; note which can generate files, mutate DB or access external systems. Running tests or apps is **not automatically read-only**; execute only separately authorized safe checks, ideally in isolated/test fixtures. If unavailable, mark `BASELINE UNKNOWN / NOT RUN`, never fabricate PASS.
- Return an **as-is snapshot** and issue shortlist with precise `path + symbol or reproducible behavior + evidence/uncertainty`, current baseline, regression hazards and exact questions requiring authority. `READ ONLY | NO WRITES | NO INSTALL | NO PUSH | NO DATA MUTATION` is the default audit contract; even writing an audit report file requires explicit WRITE ALLOWLIST.
- If the repository contains no reliable tests, start with a proposed **characterization/smoke baseline** for critical existing behavior *before* a structural refactor. This is a separate approved write/testing task, not license to rewrite tests. If production is already broken, identify the broken baseline and preserve evidence, rather than demanding a fictitious green starting state.

**Stage B — Web decision:** review observations against current customer intent and Product Goal Graph, label issues `CONFIRMED / LIKELY / UNKNOWN`, estimate benefit, impact/risk and minimal change. Categorize `KEEP / FIX NOW / IMPROVE LATER / REMOVE AFTER VERIFICATION / NEEDS DECISION`. Prioritize broken user behavior, data integrity/security and blocked development above purely aesthetic architecture preferences. Codex's audit is diagnostic evidence, **not authorization for refactor**.

**Stage C — approved incremental work:** choose one bounded repair/cleanup task with a pre-change baseline/acceptance and rollback/restore strategy where relevant; preserve API, on-disk data, model checkpoint compatibility and working user behavior unless an authorized requirement pivot explicitly changes them. Prefer seams/adapters and small verified replacements over a big-bang rewrite. Re-run the applicable baseline and new acceptance checks, compare observed before/after, then Web/user accepts or requests a scoped correction. Do not immediately rebuild an entirely new system merely because the old one has technical debt.

For an active project with an urgent feature request, audit **just the affected slice plus neighboring contracts** first; schedule broader architecture inspection when real evidence justifies its cost. Existing `PROJECT.md` and `TODO.md` remain the canonical project sources when available; don't require a new process file to enter BROWNFIELD.

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

## Operational harness gate — verify real controls in each PRODUCT

The methodology is not an installed permission profile, CI service or browser. During an **approved project-specific Bootstrap** select the smallest technically workable verification and protection scheme, then test it on a disposable branch/fixture:
1. **Review boundary:** GitHub repository, remote and branch/worktree isolation; choose a user-approved push policy; verify default-branch protection/rulesets, PR/review checks and restrictions on direct writes to main if the project's GitHub account supports them. A created YAML file or requested branch rule is not proof that enforcement is active.
2. **Agent authority:** inspect installed Codex Desktop/CLI version, actual sandbox/permission configuration and path/network access with harmless canary files/fixtures. Do not claim prompt WRITE ALLOWLIST is OS enforcement, confuse sandbox writable roots with file-specific deny rules, or assume any profile works without a failed unauthorized-write trial. Protect credentials, datasets and production systems independently of Git.
3. **Independent checks:** reuse project-native deterministic `verify` (test/lint/type/build, critical config/scope checks as applicable) and arrange **PR CI that runs from reviewed/base configuration** where justified. Protect required checks; flag dependency/lockfile, tests, assertion/skips, workflow and critical-parameter changes. A local pre-commit hook is helpful but bypassable; CI/review is the independent layer. For non-PR projects specify what independent operator/runner actually executes the check.
4. **Runtime observation:** for deployed user-facing projects run a relevant preview/E2E/browser/smoke scenario with no production secrets unless approved; for APIs/CLI/ML use a corresponding real output/inference check. Record actual invocation, versions, tool permissions, browser/viewport or inputs and evidence. Avoid installing heavy tools solely to satisfy a checklist.
5. **Verification of the bridge:** before declaring Web a code reviewer, test whether **this user's current Web access** can actually fetch default-branch file, nondefault-branch file, complete PR diff and CI result. If it cannot, fall back to targeted uploaded diff/evidence plus CI; do not claim the browser connection automatically syncs.

Record `CONTROL | CONFIGURATION | SAFE TEST | OBSERVED RESULT | OWNER | FALLBACK` in the existing Environment Profile; mark each `VERIFIED / NOT VERIFIED / NOT AVAILABLE`. If a safety-critical control is unavailable, narrow scope or use a safer isolated environment rather than representing an unenforced textual policy as hard security. No generic universal shell script, CI workflow, permission YAML or tool installation is mandated across unrelated stacks.

## Environment Gate C

- PLANNED: scope and controls approved, ready to draft project Bootstrap on **separate user request**.
- IMPLEMENTED: real files/config and commands created without erasing existing work.
- VERIFIED: project-specific smoke tests, baseline command, protective barriers and evidence observed where applicable.

Do not confuse PLANNED with VERIFIED; high-risk feature work requires appropriate verified baseline and approvals.
