import os
import click
import secrets
from pathlib import Path
from flask_meld.templates import requirements_template, config_template, init_template


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
        os.makedirs(base_dir / "app" / "templates" / "meld")
        os.makedirs(base_dir / "app" / "static" / "images")
        os.makedirs(base_dir / "app" / "static" / "css")
        os.makedirs(base_dir / "tests")
        generate_file_with_content(
            base_dir, "requirements.txt", requirements_template.template
        )
        generate_file_with_content(base_dir, "config.py", config_template.template)
        generate_file_with_content(
            base_dir, "app/__init__.py", init_template.template
        )
        generate_file_with_content(
            base_dir, "app/wsgi.py", init_template.template
        )

        generated_secret_key = secrets.token_hex(16)
        generate_file_with_content(
            base_dir, ".env", init_template.substitute(generated_secret_key)
        )
    except OSError:
        pass


def generate_file_with_content(path, filename, file_contents):
    path = Path(f"{path}/{filename}")
    with open(path, "w") as f:
        f.write(file_contents)
    return path


if __name__ == "__main__":
    meld()
