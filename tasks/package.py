import pathlib

import invoke


@invoke.task(iterable=["file"], help={"file": "check this requirement file"})
def audit(ctx, file=None):
    """ Print compromised packages from `requirements.txt`.

    Scans given *file* (can be given multiple times), uses `requirements.txt` as
    default. Doesn't follow `-r …` lines.

    """
    args = ctx.config.package.args.get("audit", [])
    files = file or ctx.config.package.files.dst

    for f in (pathlib.Path(f).resolve() for f in files):
        f = f.relative_to(ctx.paths.cwd)
        if f.exists:
            args.extend(["--file", f"'{f}'"])
        else:
            msg = f"[ERROR] no requirements file found at '{f}'"
            invoke.exceptions.Exit(msg, 2)

    args = " ".join(args)
    ctx.run(f"safety check {args}")


@invoke.task(iterable=["file"], help={"file": "check this requirement file"})
def update(ctx, file=None, upgrade=False):
    """ Creates new `*.txt` files from `*.in` files.

    Scans given *file* (can be given multiple times), uses `requirements.txt` as
    default.

    """
    args = ctx.config.package.args.get("update", [])
    if upgrade:
        args.append("--upgrade")
    files = file or ctx.config.package.files.src

    for f in (pathlib.Path(f).resolve() for f in files):
        f = f.relative_to(ctx.paths.cwd)
        if f.exists:
            args.append(f"'{f}'")
        else:
            msg = f"[ERROR] no requirements file found at '{f}'"
            invoke.exceptions.Exit(msg, 2)

    args = " ".join(args)
    ctx.run(f"pip-compile {args}")


ns_package = invoke.Collection("package")

ns_package.add_task(audit, default=True)
ns_package.add_task(update)
