# Release Tools

**VERSION**: `0.3.0`

This is a [Python Docker Image][], that comes with `git` and some other tools
installed, that can help with release related tasks:

-   [bumpversion]
-   [cookie-cutter]
-   [invoke]
-   [reno]
-   [safety]

## 🚸 Usage

The default is to run as the _user_ `root` from `/usr/local/src/` as _working
directory_. The _entry point_ is set to `/usr/local/bin/invoke`. You can use
`--workdir /foo`, `--user $(id -u):$(id -g)` and the `--entrypoint` flag to
change that.

### Alias

You can create the following _alias_ for running this image:

```shell
alias dkr-release="docker run --rm \
    --volume "$(pwd)":/usr/local/src \
    --user "$(id -u):$(id -g)" \
    release-tools"
```

### Tools

You can use the installed tools directly, by setting them as _entry points_:

```shell
docker run --rm --entrypoint reno release-tools --help
```

### Tasks

If you run this image (e.g. with the alias above), it presents you a list of
[Invoke] tasks:

    release                      Write CHANGELOG and BUMP version.
    audit.requirements (audit)   Print compromised packages in req-file.
    git.ignore (git)             Print `.gitignore` for `--ids`.
    git.list                     Print list of available IDs.
    notes.lint                   Check release notes for RST errors.
    notes.list (notes)           Print list of release note files.
    notes.new                    Create new release note.
    notes.preview                Print preview of change log.
    notes.write                  Write change log to file.
    setup.all (setup)            Setup version & release notes management.
    setup.notes                  Create `releasenotes` tree in current directory.
    setup.version                Create `.bumpversion.cfg` in current directory.
    version.bump                 Bump version based on `--part`.
    version.current (version)    Print current version.
    version.next                 Print next version based on `--part`.

The _command arguments_ given to `docker run …` are passed to `invoke` - e.g. to
run lint your release notes, you can run `dkr-release notes.lint`.

### Workflow

1. **Setup**: run `dkr-release setup` once, to create the necessary file
   structure (you generally run this from the root of your repo).

2. **Add Notes**: If you are ready commit changes, you can use
   `dkr-release notes.new`, to create a new release notes file, to edit and add
   to your commit.

3. **Release** You create an up to date _CHANGELOG_ and bump the version by
   running `dkr-release release`. By default this bumps the _patch_ number, but
   you can bump the _minor_ or _major_ number (or everything else you have
   configured) by passing it along via the `--part` flag, e.g.
   `dkr-release release --part minor`.

## 🔖 Release

If you're ready to release a new version, please…

1. ensure a clean repo (everything merged, release notes ready…),

2. run the `release` task, to create the _CHANGELOG_, _bump the version_
   and tag the commits:

    ```shell
    docker run --rm \
        --volume "$(pwd)":/usr/local/src \
        --user "$(id -u):$(id -g)" \
        release-tools release
    ```

3. and run `git push` and `git push --tags`.

## 🚀 Deployment

The _Gitlab CI_ builds new images from pushes to the _master_ branch.

Change `requirements.txt` to control the installed software (and versions) and
set the `PYTHON_VERSION` environment variable (in the settings for the _CI_) to
set the Docker tag used for the Python base image.

**NOTE** We use `3` as default tag for now (instead of `3-alpine`), because the
_dulwich_ compilation bails on _Alpine_.

[bumpversion]: https://github.com/c4urself/bump2version
[cookie-cutter]: https://pypi.org/project/cookiecutter/
[invoke]: https://pypi.org/project/invoke/
[python docker image]: https://hub.docker.com/_/python
[reno]: https://pypi.org/project/reno/
[safety]: https://pypi.org/project/safety/
