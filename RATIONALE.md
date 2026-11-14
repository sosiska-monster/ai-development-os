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

**Status:** HISTORICAL; chat-rotation details SUPERSEDED BY PR #3, main merge ef63d9ce. REAL CODEX PILOT NOT RUN.
**Current rule:** one approved outcome and STOP still apply; **same chat by default**. No mandatory NEW CHAT field or fresh chat after DONE. The original decision below is retained as historical context, not current instruction.
**Observation:** user wants full control over which task Codex performs next and wants to prevent long tool-log and failed-attempt context from contaminating subsequent tasks.
**Decision:** default to exactly **one authorized outcome** with necessary internal implementation steps, verified change evidence, short Russian status and **STOP pending the next explicit user instruction**. Every final task report MUST state **NEW CHAT: YES/NO with reason**; after DONE default to YES for a distinct next task. This is a visible recommendation and human boundary, not automatic UI control or forced restart. At natural boundaries update only durable verified facts in existing PROJECT/TODO as necessary; for a separate next task suggest a **user-opened new Codex chat** by default, especially if the current thread is noisy. For continuation of the SAME unfinished task, prefer supported native compaction rather than forced restart. No new per-task handoff files, Skills or context routers.
**Why:** retain human control and context relevance without overloading small tasks with giant evidence reports. A chat reset is not a filesystem cleanup, and a textual instruction does not control the Codex app's chat UI.
**Rejected:** automatically processing the full roadmap, unattended Goal continuation across tasks, requiring a fresh thread every turn, automatic history deletion / `.codex` cleanup, inventing context-percent thresholds, and treating compaction/fork as equivalent to a clean new thread.
**Trade-offs:** frequent new chats may require rediscovery of project facts; preserve concise verified project state, risk gates and Git history. Context compaction and new-thread UI support depend on the actual Codex surface.
**Tests:** T30–T33 (NOT RUN).
**Revisit when:** task-boundary behavior fails in Codex or context resets create more overhead than they avoid.

## RAD-020 — Web architect authors one write-scoped Codex task at a time (0.2.0-draft)

**Status:** HISTORICAL; exact-file-scope details SUPERSEDED BY PR #3, main merge ef63d9ce. LIVE TASK PILOT NOT RUN.
**Current rule:** FAST/STANDARD can edit implementation files and direct tests **within the approved feature/component**; exact path restrictions apply to CONTROLLED when risk warrants. Critical decisions, dependencies, security, data, production operations and CI policy still require authorization. The original decision below is historical.
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

**Status:** HISTORICAL; mandatory chat routing/register SUPERSEDED BY PR #3, main merge ef63d9ce. LIVE CHAT/CODEX ISOLATION TEST NOT RUN.
**Current rule:** continue the same chat; an optional register is useful only for real parallel work. Name a confirmed/proposed recipient only on an actual handoff, archive separate experiment chats only if created, and isolate experiments with side effects. Original chat requirements below are historical.
**Observation:** a Web task dispatcher saying only "new/current chat" or YES/NO leaves the human unsure where to paste a prompt. Worse, a disposable model experiment could accidentally mutate the mainline product branch or global environment.
**Decision:** Web explicitly routes each prompt to a named, user-confirmed ChatGPT Web or Codex Desktop chat with its responsibility and actual branch/worktree; proposals remain PROPOSED until created. Record a concise Chat Register in the product's existing PROJECT.md or maintained ChatGPT Project source, accessible to future Web chats; it stores names, purpose, status and verified Git context, **not** complete transcripts. For write-capable experiments, require a separately approved disposable worktree/branch or isolated repo, plus dependency/data isolation where necessary. Codex must check actual cwd/branch/dirty state and stop on mainline mismatch before side effects. Failed trials are archived without mainline merge; promote or clean up only with explicit scoped approval and actual diff/data checks.
**Why:** human can route tasks reliably, recover cross-chat ownership without fictitious memory, and experiment safely without contaminating the working product.
**Rejected:** hard-coded YES/NO instead of destination, assuming Web can create or enumerate other chats, using Git branch naming as proof of sandbox, automatic global uninstall, forced branch deletion/clean/reset, or new project-management infrastructure.
**Limit:** a Git worktree does not isolate external services, global installs or sensitive data, and model prompts do not enforce filesystem access; each boundary needs operational verification.
**Tests:** T47–T52; NOT RUN.
**Revisit when:** a real pilot demonstrates registry maintenance costs more than it saves or isolation/route behavior fails.

