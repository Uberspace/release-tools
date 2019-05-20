import pathlib

import invoke


@invoke.task
def requirements(ctx, req_file=None):
    """ Print compromised packages in req-file. """
    req_file = pathlib.Path(req_file or ctx.audit.req_file).resolve()
    if req_file.exists:
        cmd = f"safety check --bare --file='{req_file}'"
        ctx.run(cmd)
    else:
        print(f"[ERROR] no file found at '{req_file}'")


ns_audit = invoke.Collection("audit")

ns_audit.add_task(requirements, default=True)
