.. highlight:: console

===============================
Cookiecutter PyPackage (romnn)
===============================

.. image:: https://github.com/romnn/cookiecutter-pypackage/workflows/test/badge.svg
    :target: https://github.com/romnn/cookiecutter-pypackage/actions
    :alt: Build status

Opinionated ``cookiecutter`` template for python packages, forked from `briggySmalls/cookiecutter-pypackage`_.

The key features of this template include:

* Dependency tracking using ``pipenv``
* Linting using ``flake8``
* Formatting provided by ``black`` and ``isort``
* Automatic documentation from Google style docstrings with ``sphinx``
* All development tasks (``lint``, ``format``, ``test``, etc) wrapped up in a cli by ``invoke``
* Automatic deployment to PyPI_

Features
--------

This template has most of the features of the original `briggySmalls/cookiecutter-pypackage`_
(which is based on `audreyr/cookiecutter-pypackage`_), but has been configured
to my personal needs and modified for ease of use and simplicity.

.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

The following features have been **removed**:

* Support for ``python2``. It's finally over! :tada:
* Support for bootstrapping multiple licenses. MIT is used.
* Support for bootstrapping multiple testing frameworks. ``pytest`` is used.
* Optional Google docstrings are now default.
* Only ``flake8`` (no more ``pylint``) is used for linting
* No more ``HISTORY.rst`` file. Must be manually included for projects that require it.
* AppVeyor_ continuous integration. Only GitHub Actions is used.

.. _AppVeyor: https://www.appveyor.com/

The following features have been **changed**:

* ``yapf`` was replaced by ``black`` for formatting python code

The following features have been **added**:

* ``pre-commit`` hooks that are automatically installed and run before every commit
* Aggressive type-checking using ``mypy``
* good test coverage is a requirement
* Automatic initialization of a ``git`` repository post generation
* Automatic installation of development dependencies post generation

Quickstart
----------

Install ``cookiecutter>=1.4.0``, ``virtualenv`` and `pipenv <https://github.com/pypa/pipenv>`_ if you haven't already::

    $ python3 -m pip install --no-cache-dir virtualenv
    $ python3 -m pip install -U cookiecutter
    $ sudo apt install pipenv     # for apt users
    $ brew install pipenv         # for mac users

Generate your python project (you will be asked for the project name etc)::

    $ cookiecutter https://github.com/romnn/cookiecutter-pypackage.git

After your project was created:

* Create a remote repository and publish your package::

    $ cd <mypackage>
    $ git remote add origin git@github.com:myusername/mypackage.git
    $ git add .
    $ git commit -m "Initial commit"
    $ git push --set-upstream origin master

* Activate the project's virtual environment with::

    $ pipenv shell

  When your environment is active, you should see the name of your package in your command prompt.

  If you receive an error ``Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.``,
  it is likely that you are inside another shell that has been started sometime ago.
  Run ``exit`` and try again.

  .. warning:: When you are done working on this project, run ``deactivate`` to deactivate the environment.

* Get a deployment token for your package on PyPI_ under ``Manage > Settings > Create token``.
  It is good practice to use your package name as the token description and restrict access to only this package.
  Make sure to copy to copy the token as we will use it in the next steps.

* Add the token you copied in the previous step as a GitHub secret with the name `PYPI_API_TOKEN` to that the action workflow can access it.

* Start coding! Add your package dependencies to your ``setup.py`` and ``Pipfile`` as you go,
  and lock them into your virtual environment with::

  $ pipenv install --dev

* Release new versions of your package by pushing a new tag to master::

    $ bump2version (major | minor | patch)
    $ git push --tags

.. _PyPI: https://pypi.org
