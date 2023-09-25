from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.defectdojo.org/login?next=/")
    page.get_by_label("Username*").click()
    page.get_by_label("Username*").fill("admin")
    page.get_by_label("Username*").press("Tab")
    page.get_by_label("Password*").click()
    page.get_by_label("Password*").fill("1Defectdojo@demo#appsec")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Add Product", exact=True).click()
    page.get_by_label("Name*").fill("Another Product")
    page.locator("pre").nth(1).click()
    page.get_by_role("application").get_by_role("textbox").fill("Some details about another product")
    page.get_by_placeholder("Enter some tags (comma separated, use enter to select / create a new tag)").click()
    page.get_by_placeholder("Enter some tags (comma separated, use enter to select / create a new tag)").fill("stuff,")
    page.locator("#base-content div").filter(has_text="Product manager --------- (user2) (admin) (product_manager) ---------").get_by_title("---------").click()
    page.locator("#bs-select-1-2").click()
    page.locator("#base-content div").filter(has_text="Technical contact --------- (user2) (admin) (product_manager) ---------").get_by_title("---------").click()
    page.locator("#bs-select-2-2").click()
    page.locator("#base-content div").filter(has_text="Product Type* --------- Billing Commerce Research and Development ---------").get_by_title("---------").click()
    page.locator("#bs-select-4-1").click()
    page.get_by_role("combobox", name="Default").click()
    page.locator("#bs-select-5-0").click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
