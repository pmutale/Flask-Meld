def test_input_text(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("#input")
    # Fill input
    fill_text = "flask-meld input_text"
    page.fill("input", fill_text)
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-data-input") == fill_text

    # make sure the text in the input does not disappear
    assert page.input_value("#input") == fill_text


def test_text_area(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    # Click text area
    page.click("#text-area")
    # Fill input
    fill_text = "flask-meld textarea input"
    page.fill("#text-area", fill_text)
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-data-textarea") == fill_text

    # make sure the text in the input does not disappear
    assert page.input_value("#text-area") == fill_text
