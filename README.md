# AI Development OS — adaptive engineering instruction library

Version: **0.2.0-draft (unreleased, not pilot-validated)**. This repository is the *methodology*, not any customer's application.

**Русская инструкция для пользователя:** [USER_GUIDE.md](USER_GUIDE.md) — весь маршрут **ТЗ → MVP → Codex → проверки → staging → production**, выбор уровня ChatGPT/Codex и готовые сообщения. Это руководство для человека: не добавляйте его целиком в Project Instructions и не загружайте на каждую задачу.

## Workflow

ChatGPT Web is the analyst/architect, Codex Desktop executes and tests inside each real product repository, and the user approves significant decisions. The process is **dynamic**: FAST for safe local changes, STANDARD for ordinary implementation, CONTROLLED for architecture, sensitive data, production, security or other high risks. It must **switch during a task** when facts change; see `modules/delivery.md`.

## Daily loop — one useful result, minimal ceremony

For an ordinary task: **user goal → ChatGPT Web scopes a verifiable slice when needed → one approved Codex task → actual diff/checks → user acceptance → STOP**. Truly safe, local FAST edits may go straight to Codex under the project's existing AGENTS. Do not fill every template or open every module for every task. A fresh Codex chat is a recommendation for an independent next task, **not a forced reset**.

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

Replace `<TASK_BASE_SHA>` with the captured starting commit. The committed diff command assumes that task baseline is an ancestor of HEAD; use an appropriate comparison if history was rewritten. Separate pre-existing user changes from task changes; compare all task-edited paths with the approved WRITE ALLOWLIST. Run the project's actual verification command independently when warranted, checking its exit status. Git path checks **detect changes; they do not enforce per-file permissions or prove behavior correct**. Never auto-reset, clean, or delete a dirty worktree.

### Pilot priority — NOT RUN

Before declaring a stable release, use a disposable product repository and real Codex Desktop to run **T03** (tiny FAST change without bureaucracy), **T37 + T08** (out-of-scope file stops and independently inspected Git diff/checks), and **T15** (fresh-chat recovery from verified project state). Record environment, commit SHA, real outputs and PASS/FAIL in `TEST_CASES.md` only after execution. This methodology repo cannot itself establish those outcomes; no mandatory universal `STATE.md`, verification script, or Skills framework is introduced.

## Reliable start in ChatGPT Web

1. Create a ChatGPT Project per product. Place the full `CORE.md` text in **Project settings → Instructions** (subject to the actual UI's size limit), rather than assuming a GitHub URL loads it. If it does not fit, keep a shortened faithful CORE in instructions and attach the full file.
2. Provide a link to https://github.com/sosiska-monster/ai-development-os and ask ChatGPT to read `MANIFEST.md` plus a relevant module. Confirm GitHub access or attach the specific files; **public or private** visibility alone does not guarantee the selected ChatGPT mode can read them.
3. When the assistant uses an external module, it should identify what it actually read and which commit/ref it could verify. No invented version, link, full-read claim or deterministic access guarantee.
4. Submit the customer's raw specification. ChatGPT works from customer intent toward a small approved Blueprint and project Environment Profile. Existing codebases can start with a read-only Codex audit.
5. Only after the approved architecture/environment **and a separate request**, ChatGPT creates a project-specific Codex Bootstrap. Codex creates/updates only the approved setup in the **product** repo; never apply a generic bootstrap blindly.
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
