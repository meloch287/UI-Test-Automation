import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from locators.about_page_locators import AboutPageLocators


class AboutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/about"
        self.expected_url_patterns = ["about", "o-nas", "o-kompanii"]
    
    @property
    def page_title(self) -> str:
        return AboutPageLocators.PAGE_TITLE
    
    @property
    def main_content(self) -> str:
        return AboutPageLocators.MAIN_CONTENT
    
    @property
    def team_section(self) -> str:
        return AboutPageLocators.TEAM_SECTION
    
    @property
    def company_description(self) -> str:
        return AboutPageLocators.COMPANY_DESCRIPTION
    
    @allure.step("Проверить загрузку страницы О нас")
    def is_page_loaded(self) -> bool:
        current_url = self.get_current_url().lower()
        url_match = any(pattern in current_url for pattern in self.expected_url_patterns)
        content_visible = self.is_element_visible(self.main_content)
        return url_match or content_visible
    
    @allure.step("Получить заголовок страницы")
    def get_page_title_text(self) -> str:
        return self.get_text(self.page_title)
