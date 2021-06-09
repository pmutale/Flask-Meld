# Basic usage

## Project setup

### Create a new project
First, let's create our new project, let's call it `meld-example`:

```bash
meld new project meld-example
```

This will create the `meld-example` directory with the following content:

```text
meld-example
├── app
│   └── __init__.py
│   └── meld
│   └── static
│   └── templates
│   └── wsgi.py
├── tests
├── config.py
└── requirements.txt
```

### Use Meld in an existing project
Meld can be added to an existing application by completing the following steps:

- Import Meld into your application with `from flask_meld import Meld`
- Initialize the Meld extension. 
    - If you are using the Application Factory pattern, this means adding 
    `meld = Meld()` and `meld.init_app(app)` in your `__init__.py` file.
    - If using a single `app.py` instead of using the `init_app` you can simply
      initialize Meld by using `Meld(app)
    - Add `{% meld_scripts %}` in the `body` of your base HTML template
    - Use the socketio server to serve your application with `socketio.run(app)` or to 
    specify a port and debugging use `socketio.run(app=app, port=5000, debug=True)`

## Components

Components consist of a Python class and a Jinja template that together, enable
you to create dynamic content without the need to write JavaScript.

The best way to start to understand how components work is to look at an example.

```py
# app/meld/components/counter.py

from flask_meld import Component


class Counter(Component):
    count = 0

    def add(self):
        self.count = int(self.count) + 1

    def subtract(self):
        self.count = int(self.count) - 1

```
The class above creates a property named `count` and defines the `add` and
`subtract` functions which will modify the `count` property.  Combining the use of 
properties and functions in this way allows you to customize the behavior of your components.


```html
<!-- templates/meld/counter.html -->
<div>
    <button meld:click="subtract">-</button>
    <input type="text" meld:model="count" readonly></input>
    <button meld:click="add">+</button>
</div>
```

The template includes two buttons and an input field. The buttons bind to the functions
using `meld:click="add"` and `meld:click:"subtract"` while the input binds to the
`count` property with `meld:model="count"`. 

### Properties

Components store model data for the class using `properties`. 

```
class Counter(Component):
    count = 0
```

### Data Binding

You can bind a compenent property to an html element with `meld:model`. For instance,
you can easily update a property by binding it to an `input` element. When a user types
text in the input field, the property is automatically updated in the component.

```
class Person(Component):
    name = ""
---------------------------------------------
<div>
    <input meld:model="name" type="text">

    <h1>Hello {{ name }}</h1>
</div>
```

You can use `meld:model` on the following elements:

```
<input type="text">
<input type="radio">
<input type="checkbox">
<select>
<textarea>
```

## Templates

You can pass arguments to a component from a template with the following syntax:

```
{% meld "search", site_id=site.id %}
```

Use the arguments within your component by referencing `self` in your functions.

```py
class Search(Component):

    def search(self):
        site_id = self.site_id
```

### Modifiers

Use modifiers to change how Meld handles network requests.

* `debounce`: `<input meld:model.debounce-500="search">` Delay network requests for an amount of time after a keypress. Used to increase performance and sync when the user has paused typing for an amount of time. `debounce-250` will wait 250ms before it syncs with the server. The default is 150ms.

* `defer`: `<input meld:model.defer="search">` Pass the search field with the next network request. Used to improve performance when realtime databinding is not necessary.

* `prevent`: Use to prevent a default action. The following example uses `defer` to delay sending a network request until the form is submitted. An idea of how this can be used: instead of adding a keydown event listener to the input field to capture the press of the `enter` key, a form with `meld:submit.prevent="search"` can be used to to invoke a component's `search` function instead of the default form handler on form submission.

```html
<form meld:submit.prevent="search">
    <input meld:model.defer="search_text" type="text" name="name" id="name" placeholder="Search for name">
    <button meld:click="search">Search</button>

    <!-- To get the same functionality without using meld:submit.prevent="search" you
    would need to add an event listener for the enter key 
    <input meld:model.defer="search_text" meld:keydown.Enter="search" type="text" name="name" id="name" placeholder="Search for name">
    -->
</form>
```
