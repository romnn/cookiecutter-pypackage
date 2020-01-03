.. highlight:: console

PyPI Release Checklist
======================

.. _`release-checklist`:

Before Your First Release
-------------------------

#. Register the package on PyPI::

    $ python setup.py register

#. Visit PyPI to make sure it registered.

For Every Release
-----------------

#. Run the tests to make sure everything works::

    $ invoke pre-commit
    $ tox

#. Commit your changes
#. Update version number (see :ref:`here <bump-version-tutorial>` for more details)::

    $ bump2version (major | minor | patch)

#. Push the commit and tags. This will create a new release on both GitHub and PyPI::

    $ git push
    $ git push --tags

#. Check the package on PyPI and make sure that the ``README.rst`` is displayed properly.
   If not, try one of these:

   * Copy and paste the RestructuredText into http://rst.ninjs.org/ to find out what broke the formatting.

   * Check your long_description locally::

        $ pip install readme_renderer
        $ python setup.py check -r -s

#. Edit the release on GitHub at `<https://github.com/myusername/mypackage/releases>`_.
   Paste the release notes into the release's release page, and come up with a title for the release.

About this checklist
--------------------

This checklist is adapted from:

* https://gist.github.com/audreyr/5990987
* https://gist.github.com/audreyr/9f1564ea049c14f682f4
