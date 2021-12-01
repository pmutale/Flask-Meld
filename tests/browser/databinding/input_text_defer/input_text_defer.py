from flask_meld.component import Component
from flask import redirect, url_for


class InputTextDefer(Component):
    first_name = ""
