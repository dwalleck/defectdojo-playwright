from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label('Username')
        self.password = page.get_by_label('Password')
        # self.username = page.locator('id=id_username')
        # self.password = page.locator('id=id_password')
        self.login_button = page.get_by_role('button', name='Login')

    def navigate(self):
        self.page.goto("https://demo.defectdojo.org/login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