## RAD-024 — Critical decisions must be approved, not inferred by Codex (0.2.0-draft)

**Status:** IMPLEMENTED AS INSTRUCTION, REAL TRAINING PILOT NOT RUN.
**Observation:** a Codex training task without an explicit data partitioning policy can silently choose a dataset split (for example, 42% train, 8% validation and the remainder test), leading to poor training capacity, inconsistent evaluation and unreviewed model assumptions. The actual user's split and reason must be verified rather than inferred from a conversational example.
**Decision:** ChatGPT Web identifies semantic/irreversible choices before task dispatch, particularly ML split counts/ratios, unit of independence, random/group/time strategy, seed, class balancing, evaluation metric and final holdout policy. It proposes a reasoned option and obtains explicit authorized approval. The task includes DECISION LOCK with provenance. Codex stops before training/data writes when a material choice is undefined or contradicted by reality. Code-level defaults are not user consent. For approved split operations, inspect actual counts, group/record disjointness, reproducibility, dataset version and leakage. Preserve earlier training artifacts and audit suspect metrics rather than auto-retraining or deleting.
**Why:** prevent executive discretion at implementation time from silently changing the scientific or product meaning of the task. Keep implementation autonomous within clear semantics and narrow safety boundaries.
**Rejected:** enforcing 80/10/10 on every dataset, demanding approval for trivial reversible coding choices, treating a green run as proof of correct sampling, rewriting checkpoints to conceal an unapproved previous run.
**Tests:** T53–T58 (NOT RUN).
**Revisit when:** pilots demonstrate excessive friction or unnoticed split/metric drift.

## RAD-025 — Reference-first Codex → Web evidence handoff (0.2.0-draft)

**Status:** IMPLEMENTED AS DRAFT GUIDANCE; LIVE WEB/CODEX TEST NOT RUN.
**Observation:** repeated manual transfer of assorted files from Codex Desktop into Web chat wastes time, duplicates code/logs, creates privacy risk and may imply falsely that ChatGPT can open arbitrary local files.
**Decision:** the final short Codex report is a self-contained **index** with real result/check/exit, exact source/artifact paths, branch/base/head SHA and explicit access status. Reuse existing GitHub/CI evidence when available. Local paths and unpushed commits are NOT Web-accessible. Only if Web needs selected actual files, propose an approved product-local `.ai-handoff/<TASK_ID>/` folder (gitignored where configured); it is writable **only when allowlisted** and transferred manually to the exact named Web chat. Only small reviewed non-sensitive evidence may be intentionally committed/pushed under separately approved `docs/ai/evidence/<TASK_ID>/`. No per-task mandatory report file or auto-push, no raw datasets, weights, secrets, long raw logs or auto-deletion. Respect isolated experiment worktrees.
**Why:** one predictable reference-based handoff saves user effort without inventing filesystem/connector transport or multiplying permanent project memory files.
**Rejected:** copying entire project per task; mandatory HANDOFF.md per micro-task; using a local path as a clickable Web attachment; implicit GitHub push; exempting artifact copying from WRITE ALLOWLIST; silent gitignore edits, auto-cleanup.
**Tests:** T59–T64, NOT RUN.
**Revisit when:** real pilots show manual attachment overhead or inaccessible refs remain recurring problems, with measurable benefits for a provider-backed artifact connector.

