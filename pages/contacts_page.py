import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from locators.contacts_page_locators import ContactsPageLocators


class ContactsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/contacts"
        self.expected_url_patterns = ["contact", "kontakt"]
    
    @property
    def page_title(self) -> str:
        return ContactsPageLocators.PAGE_TITLE
    
    @property
    def main_content(self) -> str:
        return ContactsPageLocators.MAIN_CONTENT
    
    @property
    def phone(self) -> str:
        return ContactsPageLocators.PHONE
    
    @property
    def email(self) -> str:
        return ContactsPageLocators.EMAIL
    
    @property
    def contact_form(self) -> str:
        return ContactsPageLocators.CONTACT_FORM
    
    @allure.step("Проверить загрузку страницы Контакты")
    def is_page_loaded(self) -> bool:
        current_url = self.get_current_url().lower()
        url_match = any(pattern in current_url for pattern in self.expected_url_patterns)
        content_visible = self.is_element_visible(self.main_content)
        return url_match or content_visible
    
    @allure.step("Получить заголовок страницы")
    def get_page_title_text(self) -> str:
        return self.get_text(self.page_title)
    
    @allure.step("Проверить наличие контактной формы")
    def has_contact_form(self) -> bool:
        return self.is_element_visible(self.contact_form)
