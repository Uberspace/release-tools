# Release Tools

**VERSION**: `0.5.1`

This is a [Python Docker Image][], that comes with `git` and some other tools
installed, that can help with release related tasks:

-   [black]
-   [bumpversion]
-   [cookie-cutter]
-   [invoke]
-   [pip-tools]
-   [pre-commit]
-   [reno]
-   [safety]
-   [pip-tools]

It's available on [Docker Hub][] as `uberspace/release-tools`.

## 🚸 Usage

The default is to run as the _user_ `root` from `/usr/local/src/` as _working
directory_. The _entry point_ is set to `/usr/local/bin/invoke`. You can use
`--workdir /foo`, `--user $(id -u):$(id -g)` and the `--entrypoint` flag to
change that.

### Alias

As a shortcut, you can create the following _alias_ for running this image:

```shell
alias dkr-release="docker run --rm \
    --volume "$(pwd)":/usr/local/src \
    --user "$(id -u):$(id -g)" \
    uberspace/release-tools"
```

### Tools

The tools contained in this image can be used directly, by setting them as
_entry points_:

```shell
docker run --rm --entrypoint black uberspace/release-tools --help
```

### Tasks

If you run this image (e.g. with the alias above), it presents you a list of
[Invoke] tasks:

    release           Write CHANGELOG and BUMP version.
    git
        .ignore       Print `.gitignore` for `--ids`.
        .list*        Print list of available IDs.
    notes
        .lint         Check release notes for RST errors.
        .list*        Print list of release note files.
        .new          Create new release note.
        .preview      Print preview of change log.
        .write        Write change log to file.
    package
        .audit*       Print compromised packages from `requirements.txt`.
        .update       Creates new `*.txt` files from `*.in` files.
    setup
        .all*         Setup version & release notes management.
        .notes        Create `releasenotes` tree in current directory.
        .pre-commit   Create `.pre-commit-config.yaml` in current directory.
        .version      Create `.bumpversion.cfg` in current directory.
    version
        .bump         Bump version based on `--part`.
        .current*     Print current version.
        .next         Print next version based on `--part`.

The _command arguments_ given to `docker run …` are passed to `invoke` - e.g. to
lint your release notes, you can run `dkr-release notes.lint`.

### Workflow

1. **Setup**: run `dkr-release setup` once, to create the necessary file
   structure (you generally run this from the root of your repo).

2. **Add Notes**: If you are ready commit changes, you can use
   `dkr-release notes.new`, to create a new release notes file, to edit and add
   to your commit.

3. **Release** You create an up to date _CHANGELOG_ and bump the version by
   running `dkr-release release`.

    By default this bumps the _patch_ number, but you can bump the _minor_ or
    _major_ number (or everything else you have configured) by passing it along
    via the `--part` flag, e.g. `dkr-release release --part minor`.

## 🔖 Release

If you're ready to release a new version, please…

1. ensure a clean repo (everything merged, release notes ready…),

2. run the `release` task, to create the _CHANGELOG_, _bump the version_
   and tag the commit that bumped the version:

    ```shell
    docker run --rm \
        --volume "$(pwd)":/usr/local/src \
        --user "$(id -u):$(id -g)" \
        uberspace/release-tools release
    ```

3. and run `git push` and `git push --tags`.

## 🚀 Deployment

Pushes to _master_ trigger builds on [Docker Hub][].

Change `requirements.in` to control the installed software (and versions) and
create a new `requirements.txt` by running `pip-compile [--upgrade]`.

To change the Docker tag used for the [Python base image], set the
`PYTHON_VERSION` environment variable (default: `3-slim`).

[black]: https://github.com/psf/black
[bumpversion]: https://github.com/c4urself/bump2version
[cookie-cutter]: https://pypi.org/project/cookiecutter/
[docker hub]: https://hub.docker.com/r/uberspace/release-tools
[invoke]: https://pypi.org/project/invoke/
[pip-tools]: https://github.com/jazzband/pip-tools
[pre-commit]: https://pre-commit.com/
[python base image]: https://hub.docker.com/_/python
[python docker image]: https://hub.docker.com/_/python
[reno]: https://pypi.org/project/reno/
[safety]: https://pypi.org/project/safety/
