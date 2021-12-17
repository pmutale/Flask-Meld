def test_input_defer(browser_client, page):
    page.wait_for_timeout(500)
    page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-defer test")
    assert page.inner_text('#bound-data-defer') == ''
    page.click("#button")
    page.wait_for_timeout(100)
    assert page.inner_text('#bound-data-defer') == 'flask-defer test'


def test_checkbox_defer(browser_client, page):
    page.goto("http://127.0.0.1:5009/")
    foo_id = "#foo-id"
    foo = page.locator("#foo-id")

    assert page.inner_text("#bound-foo") == 'True'
    assert foo.is_checked()

    page.uncheck(foo_id)
    assert page.inner_text("#bound-foo") == 'True'
    page.click("#button")
    page.wait_for_timeout(200)
    assert foo.is_checked() is False
    assert page.inner_text("#bound-foo") == 'False'
    page.click("#button")

    # test_multiple_checkboxes
    page.check("#bar-a")
    assert page.inner_text("#bound-bar") == "[]"
    page.click("#button")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q']"
    page.check("#bar-b")
    page.click("#button")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q', 'v']"

    # test checkbox with int value
    page.check("#baz-id")
    page.click("#button")
    page.wait_for_timeout(100)
    assert page.inner_text("#bound-baz") == ""
    page.wait_for_timeout(100)
    assert page.inner_text("#bound-baz") == "2"

    # test multiple checkboxes in same request
    page.check("#bar-a")
    page.check("#bar-b")
    page.check("#bar-c")
    page.click("#button")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q', 'v', 'c']"
