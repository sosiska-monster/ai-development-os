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

## RAD-017 — Model selection and reasoning effort are adaptive execution controls (0.2.0-draft)

**Status:** IMPLEMENTED AS GUIDANCE, NATIVE UI SWITCHING NOT CONTROLLED BY MARKDOWN; PILOT NOT RUN.
**Context:** a different model or reasoning effort may improve a difficult decision, but using maximum effort for every small task wastes latency/allowance. Product assurance and task risk do not measure cognitive difficulty.
**Decision:** choose available model and effort by actual reasoning demand, context/tool compatibility, observed quality, budget and latency. Prefer native Default/auto routing if provided and verified, otherwise give minimal actionable **manual recommendations**; raise capability/effort for genuinely difficult analysis, lower it for bounded implementation. Never assert that CORE/AGENTS changed a model picker. Ensure approvals, verification, confidentiality and product assurance stay unchanged when switching.
**Rejected:** hard-coding a vendor/model into a permanent policy, mapping FAST to low and CONTROLLED to max unconditionally, blindly retrying high effort, adding a costly multi-agent orchestration layer before pilot evidence.
**Costs/risks:** misleading claims of automatic controls; switching may lose context or support different tools, and expensive effort does not guarantee correctness. Establish actual settings/permissions and measure verified outcomes and rework.
**Tests:** T21–T25, NOT RUN.
**Revisit when:** new native model-routing controls become available, available models change, or measured quality/latency demonstrates a different default.

