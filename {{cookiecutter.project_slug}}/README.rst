===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/test/badge.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions
        :alt: Build Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: PyPI version

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: License

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Test Coverage

""""""""

Your short description here. `{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }} <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}>`_

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

.. code-block:: python

    import {{ cookiecutter.project_slug }}

Development
-----------

For detailed instructions see `CONTRIBUTING <CONTRIBUTING.rst>`_.

Tests
~~~~~~~
You can run tests with

.. code-block:: console

    $ invoke test
    $ invoke test --min-coverage=90     # Fail when code coverage is below 90%
    $ invoke type-check                 # Run mypy type checks

Linting and formatting
~~~~~~~~~~~~~~~~~~~~~~~~
Lint and format the code with

.. code-block:: console

    $ invoke format
    $ invoke lint

All of this happens when you run ``invoke pre-commit``.

Note
-----

This project is still in the alpha stage and should not be considered production ready.