## RAD-026 — Product Goal Graph rooted in customer-accepted result (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE; LIVE WEB/CODEX PILOT NOT RUN.
**Observation:** separate agents optimize their local task descriptions differently when there is no durable, shared representation of the desired finished product. A flat backlog doesn't establish why a task matters or whether closing all tasks yields the customer-accepted system.
**Decision:** Web creates a customer-approved root outcome G0 with explicit end-to-end acceptance, decomposes into intermediate outcomes/atomic verifiable task leaves, and tracks **part-of** edges separately from a dependency DAG. Maintain stable IDs and requirement traceability in existing PROJECT/requirements plus TODO, not a mandatory new graph service. Prioritize only nearest READY leaves, require approved critical decisions and one scoped Codex task at a time; Codex can refine technical dependencies from actual read-only repository inspection. Verification evidence attaches to nodes; parent/root acceptance additionally requires integration/customer checks. Customer changes invalidate impacted descendants and dependencies. Speculative experiments are outside the required product tree until separately approved.
**Why:** make Web, Codex and user work toward the same measurable end state while retaining adaptability, evidence and minimal user bureaucracy.
**Rejected:** flat unrelated task lists as sole plan, hundreds of fully specified tasks before implementation, equating DONE leaves with accepted product, treating Mermaid screenshots as independent source of truth, automatic completion of all graph nodes or auto-merging experiment code.
**Tests:** T65–T68, NOT RUN.
**Revisit when:** actual pilot shows graph-maintenance overhead, poor task selection or inadequate customer acceptance traceability.

## RAD-027 — Web proposes a concrete product experience before Codex implements ambiguous UI (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE; LIVE WEB/CODEX PILOT NOT RUN.
**Observation:** both "build a pricing page" and a specification of three prices can leave material visual/interaction choices unresolved. Asking the user to design the page or sending a vague prompt directly to Codex causes unreviewed invention of user experience, billing semantics or business promises.
**Decision:** Web takes initiative to draft a concrete recommended user-visible experience, optionally showing a wireframe/visual concept and meaningful variants. Separate CONFIRMED customer facts from PROPOSED layout/UX and MISSING prices/payment semantics. For materially underspecified features, the goal-graph node waits in DESIGN_REVIEW until one coherent design and behavior contract is approved; then Web authorizes one Codex task with design trace, responsive behavior and objective acceptance. Codex retains autonomy for technical implementation details; trivial changes and existing approved designs skip the extra ceremony.
**Why:** reduce uncertainty without requiring the user to already know UI design; make pre-implementation approval meaningful and prevent Codex from silently inventing the product.
**Rejected:** Codex guessing pricing or substantial layout, turning all proposals into CONFIRMED requirements, mandatory pixel-perfect images before trivial edits, creating a design document per UI component, requiring user to answer endless open-ended preference questions.
**Tests:** T69–T72, NOT RUN.
**Revisit when:** real pilots show unnecessary approval overhead or persistent mismatch between proposed UI and Codex implementation.

## RAD-028 — Adopt measured engineering practices without a mandatory orchestrator (0.2.0-draft)

**Status:** IMPLEMENTED AS METHODOLOGY/TEMPLATES; LIVE PRODUCT CONTROL INSTALLATION AND PILOT NOT RUN.
**Evidence and motivation:** review of OpenAI/Anthropic coding-agent/harness, workflow and evaluation practices led to seven candidate gaps in AI Development OS: runtime outcome checks, independently observed CI/tool controls, real regression evals, bounded autonomous in-task fixes, ML/LLM comparable model eval, environmental isolation, and oversized prompt overhead. The methods are not a claim that vendor recommendations have been empirically proven optimal for this user's projects.
**Decision:** retain the small Web → approved Codex task → GitHub evidence loop. Use a risk/stack-appropriate **runtime customer journey** (browser if UI; real API/CLI/inference otherwise), verified PR CI/permission canaries in each actual product project, versioned model evaluation with approved baselines and holdouts, local safe self-repair *within* WRITE ALLOWLIST, and a traceable observation → reproducible regression → verified correction loop. Keep experiments separate from main and the critical human decision gate intact. Refine existing documents/templates instead of introducing a permanent multi-agent coordinator, Honcho, generic browser dependency or mandatory universal verification tool.
**GitHub Bridge:** commit vs push vs accessible PR are distinct states; no auto-push or auto-merge. A target Web conversation must prove access to the exact PR branch, CI status and full diff before code acceptance. Product-specific GitHub branch rules/CI may require an authorized repo administrator; this library repo does not configure unrelated product repositories.
**CORE budget:** shortened from 7,969 to 6,892 characters (~14%) while preserving critical rules; a real full-vs-short version comparison is planned, **NOT RUN**. Size reduction alone is not a measured quality improvement.
**Tests:** T73–T89 (new, all NOT RUN). Existing earlier cases likewise remain NOT RUN until observed in a disposable product repo; never report compliance as proven just because guidance was committed.
**Rejected:** automatically installing all tools in every product, treating green builds as user acceptance, using self-reports as independent evidence, auto-promoting a model, forcing a new agent or chat for every bounded local fix, declaring safety solely from written path allowlists, optimizing tokens without testing regression quality.
**Revisit when:** real pilots show repeated failures, measured user effort/rework, unavailable GitHub PR visibility or reduced compliance under the shortened CORE.

