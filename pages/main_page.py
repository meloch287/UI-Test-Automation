import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.url = "/"
    
    @property
    def header(self) -> str:
        return MainPageLocators.HEADER
    
    @property
    def logo(self) -> str:
        return MainPageLocators.LOGO
    
    @property
    def about_link(self) -> str:
        return MainPageLocators.ABOUT_LINK
    
    @property
    def contacts_link(self) -> str:
        return MainPageLocators.CONTACTS_LINK
    
    @property
    def services_link(self) -> str:
        return MainPageLocators.SERVICES_LINK
    
    @property
    def portfolio_link(self) -> str:
        return MainPageLocators.PORTFOLIO_LINK
    
    @property
    def career_link(self) -> str:
        return MainPageLocators.CAREER_LINK
    
    @property
    def main_title(self) -> str:
        return MainPageLocators.MAIN_TITLE
    
    @property
    def footer(self) -> str:
        return MainPageLocators.FOOTER
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self) -> "MainPage":
        self.open(self.url)
        return self
    
    @allure.step("Клик по ссылке 'О нас'")
    def click_about_link(self) -> None:
        self.click(self.about_link)
    
    @allure.step("Клик по ссылке 'Контакты'")
    def click_contacts_link(self) -> None:
        self.click(self.contacts_link)
    
    @allure.step("Клик по ссылке 'Услуги'")
    def click_services_link(self) -> None:
        self.click(self.services_link)
    
    @allure.step("Клик по ссылке 'Портфолио'")
    def click_portfolio_link(self) -> None:
        self.click(self.portfolio_link)
    
    @allure.step("Клик по ссылке 'Карьера'")
    def click_career_link(self) -> None:
        self.click(self.career_link)
    
    @allure.step("Клик по логотипу")
    def click_logo(self) -> None:
        self.click(self.logo)
    
    @allure.step("Проверить загрузку главной страницы")
    def is_page_loaded(self) -> bool:
        return self.is_element_visible(self.header)
    
    @allure.step("Проверить наличие header")
    def has_header(self) -> bool:
        return self.is_element_visible(self.header)
    
    @allure.step("Проверить наличие footer")
    def has_footer(self) -> bool:
        return self.is_element_visible(self.footer)
    
    @allure.step("Получить заголовок страницы")
    def get_main_title_text(self) -> str:
        return self.get_text(self.main_title)
    
    @allure.step("Проверить видимость ссылки 'О нас'")
    def is_about_link_visible(self) -> bool:
        return self.is_element_visible(self.about_link)
    
    @allure.step("Проверить видимость ссылки 'Контакты'")
    def is_contacts_link_visible(self) -> bool:
        return self.is_element_visible(self.contacts_link)
    
    @allure.step("Проверить видимость ссылки 'Услуги'")
    def is_services_link_visible(self) -> bool:
        return self.is_element_visible(self.services_link)
    
    @allure.step("Проверить видимость ссылки 'Портфолио'")
    def is_portfolio_link_visible(self) -> bool:
        return self.is_element_visible(self.portfolio_link)
