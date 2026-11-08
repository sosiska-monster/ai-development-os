# RATIONALE — почему AI Development OS устроена именно так

**Назначение:** постоянная память **методологии**, а не клиентского продукта. Хранит причины выбора структуры, ранее выявленные проблемы, рассмотренные альтернативы, допустимые компромиссы и условия пересмотра. Перед изменением организации библиотеки сначала читай соответствующие записи. Не используй этот документ как повод автоматически расширять ядро инструкций.

## Правила ведения

- Записывай **решения по устройству библиотеки**, а не обычные проектные решения заказчиков (для них есть `Decision.md` в репозитории продукта).
- Каждая запись: ID, статус, контекст, решение, почему, отвергнутая альтернатива, минусы, когда пересмотреть, ссылка на изменение/проверку при наличии.
- Разделяй факт, наблюдение, гипотезу и пользовательское предпочтение. Не придумывай результаты экспериментов.
- Новая запись нужна при **значимом** изменении библиотеки, а не каждой правке текста.
- Старые решения не стирай: помечай SUPERSEDED и связывай с новым.

## RAD-001 — Разделяем ChatGPT Web и Codex Desktop

**Статус:** APPROVED AS DESIGN DIRECTION (согласовано в обсуждении).  
**Контекст:** пользователь работает в браузере ChatGPT и отдельном установленном Codex.  
**Решение:** ChatGPT отвечает за требования/архитектуру/проверку, Codex — за код/файлы/Git/тесты.  
**Почему:** не приписываем ChatGPT доступ, которого у него нет, и не смешиваем общий управляющий промпт с локальными правилами исполнителя.  
**Отвергнуто:** один огромный промпт, который якобы сам всё делает в репозитории.  
**Пересмотреть:** если появится подтверждённое прямое безопасное подключение, позволяющее автоматизировать передачу без потери контроля.

## RAD-002 — Короткое CORE + выборочные модули

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Контекст:** большой мастер-промпт сам создавал перегрузку контекста, запреты и ритуалы.  
**Решение:** `CORE.md` всегда; `MANIFEST.md` маршрутизирует к тематическим модулям по запросу.  
**Почему:** сохраняем подробные процедуры, не загружая их все в каждом вопросе.  
**Отвергнуто:** мегапромпт из десятков обязательных разделов; один Skill на каждый случай.  
**Минусы:** нужна доступность GitHub и аккуратная маршрутизация, не гарантируется идеальное автоматическое чтение.  
**Пересмотреть:** если практические испытания покажут проблемы с загрузкой модулей — упростить структуру или закрепить критические правила в проектных инструкциях.

## RAD-003 — GitHub как источник версионируемой методологии

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Контекст:** пользователь хочет давать ChatGPT одну ссылку вместо ручной загрузки файлов при каждом проекте.  
**Решение:** отдельный центральный репозиторий для инструкций, шаблонов и обоснований; версии фиксируются тегами.  
**Почему:** одно место для исправлений и контроля эволюции; проекты не получают незаметно новые правила из `main`.  
**Отвергнуто:** копировать все инструкции в каждый новый ChatGPT Project или смешивать библиотеку с кодом продукта.  
**Минусы:** GitHub-коннектор и права на приватные репозитории могут быть недоступны в конкретном режиме.  
**Пересмотреть:** при подтверждённом лучшем способе версионируемой доставки файлов.

## RAD-004 — Память проекта специализированная, не транскрипт чатов

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Решение:** `PROJECT.md` (паспорт ≤200 строк), `TODO.md`, `Bugs.md`, `Gotchas.md`, `Decision.md`; личный `WordStyle.md` отдельно.  
**Почему:** не терять состояние при новых сессиях, искать прежние баги и не дублировать знания.  
**Отвергнуто:** один бесконечный HANDOFF или история чата как единственный источник истины.  
**Риски:** отравление памяти ложными причинами; поэтому утверждённые решения и значимые диагностические выводы требуют доказательств/ревью.  
**Пересмотреть:** если реальный проект мал, разрешить объединение файлов без потери назначений; не плодить пустые документы.

