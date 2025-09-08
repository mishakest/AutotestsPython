# E2E test (Playwright + Python)

Описание: Этот проект использует [Playwright] для автоматизации браузера и написания end-to-end тестов.
Установка и использование происходят в среде Python на Windows 10.

## Структура проекта

-- 
```
e2eTest/
- models/ # Папка с моделями
- pages/ # Папка со страницами
- tests/ # Папка с тестами
- pytest.ini # Описание маркеров, для запуска конкретных тестов
- README.md # Это описание
- requirements.txt # Список зависимостей
```
---



---

## Требования

- ОС: Windows 10 или Windows 11, Linux
- [Python](https://www.python.org/downloads/) (версия 3.13 или выше)
- Pycharm
- python-venv

---

# Установка Playwright

## Установка venv

### Общие рекомендации по созданию Venv

- Папка не рекомендуется к созданию скрытой. Отсюда имя папки `venv`, без точки
- Venv рекомендуется к расположению в папке с проектом
- Далее инструкция с учётом рекомендаций

### IDE

- Перейти в правый нижний угол IDE → нажать на текущий интерпретатор (например, Python 3.X).
- Выбрать Add New Interpreter → Add Local Interpreter.
- В открывшемся окне:
- Environment: New
- Type: Virtualenv
- Base interpreter: В большинстве случаев сработает автоопределение интерпретатора, если это не так:
    - Укажите путь к Python (C:\...\python.exe или /usr/bin/python3.X).
- Location: Указать путь, включая папку venv, например `E:\Work\Commandor\Tst\e2eTest`
- Нажать "ОК"

### Terminal

- Открыть терминал
- Перейти в папку проекта
    - Win пример: `cd E:\Work\Commandor\Tst\e2eTest`
    - Linux пример: `cd /home/user/Commandor/Tst/e2eTest`
- Создать Venv:
    - `python -m venv venv` - это создаст папку `venv`, с полным путём `/home/user/Commandor/Tst/e2eTest/venv`

## (optional) Активация Venv через внешний терминал

### Win

- Открыть терминал
- Перейти в папку проекта
    - Win пример: `cd E:\Work\Commandor\Tst\e2eTest`
    - Linux пример: `cd /home/user/Commandor/Tst/e2eTest`
- Перейти в папку `venv`
- Перейти в папку `scripts`
- Для `cmd` использовать activate.bat
- Для `powershell` использовать activate.ps1

### Linux

- Открыть терминал
- Перейти в папку проекта
    - Win пример: `cd E:\Work\Commandor\Tst\e2eTest`
    - Linux пример: `cd /home/user/Commandor/Tst/e2eTest`
- Перейти в папку `venv`
- Перейти в папку `bin`
- Для `bash` использовать команду `source activate`
- Для `fish` использовать команду `source activate.fish`

## Установка зависимостей:

### IDE

### Через интерфейс requrements

-Открыть файл requirements.txt в IDE.
-Нажать на кнопку "Install requirements" в верхней части редактора, или кликнуть правой кнопкой по файлу → "Install
Requirements"

### Через встроенный terminal IDE

По умолчанию терминал PyCharm с установленным venv и интерпретатором открывается уже с **активированным** venv

- Убедиться, что в терминале PyCharm отображается (venv) перед строкой ввода
- Перейти в папку проекта
    - Win пример: `cd E:\Work\Commandor\Tst\e2eTest`
    - Linux пример: `cd /home/user/Commandor/Tst/e2eTest`
- Установить зависимости командой: pip install -r requirements.txt

### Через внешний терминал

- Активировать venv по инструкции выше\
- Перейти в папку проекта
    - Win пример: `cd E:\Work\Commandor\Tst\e2eTest`
    - Linux пример: `cd /home/user/Commandor/Tst/e2eTest`
    - Установить зависимости командой: pip install -r requirements.txt

### 2. Установка браузеров для Playwright

После установки Playwright, выполнить команду для загрузки необходимых браузеров из `venv` в терминале:

`playwright install`

> По умолчанию устанавливаются Chromium, Firefox и WebKit. Если нужно установить только определённые браузеры,
> использовать:

`playwright install chromium webkit`

## Подготовка source root

Важный шаг для самой IDE. Т.к. в репозитории хранится несколько проектов на Python, необходимо указать корень проекта в
IDE
для корректного определения путей, для самописных модулей и классов.

- В обозревателе проекта слева найти папку `e2eTest` по пути `<корень_репозитория>/Tst/e2eTest`
- Нажать правой кнопкой мыши по папке `e2eTest`
- Нажать `Mark Directory As`
- Нажать `Sources Root`
- Если после выполнения данных шагов папка `e2eTest` стала синей, подготовка успешно завершена

# Запуск тестов

## IDE прямой запуск теста

Каждый тест в файлах начинающихся с `test_*` подсвечивается слева зелёной стрелочкой. Можно запустить нажав на неё.
Debug можно запускать так-же.

## IDE запуск теста из меню конфигураций

Меню конфигураций находится справа сверху рядом с зелёной стрелочкой.
Хоть этот пункт для запуска тестов сложнее и дольше чем предыдущий, у него есть и свои плюсы:
+ Можно указать `Environment Variables` для использования в проекте
+ Можно указать дополнительные параметры для запуска тестов 
  - Например, создание отчётов `junit` или `AllureReports`
  - Например, `-vv` и `-s` для подробной печати в выводе
  - Запускать тесты с маркерами
  - И т.д.


Для создания новой конфигурации:

- Нажать на панель конфигураций слева от зелёной стрелочки.
- Нажать `Edit Configuration`
- В меню редактирования конфигураций
    - Слева значок `+` -> `Python Tests` -> `pytest`
- Выбрать только что созданную конфигурацию в меню редактирования конфигураций
- `Name` - указать имя для сессии тестов
- `script` - изменить на `module`
- В путь для `module` можно нажать на кнопку `...`
    - Можно в поиске найти модуль по первым символам, обычно это все модули которые начинаются с `test_*`
    - Указать модуль из которого запускаются тесты (это соответственно наименование как подключение модуля в python),
      например `test_recon_rangefinder.test_recon_rangefinder`
    - В `Working Directory` указать директорию проекта
    - Нажать `Apply`
- Теперь в меню выбора конфигураций запуска можно выбрать нашу сессию для тестирования.

# Примеры запусков тестов из терминала c `venv` по маркерам:

Запуск всех тестов с маркером regression
> pytest -m regression

Запуск всех тестов с маркером recon
> pytest -m recon

Запуск тестов, которые имеют оба маркера: regression И recon
> pytest -m "regression and recon"

Запуск тестов, которые имеют маркер regression ИЛИ recon
> pytest -m "regression or recon"

Запуск тестов, которые имеют маркер regression, но НЕ имеют маркер smoke 
> pytest -m "regression and not smoke"

# Playwright Inspector
Для вызова `PlayWright Inspector` для отладки в терминале с `venv`:
> PLAYWRIGHT_DEBUG=1 python -m playwright show-trace

---

## Очистка (при необходимости)

Чтобы удалить Playwright:

> pip uninstall playwright

---

## Полезные ссылки

- [Документация Playwright (Python)](https://playwright.dev/docs/intro)
- [API Reference](https://playwright.dev/docs/api/class-playwright)
- [Playwright CLI docs](https://playwright.dev/docs/cli)
- [Python Venv](https://docs.python.org/3/library/venv.html)
- [Pycharm Requirements Install](https://www.jetbrains.com/help/pycharm/managing-dependencies.html#populate_dependency_files)