from playwright.sync_api import Page

from dojo_playwright.pages.partials.menu_sections import (
    ComponentsMenu,
    EndpointsMenu,
    FindingsMenu,
    MetricsMenu,
    ProjectsMenu,
    EngagementsMenu,
    QuestionnairesMenu,
    ToolsMenu,
    UsersMenu,
)


class NavBar:
    def __init__(self, page: Page):
        self.projects_menu = ProjectsMenu(page)
        self.engagements_menu = EngagementsMenu(page)
        self.findings_menu = FindingsMenu(page)
        self.components_menu = ComponentsMenu(page)
        self.endpoints_menu = EndpointsMenu(page)
        self.metrics_menu = MetricsMenu(page)
        self.users_menu = UsersMenu(page)
        self.questionnaires_menu = QuestionnairesMenu(page)
        self.tool_type_menu = ToolsMenu(page)
