"""
Test the Cookiecutter template.
"""
from cookiecutter.generate import generate_context
from cookiecutter.main import cookiecutter
from pathlib import Path
from shlex import split
from subprocess import run
from venv import create

import pytest


@pytest.fixture(scope="session")
def template() -> Path:
    """ The template under test.

    """
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def tmpdir(tmp_path_factory) -> Path:
    """ Test directory.

    """
    return tmp_path_factory.mktemp("test_template")


@pytest.fixture(scope="module")
def context(template) -> dict:
    """ Template context for testing.

    """
    context = generate_context(template.joinpath("cookiecutter.json"))
    context["cookiecutter"].update({
        "project_slug": "slugify"
    })
    return context["cookiecutter"]


@pytest.fixture(scope="module")
def project(tmpdir, template, context) -> Path:
    """ Create a test project from the Cookiecutter template.

    """
    cookiecutter(str(template), no_input=True, output_dir=tmpdir, extra_context=context)
    return tmpdir / context["project_slug"]


@pytest.fixture
def python(tmp_path):
    """ Create a Python virtual environment for testing.

    """
    venv = tmp_path / ".venv"
    create(venv, with_pip=True)
    return venv / "bin" / "python"


def test_project(project):
    """ Verify that the project was created correctly.

    """
    # Just a basic sanity test.
    assert len(list(project.iterdir())) == 4
    return


@pytest.fixture
def install_render_engine_cli(python):
    install_cli = "pip install render_engine[cli]"
    install_args = split(f"{python} -m {install_cli}")
    install_process = run(install_args)
    assert install_process.returncode == 0


def test_site_generation(context, project, python, install_render_engine_cli):
    generate_site = "render_engine build app:app"
    generate_args = split(f"{python} -m {generate_site}")
    generate_process = run(generate_args, cwd=project)
    assert generate_process.returncode == 0


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
