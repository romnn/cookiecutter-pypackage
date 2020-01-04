# !/usr/bin/env python

from setuptools import setup

test_requirements = [
    "tox",
    "pytest",
    "pytest-cov",
    "pytest-cookies",
    "pytest-xdist",
    "pytest-sugar",
    "oyaml",
    # "pyfakefs",
]
coverage_requirements = ["coverage", "codecov"]
docs_requirements = ["sphinx>=2.0", "romnnn_sphinx_press_theme", "sphinxemoji"]
dev_requirements = ["invoke", "pre-commit", "cookiecutter"]

setup(
    name="romnnn-cookiecutter-pypackage",
    packages=[],
    python_requires=">=3.6",
    version="0.1.0",
    description="Cookiecutter template for a python package",
    author="romnnn",
    license="BSD",
    author_email="contact@romnn.com",
    url="https://github.com/romnnn/cookiecutter-pypackage",
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
