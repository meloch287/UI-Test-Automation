import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from locators.portfolio_page_locators import PortfolioPageLocators


class PortfolioPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/portfolio"
        self.expected_url_patterns = ["portfolio", "projects", "cases", "kejsy"]
    
    @property
    def page_title(self) -> str:
        return PortfolioPageLocators.PAGE_TITLE
    
    @property
    def main_content(self) -> str:
        return PortfolioPageLocators.MAIN_CONTENT
    
    @property
    def projects_list(self) -> str:
        return PortfolioPageLocators.PROJECTS_LIST
    
    @property
    def project_item(self) -> str:
        return PortfolioPageLocators.PROJECT_ITEM
    
    @allure.step("Проверить загрузку страницы Портфолио")
    def is_page_loaded(self) -> bool:
        current_url = self.get_current_url().lower()
        url_match = any(pattern in current_url for pattern in self.expected_url_patterns)
        content_visible = self.is_element_visible(self.main_content)
        return url_match or content_visible
    
    @allure.step("Получить заголовок страницы")
    def get_page_title_text(self) -> str:
        return self.get_text(self.page_title)
