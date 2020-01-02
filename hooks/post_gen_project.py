#!/usr/bin/env python
import os
import time
import subprocess

try:
    from halo import Halo
except ImportError:
    subprocess.check_output(
        "python3 -m pip install halo", stderr=subprocess.STDOUT, shell=True
    )
    from halo import Halo


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def run_command(*cmd_args, **cmd_kwargs):
    try:
        return subprocess.check_output(*cmd_args, **cmd_kwargs).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output.decode("utf-8"))
        raise


def install_git_hooks():
    with Halo(text="Installing git hooks", spinner="dots", color="cyan") as spinner:
        try:
            run_command(
                "pre-commit install -t pre-commit", stderr=subprocess.STDOUT, shell=True
            )
            run_command(
                "pre-commit install -t pre-push", stderr=subprocess.STDOUT, shell=True
            )
            time.sleep(0.5)
        except Exception:
            spinner.fail("Failed to install git hooks")
            raise
        spinner.succeed("Successfully installed git hooks")


def initialize_git():
    with Halo(text="Initializing git repository", spinner="dots", color="red") as spinner:
        try:
            run_command(
                "cd {} && git init".format(PROJECT_DIRECTORY),
                stderr=subprocess.STDOUT,
                shell=True,
            )
            time.sleep(0.5)
        except Exception:
            spinner.fail("Failed to initialize git repository")
            raise
        spinner.succeed("Successfully initialized git repository")


def install_dependencies():
    with Halo(text="Installing development dependencies", spinner="dots", color="magenta") as spinner:
        try:
            run_command("python3 -m pip install pipx", stderr=subprocess.STDOUT, shell=True)
            run_command("python3 -m pipx ensurepath", stderr=subprocess.STDOUT, shell=True)
            run_command("pipx install pipenv", stderr=subprocess.STDOUT, shell=True)
            run_command("pipenv install --dev", stderr=subprocess.STDOUT, shell=True)
        except Exception:
            spinner.fail("Failed to install development dependencies")
            raise
        spinner.succeed("Successfully installed development dependencies")


if __name__ == "__main__":
    install_dependencies()
    initialize_git()
    install_git_hooks()
