import os
from playwright.sync_api import sync_playwright

def verify_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Index
        cwd = os.getcwd()
        index_path = f"file://{cwd}/index.html"
        print(f"Navigating to {{index_path}}")
        page.goto(index_path)
        page.screenshot(path="verification/index.png", full_page=True)
        print("Captured index.png")

        # Verify Service Page
        service_path = f"file://{cwd}/services/gcc-advisory.html"
        print(f"Navigating to {{service_path}}")
        page.goto(service_path)
        page.screenshot(path="verification/service.png", full_page=True)
        print("Captured service.png")

        # Verify Mobile Menu (simulate mobile view)
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(index_path)
        # Click the menu icon if possible, but just taking a screenshot of mobile layout is good enough
        page.screenshot(path="verification/mobile_index.png", full_page=True)
        print("Captured mobile_index.png")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    verify_pages()
