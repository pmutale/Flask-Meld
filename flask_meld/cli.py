import os
import click
from pathlib import Path


@click.group()
def meld():
    """Flask-Meld specific commands"""


@meld.command()
@click.argument("name")
def new(name):
    """Create a new flask-meld app with application defaults"""
    generate_meld_app(name)


def generate_meld_app(name):
    try:
        path = Path.cwd() / name / "app" / "meld" / "components"
        os.makedirs(path)
    except OSError:
        pass


if __name__ == "__main__":
    meld()
