=========
CHANGELOG
=========

.. _CHANGELOG_v0.6.0:

v0.6.0
======

.. _CHANGELOG_v0.6.0_Summary:

Summary
-------

A small cleanup release.

.. _CHANGELOG_v0.6.0_Added Features:

Added Features
--------------

- ➕ Added ``pip-tools`` to the requirements for the image.

- ✨ Added ``package.update`` task, to create ``requirements.txt`` form ``requirements.in`` files.


.. _CHANGELOG_v0.6.0_Changes:

Changes
-------

- 🚚 Renamed ``audit`` task to ``package.audit``.

- ✨ The ``setup.all`` task now also executes the ``setup.pre-commit`` task.

- 🔧 Added ``venv`` to the default set of IDs for the ``git.ignore`` task.

- 🔧 We included ``tests`` in the list of directories given to
   ``--application-directories`` for reordering python imports.

- 🐳 We try to be less noisy in our Docker builds (added ``-qq`` to *apt-get* and ``--quiet`` top *pip*).


.. _CHANGELOG_v0.6.0_Updates:

Updates
-------

- 🙈 Added basic files to ``.gitignore``.


.. _CHANGELOG_v0.6.0_Removed:

Removed
-------

- 🎨 Removed leftover ``requirements-txt-fixer`` hook from default `pre-commit <https://pre-commit.com>`_ configuration. We use ``reorder_python_imports`` instead.


.. _CHANGELOG_v0.6.0_Fixes:

Fixes
-----

- 🐳 We removed the ``apt-get upgrade`` step from our Docker builds (which also is a nice speed increase).


.. _CHANGELOG_v0.5.1:

v0.5.1
======

.. _CHANGELOG_v0.5.1_Added Features:

Added Features
--------------

- 🔧 Add ``pyproject.toml`` section to default *bumpversion* configuration.

- 🔧 Add *Prettier* to default *pre-commit* configuration.

- 🔧 Add *pre-commit-multi* to default *pre-commit* configuration.


.. _CHANGELOG_v0.5.1_Changes:

Changes
-------

- 📦 Dumped `Poetry <https://github.com/sdispater/poetry>`_ for `pip-tools <https://github.com/jazzband/pip-tools>`_.


.. _CHANGELOG_v0.5.1_Fixes:

Fixes
-----

- ➕ Added *curl* back to image (it got droped by switching to ``python:3-slim``).


.. _CHANGELOG_v0.5.0:

v0.5.0
======

.. _CHANGELOG_v0.5.0_Added Features:

Added Features
--------------

- 🔧 You can now configure multiple requirement files for the audit tasks.

- ➕ Added `black <https://github.com/psf/black>`_ to the list of preinstalled tools.

- ✨ Task to setup `pre-commit <https://pre-commit.com/>`_.


.. _CHANGELOG_v0.5.0_Changes:

Changes
-------

- 🚸 Echo commands for invoke tasks.

- 🐳 We use ``python:3-slim`` as base image (was ``python:3``).

- 📦 Replaced `pipenv <https://github.com/pypa/pipenv>`_ with `Poetry <https://github.com/sdispater/poetry>`_ (just to manage ``requirements.txt``).


.. _CHANGELOG_v0.5.0_Updates:

Updates
-------

- ⬆️ Update ``pip`` when creating the image.


.. _CHANGELOG_v0.4.2:

v0.4.2
======

.. _CHANGELOG_v0.4.2_Added Features:

Added Features
--------------

- ✨ Added `pre-commit <https://pre-commit.com/>`_ to list of installed tools.

- 🎨 Added ``--latest`` switch to ``notes.preview`` to only show unreleased release notes.


.. _CHANGELOG_v0.4.2_Changes:

Changes
-------

- 🎨 Made commiting of change log and version bump configurable.

- 🎨 We now list the available task as nested list (if the container is run with no arguments).

- 🎨 We now hide *stderr* output for the ``notes.…`` tasks.


.. _CHANGELOG_v0.4.2_Updates:

Updates
-------

- 📦 Updated requirements.


.. _CHANGELOG_v0.4.1:

v0.4.1
======

