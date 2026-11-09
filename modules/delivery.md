# Delivery — dynamic routing, vertical slices and evidence

**When:** implementing or reviewing work. Read with the task's risk and actual project state, not as a ritual.

## Select an initial mode, then re-route continuously

| Mode | Entry indicators | Required minimum |
|---|---|---|
| **FAST** | Small, reversible, well-understood local change; no material contract, data, security, dependency or architectural effect; working verification already exists | Codex can execute directly; scoped diff, targeted check, Lite report and Git checkpoint when justified |
| **STANDARD** | Ordinary user-visible feature, moderate bug or moderate uncertainty | Short acceptance-based task, focused verification, changed-path review, Full report when warranted |
| **CONTROLLED** | Migration/deletion, production, security/auth, confidential data, payments, public API, high-cost or irreversible impact, large ambiguity, architectural change | Plan-first + user approval, risk/rollback plan, independent diff and relevant tests, Full report, no silent production action |

There is **no hard file-count threshold**. A one-line auth change can be CONTROLLED; a ten-file mechanical rename may be STANDARD. Choose the cheapest mode that still covers actual risk.

**Dynamic transition protocol:**
- Evaluate on task intake **and at every new fact**: unexpectedly changed files, critical contract, new dependency, failed checks without progress, data exposure, user changes scope.
- FAST → STANDARD/CONTROLLED or STANDARD → CONTROLLED: **stop scope-expanding work**, preserve current uncommitted state, report trigger, impact and options; obtain approval when permissions, risks or product contract change. A tool/AI may recommend escalation, not grant itself new authority.
- CONTROLLED → STANDARD/FAST or STANDARD → FAST: possible after the risk is resolved and scope is verified safe. Keep any risk-driven check already required; do not retroactively erase evidence or permission decisions.
- At any mode, use extra checks if a specific invariant demands them. Trigger does not automatically mandate a new meeting/document.
- For serial small edits, send a concise batch summary to ChatGPT periodically or before a dependent architectural decision; no unnecessary human clipboard loop on every button.

## Two independent dimensions: product assurance and task risk

Every task inherits the product's **approved assurance baseline** (documented in the Blueprint/PROJECT/Environment Profile), while FAST/STANDARD/CONTROLLED determines how carefully **this particular change** is handled. A FAST change in production still uses the baseline safety and quality checks applicable to the affected behavior; a prototype must use CONTROLLED when a task becomes sensitive, destructive or irreversible. Do not auto-promote every production task to CONTROLLED or turn every prototype task into FAST.

When a prototype becomes an externally used product, or a demo starts processing real data, reassess the project's assurance profile, tests, deployment and recovery readiness **before the increased exposure**. Such transitions are a product decision requiring appropriate user signoff; they are not a new mode or a fixed file-count threshold.

## Adaptive model + reasoning effort (independent of task mode)

**Policy, not an imagined controller:** route by actual reasoning difficulty, required tools/context, available models, budget and empirical success; retain the product's assurance baseline and FAST/STANDARD/CONTROLLED safety gates separately.

- **Routine / narrow / verified recipe:** available efficient model and low/standard effort; do not spend high effort on renaming, straightforward edits, repetitive extraction or formatting.
- **Ordinary feature / mixed context / unfamiliar code:** balanced model + medium effort; increase only if ambiguity or the observed quality calls for it.
- **Architecture alternatives / hard root-cause debugging / conflicting requirements / subtle data or security invariants:** higher-capability available model and high effort for the **reasoning-heavy phase**, then return to a lighter setting for clear execution or routine follow-up.
- **Escalate on evidence, not prestige:** missing decisive facts, repeated *different* failed hypotheses, difficult cross-module dependencies or demonstrably inadequate output. First check clarity, actual repo access, task breakdown and tests. Never simply re-run the same failing task at maximum effort indefinitely.
- **De-escalate:** once a plan and acceptance are clear, choose cheaper/faster supported settings for bounded work. Compare cost/time **per verified success**, including rework; higher effort alone is no guarantee of correctness.
- **Platform truth:** In Work/Codex, use a native **Default** selector when available and satisfactory, or select an available model + reasoning level explicitly. A manual Codex selection may persist; do not claim markdown instructions changed it. In ChatGPT Web use available picker/auto behavior, or *recommend* a manual adjustment where supported. Settings differ by account/version. No task may rely on an unverified model switch.
- **Minimal communication:** recommend a switch only when it matters: `RECOMMEND: <UI/model/effort actually available or UNKNOWN> — <specific reason>`. Do not force the user to set a knob at every step, leak sensitive context to another provider, or install an orchestration layer solely to implement this policy.

