from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/")
    page.locator("text=Add/Remove Elements").click()
    page.wait_for_url("https://the-internet.herokuapp.com/add_remove_elements/")
    page.locator("text=Add Element").click()
    assert page.query_selector('//button[text() = "Delete"]') is not None

    page.locator("text=Delete").click()
    
    page.close()
    context.close()
    browser.close()

def test_testcase():
    with sync_playwright() as playwright:
        run(playwright)

