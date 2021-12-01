def test_input_defer(browser_client, page):
    page.wait_for_timeout(500)
    page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-defer test")
    page.click("#button")
    assert page.inner_text('#bound-data-defer') == ''
    page.wait_for_timeout(200)
    assert page.inner_text('#bound-data-defer') == 'flask-defer test'