This is execution resource routing, **not** authorization. A low-effort model in a CONTROLLED task must still satisfy strict review/testing/approvals; if capability is insufficient, pause instead of relaxing controls.

## Web-owned decomposition into small, meaningful slices

Before dispatch, ChatGPT Web breaks the approved MVP/feature into **small, independently reviewable outcomes**: minimal user-visible or technically verifiable vertical slices with objective acceptance, relevant dependency order and known risk. Prefer first working path over speculative shared infrastructure. Keep a lightweight ordered backlog in the existing project TODO or chat; do not create a separate planning artifact by default. User decides the next authorized slice.

**Sizing heuristic, not a fixed file/time quota:** one coherent outcome and one focused review/verification cycle. A slice may touch several already approved files when needed; avoid giant multi-feature batches **and** artificial one-line subtasks that cannot be verified independently. If a task exposes a new requirement or architectural decision, pause, re-slice and seek approval rather than silently expanding. A brief planning view may list several future slices, but a Codex prompt authorizes **only the next one**.

Before proposing an implementation, Web checks it against approved requirement IDs, simpler reusable options, security/quality baseline and observed architecture. Challenge unjustified complexity with the concrete conflict, trade-off and minimum viable alternative; never silently override customer requirements or turn every low-risk choice into debate.

## Evidence-led experiment selection (Web chooses, human authorizes)

At a **natural checkpoint** (failed check, repeated rework, context loss, expensive handoffs, slow build/deploy, measurable product bottleneck), Web proactively decides whether an experiment would improve the **product or the development workflow**. It should not wait for the user to name a tool or propose an experiment. **Do not interrupt delivery** for speculative optimization or manufacture a problem to justify new infrastructure.

1. **Observe:** identify a specific bottleneck backed by a real report, diff, timing, user feedback or other observable signal. Separate verified facts from hypotheses. If no trustworthy baseline exists, choose a minimal read-only measurement first.
2. **Generate options:** briefly consider up to 3 plausible directions, **including no change / simpler built-in alternative**. Examples: reduce Codex task scope, improve acceptance checks, tune model effort, simplify project memory, or *only if warranted* trial an external memory tool.
3. **Prioritize:** compare likely user/product benefit, evidence/confidence, experiment cost/complexity, reversibility, privacy/security risk and impact on the agreed roadmap. Prefer the **cheapest falsifiable, safe experiment** with meaningful expected payoff. Do not invent quantitative scores; explain the trade-off and why the winner beats doing nothing.
4. **Specify one experiment:** hypothesis, baseline/control, a bounded changed variable, objective metric, minimal sample or timebox, PASS/FAIL/INCONCLUSIVE threshold, expected cost/risk and rollback/removal path. For unmeasurable claims, first improve measurement, not architecture. Avoid optimizing for a proxy that damages user requirements.
5. **Approval and execution:** Web **independently selects and recommends** the next experiment; only the user authorizes new Codex work, tool installation, paid services, external data transfer or production effects. Codex receives **one** write-scoped task and STOP, with required evidence. Read-only analysis within an already approved task is not a second autonomous task.
6. **Learn:** compare observed result with baseline; mark PASS / FAIL / INCONCLUSIVE / NOT RUN, record only verified facts in existing project TODO/Decision or methodology TEST_CASES/RATIONALE when relevant. Adopt only if the benefit is demonstrated and safety/requirements are preserved; otherwise remove/revert through approved scoped actions. Do not repeatedly retry an unsuccessful hypothesis without new evidence.

**Compact output at a checkpoint:** `IMPROVEMENT: NONE | MEASURE | EXPERIMENT`; if EXPERIMENT: `signal → best direction → chosen test → baseline/metric → success/stop criteria → cost/risk → approval needed`. No new agent, skill, tracking database or mandatory experiment file. Lack of observed benefit is a valid reason to do nothing.

