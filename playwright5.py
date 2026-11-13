# ФИО: Столярова Валерия Антоновна
# Дата: 2026-11-13
# Время: 18:20
# Описание: В этом файле я продолжаю изучение возможностей Playwright и Pytest.
# Что изменено (20-30%):
# 1. Добавлен тест test_code_block, который проверяет наличие блока с кодом на странице "Installation".
# 2. Добавлен тест test_language_switch, проверяющий, что при нажатии на переключатель языка меняется заголовок страницы.
# Зачем: Это демонстрирует проверку динамического контента (кода) и работу с навигацией/локализацией интерфейса.

import re
import pytest
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

# ИЗМЕНЕНИЕ: Проверка наличия блока с кодом (изучаем работу с текстом)
def test_code_block(page: Page):
    page.goto("https://playwright.dev/python/docs/intro")
    
    # Ищем заголовок Installation
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    
    # Проверяем, что на странице есть блок с кодом (обычно это тег code или pre)
    # Playwright позволяет искать элементы по CSS-селекторам
    code_block = page.locator("pre").first
    expect(code_block).to_be_visible()
    # Проверяем, что в блоке есть какая-то команда (например, pip)
    expect(code_block).to_contain_text("pip")

# ИЗМЕНЕНИЕ: Тест на переключение языка (навигация)
def test_language_switch(page: Page):
    page.goto("https://playwright.dev/")
    
    # На сайте есть выпадающий список языков (Python, Node.js и т.д.)
    # Нажимаем на кнопку "Python" в меню
    page.get_by_role("button", name="Python").click()
    
    # Выбираем "Node.js" из выпадающего списка
    page.get_by_role("menuitem", name="Node.js").click()
    
    # Проверяем, что URL изменился (или заголовок поменялся на Node.js)
    expect(page).to_have_url(re.compile(".*nodejs.*"))