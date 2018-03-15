# Development, testing, and deployment tools

This directory contains a collection of tools for running Continuous Integration (CI) tests, 
conda installation, and other development tools not directly related to the coding process.


## Manifest

### Continuous Integration

You should test your code, but do not feel compelled to use these specific programs. You also may not need Unix and 
Windows testing if you only plan to deploy on specific platforms. These are just to help you get started

* `travis-ci`: Linux and OSX based testing through [Travis-CI](https://about.travis-ci.com/) 
  * `install.sh`: Pip/Miniconda installation script for Travis
* `appveyor`: Windows based testing through [AppVeyor](https://www.appveyor.com/)
  * `install_conda.ps1` Powershell installation script of Conda components

### Conda Recipe:

This directory contains the files to build and deploy on [Conda](https://conda.io/).

* `conda-recipie`: directory containing all the build objects required for Conda. All files in this folder must have their given names
  * `meta.yaml`: The yaml file needed by Conda to construct the build
  * `build.sh`: Unix-based instructions for how to install the software interpreted by Conda
  * `bld.bat`: Windows-based instructions for how to install the software interpreted by Conda


## How to contribute changes
- Clone the repository if you have write access to the main repo, fork the repository if you are a collaborator.
- Make a new branch with `git checkout -b {your branch name}`
- Make changes and test your code
- Push the branch to the repo (either the main or your fork) with `git push -u origin {your branch name}`
  * Note that `origin` is the default name assigned to the remote, yours may be different
- Make a PR on GitHub with your changes
- We'll review the changes and get your code into the repo after lively discussion!


## Checklist for updates
- [ ] Update `setup.py` version number (see specific update type for details)
- [ ] Make sure there is an/are issue(s) opened for your specific update
- [ ] Create the PR, referencing the issue
- [ ] Debug the PR as needed until tests pass
- [ ] Tag the final, debugged version as the one in `setup.py`
   *  `git tag -a X.Y.Z [latest pushed commit] && git push --follow-tags`
- [ ] Get the PR merged in
