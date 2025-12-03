import pytest
import allure
from typing import Generator
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from config.settings import settings
from utils.logger import setup_logger
from utils.allure_reporter import AllureReporter


logger = setup_logger("conftest")


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    logger.info("Запуск браузера...")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=settings.HEADLESS, slow_mo=settings.SLOW_MO)
    yield browser
    logger.info("Закрытие браузера...")
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    logger.info("Создание контекста браузера...")
    context = browser.new_context(
        viewport={"width": settings.VIEWPORT_WIDTH, "height": settings.VIEWPORT_HEIGHT}
    )
    context.set_default_timeout(settings.DEFAULT_TIMEOUT)
    yield context
    logger.info("Закрытие контекста браузера...")
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    logger.info("Создание страницы...")
    page = context.new_page()
    yield page
    logger.info("Закрытие страницы...")
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                logger.error(f"Тест {item.name} упал. Делаем скриншот...")
                AllureReporter.attach_screenshot(page, f"failure_{item.name}")
                AllureReporter.attach_text(page.url, "Current URL")
            except Exception as e:
                logger.error(f"Не удалось сделать скриншот: {e}")


def pytest_configure(config):
    logger.info("Конфигурация pytest...")
    config.addinivalue_line("markers", "smoke: Smoke тесты")
    config.addinivalue_line("markers", "regression: Регрессионные тесты")
    config.addinivalue_line("markers", "navigation: Тесты навигации")


def pytest_collection_modifyitems(config, items):
    for item in items:
        for marker in item.iter_markers():
            if marker.name == "smoke":
                item.add_marker(pytest.mark.allure_label("tag", "smoke"))
            elif marker.name == "regression":
                item.add_marker(pytest.mark.allure_label("tag", "regression"))


@pytest.fixture(autouse=True)
def test_setup_teardown(request, page: Page):
    test_name = request.node.name
    logger.info(f"=== Начало теста: {test_name} ===")
    yield
    logger.info(f"=== Конец теста: {test_name} ===")
