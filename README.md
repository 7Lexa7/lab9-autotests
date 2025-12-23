# Лабораторная работа 9: Интеграция автотестов в CI/CD

## Описание
Автоматические UI-тесты для формы обратной связи с интеграцией в GitHub Actions.

## Запуск тестов локально
1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите тесты: `pytest tests/ -v`

## Структура проекта
- `pages/` - Page Object модели
- `tests/` - тестовые сценарии
- `contact_form.html` - тестируемая форма
- `.github/workflows/run-tests.yml` - конфигурация CI/CD