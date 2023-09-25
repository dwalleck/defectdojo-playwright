from playwright.sync_api import Page


class DashboardPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.add_product_link = page.get_by_role("link", name="Add Product", exact=True)
        self.all_products_link = page.get_by_role("link", name="All Products", exact=True)
        self.projects_menu = page.get_by_label("Products")