# Flask-Meld

Official Website - [Flask-Meld.dev](https://www.flask-meld.dev)

Project inspiration (outdated examples) - [Ditch Javascript Frameworks For Pure Python Joy](https://michaelabrahamsen.com/posts/flask-meld-ditch-javascript-frameworks-for-pure-python-joy/) 

Join the community on Discord - https://discord.gg/DMgSwwdahN

Meld is a framework for Flask to meld your frontend and backend code. What does
that mean? It means you can enjoy writing dynamic user interfaces in pure Python.

Less context switching.
No need to write javascript.
More fun!

# Flask-Meld Developer information

## Tests

### Installing test requirements

```sh
pip install -r tests/requirements.txt
playwright install
```


### Run with browser tests

```sh
# run the application on port 5009 without reload
cd tests/meld_test_project; flask run --port=5009 --no-reload

# run tests in another terminal
pytest

# to watch the browser tests
pytest --headed
```

### Run without browser tests

```sh
pytest --ignore=tests/browser
```

