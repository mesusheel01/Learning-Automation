from playwright.sync_api import sync_playwright

def test_login_ui():

    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://cognitos.vercel.app/signup")
        page.fill("input[name='username']", "test2e2")
        page.fill("input[name='email']", "test2@gmail.com")
        page.fill("input[name='password']", "test2T2")

        page.click("button[type='submit']")
        
        page.wait_for_url("**/dashboard")

        assert "dashboard" in page.url

        browser.close()