## RAD-029 — Opt-in metadata-only usage ledger, no background agent (0.2.0-draft)

**Status:** optional script and guidance committed to methodology; does not auto-collect actual ChatGPT/Codex tokens and is not installed in a PRODUCT repo. Real Web/Codex pilot NOT RUN.
**Problem:** token and credit consumption is invisible across some task boundaries, while the user wants to compare prompts, model/effort, manual handoffs and successful outcomes before asking Web to patch AI Development OS. Unlimited agent-based telemetry could itself waste tokens and expose private conversations.
**Decision:** start with provider-native Usage/Usage & billing views and, **only with approved local task-scoped operation**, an offline Python standard-library ledger at `tools/usage_report.py`, which accepts explicit observed task/surface or separately labeled period records, validates duplicate rows and produces privacy-minimal Markdown. Store actual records privately in an approved gitignored product workspace path, never in the methodology repo or public PR. Share only reviewed summary with Web. Record unknown fields as UNKNOWN, estimates separately from observed, cached input as part of input, credits separately from API dollars, no summing period and task snapshots. Track verification/acceptance and retries/handoffs/time alongside measured usage to optimize quality per completed task.
**Non-goals:** scanning Codex JSONL transcripts, automatic conversation interception, background monitors, extra agent, Honcho, telemetry SaaS, retrieving ChatGPT Web account metering without user access, changing subscription/model preferences without approval. A future locally tested numeric-only extractor is possible if actual manual capture has proven friction and user explicitly approves scope and privacy controls.
**Testing:** a local prototype of the offline helper was exercised on fabricated examples; the committed script has not been independently run against real Codex/ChatGPT exports. Real app input/measurement coverage and workflow are NOT VERIFIED. Tests T90–T97 NOT RUN.
**Revisit when:** multiple comparable accepted tasks provide enough observed data to identify repeat overhead; evaluate one changed variable at a time and verify quality before optimizing.

## RAD-030 — Brownfield is a first-class intake, no default project recreation (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE, NOT TESTED IN A REAL PRODUCT.
**Observation:** earlier workflow emphasizes a new customer's specification, architecture and Bootstrap. An active user may already have years of functionality, data, dirty changes and Git history, plus architectural debt. Treating that as a fresh project or rewriting everything destroys value and confuses working code with current requirements.
**Decision:** explicitly route both NEW and EXISTING products. Existing projects begin with a bounded **read-only AS-IS audit** of the actual repository and key observed behaviors, preserving all user work. Test/app execution is not assumed read-only if it writes caches, DB or external state. Web compares audit evidence with approved customer intent and existing Product Goal Graph, identifies real debt vs unverified code smells, ranks KEEP/FIX NOW/LATER/NEEDS DECISION, and authorizes **one small remediation goal** at a time. For consequential refactors, characterize existing behavior, preserve contracts/data/checkpoints, verify before/after and use approved rollback. Continue the ongoing product and TODO: do not replace its graph, Git or memory, automatically initialize/scaffold or run full Bootstrap. A large replacement is an exceptional separately approved proposal with evidence and migration plan.
**Why:** fix real overengineering/architecture issues without losing delivered value or introducing another design rewrite cycle; allow ongoing feature work to proceed when an unrelated debt item is speculative.
**Rejected:** indiscriminate whole-repository refactoring, assuming every abstraction is bad, equating old code with bad code, making full audits compulsory for small fixes, automatically deleting artifacts/old branches or restarting the application as a new project.
**Testing:** T98–T107 added; all NOT RUN. No real product has been audited or refactored by this methodology change.
**Revisit when:** real brownfield pilots reveal unsafe commands, significant audit cost, regressions or poor prioritization.