## RAD-005 — Git checkpoints и проактивное восстановление

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Решение:** логические проверенные коммиты и контрольные точки до рискованных изменений; ChatGPT сам должен рекомендовать откат при признаках тупика.  
**Почему:** не наращивать сложность бесконечными исправлениями и не требовать, чтобы пользователь сам обнаружил точку отката.  
**Отвергнуто:** безусловный reset, переписывание общей истории, автоматическое удаление неудачных веток.  
**Риски:** Git не откатывает БД и внешние побочные эффекты.  
**Пересмотреть:** исходя из типа среды Codex, Git-flow команды и продукта.

## RAD-006 — Сначала технические проверки, потом Skills

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Решение:** обязательные правила — в кратком `AGENTS.md` и где возможно в проверках; Skills только для нужных повторяемых процедур.  
**Почему:** Skills могут подключаться по релевантности, их загрузка не является гарантией обязательного контроля.  
**Отвергнуто:** заставить каждую микрозадачу запускать тяжёлый универсальный Skill, множество MCP и субагентов.  
**Пересмотреть:** если фактические метрики показывают устойчивую пользу конкретного Skill.

## RAD-007 — Evidence Report вместо «всё работает»

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Решение:** отчёт Codex включает состояние Git, статистику изменения от базовой точки, команды и коды завершения проверок, затронутые тесты и зависимости.  
**Почему:** пересказ AI нельзя считать проверкой.  
**Отвергнуто:** только субъективный отчёт; обязательная пересылка полного гигантского лога в чат.  
**Риски:** пустой `git diff --stat` после коммита, поэтому использовать сравнение с базой или `git show`; секреты маскировать.  
**Пересмотреть:** при доступности надёжного автоматического доступа ChatGPT к diff и CI артефактам.

## RAD-008 — Методологии как идеи, не пакет обязательных инструментов

**Статус:** APPROVED AS DESIGN DIRECTION.  
**Решение:** SDD/BDD для требований, BMAD-подобная адаптивность, GSD-вертикальные срезы, Ralph-подобные чистые сессии, Harness Engineering для среды.  
**Почему:** совокупная установка всех методологических фреймворков дублирует процессы и увеличивает стоимость обслуживания.  
**Отвергнуто:** установить BMAD + GSD + OpenSpec + Ralph в каждый проект по умолчанию.  
**Пересмотреть:** только когда особенности конкретного проекта доказывают пользу определённого инструмента.

## Шаблон новой записи

```md
## RAD-009 — <название>
**Статус:** PROPOSED | APPROVED | SUPERSEDED | REJECTED
**Контекст:** …
**Решение:** …
**Почему:** …
**Альтернативы:** …
**Минусы/риски:** …
**Доказательство или ссылка на проверку:** …
**Пересмотреть, если:** …
```

**Уточнение RAD-008 (2026-11-02):** минимально достаточная архитектура — именно **стартовое решение по умолчанию**, а не один из равноправных вариантов. Сначала переиспользуем существующую систему либо выбираем простую цельную реализацию для нового продукта; новые сервисы, слои и зависимости требуют конкретной проверяемой причины. Это не требование уменьшать число строк и не разрешение ослаблять безопасность production. Применять без добавления новой обязательной документации или отдельного режима.

## RAD-009 — Dynamic modes without fixed file-count routing (0.2.0-draft)

**Status:** IMPLEMENTED IN DRAFT, PILOT NOT RUN.
**Decision:** FAST / STANDARD / CONTROLLED selected and re-evaluated per task using effect, risk, reversibility, uncertainty and newly found facts. Escalation stops new risky scope and seeks authority; de-escalation is permitted after risk removal, without dropping necessary checks.
**Why:** serial micro-edits must not require a manual ChatGPT shuttle, while a single-line migration/security change must not be classified as cheap by file count.
**Rejected:** fixed two-file gate; every task through the complete OS.
**Test:** T03–T05.

