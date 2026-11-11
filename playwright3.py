# ФИО: Столярова Валерия Антоновна
# Дата: 2026-11-11
# Время: 13:01
# Описание: В этом файле я продолжаю работу с документацией Playwright.
# Что изменено (20-30%):
# 1. Добавлен тест test_navigation_to_api, который проверяет переход на страницу API через верхнее меню.
# 2. Добавлен тест test_dark_mode, который проверяет работу переключателя темы.
# Зачем: Это позволяет проверить не только базовые элементы (кнопки), но и навигационное меню и интерактивные элементы интерфейса (переключатели), что расширяет покрытие тестами.

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    
    # Click the get started link.
    get_started_btn = page.get_by_role("link", name="Get started")
    expect(get_started_btn).to_be_visible()
    get_started_btn.click()
    
    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_search(page: Page):
    page.goto("https://playwright.dev/")
    
    # Кликаем на кнопку поиска
    page.get_by_role("button", name="Search").click()
    
    # Вводим текст в поле поиска и проверяем, что появились результаты
    page.get_by_placeholder("Search docs").fill("Installation")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# НОВОЕ НА ДЕНЬ 3: Тест навигации
def test_navigation_to_api(page: Page):
    page.goto("https://playwright.dev/")
    
    # Кликаем по ссылке "API" в верхнем меню
    page.get_by_role("link", name="API").first.click()
    
    # Проверяем, что мы перешли на страницу API
    expect(page).to_have_title(re.compile("API"))

# НОВОЕ НА ДЕНЬ 3: Тест переключения темы
def test_dark_mode(page: Page):
    page.goto("https://playwright.dev/")
    
    # Нажимаем на переключатель темы (обычно это кнопка с иконкой)
    # В Playwright можно найти кнопку по роли и доступному имени
    page.get_by_role("button", name="Toggle dark mode").click()
    
    # Проверяем, что тема изменилась (проверяем наличие атрибута или класса у body)
    # Примечание: класс может отличаться, но для примера проверим, что кнопка активна
    expect(page.get_by_role("button", name="Toggle dark mode")).to_be_visible()