## Exact chat routing and isolation for experiments

**ChatGPT Web is the dispatcher of chats.** At each meaningful handoff, read the **Chat Register** in the product's existing `PROJECT.md` **or a current, explicitly maintained ChatGPT Project source** (with optional later synchronization to product docs). The register contains only real or proposed chat names, responsibility/purpose, ACTIVE / PAUSED / ARCHIVED status, target ChatGPT/Codex surface, applicable Git branch/worktree and last verified task/checkpoint. Do **not** confuse a chat's name with a Git branch: each is a different entity. Do not duplicate full conversation transcripts or create a new register file by default.

Before handing off **any prompt**, Web provides:
- `DESTINATION: ChatGPT Web | Codex Desktop`
- `CHAT: «exact, registered name»` (never merely YES/NO, "current chat" or "new chat")
- `ACTION: CONTINUE | CREATE`. When CREATE, supply a proposed unique name and a short starter with verified context; mark PROPOSED until the user actually confirms creation
- `PROJECT REPO / BRANCH / WORKTREE: verified values or UNKNOWN`, and `TASK: one authorized result`. Never infer repo/branch from chat name; read actual Git status first

At transitions Web **proposes a minimal register update**, with latest confirmed name, purpose, status and checkpoint. A connected approved write action or a separately approved scoped Codex update can persist it in the product's `PROJECT.md`; otherwise return copy-ready lines for the user to store in the ChatGPT Project sources/product file. GitHub library `CORE.md` does NOT hold individual customer chat history. Do not pretend that ChatGPT can enumerate, create, rename, track or write to all other chats automatically; if the register is unavailable or stale, ask for it or mark unknown. Avoid making a registry edit a separate Codex task for each trivial message; batch durable changes at natural checkpoints.

**Experimental work is not mainline product development.** Before any experiment that may change files, install tools/models, run migration scripts, or create artifacts, require a separately authorized **disposable workspace**, preferably a Git worktree with a dedicated `experiment/<slug>` branch forked from a verified baseline (a standalone disposable test repo is also fine). Use isolated dependencies, test data, credentials and caches as appropriate; a branch/worktree **does not** isolate global installs, environment variables, external APIs or databases. A purely read-only model evaluation without local changes needs no new branch, but still gets a named experiment chat and a bounded protocol.

- **Preflight:** Web names both the experiment ChatGPT chat and Codex chat, records the product repo and allowed isolated worktree/branch; Codex checks `pwd`, branch, HEAD, `git status --short` before changes. If the expected isolated workspace is missing, or Codex is on `main`/shared production workspace, **BLOCKED — no writes, installs or experiment runs with side effects** until the user explicitly approves safe setup.
- **Boundaries:** experiment Codex prompt allowlists experiment-only paths and forbids edits/commits/merges/pushes on `main`, product AGENTS, stable dependency/lockfiles and production settings unless there is a separately approved bounded setup. Don't auto-create new branch, edit shared configuration or install a model globally solely because an experiment prompt mentions it. No live customer data by default.
- **Outcome:** evaluate the previously defined baseline and PASS / FAIL / INCONCLUSIVE / NOT RUN. The experiment has **no permission to promote itself**. Only after measurable benefit and a separate user-approved integration task can selected changes be copied/cherry-picked into normal development with fresh tests and diff review.
- **Failed/rejected trial:** mark experiment chat ARCHIVED with result and one-line lesson, leave `main` unchanged, then return to the exact named development chat and verified mainline branch. Propose deletion of experimental worktree/branch, temporary model/dependencies and test data **only after** checking for user edits, untracked/unpushed work and external effects, and obtaining explicit approval. Never auto `git reset --hard`, `git clean`, `git branch -D`, uninstall globally or erase user/model data.

This isolation is a **separation policy verified by tools**, not a promise that chat names or soft prompt allowlists enforce filesystem permissions.

## Critical Decision preflight — no silent data-science defaults