## RAD-010 — CORE in ChatGPT Project instructions; GitHub is modular source

**Status:** IMPLEMENTED IN DRAFT, DELIVERY NOT VERIFIED.
**Decision:** critical CORE is permanently provided in Project instructions (or concise faithful version when UI limit requires); GitHub modules are retrieved on demand with honest actual-read/ref disclosures.
**Why:** a link/connector is not deterministic full-file instruction transport.
**Rejected:** remote-only mandatory CORE; blocking a harmless task solely for missing optional module.
**Test:** T01–T02, T17. Revisit if verified direct immutable module retrieval becomes reliable.

## RAD-011 — Independent evidence and scope checks

**Status:** IMPLEMENTED AS CONTRACT, enforcement per product remains unverified.
**Decision:** Lite/Full reports, actual committed + staged/unstaged + untracked diff paths against scoped task, verified test/CI/reviewer artifacts. Report alone is not independent proof.
**Rejected:** treating a plausible Codex summary, a post-commit empty diff or a bare path whitelist as correctness.
**Test:** T08–T09. Revisit with documented platform-native independent review.

## RAD-012 — Requirements authority and persistent ledger

**Status:** IMPLEMENTED AS TEMPLATE, PILOT NOT RUN.
**Decision:** confirmed client behaviors live in a requirements ledger when materially needed; approval provenance distinct from implementation verification and developer technical decisions; preserve SUPERSEDED history.
**Rejected:** using chat memory/Decision.md as the sole specification.
**Test:** T06, T15.

## RAD-013 — Risk-calibrated harness, not universal shell policies

**Status:** IMPLEMENTED AS PROJECT SETUP PROTOCOL, NOT YET VERIFIED.
**Decision:** each real product's Codex environment must test actual controls (permissions, verify, CI, secrets, Git). Never assume hooks/rules/sandbox work based solely on documentation.
**Rejected:** universal untested Git command allowlists; untrusted magic deny rules and forced automated rollback after two failures.
**Test:** T07, T10–T11, T14.

## RAD-014 — Memory remains specialized but can be small

**Status:** IMPLEMENTED IN DRAFT; reevaluate after pilot.
**Decision:** retain distinct semantics of Bugs/Gotchas/Decisions and portable WordStyle preferences while permitting small project merges and requiring explicit PROPOSED/STALE/REVISIT_WHEN lifecycle.
**Rejected:** stuffing the entire history into AGENTS.md; auto-expiring user-approved decisions without review.
**Test:** T12–T13, T15.

## RAD-015 — Reject unreviewed production side effects

**Status:** IMPLEMENTED AS POLICY, NOT A TESTED PERMISSION BARRIER.
**Decision:** CONTROLLED mode for irreversible/data/production work, staging rehearsal, recoverable backups and separate human operator approval; Git does not undo external effects.
**Rejected:** treating a down migration or reset as automatically safe.
**Test:** T14.

## RAD-016 — Product assurance and task risk are different axes (0.2.0-draft)

**Status:** IMPLEMENTED AS DRAFT GUIDANCE, PILOT NOT RUN.
**Observation:** current task-level risk routing cannot distinguish a disposable demo from a long-lived customer-facing service with different quality, lifetime and operational obligations.
**Decision:** define a lightweight **Product Assurance Profile** in Blueprint / PROJECT / Environment Profile (intended audience, expected lifetime, exposure/data, failure impact, support and recovery expectations, time/budget and proportionate Definition of Done). Use PROTOTYPE / MVP / PRODUCTION / CRITICAL as revisable example levels, not rigid technical stacks. Keep dynamic FAST / STANDARD / CONTROLLED routing independent and risk-triggered. Require explicit user approval of the target quality bar and revisit it before a prototype is exposed to real production conditions.
**Why:** avoid both overengineering throwaway demos and underengineering long-lived services. Quality means fit-for-purpose verified behavior, not maximum code, files, bureaucracy or infrastructure.
**Rejected:** universally production-grade architecture, automatic classification from the word "prototype", making all production edits CONTROLLED, treating prototype status as a waiver for security/data obligations.
**Cost/risks:** another concept might add process burden; keep profile to a few lines and default to project documents already needed.
**Tests:** T18–T20; NOT RUN.
**Revisit when:** observed pilot outcomes show unnecessary checks, neglected baseline controls, or confusing quality-tier language.

