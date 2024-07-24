# Cookiecutter for Computational Molecular Sciences (CMS) Python Packages
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/cookiecutter-cms/workflows/Pseudo%20Validate%20GHA%20Output/badge.svg)](https://github.com/MolSSI/cookiecutter-cms/actions?query=workflow%3A%22Pseudo+Validate+GHA+Output%22)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-cms/badge/?version=latest)](https://cookiecutter-cms.readthedocs.io/en/latest/?badge=latest)

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for those interested in developing computational
molecular packages in Python. Skeletal starting repositories can be created from this template to create the file
structure semi-autonomously, so you can focus on what's important: the science!

The skeletal structure is designed to help you get started, but do not feel limited by the skeleton's features included
here. Just to name a few things you can alter to suit your needs: change continuous integration options, remove
deployment platforms, or test with a different suite.

## Features
* Python-centric skeletal structure with initial module files
* Pre-configured `pyproject.toml` and `setup.cfg` for installation and packaging
* Pre-configured Windows, Linux, and OSX continuous integration on GitHub Actions.
* Choice of dependency locations through `conda-forge`, default `conda`, or `pip`
* Basic testing structure with [PyTest](https://docs.pytest.org/en/latest/)
* Automatic `git` initialization + tag
* GitHub Hooks
* Automatic package version control with [Versioningit](https://versioningit.readthedocs.io/en/stable/)
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by [Sphinx](http://www.sphinx-doc.org/en/master/)
* Automatic license file inclusion from several common Open Source licenses (optional)

## Requirements

* Python 3.8, 3.9, or 3.10
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)
* [Git](https://git-scm.com/)

## Usage

With [`cookiecutter` installed](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter),
execute the following command inside the folder you want to create the skeletal repository.

```bash
cookiecutter gh:molssi/cookiecutter-cms
```

Which fetches this repository from github automatically and prompts the user for some simple information such as
package name, author(s), and licences.

[![The cookiecutter in action](http://img.youtube.com/vi/_E7AlaG8zbk/0.jpg)](http://www.youtube.com/watch?v=_E7AlaG8zbk "Computational Molecular Sciences Cookieucutter Example")

## Supported Python Versions
The MolSSI Cookiecutter will strive to support the current version of Python, two minor versions before. This 
philosophy is in align with [Conda-Forge's](https://conda-forge.org/docs/orga/guidelines.html#python) guidelines 
and gives projects ample time to implement new features.

### When to drop support for older Python versions?

Project developers can freely choose when to drop support for older versions of Python, or if they don't want to support
as many. The general rules we recommend are:

* Support at least two Python versions: The most recent and the preceding minor version. E.g. 3.9 and 3.8
* Dropping Python versions should require a minor Project Version increment.
* New Python versions have been supported for at least one minor revision. E.g Project X.Y supports Python 3.8 and 3.9;
  Project X.Y+1 supports Python 3.8, 3.9 and 3.10; Project X.Y+2 supports Python 3.9 and 3.10.
* Add deprecation warnings if features will be removed.

### Where is setup.py?

For a long time, many Python projects relied on one of the libraries `distutils` or `setuptools` and a corresponding
meta-data defining file often called `setup.py`. These dependencies required python to run, and by its nature limited
how much configuration could be done. `setup.py` has since been superseded by a new file called `pyproject.toml`, which
is a build-system agnostic file which serves much of the same purpose, but can be extended to any number of tools, many
of which can be retrieved from the internet simply by defining it in the `pyproject.toml` file. Many of the features
which were in `setup.py` can be replaced by equivalent keys in the `pyproject.toml`. By default, the cookiecutter uses
the `setuptools` backend anyways, just with the modernized install specification.

## Next steps and web integrations

The repository contains a number of "hooks" that integrate with a variety of web services. To fully integrate the
project with these web services and to get started developing your project please proceed through the following
directions.

### Local installation

For development work it is often recommended to do a "local" python install via `pip install -e .`. This command will
insert your new project into your Python site-packages folder so that it can be found in any directory on your computer.

### Setting up with GitHub

Upon creation, this project will initialize the output as a `git` repository. However, this does not automatically
register the repository with GitHub. To do this, follow the instructions for
[Adding an existing project to GitHub using the command line](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
. Follow the first step to create the repository on GitHub, but ignore the warnings about the README, license, and
`.gitignore` files as this repo creates them. From there, you can skip to after the "first commit" instructions and
proceed from there.

### Testing
The Python testing framework was chosen to be [pytest](https://pytest.org) for this project. Other testing frameworks are available;
however, the authors believe the combination of easy [parametrization of tests](https://docs.pytest.org/en/latest/parametrize.html),
[fixtures](https://docs.pytest.org/en/latest/fixture.html), and [test marking](https://docs.pytest.org/en/latest/example/markers.html)
make `pytest` particularly well suited for molecular software packages.

To get started additional tests can be added to the `project/tests/` folder. Any function starting with `test_*` will automatically be
included in the testing framework. While these can be added in anywhere in your directory structure, it is highly recommended to keep them
contained within the `project/tests/` folder.

Tests can be run with the `pytest -v` command. There are a number of additional command line arguments to
[explore](https://docs.pytest.org/en/latest/usage.html).

### Continuous Integration (GitHub Actions)

As of version 1.3, we provide preconfigured workflows for [GitHub Actions](https://github.com/features/actions), with
support for Linux, MacOS and Windows. Conda support is possible thanks to the excellent
[@mamba-org's `provision-with-micromamba` action](https://github.com/marketplace/actions/provision-with-micromamba). We
encourage you read its documentation for further details on GitHub Actions themselves.

The Cookiecutter's GitHub Actions does a number of things differently than the output Actions. We detail those
differences below, but none of this is needed to understand the output GitHub Action Workflows, which are much simpler.

The Cookiecutter ability to test GitHub Actions it generates has some limitations, but are still properly tested.
This repository has a multi-job GitHub Action Workflow to do a few things:
* Run the Cookiecutter and generate outputs.
* Compare the output CI's to references.
* Run an approximate implementation of the generated CI files.

If the reference files need re-generated, there is a script to help with this.

Ideally, the Cookiecutter would run the generated output files in real time. However, that is currently impossible with 
GitHub Actions (as of October 14 2020). We Cookiecutter-CMS maintainers have also looked at reactive PR’s which 
implement on different branches and make new PR’s and setting up dummy repositories and pushing to those and then 
monitoring the test/return from that. This was all determined to be overly complicated, although we welcome suggestions 
and ideas for improvements.

### Discontinued CI Strategies: Travis & AppVeyor 
We **no longer recommend** projects to use [Travis-CI](https://travis-ci.com) or [AppVeyor](https://www.appveyor.com) 
for CI services. We found the AppVeyor service to be notorious slow in practice, and Travis 
[updated their billing model](https://blog.travis-ci.com/2020-11-02-travis-ci-new-billing) to charge for OSX testing and 
further limit their Linux concurrency, even for fully open source software. Given the rise of 
[GitHub Actions](https://github.com/features/actions), we feel it was appropriate to transition off these platforms as 
of the CMS Cookiecutter's 1.5 release.

The final version of the CMS-Cookiecutter with Travis and AppVeyor support can be found 
here: https://github.com/MolSSI/cookiecutter-cms/releases/tag/1.4 for legacy purposes.

#### Pre-caching common build data

Some continuous integration platforms allow for caching of build data, which you may, or may not, find advantageous.
The general purpose of the caches are to store and fetch files and folders which may take a long time to either
generate or download every time you want to run a CI build; often because build (and developer) time is limited.
However, if the cached data changes any time during a build, then the whole targeted cache is updated and uploaded.
So, you should only cache things you do not expect to change.

You may be tempted to cache the Conda installer or Python dependencies fetched from `conda` or `pip`, however, this
is an ill advised idea for two main reasons:

1. Your package's dependencies are constantly updating,
   so you want catch things which break due to dependencies before your user does. Having CI automatically trigger when
   you make changes and at scheduled intervals helps catch these things as soon as possible.
    * Because you should expect dependencies updating, you will have to upload a new cache each build anyways, somewhat
      invalidating one of the advantages of a cache.
2. It is a good idea to make sure your testing emulates the most basic user of your code if possible.
   If your target users include people who will try to download your package and have it "just work" for their project,
   then your CI testing should try to do this as well. This would include getting newest, updated installer and
   dependencies. One example
   of this may be industry, non-developer users, who do not know all the nuances and inner workings of package
   dependencies or versions. It is not reasonable to expect them to know these nuances either, its why you are the
   developer.

There may be some times where the caching feature is helpful for you. One example: including test data which is too
large to store on GitHub, but also has a slow mirror hosting it. A cache will help speed up the test since you
will not have to download from the slower mirror. If you this sounds like a helpful feature, you can check out the
links below. We do not implement them for this Cookiecutter, but they can be added to your package as needed.

* [GitHub Actions Caching](https://docs.github.com/en/free-pro-team@latest/actions/guides/caching-dependencies-to-speed-up-workflows)

There are caching capabilities for the `mamba-org/provision-with-micromamba` action, if you are using it as well.

* [Setup Micromamba GHA Caching](https://github.com/mamba-org/provision-with-micromamba#cache-downloads)

### Documentation
Make a [ReadTheDocs](https://readthedocs.org) account and turn on the git hook. Although you can manually make the
documentation yourself through [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html), you can also
configure [ReadTheDocs](https://docs.readthedocs.io/en/latest/getting_started.html) to automatically build and
publish the documentation for you. The initial skeleton of the documentation can be found in the `docs` folder
of your output.

### Static Code Analysis
Make a [LGTM](https://lgtm.com) account and add your project. If desired you can add code review integration by clicking the large green button!

Static code analysis dramatically enhances the quality of your code by finding a large number of common mistakes that both novice and advanced programmers make. There are many static analysis codes on the market, but we have seen that LGTM is a delicate balance between verbosity and catching true errors.

### Additional Python Settings in `setup.cfg`

This Cookiecutter generates the package, but there are a several package-specific Python settings you can tune to your
package's installation needs.
These are settings in the `setup.cfg` file,
which contains instructions for Python on how to install your package.
Each of the options in the file are commented with what it does and when it should be
used.

### Versioningit

Versioningit automatically provides a version string based on the `git` tag and commit hash, which is then exposed
through a `project.__version__` attribute in your
`project/__init__.py`. For example, if you mint a tag (a release) for a project
through `git tag -a 0.1 -m "Release 0.1."` (push to GitHub through `git push origin 0.1`), this tag will then reflect in
your project: `project.__version__
== 0.1`. Otherwise, a per-commit version is available which looks like
`0.3.0+81.g332bfc1`. This string shows the current git (the "g") hash `332bfc1`
is 81 commits beyond the version 0.3 tag.


## Conda and PyPI (`pip`)

Should you deploy and/or develop on [Conda](https://anaconda.org) (with the `conda-build` tool) or [PyPI](https://pypi.org/) (with the `pip` tool)? Good question,
both have their own advantages and weaknesses as they both are designed to do very different things. Fortunately,
many of the features you will need for this Cookiecutter overlap.
We will not advocate here for one or the other, nor will we cover all the differences. We can however recommend some
additional resources where you can read and find out more at the end of this section.

We will cover the major differences that you the developer will see between the two as they relate to this Cookiecutter.

For testing purpose, the PyPi tool, `pip`, is much faster about
building your packages than the Conda tool, `conda-build`, will be. Depending on the number of dependencies, you may
have conditions where `conda-build` takes 10-20 min to resolve, download, configure, and install all dependencies
*before your tests start*, whereas `pip` would do the same in about 5 min. It is also important to note that both
`pip` and `conda-build` are not *testing tools* in and of themselves; they are deployment and dependency resolution
tools.  For pure testing, we include other packages like [pytest](https://pytest.org).

From a deployment perspective, it is possible to deploy your package on both platforms, although doing so is beyond
the scope of this Cookiecutter.

Lastly, these are optional features! You could choose to not rely on either Conda or PyPI, assuming your package
does not need dependencies. We do highly recommend you pick one of them for dependency resolution so you (and your
potential users) are not having to manually find and install all the dependencies you may have. To put some historical
perspective on this, NumPy and SciPy used to ask the users to install the [BLAS](http://www.netlib.org/blas/) and
[LAPACK](http://www.netlib.org/lapack/) libraries on their own, and
then also make sure they were linked correctly to use in Python. These hurdles are no longer required through the
package managers, Huzzah!

### Additional reading for Conda and PyPI

* [Author of the Python Data Science Handbook from O'Rilley's Blog on Conda Myths and Misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)
* [Conda's Package Management docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)
* [`pip` User Guide](https://pip.pypa.io/en/stable/user_guide/)

## Conda Build vs. Conda Environments

We recommend creating Conda environments rather than relying on conda build for *testing* purposes, assuming you have
opted for Conda as a dependency manager. Earlier versions of this Cookiecutter would conduct testing by first
bundling the package for distribution through
[Conda Build](https://conda.io/docs/user-guide/tasks/build-packages/index.html), and then installing the package
locally to execute tests on. This had the advantage of ensuring your package *could* be bundled for distribution and
that all of its dependencies resolved correctly. However, it had the disadvantage of being painfully slow and rather
confusing to debug should things go wrong on the build, even before the testing.

The replacement option to this is to pre-create the conda environment and then install your package into it with
no dependency resolution for testing. This helps separate out the concepts of **testing** and **deployment** which
are separate actions, even though deployment should only come after testing, and you should be ready to do both.
This should simplify and accelerate  the testing process, but
does mean maintaining two, albeit similar, files since a Conda Environment file has a different YAML syntax than
a Conda Build  `meta.yaml` file. We feel these benefits outweigh the costs and have adopted this model.

## Deploying your code

Simply testing your code is insufficient for good coding practices; you *should* be ready to deploy
your code as well. Do not be afraid of deployment though; Python deployment over the last several years
has been getting easier, especially when there are others to manage your deployment for you.
There are several ways to handle this. We will cover a couple here, depending on the conditions
which best suit your needs. The list below is neither exhaustive nor exclusive. There are times
when you may want to build your packages yourself and upload them for developmental purposes,
but we recommend letting others handle (and help you) with deployment.
These are meant to serve as guides to help you get started.

Deployment should not get in the way of testing. You could configure the GitHub Action scripts
to handle the build stage after the test stage, but this should only be done by advanced
users or those looking to deploy themselves.


### Deployment Method 1: Conda Forge

The [Conda Forge](https://conda-forge.org/) community is great, and it is the recommended location to deploy your
packages. The community is highly active and many scientific developers have been moving here to access not
only Conda Forge's deployment tools, but also for easy access to all the other Python packages which have
been deployed on the platform. Even though they provide the deployment architecture, you need to still
test your program's ability to be packaged through `conda-build`.
If you choose either Conda dependency option, additional
tests will be added to GitHub Actions which *only* package through `conda-build`.

This method relies on the conda `meta.yaml` file.

### Deployment Method 2: Conda through someone else's manager

This option is identical to the Conda Forge method, but relies on a different group's deployment platform
such as [Bioconda](https://bioconda.github.io/) or [Omnia](http://www.omnia.md/). Each platform has their
own rules, which may include packaging your program yourself and uploading. Check each platform's
instructions and who else deploys to them before choosing this option to ensure its right for you.

This method relies on the conda `meta.yaml` file.

### Deployment Method 3: Upload package to PyPi

The [Python Package Index (PyPi)](https://pypi.org/) is another place to manage your package and have dependencies
resolve. This option typically relies on `pip` to create your packages and dependencies must be specified in
your `pyproject.toml` file to resolve correctly.

### Deployment Method 4: Manually upload your package to some source

Sometimes, your package is niche enough, developmental enough, or proprietary enough to warrant manually
packaging and uploading your program. This may also apply if you want regular developmental builds which you
upload manually to test. In this case, you will want to change your CI scripts to include a build, and
optional upload step on completion of tests.

## Output Skeleton

This will be the skeleton made by this `cookiecutter`, the items marked in `{{ }}` will be replaced by your choices
upon setup.

```
.
├── CODE_OF_CONDUCT.md              <- Code of Conduct for developers and users
├── LICENSE                         <- License file
├── MANIFEST.in                     <- Packaging information for pip
├── README.md                       <- Description of project which GitHub will render
├── {{repo_name}}                   <- Basic Python Package import file
│   ├── {{first_module_name}}.py    <- Starting package module
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── _version.py                 <- Generated file from VersionInGit. Created on package install, not initialization.
│   ├── data                        <- Sample additional data (non-code) which can be packaged. Just an example, delete in production
│   │   ├── README.md
│   │   └── look_and_say.dat
│   ├── py.typed                    <- Marker file indicating PEP 561 type hinting.
│   └── tests                       <- Unit test directory with sample tests
│       ├── __init__.py
│       └── test_{{repo_name}}.py
├── devtools                        <- Deployment, packaging, and CI helpers directory
│   ├── README.md
│   ├── conda-envs                  <- Conda environments for testing
│   │   └── test_env.yaml
│   └── scripts
│       └── create_conda_env.py     <- OS agnostic Helper script to make conda environments based on simple flags
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                   <- Instructions on how to build the docs
│   ├── _static
│   │   └── README.md
│   ├── _templates
│   │   └── README.md
│   ├── api.rst
│   ├── conf.py
│   ├── getting_started.rst
│   ├── index.rst
│   ├── make.bat
│   └── requirements.yaml           <- Documentation building specific requirements. Usually a smaller set than the main program
├── pyproject.toml                  <- Generic Python build system configuration (PEP-517).
├── readthedocs.yml
├── setup.cfg                       <- Near-master config file to make house INI-like settings for Coverage, Flake8, YAPF, etc.
├── .codecov.yml                    <- Codecov config to help reduce its verbosity to more reasonable levels
├── .github                         <- GitHub hooks for user contribution, pull request guides and GitHub Actions CI
│   ├── CONTRIBUTING.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows
│       └── CI.yaml
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding files
├── .gitattributes                  <- Stock helper file telling GitHub how to bundle files in the tarball, should not need to be touched most times
└── .lgtm.yml
```

## Acknowledgments

This cookiecutter is developed by Levi N. Naden and Jessica A. Nash from
the [Molecular Sciences Software Institute (MolSSI)](http://molssi.org/); and Daniel G. A. Smith
of [ENTOS](https://www.entos.ai/). Additional major development has been provided by M. Eric Irrgang. Copyright (c)
2022.

Directory structure template based on recommendation from the
[Chodera Lab's Software Development Guidelines](https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md)
.

Original hosting of repository owned by the [Chodera Lab](https://github.com/choderalab)

Elements of this repository drawn from the
[cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) by Driven Data
and the [MolSSI Python Template](https://github.com/MolSSI/python_template)
