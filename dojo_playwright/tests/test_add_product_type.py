import re
from playwright.sync_api import Page, expect
from dojo_playwright.pages.login_page import LoginPage
from dojo_playwright.pages.dashboard_page import DashboardPage
from dojo_playwright.pages.add_project_type_page import AddProductTypePage


def test_add_new_product(page: Page):
    # Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("admin", "1Defectdojo@demo#appsec")

    # Go to the add product page
    dashboard_page = DashboardPage(page)
    dashboard_page.projects_menu.hover()
    dashboard_page.add_product_link.click()

    # Fill out the new product type and submit
    add_proj_type_page = AddProductTypePage(page)
    add_proj_type_page.name.fill("A Playwright Project")
    add_proj_type_page.description.fill("A Playwright Project Description")
    add_proj_type_page.submit_button.click()
