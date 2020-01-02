.. highlight:: console

Version Management
==================

.. _`bump-version-tutorial`:

Whenever you made changes to your package and you want to release a new version to PyPI and GitHub,
you need to change all version strings in the project and make a tagged commit.

To make life easier, we use bump2version_ for this.
This is how releasing a new version looks like::

    $ bump2version (major | minor | patch)
    $ git push
    $ git push --tags

Examples
--------

Let's assume the current version is ``1.3.2``.

======================= ============
Command                 New version
======================= ============
``bump2version major``  ``2.3.2``
``bump2version minor``  ``1.4.2``
``bump2version patch``  ``1.3.3``
======================= ============

.. _bump2version: https://github.com/c4urself/bump2version
