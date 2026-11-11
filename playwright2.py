# ФИО: Столярова Валерия Антоновна
# Дата: 2026-11-11
# Время: 12:54
# Описание: В этом файле я изменила исходный пример из документации.
# Что изменено (20-30%):
# 1. В тест test_get_started_link добавлена проверка видимости кнопки "Get started" перед кликом (expect(...).to_be_visible()).
# 2. Добавлен абсолютно новый тест test_search, который проверяет работу поиска на сайте.
# Зачем: Исходный пример просто кликал по кнопке. Мои изменения делают тест надежнее (проверка перед кликом) и расширяют покрытие (тест поиска). Это демонстрирует понимание того, как писать собственные проверки, а не просто копировать код.

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    
    # Click the get started link.
    # ИЗМЕНЕНИЕ: Добавила проверку, что кнопка видима перед кликом.
    get_started_btn = page.get_by_role("link", name="Get started")
    expect(get_started_btn).to_be_visible()
    get_started_btn.click()
    
    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# ИЗМЕНЕНИЕ: Новый тест для проверки поиска
def test_search(page: Page):
    page.goto("https://playwright.dev/")
    
    # Кликаем на кнопку поиска
    page.get_by_role("button", name="Search").click()
    
    # Вводим текст в поле поиска и проверяем, что появились результаты
    page.get_by_placeholder("Search docs").fill("Installation")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()