**Уточнение RAD-016 — composable MVP (2026-11-03):** если задача — проверить продукт на рынке, система предлагает собрать минимальный работающий вариант из подходящих готовых решений, запустить для реальных пользователей только после соразмерных фактическому риску проверок, а затем улучшать/заменять лишь те модули, проблемы которых подтверждены спросом, ограничениями или сбоями. Это **не** оправдывает игнорирование безопасности при обработке реальных данных и **не** требует заранее строить универсальную заменяемость всех компонентов. Цель — меньше собственного кода и преждевременного переписывания.

## RAD-017 — Model selection and reasoning effort are adaptive execution controls (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE, NATIVE UI SWITCHING NOT CONTROLLED BY MARKDOWN; PILOT NOT RUN.
**Context:** a different model or reasoning effort may improve a difficult decision, but using maximum effort for every small task wastes latency/allowance. Product assurance and task risk do not measure cognitive difficulty.
**Decision:** choose available model and effort by actual reasoning demand, context/tool compatibility, observed quality, budget and latency. Prefer native Default/auto routing if provided and verified, otherwise give minimal actionable **manual recommendations**; raise capability/effort for genuinely difficult analysis, lower it for bounded implementation. Never assert that CORE/AGENTS changed a model picker. Ensure approvals, verification, confidentiality and product assurance stay unchanged when switching.
**Rejected:** hard-coding a vendor/model into a permanent policy, mapping FAST to low and CONTROLLED to max unconditionally, blindly retrying high effort, adding a costly multi-agent orchestration layer before pilot evidence.
**Costs/risks:** misleading claims of automatic controls; switching may lose context or support different tools, and expensive effort does not guarantee correctness. Establish actual settings/permissions and measure verified outcomes and rework.
**Tests:** T21–T25, NOT RUN.
**Revisit when:** new native model-routing controls become available, available models change, or measured quality/latency demonstrates a different default.

## RAD-018 — Scope-aware housekeeping between tasks (0.2.0-draft)

**Status:** IMPLEMENTED AS DRAFT POLICY; PILOT NOT RUN.  
**Observation:** Codex can accumulate avoidable duplicate helpers, dead code, debugging statements and stale task-specific text across successive tasks, while the user sees primarily additions rather than simplifications. This is a reported usability concern, not proof that all code growth is waste.
**Decision:** at a natural verified task checkpoint or after a small batch of FAST tasks, perform a **light Hygiene Sweep** of task-introduced waste. Safely simplify/remove only clearly redundant material *within already approved scope*; re-run relevant checks and inspect actual diff. Propose cross-scope, ambiguous or potentially destructive cleanup as a separate reviewed task. Skip when there is nothing useful to remove.
**Why:** encourage simplicity and maintenance without confusing file deletion or negative line deltas with engineering quality. Keep scope boundaries, user ownership and independent evidence intact.
**Rejected:** unconditional cleanup after every microtask, automatic repository-wide refactoring, deleting untracked/dirty files, `git clean/reset`, blanket cache removal and mandatory line-count reduction.
**Cost/risks:** mistaken dead-code classification can break behavior or destroy user work; minimize impact by grounding in references/tests, respecting task scope, and escalating uncertainty.
**Tests:** T26–T29 (NOT RUN).
**Revisit when:** the pilot finds high overhead, missed debris, or unsafe cleanup suggestions.

