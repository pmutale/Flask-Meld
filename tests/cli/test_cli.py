import os
from pathlib import Path
from flask_meld.cli import generate_meld_app, generate_file_with_content
from flask_meld.templates import requirements_template
from cli.expectations import expected_requirements


def test_generate_file_content(tmpdir_factory):
    test_dir = tmpdir_factory.mktemp("test_file_content_generator")
    os.chdir(test_dir)
    path = generate_file_with_content(
        test_dir, "requirements.txt", requirements_template.template
    )
    with path.open("r") as f:
        contents = f.read()
        assert contents == expected_requirements


def test_creates_component_dir(generate_app_and_chdir):
    # generate_app_and_chdir fixture creates directory structure of project
    expected_path = Path(Path.cwd() / "test_project" / "app" / "meld" / "components")
    assert expected_path.is_dir()


def test_creates_tests_dir(generate_app_and_chdir):
    expected_path = Path(Path.cwd() / "test_project" / "tests")
    assert expected_path.is_dir()


def test_creates_tests_static(generate_app_and_chdir):
    expected_path = Path(Path.cwd() / "test_project" / "app" / "static" / "images")
    assert expected_path.is_dir()


def test_creates_templates_dir(generate_app_and_chdir):
    expected_path = Path(Path.cwd() / "test_project" / "app" / "templates" / "meld")
    assert expected_path.is_dir()


def test_creates_config_file(generate_app_and_chdir):
    expected_path = Path(Path.cwd() / "test_project" / "config.py")
    assert expected_path.exists()


def test_creates_init_file(generate_app_and_chdir):
    expected_path = Path(Path.cwd() / "test_project" / "app" / "__init__.py")
    assert expected_path.exists()
