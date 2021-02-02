# !/usr/bin/env python

from setuptools import setup

version = "0.2.0"

test_requirements = [
    "tox",
    "pytest",
    "pytest-cov",
    "pytest-cookies",
    "pytest-xdist",
    "pytest-sugar",
    "ruamel.yaml"
]
coverage_requirements = ["coverage", "codecov"]
docs_requirements = ["sphinx>=2.0", "romnn_sphinx_press_theme", "sphinxemoji"]
dev_requirements = ["invoke", "pre-commit", "cookiecutter"]

setup(
    name="romnn-cookiecutter-pypackage",
    packages=[],
    python_requires=">=3.6",
    version=version,
    description="Cookiecutter template for a python package",
    author="romnn",
    license="BSD",
    author_email="contact@romnn.com",
    url="https://github.com/romnn/cookiecutter-pypackage",
    keywords=["cookiecutter", "template", "package"],
    extras_require=dict(
        dev=dev_requirements
        + docs_requirements
        + test_requirements
        + coverage_requirements,
        docs=docs_requirements,
        test=test_requirements + coverage_requirements,
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)
