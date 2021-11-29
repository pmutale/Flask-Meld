def test_input_text(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    # wait for component.loaded
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-meld1")
    finished = False
    while not finished:
        if page.inner_text('#bound-data') == 'flask-meld1':
            finished = True
            assert page.inner_text('#bound-data') == 'flask-meld1'
