# AI Development OS — adaptive engineering instruction library

Version: **0.2.0-draft (unreleased, not pilot-validated)**. This repository is the *methodology*, not any customer's application.

**Русская инструкция для пользователя:** [USER_GUIDE.md](USER_GUIDE.md) — весь маршрут **ТЗ → MVP → Codex → проверки → staging → production**, выбор уровня ChatGPT/Codex и готовые сообщения. Это руководство для человека: не добавляйте его целиком в Project Instructions и не загружайте на каждую задачу.

## Existing project adoption — preserve and improve

This library supports **both** new-project design and **an ongoing existing product**. An existing codebase must **not** be recreated, reinitialized, rewritten wholesale or given a fresh generic bootstrap merely because architecture/overengineering problems are suspected. First run scoped **Codex read-only AS-IS reconnaissance** in the real repository, preserving dirty/untracked work, history and live behavior; tests that may mutate data need explicit safe authorization. Web compares observed behavior and evidence with customer-approved requirements, prioritizes `KEEP / FIX NOW / IMPROVE LATER / NEEDS DECISION`, and approves **one** evidence-backed remediation slice with baseline, regression/compatibility proof and safe rollback. Reuse existing PROJECT/TODO and goal graph; no new project scaffolding by default. Detailed workflow in [modules/environment.md](modules/environment.md), [modules/architecture.md](modules/architecture.md), [modules/delivery.md](modules/delivery.md) and the Russian [USER_GUIDE.md](USER_GUIDE.md). This is methodology guidance, not an audit run on the user's product.

## Workflow

ChatGPT Web is the analyst/architect, Codex Desktop executes and tests inside each real product repository, and the user approves significant decisions. The process is **dynamic**: FAST for safe local changes, STANDARD for ordinary implementation, CONTROLLED for risky architecture, production operations, sensitive data, security or other high-consequence work. It must **switch during a task** when facts change; see `modules/delivery.md`.

## Chat continuity and isolated experiments

Continue in the same chat by default; create a new one only for a genuinely different track, independent review or unusable context. Keep a chat register only for actual parallel tracks. Experiments with side effects use an **approved isolated branch/worktree or disposable repo**, never `main`; read-only analysis needs neither a new chat nor a branch. Never auto-merge, reset or delete user work. See `modules/delivery.md` and [USER_GUIDE.md](USER_GUIDE.md). Textual rules are not verified sandbox enforcement.

## Single file handoff Codex → Web

Codex final response is the **evidence index**: real changed paths, tests/exit and verifiable refs, not a fresh full report file or an upload of the entire project. If the Web chat already has access to a reviewed GitHub commit/PR, cite exact paths/ref. Local Codex paths and unpushed commits are **not** readable from Web. For necessary small sanitized attachments, use a separately approved `.ai-handoff/<TASK_ID>/` directory within the product worktree (gitignored if configured) and explicitly direct the user to upload those files to the **named Web chat**. Only explicitly approved reviewed evidence belongs in shared `docs/ai/evidence/<TASK_ID>/`; no automatic push, secrets, dataset dumps, weights or model checkpoints. See `templates/codex-report.md`.

## Runtime outcomes, model evals and engineering feedback (draft, NOT PILOT-VALIDATED)

New task-specific rules are documented in the existing `modules/delivery.md`, `modules/requirements.md` and `modules/environment.md`:
- **Accept user-visible outcomes**, not a green compilation alone: browser/mobile journey when UI work warrants it, or real API/CLI/ML inference/behavior for other products. Give exact `PASS / FAIL / NOT RUN / NOT APPLICABLE` with real evidence.
- **Allow bounded in-task autonomy**: for FAST/STANDARD, Codex may adjust related implementation files and direct tests within the approved feature, run checks and repair ordinary failures without new permission per file. STOP for critical decisions, protected data/CI/deps, weakened tests or another goal.
- **Use versioned reproducible model comparisons** for ML/LLM experiments: approved data/task set, leakage/split policy, baseline and metrics, reproducibility, critical slices and signoff before promotion.
- **Set up actual project-specific GitHub PR/CI/permission controls** in the PRODUCT repo only with user approval and safe tests; verify branch/PR/CI readability from Web before claiming independent review. A methodology instruction cannot install GitHub branch protection or Codex sandbox enforcement.
- **Turn failures into regression experiments** in existing `TEST_CASES.md`; don't count new wording as a passed test. Keep the context minimal; compare shortened CORE against the baseline before discarding crucial safety rules.

**Activation is separate from documentation:** install and run the relevant product controls only after a scoped approved Bootstrap, then record observed results and safe fallback. No generic all-stack Playwright installation, PR automation, Honcho/multiagent runtime or GitHub production changes are implied by this methodology commit.

## Optional usage observability — metadata, not surveillance

To analyze token/credit consumption across Web, Codex and API tasks, see [modules/usage-observability.md](modules/usage-observability.md). Use native provider Usage screens where available, then record **only explicitly supplied measurements** with an optional offline standard-library helper [tools/usage_report.py](tools/usage_report.py); a [clearly synthetic example](templates/usage-events.example.jsonl) demonstrates its JSONL format. The helper cannot access subscription ChatGPT Web per-turn token telemetry, does not read Codex sessions, and never runs automatically. It stores no prompts, code or secret keys. Keep the real ledger private in an approved location (e.g. a gitignored product `.ai-handoff/usage/`) and share only the reviewed Markdown summary for a later Web analysis. Missing figures are UNKNOWN; optimize observed **cost/effort per accepted outcome**, not isolated token counts. Enabling this in an actual product repo requires a separate approval.

