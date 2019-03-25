# Release Tools

**VERSION**: `0.1.1`

This is a [Python Docker Image][], that comes with `git` and some other tools
installed, that can help with release related tasks:

- [bumpversion]
- [cookiecutter]
- [invoke]
- [reno]
- [safety]

## :children_crossing: Usage

The default is to run as the _user_ `root` from `/usr/local/src/` as _working
directory_. The _entry point_ is set to `/usr/local/bin/invoke`. You can use
`--workdir /foo`, `--user $(id -u):$(id -g)` and the `--entrypoint` flag to
change that.

### Tasks

If you run this image, it presents you a list of [Invoke] tasks:

```
  release                     Write CHANGELOG and BUMP version.
  audit.all (audit)           Print compromised packages.
  audit.packages              Print compromised installed packages.
  audit.requirements          Print compromised packages in req-file.
  git.ignore (git)            Print `.gitignore` for `--ids`.
  notes.list (notes)          Print list of release note files.
  notes.new                   Create new release note.
  notes.preview               Print preview of change log.
  notes.write                 Write change log to file.
  setup.all (setup)           Setup version & release notes management.
  setup.notes                 Create `releasenotes` tree in current directory.
  setup.version               Create `.bumpversion.cfg` in current directory.
  version.bump                Bump version based on `--part`.
  version.current (version)   Print current version.
  version.next                Print next version based on `--part`.
```

The _command arguments_ given to `docker run …` are passed to `invoke`.

### Tools

You can use the installed tools directly, by setting them as _entry points_:

```shell
docker run --rm --entrypoint reno release-tools --help
```

## :bookmark: Release

If you're ready to release a new version, please…

1.  ensure a clean repo (everything merged, release notes ready…),

2.  run the `release` task, to create the _CHANGELOG_, _bump the version_
    and tag the commits:

	```shell
	docker run --rm \
		-v "$(pwd)":/usr/local/src \
		--user "--user $(id -u):$(id -g)" \
		release-tools release
	```

3.  and run `git push` and `git push --tags`.

## :rocket: Deployment

The _Gitlab CI_ builds new images from pushes to the _master_ branch.

Change `requirements.txt` to control the installed software (and versions) and
set the `PYTHON_VERSION` environment variable (in the settings for the _CI_) to
set the Docker tag used for the Python base image.

**NOTE** We use `3` as default tag for now (instead of `3-alpine`), because the
_dulwich_ compilation bails on _Alpine_.

[bumpversion]: https://github.com/c4urself/bump2version
[cookiecutter]: https://pypi.org/project/cookiecutter/
[invoke]: https://pypi.org/project/invoke/
[python docker image]: https://hub.docker.com/_/python
[reno]: https://pypi.org/project/reno/
[safety]: https://pypi.org/project/safety/
