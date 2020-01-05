.. highlight:: console

===============================
Cookiecutter PyPackage (romnnn)
===============================

.. image:: https://travis-ci.org/romnnn/cookiecutter-pypackage.svg?branch=master
    :target: https://travis-ci.com/romnnn/cookiecutter-pypackage
    :alt: Build status
.. image:: https://readthedocs.org/projects/romnnn-cookiecutter-pypackage/badge/?version=latest
    :target: https://romnnn-cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Opinionated ``cookiecutter`` template for python packages, forked from `briggySmalls/cookiecutter-pypackage`_.

The key features of this template include:

* Dependency tracking using ``pipenv``
* Linting using ``flake8``
* Formatting provided by ``black`` and ``isort``
* Automatic documentation from Google style docstrings with ``sphinx``
* All development tasks (``lint``, ``format``, ``test``, etc) wrapped up in a cli by ``invoke``
* Automatic deployment to PyPI_
* Automatic publishing of your documentation to `GitHub Pages`_


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
* AppVeyor_ continuous integration. Only Travis-CI_ is used.

.. _AppVeyor: https://www.appveyor.com/

The following features have been **changed**:

* ``yapf`` was replaced by ``black`` for formatting python code
* ``alabaster`` was replaced by ``press`` as the default documentation theme

The following features have been **added**:

* ``pre-commit`` hooks that are automatically installed and run before every commit
* Aggressive type-checking using ``mypy``
* good test coverage is a requirement
* Automatic initialization of a ``git`` repository post generation
* Automatic installation of development dependencies post generation
* Automatic deployment to `GitHub Pages`_ of the documentation.

Quickstart
----------

Install ``cookiecutter>=1.4.0`` if you haven't already::

    $ pip install -U cookiecutter

Generate your python project (you will be asked for the project name etc)::

    $ cookiecutter https://github.com/romnnn/cookiecutter-pypackage.git

After your project was created:

* Create a remote repository and publish your package::

    $ cd <mypackage>
    $ git remote add origin git@github.com:myusername/mypackage.git
    $ git add .
    $ git commit -m "Initial commit"
    $ git push origin master

* Activate the project's virtual environment with::

    $ pipenv shell

  When your environment is active, you should see the name of your package in your command prompt.

  If you receive an error ``Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.``,
  it is likely that you are inside another shell that has been started sometime ago.
  Run ``exit`` and try again.

  .. warning:: When you are done working on this project, run ``deactivate`` to deactivate the environment.



* Make an initial release of your package to PyPI_. You will be asked for your credentials::

    $ pip install twine
    $ python setup.py sdist
    $ twine upload dist/*

* Get a deployment token for your package on PyPI_ under ``Manage > Settings > Create token``.
  It is good practice to use your package name as the token description and restrict access to only this package.\
  Make sure to copy to copy the token as we will use it in the next steps.
* Add the repo to your `Travis-CI`_ account. If you have connected travis with GitHub this is done automatically.
* `Install the Travis CLI`_ and run::

    $ travis encrypt <your-token> --add deploy.password         # When using travis.org
    $ travis encrypt <your-token> --add deploy.password --com   # When using travis.com

  to automatically encrypt your PyPI token into your ``.travis.yml`` config.

  Unfortunately, the travis cli tool appends the token outside of any build stage,
  so you need to manually edit the ``.travis.yml`` config or run::

    $ invoke fix-token

  Now you can push the new ``.travis.yml`` to your remote repository::

    $ git add .travis.yml
    $ git commit -m "Add PyPI deployment token"
    $ git push

* Add the repo to your ReadTheDocs_ account under ``My Projects > Import Project`` and enable the service hook
  if you did not connect ReadTheDocs to your GitHub.
* If you wish to also publish your documentation on `GitHub Pages`_,
  `generate a GitHub access token <https://github.com/settings/tokens>`_ for `repo:public_repo` and set this
  token in your travis build settings at `<https://travis-ci.com/myusername/mypackage/settings>`_
  as a secret environment variable ``GH_TOKEN``.

  If you do not want to deploy to `GitHub Pages`_, remove the ``deploy pages`` build stage from ``.travis.yml``.

* Start coding! Add your package dependencies to your ``setup.py`` and ``Pipfile`` as you go,
  and lock them into your virtual environment with::

  $ pipenv install --dev

* Release new versions of your package by pushing a new tag to master::

    $ bump2version (major | minor | patch)
    $ git push
    $ git push --tags

.. _Travis-CI: https://travis-ci.com
.. _PyPI: https://pypi.org
.. _Install the Travis CLI: https://github.com/travis-ci/travis.rb#installation
.. _ReadTheDocs: https://readthedocs.org/
.. _GitHub Pages: https://pages.github.com/

Documentation
-------------

If you need more guidance I encourage you to have a look at the `more extensive documentation`_.

.. _`more extensive documentation`: https://romnnn-cookiecutter-pypackage.readthedocs.io/en/latest/
