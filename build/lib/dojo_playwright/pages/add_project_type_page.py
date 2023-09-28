from playwright.sync_api import Page


class AddProductTypePage:
    def __init__(self, page: Page):
        self.name = page.get_by_label('Name')
        self.description = page.get_by_role("application").get_by_role("textbox")
        self.submit_button = page.get_by_role('button', name='Submit')
