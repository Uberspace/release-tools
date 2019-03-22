import pathlib

import invoke


@invoke.task
def requirements(ctx, req_file=None):
    """ Print compromised packages in req-file. """
    req_file = req_file or ctx.audit.req_file
    cmd = f"safety check --bare --file='{req_file}'"
    ctx.run(cmd)


@invoke.task
def packages(ctx):
    """ Print compromised installed packages. """
    cmd = f"safety check --bare"
    ctx.run(cmd)


@invoke.task
def all(ctx, req_file=None):
    """ Print compromised packages. """
    req_file = req_file or ctx.audit.req_file
    if pathlib.Path(req_file).exists:
        requirements(ctx, req_file)
    packages(ctx)


ns_audit = invoke.Collection("audit")

ns_audit.add_task(all, default=True)
ns_audit.add_task(packages)
ns_audit.add_task(requirements)