Before Web dispatches any task that will **split training data, train/evaluate an ML model, select metrics/thresholds, alter sensitive data semantics or make another material product choice**, it first checks approved requirements/Decisions and actual dataset constraints. If a material choice is absent, Web proposes options and obtains user authorization **before** issuing a write/training task. A narrow **read-only data audit** can run first to determine real counts and group/label distributions, without revealing private samples.

Codex must not silently infer train/validation/test ratios, time/group/stratification policy, data/label weighting, success metrics or final test use from a generic coding convention. Its preflight matches `DECISION LOCK` in the Web task to the code/config/manifest and actual dataset; missing or contradictory material parameters → `BLOCKED — CRITICAL DECISION MISSING` **before split generation, training, checkpoint overwrite or export**. Codex reports the proposed alternative, not an unauthorized automatic fix. Low-risk implementation details remain delegated; avoid paperwork for every parameter. The exact decision boundaries depend on the product.

For a split-changing task, verification must show **actual** train/val/test counts and ratios, no overlap/duplication or entity/time-group leakage relevant to the intended deployment, acceptable label coverage where possible, dataset identifier, deterministic seed/cutoff and correct separation of preprocessing/training from final test. Code-only review or a green training exit is insufficient. Never re-use final test results to choose the winning model. For prior training under unknown/unapproved split, preserve evidence/artifacts, mark metrics NON-COMPARABLE / NEEDS REVIEW, and propose a separate approval-scoped correction. See `modules/requirements.md`.

## One task at a time — explicit human gate, small reports

Codex may implement necessary internal steps of **one user-authorized task**, then verify the task-scoped diff and checks, produce a short Russian report and **stop**. A task can include multiple files but must have a single approved outcome. Do not silently proceed to the next task, roadmap step, deferred cleanup or suggested next item even if its work looks obvious. User authorization is required for the next independent task; a NEXT suggestion in the report is not approval. For several unrelated requested tasks without a clear first task, request a choice.

Default report at this boundary: `DONE | PARTIAL | BLOCKED; WHAT/WHY; CHANGED PATHS; VERIFY(command, exit or NOT RUN); RISKS; NEXT suggestion + question`. Reuse Lite/Full evidence as appropriate; do not duplicate giant reports or omit risk-required evidence. If BLOCKED or a task becomes risky, stop only expanding beyond the approved scope and preserve current worktree without destructive cleanup.

**Context management at task boundaries:** after verified results and necessary updates to existing PROJECT/TODO/requirements, prefer the user starting a **new Codex chat for an independent next task** when the prior thread has become noisy. Re-read project sources, not the old transcript. For continuation of the **same unfinished complex task**, consider native compaction where supported and preserving approved decisions; it is not a full reset. Do not claim that AGENTS/CORE can close threads or clear the model's state. No new context-manager Skill, permanent handoff file per task, automatic deletion of `.codex`, caches, Git history, logs, project files or user data. Disable/avoid auto-continuing multi-task Goal workflows unless explicitly requested by user.

## Task contract

ChatGPT Web authors **exactly ONE actionable Codex prompt for ONE verifiable outcome** after agreeing on its scope; the rest of the roadmap stays with ChatGPT Web/user. Include objective GOAL, necessary read context, **narrow WRITE ALLOWLIST**, DO NOT MODIFY, acceptance criteria, verification, stop/escalation triggers and Git/memory policy. For a known low-risk change, make this a short copy-ready task, not a full form. If paths are unknown, first issue a separate **read-only reconnaissance** task. Files read for context are not automatically writable. The write path set must be concrete before implementation; if codebase structure is unknown, Codex must discover relevant paths read-only and report them before any writes. Codex must **STOP before** creating/modifying any non-allowlisted file, including tests, configs, dependencies, project memory and extra architecture; ChatGPT Web/user must issue a revised authorized contract. Do not let a seemingly useful cleanup become another task. Prompt-level scope is a soft restriction; for stronger protection, use verified workspace isolation, permissions and independent review of real diff. A separate Git worktree isolates branch changes but is not a per-file access-control system. Legitimate tests/lockfiles can be approved additions, never silently exempt.

## Between-task hygiene — remove waste without deleting user work

