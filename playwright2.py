# ФИО: Столярова Валерия Антоновна
# Дата: 2026-11-11
# Время: 12:48
# Описание: В этом файле я использую настройки контекста из справочника Pytest.
# Что изменено (20-30%): 
# 1. Добавлена фикстура browser_context_args (из справочника), которая задает кастомный размер экрана 1280x720.
# 2. Добавлен новый тест test_search, проверяющий работу поиска на сайте.
# Зачем: Это демонстрирует умение настраивать окружение браузера и писать новые тесты.

import re
import pytest
from playwright.sync_api import Page, expect

# ИЗМЕНЕНИЕ: Настройка размера экрана через фикстуру
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        }
    }

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    
    # Изменение: проверяем, что кнопка видима перед кликом
    get_started_btn = page.get_by_role("link", name="Get started")
    expect(get_started_btn).to_be_visible()
    get_started_btn.click()
    
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# ИЗМЕНЕНИЕ: Новый тест для проверки поиска
def test_search(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("button", name="Search").click()
    page.get_by_placeholder("Search docs").fill("Installation")
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()