import pathlib

import invoke

from . import audit
from . import git
from . import notes
from . import setup
from . import version


@invoke.task
def release(ctx, part=None):
    """ Write CHANGELOG and BUMP version. """
    new_version = version.get_next(ctx, part)
    tag = ctx.git.tag.format(version=new_version)
    msg = ctx.git.message.format(tag=tag)

    ctx.run(f"git tag '{tag}'")
    notes.write(ctx)
    ctx.run(f"git tag -d '{tag}'")

    ctx.run(f"git add '{ctx.notes.output}'")
    ctx.run(f"git commit -m '{msg}'")

    version.bump(ctx, part)


ns = invoke.Collection()

ns.configure({
    "paths": {
        "base": pathlib.Path(__file__).parent,
        "cwd": pathlib.Path.cwd(),
    },
    "audit": {
        "req_file": "requirements.txt",
    },
    "git": {
        "tag": "v{version}",
        "message": ":memo: update CHANGELOG for {tag} #0",
    },
    "notes": {
        "config_file": pathlib.Path.cwd() / "releasenotes" / "config.yaml",
        "title": "CHANGELOG",
        "output": "CHANGELOG.rst",
    },
    "version": {
        "config_file": pathlib.Path.cwd() / ".bumpversion.cfg",
        "parts": ("major", "minor", "patch"),
        "default_part": "patch",
    },
})

ns.add_collection(audit.ns_audit)
ns.add_collection(git.ns_git)
ns.add_collection(notes.ns_notes)
ns.add_collection(setup.ns_setup)
ns.add_collection(version.ns_version)

ns.add_task(release)
