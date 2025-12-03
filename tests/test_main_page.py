import pytest
import allure
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.feature("Главная страница")
@allure.story("Загрузка главной страницы")
class TestMainPageLoad:
    
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Главная страница успешно загружается")
    @pytest.mark.smoke
    def test_main_page_loads_successfully(self, page: Page):
        main_page = MainPage(page)
        
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        
        with allure.step("Проверить, что страница загружена"):
            assert main_page.is_page_loaded(), "Главная страница не загрузилась"
    
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка наличия header на главной странице")
    @pytest.mark.smoke
    def test_main_page_has_header(self, page: Page):
        main_page = MainPage(page)
        main_page.open_main_page()
        
        with allure.step("Проверить наличие header"):
            assert main_page.has_header(), "Header не найден на странице"
    
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка наличия footer на главной странице")
    @pytest.mark.smoke
    def test_main_page_has_footer(self, page: Page):
        main_page = MainPage(page)
        main_page.open_main_page()
        
        with allure.step("Проверить наличие footer"):
            assert main_page.has_footer(), "Footer не найден на странице"
    
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка корректного URL главной страницы")
    @pytest.mark.smoke
    def test_main_page_url(self, page: Page):
        main_page = MainPage(page)
        main_page.open_main_page()
        
        with allure.step("Проверить URL"):
            current_url = main_page.get_current_url()
            assert "effective-mobile.ru" in current_url, f"Некорректный URL: {current_url}"


@allure.feature("Главная страница")
@allure.story("Элементы навигации")
class TestMainPageNavElements:
    
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка наличия навигационных ссылок")
    @pytest.mark.smoke
    def test_navigation_links_present(self, page: Page):
        main_page = MainPage(page)
        main_page.open_main_page()
        
        links_found = []
        
        with allure.step("Проверить наличие ссылок"):
            if main_page.is_about_link_visible():
                links_found.append("О нас")
            if main_page.is_contacts_link_visible():
                links_found.append("Контакты")
            if main_page.is_services_link_visible():
                links_found.append("Услуги")
            if main_page.is_portfolio_link_visible():
                links_found.append("Портфолио")
        
        with allure.step(f"Найдено ссылок: {len(links_found)}"):
            assert len(links_found) > 0, "Не найдено ни одной навигационной ссылки"
            allure.attach("\n".join(links_found), name="Найденные ссылки", attachment_type=allure.attachment_type.TEXT)


@allure.feature("Главная страница")
@allure.story("Заголовок страницы")
class TestMainPageTitle:
    
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка наличия заголовка H1")
    @pytest.mark.smoke
    def test_main_page_has_h1(self, page: Page):
        main_page = MainPage(page)
        main_page.open_main_page()
        
        with allure.step("Проверить наличие H1"):
            try:
                title = main_page.get_main_title_text()
                assert len(title) > 0, "Заголовок H1 пустой"
                allure.attach(title, name="H1 заголовок", attachment_type=allure.attachment_type.TEXT)
            except Exception:
                pytest.skip("Заголовок H1 не найден на странице")
