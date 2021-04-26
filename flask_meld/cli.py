import os
import sys
import typer
from pathlib import Path, PurePath

app = typer.Typer()


@app.command()
def init(name: str):
    """Create a new flask-meld app with application defaults"""
    typer.echo(f"Generating app {name}")
    generate_meld_app(name)


@app.callback()
def main(ctx: typer.Context):
    """
    Manage Meld applications with the commandline
    """
    pass


def generate_meld_app(name: str):
    try:
        path = Path.cwd() / 'app' / 'meld' / 'components'
        os.makedirs(path)
        print(path)
    except OSError:
        pass

if __name__ == "__main__":
    app()