## RAD-019 — One authorized task, concise report, human gate and context rotation (0.2.0-draft)

**Status:** IMPLEMENTED AS DRAFT INSTRUCTIONS; REAL CODEX PILOT NOT RUN.
**Observation:** user wants full control over which task Codex performs next and wants to prevent long tool-log and failed-attempt context from contaminating subsequent tasks.
**Decision:** default to exactly **one authorized outcome** with necessary internal implementation steps, verified change evidence, short Russian status and **STOP pending the next explicit user instruction**. Every final task report MUST state **NEW CHAT: YES/NO with reason**; after DONE default to YES for a distinct next task. This is a visible recommendation and human boundary, not automatic UI control or forced restart. At natural boundaries update only durable verified facts in existing PROJECT/TODO as necessary; for a separate next task suggest a **user-opened new Codex chat** by default, especially if the current thread is noisy. For continuation of the SAME unfinished task, prefer supported native compaction rather than forced restart. No new per-task handoff files, Skills or context routers.
**Why:** retain human control and context relevance without overloading small tasks with giant evidence reports. A chat reset is not a filesystem cleanup, and a textual instruction does not control the Codex app's chat UI.
**Rejected:** automatically processing the full roadmap, unattended Goal continuation across tasks, requiring a fresh thread every turn, automatic history deletion / `.codex` cleanup, inventing context-percent thresholds, and treating compaction/fork as equivalent to a clean new thread.
**Trade-offs:** frequent new chats may require rediscovery of project facts; preserve concise verified project state, risk gates and Git history. Context compaction and new-thread UI support depend on the actual Codex surface.
**Tests:** T30–T33 (NOT RUN).
**Revisit when:** task-boundary behavior fails in Codex or context resets create more overhead than they avoid.

## RAD-020 — Web architect authors one write-scoped Codex task at a time (0.2.0-draft)

**Status:** IMPLEMENTED AS DRAFT INSTRUCTIONS; LIVE TASK PILOT NOT RUN.
**Observation:** user wants ChatGPT Web to plan/curate the project and issue tightly bounded single-result prompts to Codex, instead of letting Codex pick later roadmap steps or expand code unpredictably.
**Decision:** ChatGPT Web owns task selection and approved architecture. Every Codex implementation prompt authorizes **one verifiable outcome** and declares READ CONTEXT separately from a narrow WRITE ALLOWLIST and DO NOT MODIFY. Unknown paths require read-only recon first. Codex stops for approval before any extra paths, tests, dependencies, memory writes or new components, then returns a short report and STOPS.
**Why:** preserves human direction and limits task drift with a minimal contract rather than additional tools, agents or per-task files.
**Limit:** prompt/AGENTS restrictions are behavioral, **not filesystem access controls**; tighter protection requires configured and verified sandbox/permissions or isolated workspaces, plus actual diff review. Worktree isolation does not itself enforce a per-file allowlist.
**Rejected:** free-form implement-next-roadmap prompts, silent "needed" exceptions, full planning documents for trivial tasks, mandatory external task orchestrator.
**Tests:** T36–T38 (NOT RUN).
**Revisit when:** repeated out-of-scope writes indicate mechanical safeguards are needed or manual approvals become excessive.

## RAD-021 — Web decomposition and evidence-based challenge (0.2.0-draft)

