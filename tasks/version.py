import configparser

import invoke


def check_cfg_file(ctx):
    """ Raise error on misisng cfg file. """
    cfg_file = ctx.version.config_file
    if not cfg_file.exists():
        msg = "bumpversion configuration not found at '{cfg_file}'"
        invoke.exceptions.Exit(msg, 2)


def check_part(ctx, part):
    """ Return part or Raise error. """
    if part is None:
        part = ctx.version.default_part

    parts = ctx.version.parts
    if part not in parts:
        msg = f"part needs to be one of these: {', '.join(parts)} - not '{part}'"
        raise invoke.exceptions.Exit(msg, 2)

    if not part:
        msg = "no part given and no default set"
        raise invoke.exceptions.Exit(msg, 2)

    return part


def get_current(ctx):
    """ Return current version. """
    check_cfg_file(ctx)
    c = configparser.ConfigParser()
    c.read(ctx.version.config_file)
    try:
        return c["bumpversion"]["current_version"]
    except KeyError:
        msg = "[ERROR] no current version found"
        raise invoke.exceptions.Exit(msg, 2)


def get_next(ctx, part=None):
    """ Return next version when incrementing *part*. """
    check_cfg_file(ctx)
    part = check_part(ctx, part)
    cmd = f"bumpversion --dry-run --list --allow-dirty {part}"
    res = ctx.run(cmd, echo=False, hide="both")
    for line in res.stdout.split("\n"):
        if line.startswith("new_version="):
            return line.split("=")[1].strip()
    msg = "[ERROR] no next version found"
    raise invoke.exceptions.Exit(msg, 2)


@invoke.task
def current(ctx):
    """ Print current version. """
    version = get_current(ctx)
    print(version)


@invoke.task(help={"part": "version part to bump ('major', 'minor' or 'patch')"})
def next(ctx, part=None):
    """ Print next version based on `--part`. """
    version = get_next(ctx, part)
    print(version)


@invoke.task(help={"part": "version part to bump ('major', 'minor' or 'patch')"})
def bump(ctx, part=None):
    """ Bump version based on `--part`. """
    check_cfg_file(ctx)
    part = check_part(ctx, part)
    cmd = f"bumpversion {part} --list"
    ctx.run(cmd)


ns_version = invoke.Collection("version")

ns_version.add_task(current, default=True)
ns_version.add_task(next)
ns_version.add_task(bump)
