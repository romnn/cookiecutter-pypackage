#!/usr/bin/env python
import os
import time
import subprocess


class _Halo:
    def __init__(self, *args, **kwargs):
        self.text = kwargs.get("text", "")

    def __enter__(self):
        print(self.text)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def _print(text):
        print(text)

    fail = succeed = _print


try:
    from halo import Halo
except (ImportError, ModuleNotFoundError):
    subprocess.check_output(
        "pip install --no-cache-dir halo", stderr=subprocess.STDOUT, shell=True
    )

try:
    from halo import Halo
except Exception:
    print("Failed to install progress spinners. Will fall back to plain text.")
    Halo = _Halo


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
                "pipenv run pre-commit install -t pre-commit", stderr=subprocess.STDOUT, shell=True
            )
            run_command(
                "pipenv run pre-commit install -t pre-push", stderr=subprocess.STDOUT, shell=True
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
            run_command("pipenv install --clear --dev", stderr=subprocess.STDOUT, shell=True)
        except Exception:
            spinner.fail("Failed to install development dependencies")
            raise
        spinner.succeed("Successfully installed development dependencies")


if __name__ == "__main__":
    install_dependencies()
    initialize_git()
    install_git_hooks()
