# Temporarily change directory to $HOME to install software
pushd .
cd $HOME

{% if (cookiecutter.dependency_source == 'conda-forge' or cookiecutter.dependency_source == 'conda') %}
# Install Miniconda
MINICONDA=Miniconda3-latest-Linux-x86_64.sh
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
    {% if cookiecutter.dependency_source == "conda-forge" %}
conda config --add channels conda-forge
    {% endif %}
conda install --yes conda conda-build jinja2 anaconda-client pip pytest pytest-cov
conda update --quiet --yes --all
{% elif cookiecutter.dependency_source == 'pip' %}
if [ "$TRAVIS_OS_NAME" == "osx" ]; then
    brew install pyenv
    pyenv install $PYTHON_VER
    pyenv local $PYTHON_VER
fi
pip install --upgrade pip setuptools
pip install pytest pytest-cov
{% endif %}

{% if cookiecutter.dependency_source == "conda-forge" %}
conda install --yes codecov  # Only available in conda-forge channel or pip
{% else %}
pip install codecov  # Only available in conda-forge channel or pip
{% endif %}

# Restore original directory
popd