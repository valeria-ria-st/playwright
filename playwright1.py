# ФИО: Столярова Валерия Антоновна
# Дата: 2026-11-11
# Время: 12:47
# Описание: Этот код запускает браузер Chromium, открывает страницу playwright.dev и проверяет, что заголовок страницы содержит слово "Playwright", а также кликает по ссылке "Get started".
# Я скопировала пример из раздела "Installation" (Запуск примера теста) и запустила его локально.
# Зачем: Исходный пример демонстрирует использование встроенных ожиданий (expect) и поиск элементов по ролям (get_by_role), что является современным стандартом для написания надежных и читаемых автотестов.
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()