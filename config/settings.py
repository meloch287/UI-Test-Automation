from typing import Optional


class Settings:
    BASE_URL: str = "https://effective-mobile.ru"
    DEFAULT_TIMEOUT: int = 15000
    ELEMENT_TIMEOUT: int = 10000
    PAGE_LOAD_TIMEOUT: int = 30000
    BROWSER: str = "chromium"
    HEADLESS: bool = True
    SLOW_MO: int = 0
    VIEWPORT_WIDTH: int = 1920
    VIEWPORT_HEIGHT: int = 1080
    MAX_RETRIES: int = 2
    SCREENSHOT_ON_FAILURE: bool = True
    PARALLEL_WORKERS: int = 4


settings = Settings()
