import inspect
import allure
import pytest
import sys
import os

from helpers.display import get_main_display_resolution

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Базовый URL для тестов
BASE_URL = "http://localhost:5100"


def pytest_configure(config):
    """
    Регстрация метод и тегов к тесту
    :param config:
    :return:
    """
    config.addinivalue_line(
        "markers", "annotate(tag): mark test with specific tag for categorization"
    )

@pytest.fixture(scope="session")
def context(playwright):
    resolution = get_main_display_resolution()
    ctx = playwright.chromium.launch_persistent_context(
        "/tmp/kiosk-profile",
        headless=False,
        no_viewport=True,
        args=[
            "--kiosk",
            f"--app={BASE_URL}/Domain/Index",
            "--disable-infobars",
            "--noerrdialogs",
            "--maximize",
            rf"--window-size={resolution["width"]},{resolution["height"]}",
            "--window-position=0,0"
        ],
        ignore_default_args=["--enable-automation"]
    )
    yield ctx
    ctx.close()


@pytest.fixture
def page(context, request):
    """
    Фикстура для создания страницы с предварительной авторизацией
    """
    page = context.pages[0]
    resolution = get_main_display_resolution()
    page.set_viewport_size(resolution)

    if request.node.get_closest_marker('no_profile'):
       yield context.pages[0]
       return



    # Пропускаем создание профиля, если тест помечен как no_profile
    # Открываем страницу создания профиля только если нет маркера no_profile
    page.goto(f"{BASE_URL}/Profile/ProfileCreateNew", timeout=60000)
    page.get_by_role("textbox", name="ВЫБРАТЬ КАРТУ").click()
    page.get_by_role("option", name="1x1").click()
    page.get_by_role("textbox", name="ВЫБРАТЬ АС/РСЗО").click()
    page.get_by_role("option", name="Ствольные").click()
    page.get_by_text("Орудие").click()
    page.get_by_text("Далее").click()

    yield page
    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Модифицирует отчёт о выполнении тестов
    """
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring


def pytest_runtest_call(item):
    """
    Логирует аргументы теста на экран и в Allure отчётах.
    """
    sig = inspect.signature(item.function)
    callspec = getattr(item, "callspec", None)

    selected = {
        name: callspec.params[name]
        for name in sig.parameters
        if callspec and name in callspec.params
    }

    bound = sig.bind_partial(**selected)
    bound.apply_defaults()

    for name, value in bound.arguments.items():
        allure.dynamic.parameter(name=name, value=repr(value))
        print(f"{name}: {repr(value)}")
