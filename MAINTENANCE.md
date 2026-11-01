# MAINTENANCE — как улучшать библиотеку без повторных граблей

## Изменение методологии

1. Опиши наблюдаемую проблему и затронутый этап (на основе реального отчёта/проверки или явно как гипотезу).
2. Найди связанные записи в `RATIONALE.md`. Прочитай модули и шаблоны, которых изменение касается.
3. Предложи **минимальный** diff: изменение модуля, шаблона или CORE лишь если правило нужно всегда.
4. Проверь отсутствие противоречий между `CORE.md`, `MANIFEST.md`, модулями и шаблонами.
5. Прогони примеры из `TEST_CASES.md`: маленькая задача не превращается в бюрократию, high-risk задача не теряет защиты.
6. Зафиксируй решение в `RATIONALE.md` только если оно существенно для будущей эволюции.
7. Обнови `CHANGELOG.md` и версию в `MANIFEST.md`, создай Git-тег при выпуске проверенной версии.

## Права и границы

- Новые методологические решения не считаются APPROVED от имени пользователя без явного согласия.
- Не помещай сюда секреты, реальные клиентские ТЗ и приватные данные.
- Библиотека не должна хранить проектные TODO, баги и архитектуру конкретного клиента.
- Не объявляй тесты пройденными, пока они реально не были выполнены.
- Новые постоянные обязательные правила требуют повышенного обоснования.
- Документируй **причины**, а не только перечень файлов.

## Правило качества

Если добавление нового модуля экономит меньше работы, чем его сопровождение, предпочти расширение существующего или удаление ненужной процедуры.

## Dynamic routing and evidence maintenance — 0.2.0-draft

- Test both directions of mode changes: innocuous FAST → CONTROLLED on discovery, and CONTROLLED → lower mode when hazard is genuinely resolved. Do not use number-of-files as the risk model.
- Run `TEST_CASES.md` using actual disposable repos and fresh sessions; do not convert NOT RUN to PASS without captured evidence.
- Check changed wording for contradicting CORE, MANIFEST, modules, template AGENTS, scope, requirement authority and product-specific permission boundaries.
- For any proposed new technical barrier, distinguish PLANNED, IMPLEMENTED and VERIFIED against actual Codex interface/installed settings. Never promise a GitHub template can enforce sandbox behavior automatically.
- Review exact PR diff, unchanged relevant behavior, secret hygiene and release/rollback implications before merging. Prefer a single fix over a new framework.
- When updating library version, preserve old commit SHA, track downstream project instruction compatibility, and require conscious adoption. Record substantive decisions in RATIONALE, not every minor editorial edit.
