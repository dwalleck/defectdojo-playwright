import re
from playwright.sync_api import Page, expect
from login_page import LoginPage
from dashboard_page import DashboardPage
from add_project_page import AddProjectPage


def test_add_new_product(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('admin', '1Defectdojo@demo#appsec')


    # Go to the add product page
    dashboard_page = DashboardPage(page)
    dashboard_page.projects_menu.hover()
    dashboard_page.add_product_link.click()

    # Fill out the details of the project and submit them
    add_proj_page = AddProjectPage(page)
    add_proj_page.name_field.fill('From Playwright4')
    add_proj_page.description.fill('Something about Playwright')
    add_proj_page.project_manager.select_option('(admin)')
    add_proj_page.project_type.select_option('Billing')
    add_proj_page.sla_config.select_option('Default')
    add_proj_page.submit_button.click()

    # Verify the new product is listed
    dashboard_page.projects_menu.hover()
    dashboard_page.all_products_link.click()
    pw_cell = page.locator('tr').filter(has_text='From Playwright4')
    expect(pw_cell).to_be_visible()

    
