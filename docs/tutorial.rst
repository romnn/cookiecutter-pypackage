Tutorial
========

.. note:: Do you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/romnn/cookiecutter-pypackage/blob/master/docs/tutorial.rst

To start with, you will need a `GitHub account`_ and an account on `PyPI`_. Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


|:cookie:| Step 1: Install Cookiecutter
---------------------------------------

Install ``cookiecutter>=1.4.0``:

.. code-block:: console

    $ pip install cookiecutter>=1.4.0

We'll also need ``pipenv`` so install that too:

.. code-block:: console

    $ pip install pipenv


|:package:| Step 2: Generate Your Package
-----------------------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

.. code-block:: console

    $ cookiecutter https://github.com/romnn/cookiecutter-pypackage.git

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


|:octopus:| Step 3: Create a GitHub Repo
----------------------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter.
This is so that Travis CI can find it when we get to Step 5.

You will find one folder named after the ``[project_slug]``.
Move into this folder, and then setup git to use your GitHub repo and upload the code:

.. code-block:: console

    $ cd mypackage
    $ git init .
    $ git add .
    $ git commit -m "Initial commit."
    $ git remote add origin git@github.com:myusername/mypackage.git
    $ git push -u origin master

Where ``myusername`` and ``mypackage`` are adjusted for your username and package name.

You can use HTTPS to push the repository, but it's more convenient to use a ssh key to push the repo.
You can `Generate`_ a key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

|:hammer_and_wrench:| Step 4: Install development requirements
--------------------------------------------------------------

You should still be in the folder containing the ``Pipfile`` file.

Install the new project's local development requirements inside a virtual environment using ``pipenv``:

.. code-block:: console

    $ pipenv install --dev

|:tada:| Step 5: Initial release to PyPI
----------------------------------------

The Python Package Index or `PyPI`_ is the official third-party software repository for the Python programming language.
Python developers intend it to be a comprehensive catalog of all open source Python packages.

See `PyPI Help`_ for more information about submitting a package.

Before you release, make sure to go through the :ref:`release-checklist`.

.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html

When you are ready, upload your package:

.. code-block:: console

    $ pip install twine
    $ python setup.py sdist
    $ twine upload dist/*  # You will be asked for your PyPI credentials

If everything goes well, your package should be online.

|:construction_worker:| Step 6: Set up TravisCI
-----------------------------------------------

`Travis-CI`_ [*]_ is a continuous integration tool used to prevent integration problems.
Every commit to the master branch will trigger automated builds of the application.

Add the repository to your Travis-CI account by activating it.
If you have connected travis with GitHub this is done automatically.
If you have not yet installed the Travis CLI (Command line interface), follow `the installation guide`_.

Make sure your repository is added and you successfully uploaded your package to PyPI in Step 5.
Now get a deployment token for your package on PyPI. It is advised to restrict the token's access to only this package.

Once you obtained your deployment token, proceed by running:

.. code-block:: console

    $ travis encrypt <your-token> --add deploy.password         # When using travis.org
    $ travis encrypt <your-token> --add deploy.password --com   # When using travis.com

This will:

* Encrypt your deployment token in your ``.travis.yml`` config
* Activate automated deployment on PyPI when you push a new tag to master branch.

Because the token is appended outside of any build stage,
you still need to manually edit the ``.travis.yml`` config or run:

.. code-block:: console

    $ invoke fix-token

.. [*] For private projects go to `travis-ci.com`_, for public ones go to `travis-ci.org`_ has been a thing.
       But afaik all projects should use `travis-ci.com`_ as of now.

.. _`Travis-CI`: https://travis-ci.com/
.. _`travis-ci.org`: https://travis-ci.org/
.. _`travis-ci.com`: https://travis-ci.com/
.. _the installation guide: https://github.com/travis-ci/travis.rb#installation


|:book:| Step 7: Set up ReadTheDocs
-----------------------------------

`ReadTheDocs`_ hosts documentation for the open source community.
Think of it as Continuous Documentation.

Log into your account at `ReadTheDocs`_ . If you don't have one, create one and log into it.

Go to "My Projects" and import the repository.
In your GitHub repo, select ``Settings > Webhooks & Services`` and turn on the ReadTheDocs service hook.
This is done automatically when you connected ReadTheDocs with GitHub.

Now your documentation will get rebuilt when you make changes to your package's documentation.

.. _`ReadTheDocs`: https://readthedocs.org/

|:pencil:| Step 8: Set up GitHub Pages
--------------------------------------

`GitHub Pages`_ is a service offered by GitHub that will host a static website along with your package for free.
Per default, GitHub Pages uses `jekyll <https://jekyllrb.com/>`_ for templating, but you can use any other tool as long as it generated static html (we will be using it with ``Sphinx``).
Once enabled in GitHub's repository settings, it works by hosting any static assets (using ``index.html`` as an entrypoint) in a branch named ``gh-pages``.
When using static html from another tool, GitHub requires a file named ``.nojekyll`` in the branches root so ``jekyll`` won't be used.

If you do not want to deploy to `GitHub Pages`_, remove the ``deploy pages`` build stage from ``.travis.yml``.

If you wish to deploy to GitHub Pages, `generate a GitHub access token <https://github.com/settings/tokens>`_ for `public_repo` and set this token in your travis build settings at `<https://travis-ci.com/myusername/mypackage/settings>`_ as a secret environment variable ``GH_TOKEN``.
This will allow travis to access the secret token as ``$GH_TOKEN`` to be able to commit and push to the ``gh-pages`` branch.
The website will be available at `<https://myusername.github.io/mypackage/>`_.

The default ``deploy pages`` stage in your ``.travis.yml`` will publish your documentation to GitHub Pages (the same as on ReadTheDocs), but you might deploy a different website for your project.


.. _GitHub Pages: https://pages.github.com/

|:rotating_light:| Having problems?
-----------------------------------

Visit our :ref:`troubleshooting` page for help.
If that doesn't help, `create an issue`_.
Be sure to give as much information as possible.

.. _`create an issue`: https://github.com/audreyr/cookiecutter-pypackage/issues
