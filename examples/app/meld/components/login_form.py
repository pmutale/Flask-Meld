from flask_meld.component import Component
from flask import redirect, url_for
from app.forms import LoginForm as Form


class LoginForm(Component):
    form = Form()
    errors = None
    valid = True
    submitted = False
    show_password = False

    def updated(self, field):
        self.validate(field)
        self.submitted = False

    def save(self):
        self.valid = self.validate()
        self.submitted = True
        print(redirect(url_for("index")))
        #return redirect(url_for("index"))

    def toggle_show_password(self):
        self.show_password = not self.show_password
