import pathlib

import invoke


@invoke.task(iterable=["file"], help={"file": "check this requirement file"})
def requirements(ctx, file=None):
    """ Print compromised packages from `requirements.txt`.

    Scans given *file* (can be given multiple times), uses `requirements.txt` as
    default. Doesn't follow `-r …` lines.

    """
    args = ctx.config.audit.args
    files = file or ctx.config.audit.files

    for f in (pathlib.Path(f).resolve() for f in files):
        if f.exists:
            args.extend(["--file", f"'{f}'"])
        else:
            msg = f"[ERROR] no requirements file found at '{f}'"
            invoke.exceptions.Exit(msg, 2)

    args = " ".join(args)
    ctx.run(f"safety check {args}")


ns_audit = invoke.Collection("audit")

ns_audit.add_task(requirements, default=True)
