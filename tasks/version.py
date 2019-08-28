import configparser

import invoke


def get_config_file(ctx, cfg_file=None):
    """ Return config file or raise error if missing. """
    cfg_file = cfg_file or ctx.config.version.config_file
    if not cfg_file.exists():
        msg = "bumpversion configuration not found at '{cfg_file}'"
        invoke.exceptions.Exit(msg, 2)
    return cfg_file


def get_config(ctx, cfg_file=None):
    """ Return configuration dictionary from *cfg_file*. """
    cfg_file = get_config_file(ctx, cfg_file)
    c = configparser.ConfigParser()
    c.read(cfg_file)
    return c


def get_part(ctx, part):
    """ Return part or Raise error. """
    if part is None:
        part = ctx.config.version.default_part

    parts = ctx.config.version.parts
    if part not in parts:
        msg = f"part needs to be one of these: {', '.join(parts)} - not '{part}'"
        raise invoke.exceptions.Exit(msg, 2)

    if not part:
        msg = "no part given and no default set"
        raise invoke.exceptions.Exit(msg, 2)

    return part


def get_current(ctx):
    """ Return current version. """
    c = get_config(ctx)
    try:
        return c["bumpversion"]["current_version"]
    except KeyError:
        msg = "[ERROR] no current version found"
        raise invoke.exceptions.Exit(msg, 2)


def get_next(ctx, part=None):
    """ Return next version when incrementing *part*. """
    get_config_file(ctx)
    part = get_part(ctx, part)
    args = " ".join(ctx.config.version.args)
    cmd = f"bumpversion {args} --dry-run --allow-dirty {part}"
    res = ctx.run(cmd, echo=False, hide="both")
    for line in res.stdout.split("\n"):
        if line.startswith("new_version="):
            return line.split("=")[1].strip()
    msg = "[ERROR] no next version found"
    raise invoke.exceptions.Exit(msg, 2)


@invoke.task
def show_current(ctx):
    """ Print current version. """
    version = get_current(ctx)
    print(version)


@invoke.task(help={"part": "version part to bump ('major', 'minor' or 'patch')"})
def show_next(ctx, part=None):
    """ Print next version based on `--part`. """
    version = get_next(ctx, part)
    print(version)


@invoke.task(help={"part": "version part to bump ('major', 'minor' or 'patch')"})
def bump(ctx, part=None):
    """ Bump version based on `--part`. """
    get_config_file(ctx)
    part = get_part(ctx, part)
    args = " ".join(ctx.config.version.args)
    cmd = f"bumpversion {args} {part}"
    ctx.run(cmd)


ns_version = invoke.Collection("version")

ns_version.add_task(show_current, "current", default=True)
ns_version.add_task(show_next, "next")
ns_version.add_task(bump)
