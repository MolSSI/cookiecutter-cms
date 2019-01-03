#!/usr/bin/env bash

# Travis decided to remove pip from their OSX images post xcode 7.3
# Travis official stance: Python package development is not supported in OSX.
# There is technically a pip2 located in the path, but installing packages through it actually installs to a Python
# in the Brew cellar, which is NOT the same as the python on the path. So mapping pip to $(which pip2) won't work.
# Easy install does not work, there is no ensurepip, and short of re-mapping the python to the version in the Cellar
# (which I don't want to do since I fully expect even that to disappear), I've burned out of ideas.
# ...
# SO! This file exists as a helper to set up the pyenv
# ...
# SIGH - LNN

# IMPORTANT: This should ONLY be used for OSX in Travis CI, not for local production builds of any kind

# Use PyEnv, don't let brew update EVERYTHING ELSE that we don't need it to
HOMEBREW_NO_AUTO_UPDATE=1 brew upgrade pyenv
# Pyenv requires minor revision, get the latest
PYENV_VERSION=$(pyenv install --list |grep $PYTHON_VER | sed -n "s/^[ \t]*\(${PYTHON_VER}\.*[0-9]*\).*/\1/p" | tail -n 1)
# Install version
pyenv install $PYENV_VERSION
# Use version for this
pyenv global $PYENV_VERSION
# Setup up path shims
eval "$(pyenv init -)"
