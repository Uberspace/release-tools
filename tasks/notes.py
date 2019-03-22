import invoke


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
    cmd = f"reno list"
    ctx.run(cmd)


@invoke.task(
    iterable=["version"],
    help={"version": "limit output to this version (can be given multiple times)"},
)
def preview(ctx, title=None, version=None):
    """ Print preview of change log. """
    title = title or ctx.notes.title
    version = version or []
    cmd = f"reno report --title='{title}'"
    for v in version:
        cmd += f" --version {v}"
    ctx.run(cmd)


@invoke.task(
    iterable=["version"],
    help={"version": "limit output to this version (can be given multiple times)"},
)
def write(ctx, title=None, output=None, version=None):
    """ Write change log to file. """
    title = title or ctx.notes.title
    output = output or ctx.notes.output
    version = version or []
    cmd = f"reno report --title='{title}' --output='{output}' --no-show-source"
    for v in version:
        cmd += f" --version {v}"
    ctx.run(cmd)


ns_notes = invoke.Collection("notes")

ns_notes.add_task(list_notes, "list", default=True)
ns_notes.add_task(new)
ns_notes.add_task(preview)
ns_notes.add_task(write)
