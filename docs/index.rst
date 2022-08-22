.. Computational Molecular Sciences Cookiecutter documentation master file, created by
   sphinx-quickstart on Fri Apr 27 10:12:46 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cookiecutter for Computational Molecular Sciences Python Packages
=================================================================

.. note::

   These docs are are mainly a recreation of the package's ``README.md`` file as an example of building the docs.
   Feel free to borrow from this example and consider splitting the docs into multiple pages!


A `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ template for those interested in developing computational
molecular sciences packages in Python. Skeletal starting repositories can be created from this template to create the
file structure semi-autonomously so you can focus on what's important: the science!

The skeletal structure is designed to help you get started, but do not feel limited by the skeleton's features
included here. Just to name a few things you can alter to suite your needs: change continuous integration options,
remove deployment platforms, or test with a different suite.

Features
--------
* Python-centric skeletal structure with initial module files
* Pre-configured ``pyproject.toml`` and ``setup.cfg`` for installation and packaging
* Pre-configured Window, Linux, and OSX continuous integration on GitHub Actions
* Choice of dependency locations through ``conda-forge``, default ``conda``, or ``pip``
* Basic testing structure with `PyTest <https://docs.pytest.org/en/latest/>`_
* Automatic ``git`` initialization + tag
* GitHub Hooks
* Automatic package version control with `Versioningit <https://versioningit.readthedocs.io/>`_
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by `Sphinx <http://www.sphinx-doc.org/en/master/>`_
* Automatic license file inclusion from several common Open Source licenses (optional)

.. versionchanged:: 1.7
    Added support for :pep:`517` and :pep:`561`.

.. versionchanged:: 1.8
    Switch from Versioneer to Versioningit for :pep:`517`-only builds.
    ``setup.py`` file is no longer generated.

.. versionchanged:: 1.9
    Added support for :pep:`621`. Update to Python 3.10

.. versionchanged:: 1.10
    Switched to Micromamba as CI conda source.

Requirements
------------

* Python 3.8, 3.9, or 3.10
* `Cookiecutter <http://cookiecutter.readthedocs.io/en/latest/installation.html>`_
* `Git <https://git-scm.com/>`_


Usage
-----

With `cookiecutter installed <https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter>`_,
execute the following command inside the folder you want to create the skeletal repository.

.. code:: bash

   cookiecutter gh:molssi/cookiecutter-cms


Which fetches this repository from github automatically and prompts the user for some simple information such as
package name, author(s), and licences.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/_E7AlaG8zbk"
     frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>


Next steps and web integrations
-------------------------------
The repository contains a number of "hooks" that integrate with a variety of web services. To fully integrate the project
with these web services and to get started developing your project please proceed through the following directions.

Local installation
^^^^^^^^^^^^^^^^^^
For development work it is often recommended to do a "local" python install via ``pip install -e .``. 
This command will insert your
new project into your Python site-packages folder so that it can be found in any directory on your computer.

Setting up with GitHub
^^^^^^^^^^^^^^^^^^^^^^
Upon creation, this project will initialize the output as a ``git`` repository compatible with
`Versioneer <https://github.com/warner/python-versioneer>`_. However, this does not automatically register the
repository with GitHub. To do this, follow the instructions for
`Adding an existing project to GitHub using the command line <https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/>`_.
Follow the first step to create the repository on GitHub, but ignore the warnings about the README, license, and
``.gitignore`` files as this repo creates them. From there, you can skip to after the "first commit" instructions and
proceed from there.

Testing
^^^^^^^
The Python testing framework was chosen to be `pytest <https://pytest.org>`_ for this project. Other testing frameworks are available;
however, the authors believe the combination of easy `parametrization of tests <https://docs.pytest.org/en/latest/parametrize.html>`_,
`fixtures <https://docs.pytest.org/en/latest/fixture.html>`_, and `test marking <https://docs.pytest.org/en/latest/example/markers.html>`_
make ``pytest`` particularly well suited for molecular software packages.

To get started additional tests can be added to the ``project/tests/`` folder. Any function starting with ``test_*`` will automatically be
included in the testing framework. While these can be added in anywhere in your directory structure, it is highly recommended to keep them
contained within the ``project/tests/`` folder.

Tests can be run with the ``pytest -v`` command. There are a number of additional command line arguments to
`explore <https://docs.pytest.org/en/latest/usage.html>`_.

Continuous Integration
^^^^^^^^^^^^^^^^^^^^^^

As of version 1.3, we provide preconfigured workflows for [GitHub Actions](https://github.com/features/actions), with
support for Linux, MacOS and Windows. Conda support is possible thanks to the excellent
[@conda-incubator's `setup-miniconda` action](https://github.com/conda-incubator/setup-miniconda). We encourage you
read its documentation for further details on GitHub Actions themselves.

Testing is accomplished with `GitHub Actions <https://github.com/features/actions>`_ for Linux, Windows, and macOS
testing. This framework is chosen as it is completely free for open source projects and allow you to automatically
verify that your project works under a variety of OS's and
Python versions; all within the existing GitHub Framework.
To begin please, ensure GitHub Actions are enabled for your repository in its main settings area. This is often on by
default, so there may not need to be any additional steps needed.
You will also want to correct the badges which appear on the output README file to point to the correct links

Documentation
^^^^^^^^^^^^^
Make a `ReadTheDocs <https://readthedocs.org>`_ account and turn on the git hook. Although you can manually make the
documentation yourself through `Sphinx <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_, you can also
`configure ReadTheDocs <https://docs.readthedocs.io/en/latest/getting_started.html>`_ to automatically build and
publish the documentation for you. The initial skeleton of the documentation can be found in the ``docs`` folder
of your output.

Additional Python Settings in ``setup.cfg`` and ``pyproject.toml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This Cookiecutter generates the package, but there are a several package-specific Python settings you can tune to your
package's installation needs.
These are settings in :file:`setup.cfg` and :file:`pyproject.toml`,
which contain instructions for Python on
how to install your package. Each of the options in the file are commented with what it does and when it should be
used.


Why is Python 2.X not on the supported versions?
------------------------------------------------
New projects generally should not be built with Python 2.7 support in mind, see the
`Python 3 Statement <https://python3statement.org/>`_. Although the final Python 2.7 release was
`supported through 2020 <http://legacy.python.org/dev/peps/pep-0373/>`_ and is the default on many legacy systems, Python
3 has been released for almost a decade and projects long term usage should not be shacked by legacy methods that will
have to be replaced in very short order as Python 2 support is retired.



Additional Pages
================

.. toctree::
   :maxdepth: 2

   nuances


Acknowledgments
===============

This cookiecutter is developed by Levi N. Naden and Jessica A. Nash
from the `Molecular Sciences Software Institute (MolSSI) <http://molssi.org/>`_; and
Daniel G. A. Smith of `ENTOS <https://www.entos.ai/>`_. Additional major development has been provided by M. Eric Irrgang.
Copyright (c) 2022.

Directory structure template based on recommendation from the
`Chodera Lab's Software Development Guidelines <https://github.com/choderalab/software-development/blob/master/STRUCTURING_YOUR_PROJECT.md>`_.

Original hosting of repository owned by the `Chodera Lab <https://github.com/choderalab>`_

Elements of this repository drawn from the
`cookiecutter-data-science <https://github.com/drivendata/cookiecutter-data-science>`_ by Driven Data
and the `MolSSI Python Template <https://github.com/MolSSI/python_template>`_.
