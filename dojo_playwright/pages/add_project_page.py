from playwright.sync_api import Page

class AddProjectPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.name_field = page.get_by_label("Name")
        self.description = page.get_by_role("application").get_by_role("textbox")
        self.project_manager = page.locator('#id_product_manager')
        self.project_type = page.locator('#id_prod_type')
        self.sla_config = page.locator('#id_sla_configuration')
        self.submit_button = page.get_by_role('button', name='Submit')