## Templates

Create a component template in `templates/meld/counter.html`. By creating a file
within the `templates/meld` directory just include `{% meld 'counter' %}` where
you want the component to load.

Here is an example for counter:

```html
{# templates/meld/counter.html #}
<div>
    <button meld:click="subtract">-</button>
    <input type="text" meld:model="count" readonly></input>
    <button meld:click="add">+</button>
</div>
```
Let's take a look at that template file in more detail.

The buttons use `meld:click` to call the `add` or `subtract` function of the
Counter component.
The input uses `meld:model` to bind the input to the `count` property on the
Counter component.  

Note, to avoid errors, when adding a comment to a component template use the
Jinja syntax, `{# comment here #}`, rather than the HTML syntax.

### Pass data to a component

You can, of course, pass data to your meld component. Meld is passing **kwargs 
to the render function of the *meld* templatetag, so you can pass any number of 
named arguments. The component is found based on the first parameter, aka name 
of the component, and any number of data passed afterwards. 

Providing a very basic component as an example to display a greeting message using
the passed value for the keyword "name" in the corresponding template.

```html
{# templates/meld/greeter.html #}
<div>
    Hello, {{name or "Nobody"}}
</div>
```
which can be invoked using:

```html
{# templates/base.html #}
{% meld 'greeter', name="John Doe" %}
```

### Use passed values in a component (advanced use)

If you want to use the passed arguments from the meld template tag in your component (e.g. configuring the component or adding initial data), you can simply use them from the constructor: 

```py
class Greeter(Component):

    def __init__(self, **kwargs):
        super().__init__()
        name = kwargs.get('name', 'Nobody')
```

```html
<div>
    Hello, {{name}}
</div>
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
