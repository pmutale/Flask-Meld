import pytest
from flask import url_for, render_template, render_template_string


def test_input_text(live_server, page, browser_client):
    @live_server.app.route('/load-data')
    def get_endpoint():
        return render_template_string("""
    {% extends "base.html" %}
    {% block content %}
    {% meld 'default' %}{% endblock %}
    """, _external=True)

    live_server.start()
    # page.goto(url_for('index', _external=True))
    page.goto(url_for('get_endpoint', _external=True))
    # page.goto("http://127.0.0.1:5009/")
    # Click input
    page.click("#input")
    # Fill input
    fill_text = "flask-meld input_text"
    page.fill("input", fill_text)
    page.wait_for_timeout(2000)
    assert page.inner_text("#bound-data-input") == fill_text

    # # make sure the text in the input does not disappear
    # assert page.input_value("#input") == fill_text


# def test_text_area(browser_client, page):
#     page.goto("http://127.0.0.1:5009/")
#     # Click text area
#     page.click("#text-area")
#     # Fill input
#     fill_text = "flask-meld textarea input"
#     page.fill("#text-area", fill_text)
#     page.wait_for_timeout(200)
#     assert page.inner_text("#bound-data-textarea") == fill_text
#
#     # make sure the text in the input does not disappear
#     assert page.input_value("#text-area") == fill_text
#
#
# def test_checkbox(browser_client, page):
#     page.goto("http://127.0.0.1:5009/")
#     foo_id = "#foo-id"
#     foo = page.locator(foo_id)
#
#     assert page.inner_text("#bound-foo") == 'True'
#     assert foo.is_checked()
#
#     page.uncheck(foo_id)
#     page.wait_for_timeout(200)
#
#     assert foo.is_checked() is False
#     assert page.inner_text("#bound-foo") == 'False'
#
#     # test_multiple_checkboxes
#     page.check("#bar-a")
#     page.wait_for_timeout(200)
#     page.check("#bar-b")
#     page.wait_for_timeout(200)
#     assert page.inner_text("#bound-bar") == "['q', 'v']"
#
#     # test checkbox with int value
#     page.check("#baz-id")
#     page.wait_for_timeout(200)
#     assert page.inner_text("#bound-baz") == "2"
#
#
# def test_radio_field(browser_client, page):
#     page.goto("http://127.0.0.1:5009/")
#     page.click("#html")
#     page.wait_for_timeout(200)
#
#     assert page.inner_text("#bound-radio") == 'HTML'
#
#     page.click("#python")
#     page.wait_for_timeout(200)
#     assert page.inner_text("#bound-radio") == 'Python'
