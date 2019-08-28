import invoke

from .git import get_latest_tag


@invoke.task(help={"slug": "prefix for the new note", "edit": "open in `$EDITOR`"})
def new(ctx, slug, edit=False):
    """ Create new release note. """
    cmd = f"reno new '{slug}'"
    if edit:
        cmd += " --edit"
    ctx.run(cmd)


@invoke.task
def list_notes(ctx):
    """ Print list of release note files. """
    ctx.run("reno list", hide="stderr")


@invoke.task
def lint(ctx):
    """ Check release notes for RST errors. """
    ctx.run("reno lint", hide="stderr")


@invoke.task(
    iterable=["version"],
    help={
        "version": "limit output to this version (can be given multiple times)", "title": "header for the notes", "latest": "show latest version"},
)
def preview(ctx, title=None, version=None, latest=False):
    """ Print preview of change log. """
    title = title or ctx.config.notes.title
    version = version or []
    if latest:
        version.append(get_latest_tag(ctx))
    cmd = f"reno report --title='{title}'"
    for v in version:
        cmd += f" --version {v}"
    ctx.run(cmd, hide="stderr")


@invoke.task(
    iterable=["version"],
    help={"version": "limit output to this version (can be given multiple times)"},
    pre=[lint],
)
def write(ctx, title=None, output=None, version=None):
    """ Write change log to file. """
    title = title or ctx.config.notes.title
    output = output or ctx.config.notes.changelog_file
    version = version or []
    cmd = f"reno report --title='{title}' --output='{output}' --no-show-source"
    for v in version:
        cmd += f" --version {v}"
    ctx.run(cmd, hide="stderr")


ns_notes = invoke.Collection("notes")

ns_notes.add_task(list_notes, "list", default=True)
ns_notes.add_task(new)
ns_notes.add_task(lint)
ns_notes.add_task(preview)
ns_notes.add_task(write)
