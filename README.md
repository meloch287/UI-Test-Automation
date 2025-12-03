# UI Test Automation - effective-mobile.ru

Проект автоматизации UI-тестирования сайта effective-mobile.ru с использованием Python, Playwright, Allure и Docker.

## Содержание

1. [Описание проекта](#описание-проекта)
2. [Требования к системе](#требования-к-системе)
3. [Локальная установка](#локальная-установка)
4. [Запуск тестов](#запуск-тестов)
5. [Запуск с Docker](#запуск-с-docker)
6. [Просмотр отчета Allure](#просмотр-отчета-allure)
7. [Структура проекта](#структура-проекта)
8. [Конфигурация](#конфигурация)
9. [Troubleshooting](#troubleshooting)

## Описание проекта

Проект реализует автоматизированное тестирование UI сайта effective-mobile.ru:
- Тесты главной страницы
- Тесты навигации по разделам (О нас, Контакты, Услуги, Портфолио)
- Проверка корректности URL после переходов
- Верификация элементов на страницах

### Используемые технологии
- **Python 3.10+**
- **Playwright** - браузерная автоматизация
- **Pytest** - фреймворк тестирования
- **Allure** - отчетность
- **Docker** - контейнеризация

### Архитектурные паттерны
- **Page Object Model (POM)**
- **Page Factory**

## Требования к системе

- Python 3.10 или выше
- pip (менеджер пакетов Python)
- Docker и Docker Compose (для контейнеризации)
- Allure CLI (для просмотра отчетов)

## Локальная установка

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/meloch287/UI-Test-Automation.git
cd UI-Test-Automation
```

### Шаг 2: Создание виртуального окружения
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/MacOS
source venv/bin/activate
```

### Шаг 3: Установка зависимостей
```bash
pip install -r requirements.txt
```

### Шаг 4: Установка браузеров Playwright
```bash
playwright install chromium
```

## Запуск тестов

### Запуск всех тестов
```bash
pytest tests/ -v --alluredir=allure-results
```

### Запуск smoke тестов
```bash
pytest tests/ -v -m smoke --alluredir=allure-results
```

### Запуск тестов навигации
```bash
pytest tests/ -v -m navigation --alluredir=allure-results
```

### Параллельный запуск тестов
```bash
pytest tests/ -v -n 4 --alluredir=allure-results
```

### Запуск с повторами при падении
```bash
pytest tests/ -v --reruns 2 --alluredir=allure-results
```

## Запуск с Docker

### Сборка образа
```bash
docker build -t effective-mobile-tests .
```

### Запуск тестов в контейнере
```bash
docker run -v ${PWD}/allure-results:/app/allure-results effective-mobile-tests
```

### Запуск через Docker Compose
```bash
# Запуск тестов
docker-compose up tests

# Запуск с Allure сервером
docker-compose up

# Остановка
docker-compose down
```

## Просмотр отчета Allure

### Установка Allure CLI

**Windows (Scoop):**
```bash
scoop install allure
```

**MacOS (Homebrew):**
```bash
brew install allure
```

**Linux:**
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### Генерация и просмотр отчета
```bash
allure serve allure-results
```

### Генерация статического отчета
```bash
allure generate allure-results -o allure-report --clean
```

## Структура проекта

```
project-root/
├── README.md                    # Документация
├── requirements.txt             # Python зависимости
├── pytest.ini                   # Конфигурация pytest
├── Dockerfile                   # Docker образ
├── docker-compose.yml           # Docker Compose
├── .gitignore                   # Git ignore
├── .dockerignore                # Docker ignore
├── conftest.py                  # Pytest fixtures
│
├── tests/                       # Тесты
│   ├── __init__.py
│   ├── test_main_page.py        # Тесты главной страницы
│   └── test_navigation.py       # Тесты навигации
│
├── pages/                       # Page Objects
│   ├── __init__.py
│   ├── base_page.py             # Базовый класс
│   ├── main_page.py             # Главная страница
│   ├── about_page.py            # Страница "О нас"
│   ├── contacts_page.py         # Страница "Контакты"
│   ├── services_page.py         # Страница "Услуги"
│   └── portfolio_page.py        # Страница "Портфолио"
│
├── locators/                    # Локаторы элементов
│   ├── __init__.py
│   ├── main_page_locators.py
│   ├── about_page_locators.py
│   ├── contacts_page_locators.py
│   ├── services_page_locators.py
│   └── portfolio_page_locators.py
│
├── config/                      # Конфигурация
│   ├── __init__.py
│   └── settings.py              # Настройки проекта
│
├── utils/                       # Утилиты
│   ├── __init__.py
│   ├── logger.py                # Логирование
│   └── allure_reporter.py       # Allure утилиты
│
└── allure-results/              # Результаты тестов (генерируется)
```

## Конфигурация

Основные настройки находятся в `config/settings.py`:

| Параметр | Описание | Значение по умолчанию |
|----------|----------|----------------------|
| BASE_URL | URL тестируемого сайта | https://effective-mobile.ru |
| DEFAULT_TIMEOUT | Таймаут ожидания (мс) | 5000 |
| HEADLESS | Режим без GUI | True |
| VIEWPORT_WIDTH | Ширина окна | 1920 |
| VIEWPORT_HEIGHT | Высота окна | 1080 |

## Troubleshooting

### Ошибка: "Browser not found"
```bash
playwright install chromium
```

### Ошибка: "Timeout exceeded"
Увеличьте таймаут в `config/settings.py`:
```python
DEFAULT_TIMEOUT = 10000
```

### Тесты падают в Docker
Убедитесь, что установлены все зависимости браузера:
```bash
playwright install-deps chromium
```

### Allure отчет не генерируется
Проверьте наличие директории `allure-results`:
```bash
mkdir allure-results
```

## Маркеры тестов

- `@pytest.mark.smoke` - Smoke тесты (критичные, быстрые)
- `@pytest.mark.regression` - Регрессионные тесты
- `@pytest.mark.navigation` - Тесты навигации

## Автор

meloch287
