from flask_meld.component import Component
from flask import redirect, url_for


class InputTextDebounce(Component):
    first_name = ""
