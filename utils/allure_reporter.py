import allure
from playwright.sync_api import Page


class AllureReporter:
    @staticmethod
    def attach_screenshot(page: Page, name: str = "screenshot") -> None:
        screenshot = page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
    
    @staticmethod
    def attach_text(text: str, name: str = "text") -> None:
        allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)
    
    @staticmethod
    def attach_html(html: str, name: str = "html") -> None:
        allure.attach(html, name=name, attachment_type=allure.attachment_type.HTML)
