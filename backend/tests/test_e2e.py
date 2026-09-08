from playwright.sync_api import sync_playwright

def test_health_endpoint():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        response = page.goto("http://localhost:8000/health")
        assert response.status == 200
        browser.close()

def test_incident_api():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        response = page.goto("http://localhost:8000/incidents")
        assert response.status == 200
        browser.close()