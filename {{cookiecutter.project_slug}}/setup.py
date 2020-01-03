#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup
from pathlib import Path

short_description = "No description has been added so far."

try:
    if (Path().parent / "README.rst").is_file():
        with open(str(Path().parent / "README.rst")) as readme_file:
            long_description = readme_file.read()
    elif (Path().parent / "README.md").is_file():
        import m2r

        long_description = m2r.parse_from_file(Path().parent / "README.md")
    else:
        raise AssertionError("No readme file")
except (ImportError, AssertionError):
    long_description = short_description

requirements = ["Click>=6.0"]
setup_requirements = ["pytest-runner"]
test_requirements = ["pytest", "pre-commit"]
docs_requirements = ["sphinxemoji", "sphinx>=2.0", "romnnn_sphinx_press_theme"]
dev_requirements = (
    ["m2r", "twine"] + setup_requirements + test_requirements + docs_requirements
)

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main"
        ]
    },
    install_requires=requirements,
    license="MIT",
    python_requires=">=3.5",
    description=short_description,
    long_description=long_description,
    include_package_data=True,
    package_data={"{{ cookiecutter.project_slug }}": []},
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require=dict(
        dev=dev_requirements, docs=docs_requirements
    ),
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    zip_safe=False,
)
