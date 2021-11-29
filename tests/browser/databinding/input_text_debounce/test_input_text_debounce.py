def test_input_defer(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-debounce test")
    assert page.inner_text('#bound-data') == ''
    page.wait_for_timeout(200)
    assert page.inner_text('#bound-data') == 'flask-debounce test'
