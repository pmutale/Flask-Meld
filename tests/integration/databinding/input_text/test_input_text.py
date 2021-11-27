def test_this(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-meld1")
    page.wait_for_timeout(500)
    assert page.inner_text('#bound-data') == 'flask-meld1'