**Status:** IMPLEMENTED AS DRAFT GUIDANCE; LIVE PILOT NOT RUN.
**Observation:** user wants the Web architect to own MVP breakdown into small, light tasks and to disagree constructively when a suggested implementation contradicts confirmed specifications or creates unnecessary complexity.
**Decision:** Web maintains a lightweight dependency-aware roadmap but dispatches exactly one independently reviewable, verifiable vertical slice per Codex prompt, using an explicitly limited write scope and a human approval gate. Slices must be small enough for focused diff/check review, not mechanically one file or one line. Web distinguishes **customer-approved desired behavior** from **developer-proposed implementation**; when the latter conflicts with requirements, environment, evidence, or KISS/YAGNI, it explains a concrete mismatch/uncertainty, consequence, simpler alternative and decision needed. It does not manufacture objections or silently override customer authority.
**Why:** prevent large uncontrolled implementation batches, needless architecture and sycophantic technical approvals without creating a heavy task-management system.
**Rejected:** giant roadmap prompts sent directly to Codex, compulsory multi-agent planning, one-file quotas, endless argument or changing client-confirmed requirements unilaterally.
**Costs/risks:** too-fine decomposition can increase handoff overhead; apply one coherent result and clear acceptance, combining necessary steps within that task. Technical disagreement must be evidence-based and proportional to impact.
**Tests:** T39–T42 (NOT RUN).
**Revisit when:** the pilot shows unnecessary gatekeeping, fragmented work or unchecked expansion.

## RAD-022 — Web proactively chooses the next useful experiment (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE; REAL CODEX/WEB PILOT NOT RUN.
**Observation:** the methodology should independently notice when an approach (including memory, model routing or task process) could be improved, rather than merely accepting new tool suggestions or waiting for the user to specify which experiment to try.
**Decision:** at natural checkpoints, Web inspects actual evidence, generates a few plausible options including no change, prioritizes likely benefit against confidence, cost, risk, privacy and reversibility, and selects **one falsifiable experiment** with baseline, metric, threshold and stopping rule. If evidence is missing, choose measurement; if no meaningful bottleneck exists, do nothing. Product delivery remains primary. Codex only runs a separately authorized, scoped one-task experiment and stops. No automatic external API uploads or infrastructure installs.
**Why:** enables intelligent continuous improvement **without** introducing an autonomous experiment orchestrator, accumulating speculative tooling or overriding human control.
**Rejected:** installing Honcho or any fashionable tool without measured need; fabricated performance scores; trials on customer secrets; automatic multi-task loops; mandatory experiment registry.
**Tests:** T43–T46, NOT RUN.
**Revisit when:** measured pilots show poor experiment prioritization, excessive suggestion noise, missed high-value improvements or unreasonable approval overhead.

## RAD-023 — Named Web chat ownership and sandboxed experiments (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE; LIVE CHAT/CODEX ISOLATION TEST NOT RUN.
**Observation:** a Web task dispatcher saying only "new/current chat" or YES/NO leaves the human unsure where to paste a prompt. Worse, a disposable model experiment could accidentally mutate the mainline product branch or global environment.
**Decision:** Web explicitly routes each prompt to a named, user-confirmed ChatGPT Web or Codex Desktop chat with its responsibility and actual branch/worktree; proposals remain PROPOSED until created. Record a concise Chat Register in the product's existing PROJECT.md or maintained ChatGPT Project source, accessible to future Web chats; it stores names, purpose, status and verified Git context, **not** complete transcripts. For write-capable experiments, require a separately approved disposable worktree/branch or isolated repo, plus dependency/data isolation where necessary. Codex must check actual cwd/branch/dirty state and stop on mainline mismatch before side effects. Failed trials are archived without mainline merge; promote or clean up only with explicit scoped approval and actual diff/data checks.
**Why:** human can route tasks reliably, recover cross-chat ownership without fictitious memory, and experiment safely without contaminating the working product.
**Rejected:** hard-coded YES/NO instead of destination, assuming Web can create or enumerate other chats, using Git branch naming as proof of sandbox, automatic global uninstall, forced branch deletion/clean/reset, or new project-management infrastructure.
**Limit:** a Git worktree does not isolate external services, global installs or sensitive data, and model prompts do not enforce filesystem access; each boundary needs operational verification.
**Tests:** T47–T52; NOT RUN.
**Revisit when:** a real pilot demonstrates registry maintenance costs more than it saves or isolation/route behavior fails.

