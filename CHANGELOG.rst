=========
CHANGELOG
=========

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

We reach *MVP* state 🎉 - still a new *reno* release would be nice.

.. _CHANGELOG_v0.2.0_Added Features:

Added Features
--------------

- 👷 🐳 Add ``.gitlab-ci.yaml`` to build the Docker image from *master*.


.. _CHANGELOG_v0.2.0_Fixes:

Fixes
-----

- ✏️ fixed some typos in the release notes for ``0.1.0``.


.. _CHANGELOG_v0.2.0_Known Issues:

Known Issues
------------

- 📌 Use a *reno* version that comes with a *dulwich* version that fixes the *git-submodule* issue (probably ``0.19.12``).


.. _CHANGELOG_v0.1.1:

v0.1.1
======

.. _CHANGELOG_v0.1.1_Updates:

Updates
-------

- ⬆️ install *dulwich* from *master zipball*, to include PR for *git-submodule* fix.


.. _CHANGELOG_v0.1.1_Fixes:

Fixes
-----

- ✏️ fixed some typos in the release notes for ``0.1.0``.


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