## Daily loop — one useful result, minimal ceremony

For an ordinary task: **user goal → ChatGPT Web scopes a verifiable slice when needed → one approved Codex task → actual diff/checks → user acceptance → STOP**. Truly safe, local FAST edits may go straight to Codex under the project's existing AGENTS. Do not fill every template or open every module for every task. Keep the current Codex chat by default; a new chat is optional only when context is no longer useful, for independent review or at the user's request.

### Practical Git evidence in a PRODUCT repository

Before a task, record the current branch, HEAD and any pre-existing dirty/untracked paths. After Codex reports completion, independently inspect the real repository with:

```sh
git status --short
git diff --name-status
git diff --cached --name-status
git diff --name-status <TASK_BASE_SHA> HEAD
git ls-files --others --exclude-standard
git diff --check
```

Replace `<TASK_BASE_SHA>` with the captured starting commit. The committed diff command assumes that task baseline is an ancestor of HEAD; use an appropriate comparison if history was rewritten. Separate pre-existing user changes from task changes; compare the task diff with the approved feature/component boundary, and also with exact permitted paths for CONTROLLED tasks when specified. Run the project's actual verification command independently when warranted, checking its exit status. Git path checks **detect changes; they do not enforce per-file permissions or prove behavior correct**. Never auto-reset, clean, or delete a dirty worktree.

### Pilot priority — NOT RUN

Before declaring a stable release, use a disposable product repository and real Codex Desktop to run **T03** (tiny FAST change without bureaucracy), **T37 + T08** (out-of-scope file stops and independently inspected Git diff/checks), and **T15** (fresh-chat recovery from verified project state). Record environment, commit SHA, real outputs and PASS/FAIL in `TEST_CASES.md` only after execution. This methodology repo cannot itself establish those outcomes; no mandatory universal `STATE.md`, verification script, or Skills framework is introduced.

## Reliable start in ChatGPT Web

1. Create a ChatGPT Project per product. Place the full `CORE.md` text in **Project settings → Instructions** (subject to the actual UI's size limit), rather than assuming a GitHub URL loads it. If it does not fit, keep a shortened faithful CORE in instructions and attach the full file.
2. Provide a link to https://github.com/sosiska-monster/ai-development-os and ask ChatGPT to read `MANIFEST.md` plus a relevant module. Confirm GitHub access or attach the specific files; **public or private** visibility alone does not guarantee the selected ChatGPT mode can read them.
3. When the assistant uses an external module, it should identify what it actually read and which commit/ref it could verify. No invented version, link, full-read claim or deterministic access guarantee.
4. Submit the customer's raw specification. ChatGPT works from customer intent toward a small approved Blueprint and project Environment Profile. Existing codebases can start with a read-only Codex audit.
5. For a new project, after approved requirements/architecture and a separate request, ChatGPT prepares a minimal project-specific Codex Bootstrap. For an existing product, start from its actual code and working setup: only propose necessary adaptations, never run a generic reinitialization.
6. Small reversible tasks can run directly in Codex under project `AGENTS.md`; promote to more controlled review when risk/scope grows. Keep evidence and a resynchronization checkpoint for ChatGPT.

Sample launch message:

> Ты мой инженерный архитектор в ChatGPT Web; Codex Desktop пишет код. Моё постоянное ядро лежит в инструкциях этого ChatGPT Project. Библиотека: https://github.com/sosiska-monster/ai-development-os . Прочитай MANIFEST.md и только нужные модули, честно назови реально прочитанные файлы и проверенную версию. Сначала разберём ТЗ и архитектуру; проектный Codex Bootstrap только после согласования и моего отдельного запроса.

## Library map

- [CORE.md](CORE.md) — permanently active ChatGPT policy
- [MANIFEST.md](MANIFEST.md) — dynamic routing, source integrity
- [modules/](modules/) — requirements, architecture, environment, delivery, memory, security
- [templates/](templates/) — generic task, report, bootstrap, memory and requirements formats
- [TEST_CASES.md](TEST_CASES.md) — reproducible negative/positive evaluation, not claimed PASS
- [RATIONALE.md](RATIONALE.md) — *why* the methodology is designed this way, rejected alternatives and revisit triggers
- [MAINTENANCE.md](MAINTENANCE.md) — *how* to change the library safely
- [CHANGELOG.md](CHANGELOG.md) — history and release state

## Boundaries, privacy and versioning

No client secrets, contracts, personally identifying project data or code belong in this central library. Personal `WordStyle.md` belongs outside customer repositories. Project-state files (such as `PROJECT.md` and `REQUIREMENTS.md`) belong to the **product** repository, not this library. If AI use of customer material is contractually restricted, obtain permission or use an approved environment before sharing it.

Pin a reviewed release to an immutable commit SHA; use tags as human-readable release markers only after validation. A named draft in `main` is not a verified release. This repository's published guidance does not silently upgrade existing product-level `AGENTS.md`.
