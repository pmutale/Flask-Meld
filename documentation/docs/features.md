# Features
## Form Validation

A big part of creating web applications is using forms. Flask-Meld integrates with
Flask-WTF to give you real-time form validation without writing any Javascript.

### Integration with WTForms for validation

Define your form with Flask-WTF

```py
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
```

### Create your template

Use WTForm helpers to create your form in your HTML template. 

```html
<!-- templates/meld/register.html -->
<div>
    <form method="POST">
        <div>
            {{ form.email.label }}
            {{ form.email }}
            <span> {{ errors.password | first }} </span>
        </div>

        <div>
            {{ form.password.label }}
            {{ form.password }}
            <span> {{ errors.password | first }} </span>
        </div>
        <div>
            {{ form.password_confirm.label }}
            {{ form.password_confirm }}
            <span> {{ errors.password_confirm | first }} </span>
        </div>
        <div>
            {{ form.submit }}
        </div>
    </form>
</div>
```

Using the WTForm helpers saves you some typing. 
Alternatively, you can define your HTML form without using the helpers. 
For example, to make a field use
`<input id="email" meld:model="email" name="email" required="" type="text" value="">`
Make sure that `meld:model="name_of_field"` exists on each field.

### Define the form in the component

```py
# meld/components/register.py
from flask_meld import Component
from forms import RegistrationForm


class Register(Component):
    form = RegistrationForm()
```

## Realtime form validation

To make your form validate as a user types use the `updated` function. This will provide
the form field and allow you to validate on the fly. Simply call `validate` on the
field.

```py
# meld/components/register.py
from flask_meld import Component
from forms import RegistrationForm


class Register(Component):
    form = RegistrationForm()

    def updated(self, field):
        self.validate(field)
```

### Routes

You can create a custom method on your component (such as a `save` method) to handle
submissions or you can use your regular old Flask routes. 

```py
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # do anything you need with your form data...
        return redirect(url_for("index"))
    return render_template("register_page.html")
```
