from playwright.sync_api import Page


class ProjectsMenu:
    def __init__(self, page: Page):
        self.section_icon = page.get_by_label("Products")
        page.get_by_role("link", name="All Products")
        page.get_by_role("link", name="Add Product", exact=True)
        page.get_by_role("link", name="All Product Types")
        page.get_by_role("link", name="Add Product Type")


class EngagementsMenu:
    def __init__(self, page: Page):
        self.section_icon = page.get_by_label("Engagements")
        page.get_by_role("link", name="Active Engagements")
        page.get_by_role("link", name="All Engagements")
        page.get_by_role("link", name="Engagements by Product")
        page.get_by_role("link", name="Test Types")
        page.get_by_role("link", name="Environments")


class FindingsMenu:
    def __init__(self, page: Page):
        self.section_icon = page.get_by_label("Findings")
        page.get_by_role("link", name="Open Findings")
        page.get_by_role("link", name="All Findings")
        page.get_by_role("link", name="Closed Findings")
        page.get_by_role("link", name="Risk Accepted Findings")
        page.get_by_role("link", name="Finding Templates")


class ComponentsMenu:
    def __init__(self, page: Page):
        self.section_icon = page.get_by_label("Components")
        page.get_by_role("link", name="All Components")


class EndpointsMenu:
    def __init__(self, page: Page):
        self.section_icon = page.get_by_label("Endpoints")
        page.get_by_role("link", name="All Endpoints")
        page.get_by_role("link", name="All Hosts")
        page.get_by_role("link", name="Vulnerable Endpoints")
        page.get_by_role("link", name="Vulnerable Hosts")
        page.get_by_role("link", name="Migrate Endpoints")


class MetricsMenu:
    def __init__(self, page: Page):
        self.section_menu = page.get_by_label("Metrics")
        page.get_by_role("link", name="Metrics Dashboard")
        page.get_by_role("link", name="Critical Product Metrics")
        page.get_by_role("link", name="Product Type Metrics")
        page.get_by_role("link", name="Product Type Counts")
        page.get_by_role("link", name="Simple Metrics")
        page.get_by_role("link", name="Engineer Metrics")


class UsersMenu:
    def __init__(self, page: Page):
        self.section_menu = page.get_by_label("Users")
        page.locator("#side-menu").get_by_role("list").get_by_role("link", name="Users")
        page.get_by_role("link", name="Groups")


class QuestionnairesMenu:
    def __init__(self, page: Page):
        self.section_menu = page.get_by_label("Questionnaires")
        page.get_by_role("link", name="All Questionnaires")
        page.get_by_role("link", name="All Questions")


class ToolsMenu:
    def __init__(self, page: Page):
        self.tool_type_menu = page.get_by_label("Configuration")
        page.get_by_role("link", name="Announcement")
        page.get_by_role("link", name="Credential Manager")
        page.get_by_role("link", name="Login Banner")
        page.get_by_role("link", name="Note Types")
        page.get_by_role("link", name="Notifications")
        page.get_by_role("link", name="Regulations")
        page.get_by_role("link", name="SLA Configuration")
        page.get_by_role("link", name="System Settings")
        page.get_by_role("link", name="Tool Configuration")
        page.get_by_role("link", name="Tool Type")
