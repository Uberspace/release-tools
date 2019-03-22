import invoke


@invoke.task(help={"ids": "one or more identifiers, seperated by `,`"})
def ignore(ctx, ids="python,visualstudiocode"):
    """ Print `.gitignore` for `--ids`. """
    cmd = f"git ignore '{ids}'"
    ctx.run(cmd)


ns_git = invoke.Collection("git")

ns_git.add_task(ignore, default=True)