.. _CHANGELOG_v0.4.1_Fixes:

Fixes
-----

- 🚀 Add workaround for recent GitLab docker services - see this `Issue <https://cdn.knightlab.com/>`_ for more.


.. _CHANGELOG_v0.4.0:

v0.4.0
======

.. _CHANGELOG_v0.4.0_Summary:

Summary
-------

This image is now on `Docker Hub <https://hub.docker.com/r/uberspace/release-tools>`_ as ``uberspace/release-tools``.


.. _CHANGELOG_v0.4.0_Changes:

Changes
-------

- 📦 Moved the repo on GitHub from ``brutus/release-tools`` to ``uberspace/release-tools``.

- 📦 The internal GitLab version now only mirrors the GitHub repo.


.. _CHANGELOG_v0.4.0_Updates:

Updates
-------

- ⬆️ Updated *reno* to ``2.11.3``.

- ⬆️ Updated *dulwich* to ``0.19.13``.


.. _CHANGELOG_v0.4.0_Fixes:

Fixes
-----

- 📌 Updated *dulwich* to a version, that fixes the *git-submodule* issue.


.. _CHANGELOG_v0.3.1:

v0.3.1
======

.. _CHANGELOG_v0.3.1_Added Features:

Added Features
--------------

- 🔊 Log versions in Gitlab CI.

- 📦 Added *Pipfile* - to update requirements more easily (``pipenv run pip freeze > requirements.txt``).


.. _CHANGELOG_v0.3.1_Updates:

Updates
-------

- ⬆️  Updated required packages.

- 📝 Added a section on workflow to the Readme.


.. _CHANGELOG_v0.3.1_Removed:

Removed
-------

- 🔒 Removed task to audit virtual env.


.. _CHANGELOG_v0.3.0:

v0.3.0
======

.. _CHANGELOG_v0.3.0_Added Features:

Added Features
--------------

- ✨ New task to *lint release notes*.

- ✨ New task to *list IDs* for git ignore files.

- 🔧 Basic ``.editorconfig`` file (4 spaces).


.. _CHANGELOG_v0.3.0_Changes:

Changes
-------

- 🚨 Lint before release.


.. _CHANGELOG_v0.3.0_Fixes:

Fixes
-----

- 🙈 Added `.keep` file to the `releasenotes/notes/` directory of the *Reno* cookie, to prevent `git` from ignoring it.


.. _CHANGELOG_v0.2.0:

v0.2.0
======

.. _CHANGELOG_v0.2.0_Summary:

Summary
-------

We reach *MVP* state 🎉 - still a new *reno* release would be nice (until now there's no ``0.19.12`` version released, so we keep using *master* from now on).

.. _CHANGELOG_v0.2.0_Added Features:

Added Features
--------------

- 👷 🐳 Add ``.gitlab-ci.yaml`` to build the Docker image from *master*.


.. _CHANGELOG_v0.1.1:

v0.1.1
======

.. _CHANGELOG_v0.1.1_Updates:

Updates
-------

- ⬆️ install *dulwich* from *master zipball*, to include PR for *git-submodule* fix.


.. _CHANGELOG_v0.1.1_Known Issues:

Known Issues
------------

- 📌 Use a *reno* version that comes with a *dulwich* version that fixes the *git-submodule* issue (probably ``0.19.12``).


.. _CHANGELOG_v0.1.0:

v0.1.0
======

.. _CHANGELOG_v0.1.0_Summary:

Summary
-------

Initial version 🎉. Added *bumpversion* and *reno* for release management, *cookiecutters* for bootstrapping, *invoke* as task runner / make file and *git* for good measure.

.. _CHANGELOG_v0.1.0_Added Features:

Added Features
--------------

- ✨ Installed package ``git``.

- ✨ Added Python package ``bumpversion`` and example configuration.

- ✨ Added Python package ``reno`` and example configuration.

- ✨ Added Python package ``cookiecutter``, with cookies to setup *bumpversion* and *reno*.

- ✨ Added Python package ``safety``.

- ✨ Added Python package ``invoke`` with tasks for bumping versions, creating release notes, creating git ignore files and auditing Python packages.

