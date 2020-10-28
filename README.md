[![PyPi Version](https://img.shields.io/pypi/v/s2-data.svg)](https://pypi.python.org/pypi/s2-data/)

# s2-data

Repository for documenting and interacting with various formats for Spelunky 2.

Currently we have documents for the following:
  * [Save Format](docs/save-format.md)
  * [Leaderboards Format](docs/leaderboards-format.md)
  
as well as libraries for asset extraction and repacking.
  
## Installation

You'll need to have [Python 3.7 or 3.8](https://www.python.org/downloads/) installed to install these tools. Make sure when you're installing Python that you click the checkbox to add Python to your `PATH`:

![Add Python to PATH](https://cdn.discordapp.com/attachments/756241793753809106/771016197424152576/0001_add_Python_to_Path.png).

If you've already installed Python without doing this you can either re-install or follow the instructions at this site: https://datatofish.com/add-python-to-windows-path/

Once you have python installed you can open `cmd` and run the following:

```console
pip install --upgrade s2-data
```

## Modding

> :warning: This currently only works on version 1.14+ of Spelunky 2

Once installed you should have two binaries related to modding. `s2-asset-extract` and `s2-asset-pack`. You can then use the following sections for instructions on extracting, modifying, and repacking the assets.

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
> s2-asset-pack Spel2-orig.exe Spel2.exe
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
