import invoke


def get_latest_tag(ctx, annotated=False):
    """ Return latest tag. """
    cmd = "git describe --tags"
    if annotated:
        cmd += " --abbrev=0"
    res = ctx.run(cmd)
    tag = res.stdout.strip()
    if annotated:
        return tag
    else:
        return tag.rsplit("-", 1)[0]


@invoke.task(help={"ids": "one or more identifiers, seperated by `,`"})
def ignore(ctx, ids="python,visualstudiocode"):
    """ Print `.gitignore` for `--ids`. """
    cmd = f"git ignore '{ids}'"
    ctx.run(cmd)


@invoke.task
def list_available(ctx):
    """ Print list of available IDs. """
    cmd = f"git ignore list"
    ctx.run(cmd)


ns_git = invoke.Collection("git")

ns_git.add_task(ignore)
ns_git.add_task(list_available, "list", default=True)
