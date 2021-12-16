def test_input_debounce(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-debounce test")
    assert page.inner_text('#bound-data') == ''
    page.wait_for_timeout(100)
    assert page.inner_text('#bound-data') == ''
    page.wait_for_timeout(200)
    assert page.inner_text('#bound-data') == 'flask-debounce test'


def test_checkbox(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    foo_id = "#foo-id"
    foo = page.locator("#foo-id")

    assert page.inner_text("#bound-foo") == 'True'
    assert foo.is_checked()

    page.uncheck(foo_id)
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-foo") == 'True'
    page.wait_for_timeout(200)
    assert foo.is_checked() is False
    assert page.inner_text("#bound-foo") == 'False'

    # test_multiple_checkboxes
    page.check("#bar-a")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "[]"
    page.check("#bar-b")
    page.wait_for_timeout(100)
    assert page.inner_text("#bound-bar") == "['q']"
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q', 'v']"

    # test checkbox with int value
    page.check("#baz-id")
    page.wait_for_timeout(100)
    assert page.inner_text("#bound-baz") == ""
    page.wait_for_timeout(100)
    assert page.inner_text("#bound-baz") == "2"
