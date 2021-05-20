# Your python console application

This is a small template for building and distributing a python console application.

**TODOS:**

- Do this
- Do that

## Installation

Can be easily installed from pypi with pip3.

```bash
pip3 install python_console_template
```

## Running from source

You can also alway clone the repo from [GitHub](https://github.com/MarkusPeitl/python-console-template) and run with python.

```bash
python3 launcher.py "this/is/my/source/path"
```

or by

```bash
python3 entrypoint.py "this/is/my/source/path"
```

If installed through pypi then executing the script name `entrypoint` essentially runs something like `python3 package/entrypoint.py`,
which is used in the further usage examples.

## FILES and their functions

### build.py

```bash
python3 build.py
```

to build and package the application using setuptools to the **dist** directory.  

### entrypoint.py

```bash
python3 entrypoint.py
```

this is a launcher for the main script, can be used interchangably with package/entrypoint.py.  

### install-dev.py

```bash
python3 install-dev.py
```

use the pip3 installer to install this project directory to the system. (Immediatly reflects the changes done to the scripts).  

### install.py

```bash
python3 install.py
```

Build the application and install the resulting package -> the installation is the same as if you would install the package from pypi.  

### LICENCE.txt

The License of your project, do your research and choose your License with care.  
(Here it is APACHE 2.0)  

### MANIFEST.in

Specifies additional non-python files that should be included into the distributed package.  

### publish.py

```bash
python3 publish.py
```

Build the application and upload to pypi using twine (make sure everything is working before as you can not replace a version once it is online).  

### README.md

Main description and documentation of your project.  

### RELEASE.md

A markdown file containing info about the release versions and their changes.  

### setup.py

The setuptools configuration, which contains all packaging information and some installation information for your project.
Make sure to replace the info before packaging your application.
Contains:

- Meta information like: author, version, classifiers, url, description
- Importent information about the structure and files of your package for installation: modules, entrypoints, name, dependencies

## Usage: Setting up app

```bash
entrypoint --setup
```

### If you like the project consider dropping me a coffee

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=BSFX8LCPHW2AE)
  
<br>  
<br>