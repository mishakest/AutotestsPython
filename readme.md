# Automated Test Suite for Web Platform

Этот репозиторий содержит пример автоматизированных end-to-end (E2E) тестов для веб-приложения, написанных на Python с использованием фреймворка Playwright.

Структура проекта построена по паттерну **Page Object Model (POM)**, что обеспечивает поддержку кода и его переиспользование.

## 🚀 Технологический стек

*   **Язык программирования:** Python 3.10+
*   **Фреймворк для тестирования:** Playwright
*   **Фреймворк для запуска тестов:** Pytest
*   **Менеджер пакетов:** pip
*   **Система контроля версий:** Git

## 📁 Структура проекта
project/
├── models/ # Pydantic-модели или классы для представления тестовых данных
├── pages/ # Классы Page Object Model (POM)
│ ├── base_page.py # Базовый класс для всех страниц
│ └── ... # Классы конкретных страниц
├── tests/ # Наборы тестов (pytest)
├── helpers/ # Вспомогательные утилиты и хелперы
├── conftest.py # Фикстуры Pytest
└── requirements.txt # Зависимости проекта

## ⚙️ Установка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/mishakest/playwright-project.git
    cd playwright-demo-project
    ```

2.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Установите браузеры для Playwright:**
    ```bash
    playwright install
    ```

4.  **Запустите тесты:**
    ```bash
    # Все тесты
    pytest

    # Тесты из конкретной директории
    pytest tests/recon/

    # Тест с генерацией Allure-отчета
    pytest --alluredir=allure-results
    ```