After a verified task or a **small batch of FAST edits**, at a natural Git/checkpoint boundary, do a **light, scope-aware hygiene sweep**, proportional to the Product Assurance Profile and current risk. The purpose is to keep the codebase from accumulating avoidable complexity — **not** to optimize net line count or add a mandatory cleanup ceremony to every microtask.

1. **Inspect, don't guess:** use actual diff/status and relevant references/tests to identify task-introduced unused imports/variables/helpers, duplicate logic, temporary debug statements, obsolete comments/TODOs, stale documentation or known disposable generated artifacts. A file's age, size or unfamiliarity alone does not make it garbage.
2. **Classify before acting:**
   - **LOCAL SAFE:** clearly redundant items introduced in the **approved task scope**; remove/simplify while preserving behavior and before final verification/checkpoint. Run relevant verify and review the resulting diff. A task already at a clean checkpoint may skip changes.
   - **REVIEW:** deletion across scope boundaries, potentially used code, dependency/lockfile changes, public APIs, tests/fixtures or broad refactoring. **Propose** a separately scoped task with rationale and appropriate FAST/STANDARD/CONTROLLED risk mode; never silently expand the previous task.
   - **PROTECTED/UNKNOWN:** pre-existing user changes, untracked files of uncertain ownership, secrets, real data, migration history, backups, audit logs, deployment/CI configs and unknown artifacts. **Do not auto-delete**; request explicit authorization and safe, evidence-backed handling when removal is truly needed.
3. **Validate:** compare worktree to task baseline, including committed/staged/unstaged/untracked changes and pre-existing edits. Check behavior/tests, scope and any loss of observability or recoverability. Do not delete necessary diagnostics or weaken tests to make a project look tidy.
4. **Report briefly:** `HYGIENE: CLEAN | REMOVED <what + why + verified check> | DEFERRED <candidate + reason>`. Batch/report only meaningful findings, not an extra giant log. If cleanup creates more work than it saves, stop and leave a small candidate list rather than refactoring blindly.

Never use `git clean -fd`, `git reset --hard`, recursive deletion or blanket cache/artifact deletion as an automatic housekeeping action. Git ignores and generated folders require project-specific verification; do not touch unrelated files simply because Codex did not create them. An unneeded abstraction may be **replaced or removed** instead of wrapped in another abstraction.

## Scope check — actual repository evidence

For each task use a base SHA and inspect:
- committed changes vs base (e.g. `git diff --name-status BASE..HEAD` for an ordinary linear task; choose correct merge-base semantics for PRs),
- staged/unstaged changes (`git diff --name-status`, `git diff --cached --name-status`),
- untracked files (`git ls-files --others --exclude-standard`),
- dirty pre-existing changes **separately**, so they are not falsely attributed to Codex.

Compare *all* effective task paths with approved scope. If outside scope, report MISMATCH, explain and seek approval; **never mark ACCEPT just because tests pass**. Path checks don't prove behavior, test integrity or freedom from secret leakage.

## Integrity and verification

- Test behavior from approved requirements; use risk-based test-first for critical invariants. Do not replace failing tests with skips, removed assertions, mocks or type/lint suppression to fake green results.
- Test changes can be legitimate when requirements change; disclose exact diff and approval/evidence. Scan configuration, dependency and lockfile modifications, too.
- A stable, fast project `verify` should exist **before ordinary feature work when practical**; for an empty repo the first environment setup may establish it. Record baseline SHA and baseline results; `verify-full` by risk.
- Repeat failures without progress → pause, diagnose and escalate; never automatically erase the worktree or run destructive restore.
- For product behavior review, prefer independently retrieved GitHub diff, CI results or user-inspected Codex diff. Command output authored by Codex alone is **not independent proof**.

## Reports and decisions

FAST/LOW uses the Lite evidence format. STANDARD generally Full if meaningful; CONTROLLED always Full with targeted diff, tests, and approval status. See `templates/codex-report.md`.

ChatGPT verdict: **ACCEPT / FIX / REWORK / INSUFFICIENT EVIDENCE**. If real artifacts are unavailable, do not assert verified success. A vertical slice is valuable user behavior, not volume of files.

Git checkpoint: logical verified commits, preserving unrelated/uncommitted work; no silent push, force, reset, cleaning or production operations. Use branch/worktree when it improves isolation, not as a universal ritual.
