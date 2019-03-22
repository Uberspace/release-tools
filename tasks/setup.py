import invoke

from cookiecutter.main import cookiecutter


@invoke.task
def setup_version(ctx, force=False):
    """ Create `.bumpversion.cfg` in current directory. """
    force = force or ctx.get("force", False)
    config_file = ctx.version.config_file
    if config_file.exists() and not force:
        print(f"'{config_file}' already exists, use `--force` to override")
    else:
        print(f"creating '{config_file}'")
        cookiecutter(
            "bumpversion", no_input=True, overwrite_if_exists=True,
            output_dir=ctx.paths.cwd
        )


@invoke.task
def setup_notes(ctx, force=False):
    """ Create `releasenotes` tree in current directory. """
    force = force or ctx.get("force", False)
    config_file = ctx.notes.config_file
    if config_file.exists() and not force:
        print(f"'{config_file}' already exists, use `--force` to override")
    else:
        print(f"creating '{config_file}'")
        cookiecutter(
            "reno", no_input=True, overwrite_if_exists=True,
            output_dir=ctx.paths.cwd
        )


@invoke.task(post=[setup_version, setup_notes])
def setup_all(ctx, force=False):
    """ Setup version & release notes management. """
    if force:
        ctx.force = True


ns_setup = invoke.Collection("setup")
ns_setup.add_task(setup_all, "all", default=True)
ns_setup.add_task(setup_version, "version")
ns_setup.add_task(setup_notes, "notes")
