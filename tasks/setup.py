import invoke
from cookiecutter.main import cookiecutter


@invoke.task
def setup_version(ctx, force=False):
    """ Create `.bumpversion.cfg` in current directory. """
    force = force or ctx.config.get("force", False)
    config_file = ctx.config.version.config_file
    if config_file.exists() and not force:
        print(f"'{config_file}' already exists, use `--force` to override")
    else:
        print(f"creating '{config_file}'")
        cookiecutter(
            "bumpversion",
            no_input=True,
            overwrite_if_exists=True,
            output_dir=ctx.config.paths.cwd,
        )


@invoke.task
def setup_notes(ctx, force=False):
    """ Create `releasenotes` tree in current directory. """
    force = force or ctx.config.get("force", False)
    config_file = ctx.config.notes.config_file
    if config_file.exists() and not force:
        print(f"'{config_file}' already exists, use `--force` to override")
    else:
        print(f"creating '{config_file}'")
        cookiecutter(
            "reno",
            no_input=True,
            overwrite_if_exists=True,
            output_dir=ctx.config.paths.cwd,
        )


@invoke.task
def setup_pre_commit(ctx, force=False, init=True):
    """ Create `.pre-commit-config.yaml` in current directory.

    If *init* is set, run ``.

    """
    force = force or ctx.config.get("force", False)
    config_file = ctx.config.pre_commit.config_file
    if config_file.exists() and not force:
        print(f"'{config_file}' already exists, use `--force` to override")
    else:
        print(f"creating '{config_file}'")
        cookiecutter(
            "pre-commit",
            no_input=True,
            overwrite_if_exists=True,
            output_dir=ctx.config.paths.cwd,
        )
    if init:
        ctx.run("pre-commit install --overwrite --install-hooks")


@invoke.task(post=[setup_version, setup_notes, setup_pre_commit])
def setup_all(ctx, force=False):
    """ Setup version & release notes management. """
    if force:
        ctx.config.force = True


ns_setup = invoke.Collection("setup")
ns_setup.add_task(setup_all, "all", default=True)
ns_setup.add_task(setup_version, "version")
ns_setup.add_task(setup_notes, "notes")
ns_setup.add_task(setup_pre_commit, "pre-commit")
