import allure
from playwright.sync_api import Page
from typing import Optional
import logging

from config.settings import settings


logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = settings.BASE_URL
        self.timeout = settings.DEFAULT_TIMEOUT
    
    @allure.step("Открыть страницу: {url}")
    def open(self, url: str = "") -> None:
        full_url = url if url.startswith("http") else f"{self.base_url}{url}"
        logger.info(f"Открываем страницу: {full_url}")
        self.page.goto(full_url, timeout=settings.PAGE_LOAD_TIMEOUT)
    
    @allure.step("Клик по элементу: {locator}")
    def click(self, locator: str, timeout: Optional[int] = None) -> None:
        timeout = timeout or self.timeout
        logger.info(f"Клик по элементу: {locator}")
        self.page.locator(locator).first.click(timeout=timeout)
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator: str, timeout: Optional[int] = None) -> str:
        timeout = timeout or self.timeout
        element = self.page.locator(locator).first
        element.wait_for(timeout=timeout)
        text = element.text_content() or ""
        logger.info(f"Текст элемента '{locator}': {text[:50]}...")
        return text.strip()
    
    @allure.step("Заполнить поле {locator} значением")
    def fill(self, locator: str, value: str, timeout: Optional[int] = None) -> None:
        timeout = timeout or self.timeout
        logger.info(f"Заполняем поле '{locator}' значением: {value}")
        self.page.locator(locator).first.fill(value, timeout=timeout)
    
    def get_current_url(self) -> str:
        url = self.page.url
        logger.info(f"Текущий URL: {url}")
        return url
    
    @allure.step("Ожидание элемента: {locator}")
    def wait_for_element(self, locator: str, state: str = "visible", timeout: Optional[int] = None) -> None:
        timeout = timeout or self.timeout
        logger.info(f"Ожидаем элемент '{locator}' в состоянии '{state}'")
        self.page.locator(locator).first.wait_for(state=state, timeout=timeout)
    
    def is_element_visible(self, locator: str, timeout: Optional[int] = None) -> bool:
        timeout = timeout or self.timeout
        try:
            self.page.locator(locator).first.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False
    
    @allure.step("Сделать скриншот: {name}")
    def take_screenshot(self, name: str = "screenshot") -> bytes:
        logger.info(f"Делаем скриншот: {name}")
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        return screenshot
    
    def scroll_to_element(self, locator: str) -> None:
        logger.info(f"Прокручиваем к элементу: {locator}")
        self.page.locator(locator).first.scroll_into_view_if_needed()
    
    def get_attribute(self, locator: str, attribute: str) -> Optional[str]:
        return self.page.locator(locator).first.get_attribute(attribute)
    
    def wait_for_url(self, url_pattern: str, timeout: Optional[int] = None) -> None:
        timeout = timeout or settings.PAGE_LOAD_TIMEOUT
        logger.info(f"Ожидаем URL: {url_pattern}")
        self.page.wait_for_url(url_pattern, timeout=timeout)
