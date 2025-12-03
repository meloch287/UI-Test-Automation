import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from locators.services_page_locators import ServicesPageLocators


class ServicesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/services"
        self.expected_url_patterns = ["service", "uslugi"]
    
    @property
    def page_title(self) -> str:
        return ServicesPageLocators.PAGE_TITLE
    
    @property
    def main_content(self) -> str:
        return ServicesPageLocators.MAIN_CONTENT
    
    @property
    def services_list(self) -> str:
        return ServicesPageLocators.SERVICES_LIST
    
    @property
    def service_item(self) -> str:
        return ServicesPageLocators.SERVICE_ITEM
    
    @allure.step("Проверить загрузку страницы Услуги")
    def is_page_loaded(self) -> bool:
        current_url = self.get_current_url().lower()
        url_match = any(pattern in current_url for pattern in self.expected_url_patterns)
        content_visible = self.is_element_visible(self.main_content)
        return url_match or content_visible
    
    @allure.step("Получить заголовок страницы")
    def get_page_title_text(self) -> str:
        return self.get_text(self.page_title)
