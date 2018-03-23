# Compiling {{cookiecutter.project_name}}'s Documentation

The docs for this project are built with [Sphinx](http://www.sphinx-doc.org/en/master/).
To compile the docs, first ensure that Sphinx and the ReadTheDocs theme are installed.

{% if (cookiecutter.dependency_source == 'Prefer conda-forge over the default anaconda channel with pip fallback' or cookiecutter.dependency_source == 'Prefer default anaconda channel with pip fallback') %}
```bash
conda install sphinx sphinx_rtd_theme 
```
{% elif cookiecutter.dependency_source == 'Dependencies from pip only (no conda)' %}
```bash
pip install sphinx sphinx_rtd_theme
```
{% endif %}

Once installed, you can use the `Makefile` in this directory to compile static HTML pages by
```bash
make html
```

The compiled docs will be in the `_build` directory and can be viewed by opening `index.html` (which may itself 
be inside a directory called `html/` depending on what version of Sphinx is installed).