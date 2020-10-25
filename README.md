[![PyPi Version](https://img.shields.io/pypi/v/s2-data.svg)](https://pypi.python.org/pypi/s2-data/)

# s2-data

Repository for documenting and interacting with various formats for Spelunky 2.

Currently we have documents for the following:
  * [Save Format](docs/save-format.md)
  * [Leaderboards Format](docs/leaderboards-format.md)
  
as well as libraries for asset extraction and repacking.
  
## Installation

Packages are pushed up to PyPI so assuming you have Python installed you should just be able to run the following to install s2-data:

```console
pip install --upgrade s2-data
```

## Modding

> :warning: This currently only works on version 1.14 of Spelunky 2

s2-data provides two binaries related to modding. `s2-asset-extract` and `s2-asset-pack`. Assuming you ran the command above to
install `s2-data` you should find these two packages in directories such as

```
C:\Users\$USER\AppData\Local\Programs\Python\Python$VERSION\Scripts\s2-asset-extract.exe
C:\Users\$USER\AppData\Local\Programs\Python\Python$VERSION\Scripts\s2-asset-pack.exe
```

if `C:\Users\$USER\AppData\Local\Programs\Python\Python$VERSION\Scripts` is on your path then you can use `s2-asset-extract` and `s2-asset-pack` directly, otherwise you need to specify the fully qualified path. I will use the short names in the rest of this document. If you'd like to learn more about adding python and installed scripts to your path you can learn more here: https://datatofish.com/add-python-to-windows-path/

### Extraction

```console
> cd "C:\Program Files (x86)\Steam\steamapps\common\Spelunky 2"
> copy Spel2.exe Spel2-orig.exe
> s2-asset-extract Spel2-orig.exe
```

This will made a directory called `Mods` that has an `Extracted` and `Overrides` directory in it. All of the assets that were extracted from the binary will be in `Extracted`. This directory should be considered read-only for the purposes of modding but you have access to all assets in there for reference. The `Overrides` directory has the same directory layout as `Extracted` but is otherwise empty. This is where you would put files for repacking in the next step.

### Repacking

Repacking expects the directory structure from the extraction step above. It will first check the `Overrides` directory for any files and prefer them when repacking the binary. Any assets you want to override should go in the `Overrides` directory, matching the layout and name of the file from the `Extracted` directory.

```console
> cd "C:\Program Files (x86)\Steam\steamapps\common\Spelunky 2"
> s2-asset-pack.exe Spel2-orig.exe Spel2.exe
```

## Development

If you'd like to contribute to s2-data here are some steps to setup your environment.

### Creating VirtualEnv
In the root directory you can make a virtualenv. It will be excluded from commits by default
```console
> python -m venv venv
```

### Activate VirtualEnv

You'll want to activate the virtual environment whenever you're testing any commands from this package

#### Powershell
```console
> venv\Scripts\activate.bat
```

#### cmd
```console
> venv/Scripts/Activate.ps1
```

#### bash/zsh
```console
> source venv/bin/activate
```

### Setup

Once you have your virtual environment setup and activated you'll want to finish setting up the development environment.

```console
> python setup.py develop
```

This will install any dependencies as well as setting up links on your path to your local source files. Once this is done
you'll be able to execute the binaries right from your path after any changes to the source without the need to build or
install anything. If you add new source files you may have to run `python setup.py develop` again to make sure they're linked.
