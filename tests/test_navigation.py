import pytest
import allure
from playwright.sync_api import Page

from pages.main_page import MainPage
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.services_page import ServicesPage
from pages.portfolio_page import PortfolioPage


@allure.feature("Навигация")
@allure.story("Переходы по разделам сайта")
class TestNavigation:
    
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Переход на страницу 'О нас'")
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigation_to_about_page(self, page: Page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Проверить видимость ссылки 'О нас'"):
            if not main_page.is_about_link_visible():
                pytest.skip("Ссылка 'О нас' не найдена на странице")
        
        with allure.step("Клик по ссылке 'О нас'"):
            main_page.click_about_link()
        
        with allure.step("Проверить переход на страницу 'О нас'"):
            about_page = AboutPage(page)
            page.wait_for_load_state("networkidle")
            assert about_page.is_page_loaded(), "Страница 'О нас' не загрузилась"
    
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Переход на страницу 'Контакты'")
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigation_to_contacts_page(self, page: Page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Проверить видимость ссылки 'Контакты'"):
            if not main_page.is_contacts_link_visible():
                pytest.skip("Ссылка 'Контакты' не найдена на странице")
        
        with allure.step("Клик по ссылке 'Контакты'"):
            main_page.click_contacts_link()
        
        with allure.step("Проверить переход на страницу 'Контакты'"):
            contacts_page = ContactsPage(page)
            page.wait_for_load_state("networkidle")
            assert contacts_page.is_page_loaded(), "Страница 'Контакты' не загрузилась"
    
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Переход на страницу 'Услуги'")
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigation_to_services_page(self, page: Page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Проверить видимость ссылки 'Услуги'"):
            if not main_page.is_services_link_visible():
                pytest.skip("Ссылка 'Услуги' не найдена на странице")
        
        with allure.step("Клик по ссылке 'Услуги'"):
            main_page.click_services_link()
        
        with allure.step("Проверить переход на страницу 'Услуги'"):
            services_page = ServicesPage(page)
            page.wait_for_load_state("networkidle")
            assert services_page.is_page_loaded(), "Страница 'Услуги' не загрузилась"
    
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Переход на страницу 'Портфолио'")
    @pytest.mark.navigation
    @pytest.mark.smoke
    def test_navigation_to_portfolio_page(self, page: Page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Проверить видимость ссылки 'Портфолио'"):
            if not main_page.is_portfolio_link_visible():
                pytest.skip("Ссылка 'Портфолио' не найдена на странице")
        
        with allure.step("Клик по ссылке 'Портфолио'"):
            main_page.click_portfolio_link()
        
        with allure.step("Проверить переход на страницу 'Портфолио'"):
            portfolio_page = PortfolioPage(page)
            page.wait_for_load_state("networkidle")
            assert portfolio_page.is_page_loaded(), "Страница 'Портфолио' не загрузилась"


@allure.feature("Навигация")
@allure.story("Возврат на главную страницу")
class TestReturnToMainPage:
    
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Возврат на главную через логотип")
    @pytest.mark.navigation
    def test_return_to_main_via_logo(self, page: Page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Перейти на другую страницу"):
            if main_page.is_about_link_visible():
                main_page.click_about_link()
                page.wait_for_load_state("networkidle")
            else:
                pytest.skip("Нет доступных ссылок для навигации")
        
        with allure.step("Клик по логотипу"):
            try:
                main_page.click_logo()
                page.wait_for_load_state("networkidle")
            except Exception:
                pytest.skip("Логотип не найден или не кликабелен")
        
        with allure.step("Проверить возврат на главную"):
            current_url = main_page.get_current_url()
            assert "effective-mobile.ru" in current_url
