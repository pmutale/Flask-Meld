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
    click.echo(f"Creating app {name}")
    generate_meld_app(name)


def generate_meld_app(name):
    try:
        base_dir = Path.cwd() / name
        os.makedirs(base_dir / "app" / "meld" / "components")
    except OSError:
        pass


def generate_file_with_content(path, filename, file_contents):
    path = Path(f"{path}/{filename}")
    with open(path, "w") as f:
        f.write(file_contents)
    return path


if __name__ == "__main__":
    meld()
