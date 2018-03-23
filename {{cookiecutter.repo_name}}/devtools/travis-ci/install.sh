# Temporarily change directory to $HOME to install software
pushd .
cd $HOME
{% if (cookiecutter.dependency_source == 'Prefer conda-forge over the default anaconda channel with pip fallback' or cookiecutter.dependency_source == 'Prefer default anaconda channel with pip fallback') %}
# Install Miniconda
if [ "$TRAVIS_OS_NAME" == "osx" ]; then
    # Make OSX md5 mimic md5sum from linux, alias does not work
    md5sum () {
        command md5 -r "$@"
    }
    MINICONDA=Miniconda3-latest-MacOSX-x86_64.sh
else
    MINICONDA=Miniconda3-latest-Linux-x86_64.sh
    export PYTHON_VER=$TRAVIS_PYTHON_VERSION
fi
MINICONDA_HOME=$HOME/miniconda
MINICONDA_MD5=$(curl -s https://repo.continuum.io/miniconda/ | grep -A3 $MINICONDA | sed -n '4p' | sed -n 's/ *<td>\(.*\)<\/td> */\1/p')
wget -q https://repo.continuum.io/miniconda/$MINICONDA
if [[ $MINICONDA_MD5 != $(md5sum $MINICONDA | cut -d ' ' -f 1) ]]; then
    echo "Miniconda MD5 mismatch"
    exit 1
fi
bash $MINICONDA -b -p $MINICONDA_HOME

# Configure miniconda
export PIP_ARGS="-U"
export PATH=$MINICONDA_HOME/bin:$PATH
    {% if cookiecutter.dependency_source == "Prefer conda-forge over the default anaconda channel with pip fallback" %}
conda config --add channels conda-forge
    {% endif %}
conda install --yes conda conda-build jinja2 anaconda-client
conda update --quiet --yes --all
{% elif cookiecutter.dependency_source == 'Dependencies from pip only (no conda)' %}
if [ "$TRAVIS_OS_NAME" == "osx" ]; then
    brew upgrade pyenv
    # Pyenv requires minor revision, get the latest
    PYENV_VERSION=$(pyenv install --list |grep $PYTHON_VER | sed -n "s/^[ \t]*\(${PYTHON_VER}\.*[0-9]*\).*/\1/p" | tail -n 1)
    # Install version
    pyenv install $PYENV_VERSION
    # Use version for this
    pyenv global $PYENV_VERSION
    # Setup up path shims
    eval "$(pyenv init -)"
fi
pip install --upgrade pip setuptools
pip install pytest pytest-cov codecov
{% endif %}
# Restore original directory
popd
