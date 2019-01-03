# Cookiecutter for Computational Molecular Sciences (CMS) Python Packages
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/MolSSI/cookiecutter-cms.svg?branch=master)](https://travis-ci.org/MolSSI/cookiecutter-cms)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/yxb39cib8osqg41l/branch/master?svg=true)](https://ci.appveyor.com/project/Lnaden/cookiecutter-cms/branch/master)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-cms/badge/?version=latest)](https://cookiecutter-cms.readthedocs.io/en/latest/?badge=latest)


A [cookiecutter](https://github.com/audreyr/cookiecutter) template for those interested in developing computational 
molecular packages in Python. Skeletal starting repositories can be created from this template to create the 
file structure semi-autonomously so you can focus on what's important: the science!

The skeletal structure is designed to help you get started, but do not feel limited by the skeleton's features 
included here. Just to name a few things you can alter to suite your needs: change continuous integration options, 
remove deployment platforms, or test with a different suite.

## Features
* Python-centric skeletal structure with initial module files
* Pre-configured `setup.py` for installation and packaging
* Pre-configured Window, Linux, and OSX continuous integration on AppVeyor and Travis-CI
* Choice of dependency locations through `conda-forge`, default `conda`, or `pip` 
* Basic testing structure with [PyTest](https://docs.pytest.org/en/latest/)
* Automatic `git` initialization + tag
* GitHub Hooks
* Automatic package version control with [Versioneer](https://github.com/warner/python-versioneer)
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by [Sphinx](http://www.sphinx-doc.org/en/master/)
* Automatic license file inclusion from several common Open Source licenses (optional)

## Requirements

* Python 3.6, or 3.7
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

## Next steps and web integrations
The repository contains a number of "hooks" that integrate with a variety of web services. To fully integrate the project
with these web services and to get started developing your project please proceed through the following directions.

### Local installation
For development work it is often recommended to do a "local" python install via `pip install -e .`. This command will insert your
new project into your Python site-packages folder so that it can be found in any directory on your computer.

### Setting up with GitHub
Upon creation, this project will initialize the output as a `git` repository compatible with 
[Versioneer](https://github.com/warner/python-versioneer). However, this does not automatically register the 
repository with GitHub. To do this, follow the instructions for 
[Adding an existing project to GitHub using the command line](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/). 
Follow the first step to create the repository on GitHub, but ignore the warnings about the README, license, and 
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

### Continuous Integration
Testing is accomplished with both [Appveyor](https://www.appveyor.com) (for Windows testing) and 
[Travis-CI](https://travis-ci.org) (for Linux testing). These frameworks are chosen as they
are completely free for open source projects and allow you to automatically verify that your project works under a 
variety of OS's and
Python versions. To begin please register with both Appveyor and Travis-CI and turn on the git hooks under the project 
tabs. You will also want to correct the badges which appear on the output README file to point to the correct links

You may notice that our scripts 
[check the MD5 hash for the Miniconda installer](%7B%7Bcookiecutter.repo_name%7D%7D/devtools/travis-ci/before_install.sh) 
before installing. In general, it is often good idea to check the MD5 of any file which you are pulling from the net
automatically, 
especially if there are mirrors, as a simple (but not fool-proof) method of ensuring you got the expected file for 
effectively free.
However, there are a couple other reasons we check the MD5 for the Miniconda installer:

* Prevent getting the wrong Miniconda version. Sometimes the Miniconda maintainers will update their download links for 
  `latest` version before updating the MD5 hashes on the site. This can lead to some unexpected behavior, 
  especially on major Conda version upgrades. Thus, the MD5 check helps trap that.
* Should Miniconda ever change their distribution method, this check will fail and you the maintainer can find out 
  what has changed to update your code as needed. 
* Some projects may need to pin to very specific, or maximum Conda versions. This helps ensure version expectations. 
  It should be noted this is a very rare case. 

  
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
 wont have to download from the slower mirror. If you this sounds like a helpful feature, you can check out the 
links below. We do not implement them for this Cookiecutter, but they can be added to your package as needed.

* [Travis-CI Caching](https://docs.travis-ci.com/user/caching/)
* [AppVeyor Caching](https://www.appveyor.com/docs/build-cache/)
 
  

### Documentation 
Make a [ReadTheDocs](https://readthedocs.org) account and turn on the git hook. Although you can manually make the 
documentation yourself through [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html), you can also 
configure [ReadTheDocs](https://docs.readthedocs.io/en/latest/getting_started.html) to automatically build and 
publish the documentation for you. The initial skeleton of the documentation can be found in the `docs` folder 
of your output.

### Static Code Analysis
Make a [LGTM](https://lgtm.com) account and add your project. If desired you can add code review integration by clicking the large green button!

Static code analysis dramatically enhances the quality of your code by finding a large number of common mistakes that both novice and advanced programmers make. There are many static analysis codes on the market, but we have seen that LGTM is a delicate balance between verbosity and catching true errors.

### Additional Python Settings in `setup.py`

This Cookiecutter generates the package, but there are a several package-specific Python settings you can tune to your 
package's installation needs. These are settings in the `setup.py` file which contains instructions for Python on 
how to install your package. Each of the options in the file are commented with what it does and when it should be 
used. 


## Why is Python 2.X not on the supported versions?
New projects generally should not be built with Python 2.7 support in mind, see the 
[Python 3 Statement](https://python3statement.org/). Although the final Python 2.7 release will be 
[supported through 2020](http://legacy.python.org/dev/peps/pep-0373/) and is the default on many legacy systems, Python 
3 has been released for almost a decade and projects long term usage should not be shacked by legacy methods that will 
have to be replaced in very short order as Python 2 support is retired.


## Conda and PyPI (`pip`)

Should you deploy and/or develop on Conda (with the `conda-build` tool) or PyPI (with the `pip` tool)? Good question, 
both have their own advantages and weaknesses as they both are designed to do very different things. Fortunately, 
many of the features you will need for this Cookiecutter overlap.
We will not advocate here for one or the other, nor will we cover all the differences. We can however recommend some 
additional resources where you can read and find out more at the end of this section.

We will cover the major differences you the developer will see between the two as they relate to this Cookiecutter. 

The first major difference is the dependency sources. Both [Conda](https://anaconda.org) and [PyPI](https://pypi.org/) 
have different packages which individually choose to deploy on one or the other (often both), so its important to keep 
that in mind when choosing a dependency source. 

For testing purpose, the PyPi tool, `pip`, is much faster about 
building your packages than the Conda tool, `conda-build`, will be. Depending on the number of dependencies, you may 
have conditions where `conda-build` takes 10-20 min to resolve, download, configure, and install all dependencies 
*before your tests start*, whereas `pip` would do the same in about 5 min. It is also important to note that both 
`pip` and `conda-build` are not *testing tools* in and of themselves, they are deployment and dependency resolution 
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
* [Conda's Package Management docs](https://conda.io/docs/user-guide/tasks/manage-pkgs.html)
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
a Conda Build  `meta.yaml` file. We feel this benefits outweigh the costs and have adopted this model.

## Deploying your code

Simply testing your code is insufficient for good coding practices, you *should* be ready to deploy 
your code as well. Do not be afraid of deployment though; Python deployment over the last several years 
has been getting easier, especially when there are others to manage your deployment for you. 
There are several ways to handle this, we will cover a couple here, depending on the conditions 
which best suit your needs. The list below is neither exhaustive nor exclusive. There are times
when you may want to build your packages yourself and upload them for developmental purposes, 
but we recommend letting others handle (and help you) with deployment.
These are meant to serve as guides to help you get started.

Deployment should not get in the way of testing. You could configure the Travis and AppVeyor scripts
to handle the build stage after the test stage, but this is should only be done by advanced 
users or those looking to deploy themselves.


### Deployment Method 1: Conda Forge

The [Conda Forge](https://conda-forge.org/) community is a great, and the recommended location to deploy your 
packages. The community is highly active and many scientific developers have been moving here to access not 
only Conda Forge's deployment tools, but also for easy access to all the other Python packages which have 
been deployed on the platform. Even though they provide the deployment architecture, you need to still 
test your program's ability to be packaged through `conda-build`. 
If you choose either Conda dependency option, additional 
tests will be added to Travis and/or AppVeyor which *only* package through `conda-build`.

This method relies on the conda `meta.yaml` file.

### Deployment Method 2: Conda through someone else's manager

This option is identical to the Conda Forge method, but relies on a different group's deployment platform
such as [Bioconda](https://bioconda.github.io/) or [Omnia](http://www.omnia.md/). Each platform has their
own rules, which may include packaging your program yourself and uploading. Check each platform's 
instructions and who else deploys to them before choosing this option to ensure its right for you.

This method relies on the conda `meta.yaml` file.

## Deployment Method 3: Upload package to PyPi

The [Python Package Index (PyPi)](https://pypi.org/) is another place to manage your package and have 
dependencies resolve. This option typically relies on `pip` to create your packages and dependencies 
must be specified in your `setup.py` file to resolve correctly.

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
├── LICENSE                         <- License file
├── README.md                       <- Description of project which GitHub will render
├── appveyor.yml                    <- AppVeyor config file for Windows testing (if chosen)
├── {{repo_name}}
│   ├── __init__.py                 <- Basic Python Package import file
│   ├── {{first_module_name}}.py    <- Starting packge module
│   ├── data                        <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   └── look_and_say.dat
│   ├── tests                       <- Unit test directory with sample tests
│   │   ├── __init__.py
│   │   └── test_{{repo_name}}.py
│   └── _version.py                 <- Automatic version control with Versioneer
├── devtools                        <- Deployment, packaging, and CI helpers directory 
│   ├── README.md
│   ├── conda-envs                  <- Environments for testing
│   │   └── test_env.yaml
│   ├── conda-recipe                <- Conda build and deployment skeleton
│   │   ├── bld.bat                 <- Win specific file, not present if Win CI not chosen
│   │   ├── build.sh
│   │   └── meta.yaml
│   ├── scripts
│   │   └── create_conda_env.py     <- OS anostic Helper script to make conda environments based on simple flags
│   └── travis-ci
│       └── install.sh
├── docs                            <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                   <- Instructions on how to build the docs
│   ├── _static
│   ├── _templates
│   ├── conf.py
│   ├── index.rst
│   └── make.bat
├── setup.cfg                       <- Near-master config file to make house INI-like settings for Coverage, Flake8, YAPF, etc.
├── setup.py                        <- Your package's setup file for installing with additional options that can be set
├── versioneer.py                   <- Automatic version control with Versioneer
├── .github                         <- GitHub hooks for user contrubtion and pull request guides
│   ├── CONTRIBUTING.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .codecov.yml                    <- Codecov config to help reduce its verbosity to more reasonable levels
├── .gitignore                      <- Stock helper file telling git what file name patterns to ignore when adding 
└── .travis.yml                     <- Travis-CI config file for Linux and OSX testing
```

## Acknowledgments

This cookiecutter is developed by Levi N. Naden and 
Daniel G. A. Smith from the [Molecular Sciences Software Institute (MolSSI)](http://molssi.org/). Copyright (c) 2018.

Directory structure template based on recommendation from the 
[Chodera Lab's Software Development Guidelines](https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md).

Original hosting of repository owned by the [Chodera Lab](https://github.com/choderalab)

Elements of this repository drawn from the 
[cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) by Driven Data
and the [MolSSI Python Template](https://github.com/MolSSI/python_template)
