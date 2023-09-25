import re
from playwright.sync_api import Page, expect
from login_page import LoginPage
from dashboard_page import DashboardPage
from add_project_page import AddProjectPage


def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('admin', '1Defectdojo@demo#appsec')

    dashboard_page = DashboardPage(page)
    dashboard_page.projects_menu.hover()
    dashboard_page.all_products_link.click()
    #pw_cell = page.locator('projects').filter(has=page.locator('tr').filter(has_text='From Playwright'))
    #pw_cell = page.locator('tr').filter(has_text='From Derp')
    pw_cell = page.locator('projects').locator('tr').filter(has_text='From Playwright')
    expect(pw_cell).to_be_visible()
    # dashboard_page.add_product_link.click()

    # add_proj_page = AddProjectPage(page)
    # add_proj_page.name_field.fill('From Playwright')
    # add_proj_page.description.fill('Something about Playwright')
    # add_proj_page.project_manager.select_option('(admin)')
    # add_proj_page.project_type.select_option('Billing')
    # add_proj_page.sla_config.select_option('Default')
    # add_proj_page.submit_button.click()

    
