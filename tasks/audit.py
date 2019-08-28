import pathlib

import invoke


@invoke.task(help={"bare": "only print vulnarable packages", "req-file": "use this requirement file"})
def requirements(ctx, bare=False, req_file=None):
    """ Print compromised packages in req-file. """
    req_file = pathlib.Path(req_file or ctx.config.audit.req_file).resolve()
    args = ctx.config.audit.args
    if bare:
        args.append('--bare')
    args = " ".join(args)
    if req_file.exists:
        cmd = f"safety check {args} --file='{req_file}'"
        ctx.run(cmd)
    else:
        print(f"[ERROR] no file found at '{req_file}'")


ns_audit = invoke.Collection("audit")

ns_audit.add_task(requirements, default=True)
