from playwright.sync_api import Page

from dojo_playwright.pages.nav_bar import NavBar


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.nav_bar = NavBar(page)
        self.add_product_link = page.get_by_role("link", name="Add Product", exact=True)
        self.all_products_link = page.get_by_role(
            "link", name="All Products", exact=True
        )
        self.add_project_type_link = page.get_by_role(
            "link", name="Add Project Type", exact=True
        )
        self.projects_menu = page.get_by_label("Products")

        # 4GTNR-HQD99-WCWF6-M7GFW-TQ8GG
