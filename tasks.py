"""Development tasks for the cookiecutter template project"""

import webbrowser
import platform
from invoke import task
from pathlib import Path
Path().expanduser()

ROOT_DIR = Path(__file__).parent
TEST_DIR = ROOT_DIR.joinpath('tests')


@task
def test(c):
    """
    Run tests
    """
    pty = platform.system() == 'Linux'
    c.run("pipenv run pytest --cov={}".format(ROOT_DIR), pty=pty)
