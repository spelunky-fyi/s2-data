[![PyPi Version](https://img.shields.io/pypi/v/s2-data.svg)](https://pypi.python.org/pypi/s2-data/)

# s2-data

Repository for documenting and interacting with various formats for Spelunky 2.

Currently we have documents for the following:
  * [Save Format](docs/save-format.md)
  * [Leaderboards Format](docs/leaderboards-format.md)

as well as libraries for asset extraction and repacking.

## Installation

```console
pip install --upgrade s2-data
```

## Development

If you'd like to contribute to `s2-data` here are some steps to setup your environment.

### VirtualEnv

*While not required, a virtualenv is a nice way to keep this projects dependencies isolated from the rest of your system. This step is optional but recommended*

In the root directory you can make a virtualenv. It will be excluded from commits by default

```console
python -m venv venv
```
Whenever developing the project you'll want to activate the virtualenv in your terminal. This is platform dependent and there are more comprehensive docs available here: https://docs.python.org/3/library/venv.html


### Setup

Once you have your virtual environment setup and activated you'll want to finish setting up the development environment.

```console
> python setup.py develop
```

This will install any dependencies as well as setting up links on your path to your local source files. Once this is done
you'll be able to execute the binaries right from your path after any changes to the source without the need to build or
install anything. If you add new source files you may have to run `python setup.py develop` again to make sure they're linked.
