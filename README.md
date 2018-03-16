# Cookiecutter for Computational Chemistry Python Packages

An [cookiecutter](https://github.com/audreyr/cookiecutter) template for those interested in developing computational 
chemistry packages in Python. Skeletal starting repositories can be created from this template to create the 
file structure semi-autonomously so you can focus on what's important: the science!

The skeletal structure is designed to help you get started, but do not feel limited by the skeleton's features 
included here. Just to name a few things you can alter to suite your needs: change continuous integration options, 
remove deployment platforms, or test with a different suite.

## Features
* Python-centric skeletal structure with initial module files
* Pre-configured `setup.py` for installation and packaging
* Pre-configured Window, Linux, and OSX continuous integration on AppVeyor and Travis-CI
* Choice of dependency locations through `conda-forge`, default `conda`, or `pip` 
* Basic testing structure with PyTest
* GitHub Hooks
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by [Sphinx](http://www.sphinx-doc.org/en/master/)
* Automatic license file inclusion from several common Open Source licenses or none at all 

## Requirements

* Python 2.7, 3.5, or 3.6
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)

## Usage

With [`cookiecutter` installed](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter), 
execute the following command inside the folder you want to create the skeletal repository. 

```bash
cookiecutter gh:choderalab/cookiecutter-python-comp-chem
```

Which fetches this repository from github automatically and prompts the user for some simple information such as 
package name, author(s), and licences. 

## Output Skeleton

This will be the skeleton made by this `cookiecutter`, the items marked in `{{ }}` will be replaced by your choices 
upon setup.

```
.
├── LICENSE                         <- License file
├── README.md                       <- Description of project which GitHub will render
├── appveyor.yml                    <- AppVeyor config file for Windows testing
├── {{repo_name}}
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── {{first_package_name}}.py   <- Starting packge module
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   └── look_and_say.dat
│   └── tests                       <- Unit test directory with sample tests
│       ├── __init__.py
│       └── test_{{repo_name}}.py
├── devtools                        <- Deployment, packaging, and CI helpers directory 
│   ├── README.md
│   ├── appveyor
│   ├── conda-recipe                <- Conda build and deployment skeleton
│   │   ├── bld.bat
│   │   ├── build.sh
│   │   └── meta.yaml
│   └── travis-ci
│       └── install.sh
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── _static
│   ├── _templates
│   ├── conf.py
│   ├── index.rst
│   └── make.bat
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
├── .github                         <- GitHub hooks for user contrubtion and pull request guides
│   ├── CONTRIBUTING.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .coveragerc                     <- PyTest + Coverage config file for ignoring test directory itself in coverage
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding 
└── .travis.yml                     <- Travis-CI config file for Linux and OSX testing
```

## Acknowledgments

This cookiecutter is developed by Levi N. Naden of Memorial Sloan Kettering Cancer Center in conjunction with 
the [Molecular Sciences Software Institute (MolSSI)](http://molssi.org/). Copyright (c) 2018.

Directory structure template based on recommendation from the 
[Chodera Lab's Software Development Guidelines](https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md).

Elements of this repository drawn from the 
[cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) by Driven Data
and the [MolSSI Python Template](https://github.com/MolSSI/python_template)