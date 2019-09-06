ARG PYTHON_VERSION=3-slim
FROM python:$PYTHON_VERSION

# update image
RUN set -ex \
    && apt-get update \
    && apt-get upgrade --yes \
    && apt-get install --yes --no-install-recommends \
        git

# install tools
WORKDIR /tmp
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# setup git
COPY configs/gitconfig /etc/gitconfig

# setup cookiecutter
ENV COOKIECUTTER_CONFIG=/etc/cookiecutter.yaml
COPY configs/cookiecutter.yaml /etc/cookiecutter.yaml
COPY cookies /usr/local/share/cookies

# setup invoke
COPY configs/invoke.yaml /etc/invoke.yaml
COPY tasks /usr/local/share/invoke/tasks

# setup entry point
ENV TMPDIR=/tmp
ENV HOME=$TMPDIR/release-tools
ENV XDG_CONFIG_HOME=$HOME/.config
ENV XDG_DATA_HOME=$HOME/.local
ENV XDG_CACHE_HOME=$HOME/.cache
ENV XDG_RUNTIME_DIR=$HOME/.run
WORKDIR /usr/local/src
ENTRYPOINT [ "/usr/local/bin/invoke"]
CMD ["--list", "--list-format", "nested"]
