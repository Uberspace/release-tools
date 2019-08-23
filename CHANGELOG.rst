=========
CHANGELOG
=========

.. _CHANGELOG_v0.4.1:

v0.4.1
======

.. _CHANGELOG_v0.4.1_Summary:

Summary
-------

This image is now on `Docker Hub <https://hub.docker.com/r/uberspace/release-tools>`_ as ``uberspace/release-tools``.


.. _CHANGELOG_v0.4.1_Changes:

Changes
-------

- 📦 Moved the repo on GitHub from ``brutus/release-tools`` to ``uberspace/release-tools``.

- 📦 The internal GitLab version now only mirrors the GitHub repo.


.. _CHANGELOG_v0.4.1_Updates:

Updates
-------

- ⬆️ Updated *reno* to ``2.11.3``.

- ⬆️ Updated *dulwich* to ``0.19.13``.


.. _CHANGELOG_v0.4.1_Fixes:

Fixes
-----

- 🚀 Add workaround for recent GitLab docker services - see this `Issue <https://cdn.knightlab.com/>`_ for more.

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

