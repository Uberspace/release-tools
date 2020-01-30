import pathlib

import invoke

from . import git
from . import notes
from . import package
from . import setup
from . import version


@invoke.task(help={"part": "version part to bump (e.g. 'major', 'minor' or 'patch')"})
def release(ctx, part=None, commit=None):
    """ Write CHANGELOG and BUMP version. """
    if commit is None:
        commit_notes = ctx.config.notes.commit
        commit_version = ctx.config.version.commit
    else:
        commit_notes = commit
        commit_version = commit

    # lint notes
    notes.lint(ctx)

    # get version info
    ctx.config.current_version = version.get_current(ctx)
    ctx.config.new_version = version.get_next(ctx, part)
    ctx.config.tag = ctx.config.git.tag_name.format(**ctx.config)

    # write change log
    try:
        ctx.run(f"git tag '{ctx.config.tag}'")
        notes.write(ctx)
    finally:
        ctx.run(f"git tag -d '{ctx.config.tag}'")

    # commit change log
    if commit_notes:
        msg = ctx.config.git.message.notes.format(**ctx.config)
        ctx.run(f"git add '{ctx.config.notes.changelog_file}'")
        ctx.run(f"git commit --no-verify -m '{msg}'")

    # bump version
    version.bump(ctx, part)

    # commit version bump
    if commit_version:
        msg = ctx.config.git.message.version.format(**ctx.config)
        ctx.run(f"git add -u")
        ctx.run(f"git commit --no-verify -m '{msg}'")

    # tag
    ctx.run(f"git tag '{ctx.config.tag}'")


ns = invoke.Collection()

ns.add_collection(git.ns_git)
ns.add_collection(notes.ns_notes)
ns.add_collection(package.ns_package)
ns.add_collection(setup.ns_setup)
ns.add_collection(version.ns_version)

ns.add_task(release)

# fmt: off
ns.configure(
    {
        "paths": {
            "base": pathlib.Path(__file__).parent,
            "cwd": pathlib.Path.cwd(),
        },
        "package": {
            "files": {
                "src": [
                    "requirements.in",
                ],
                "dst": [
                    "requirements.txt",
                ],
            },
            "args": {
                "audit": ["--bare"],
                "update": ["--annotate", "--generate-hashes"],
            },
        },
        "git": {
            "tag_name": "v{new_version}",
            "message": {
                "notes": ":memo: update CHANGELOG for {new_version} #0",
                "version": ":bookmark: set version {current_version} → {new_version} #0",
            },
        },
        "notes": {
            "changelog_file": "CHANGELOG.rst",
            "commit": True,
            "config_file": pathlib.Path.cwd() / "releasenotes" / "config.yaml",
            "title": "CHANGELOG",
        },
        "version": {
            "args": ["--no-commit", "--no-tag", "--list"],
            "commit": True,
            "config_file": pathlib.Path.cwd() / ".bumpversion.cfg",
            "default_part": "patch",
            "parts": ("major", "minor", "patch"),
        },
        "pre_commit": {
            "config_file": pathlib.Path.cwd() / ".pre-commit-config.yaml"
        },
        "run": {"echo": True},
    }
)
# fmt: on
