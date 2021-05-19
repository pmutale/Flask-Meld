import os
import secrets
from pathlib import Path

import click

from flask_meld.templates import (
    base_html_template,
    config_template,
    components,
    components_template,
    env_template,
    index_html_template,
    init_template,
    requirements_template,
    wsgi_template,
)


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
        generate_file_with_content(base_dir, "app/__init__.py", init_template.template)
        generate_file_with_content(base_dir, "app/wsgi.py", wsgi_template.template)
        generate_file_with_content(
            base_dir, "app/templates/base.html", base_html_template.template
        )
        generate_file_with_content(
            base_dir, "app/templates/index.html", index_html_template.template
        )

        generated_secret_key = secrets.token_hex(16)
        generate_file_with_content(
            base_dir, ".env", env_template.substitute(secret_key=generated_secret_key)
        )
    except OSError:
        pass


@meld.command()
@click.argument("name")
def component(name):
    """Create a new component"""
    click.echo(f"Creating component '{name}'.")
    generate_meld_component(name)


def generate_meld_component(name):
    try:
        base_dir = Path.cwd()
        components_dir = (base_dir / "app" / "meld" / "components")
        templates_dir = (base_dir / "app" / "templates" / "meld")
        # todo: get root dir from any position
        if not (os.path.exists(components_dir) and os.path.exists(templates_dir)):
            click.echo(f"Failed. Are you in the app directory? Could not find:\n{components_dir}\n{templates_dir}")
            return
        class_name = name[:1].upper() + name[1:]  # Capitalize, and leave any other capitalization intact
        if os.path.exists(components_dir / f"{name}.py") or os.path.exists(templates_dir / f"{name}.html"):
            click.echo(f"Failed. Component named '{name}' already exists.")
            return
        generate_file_with_content(components_dir, f"{name}.py", components.substitute(class_name=class_name))
        generate_file_with_content(templates_dir, f"{name}.html", components_template.template)
        click.echo(f"Component '{name}' successfully created.")
    except OSError:
        click.echo(f"Failed. Unable to write to disk. Is the disk full/do we have sufficient permissions?")


def generate_file_with_content(path, filename, file_contents):
    path = Path(f"{path}/{filename}")
    with open(path, "w") as f:
        f.write(file_contents)
    return path


if __name__ == "__main__":
    meld()
