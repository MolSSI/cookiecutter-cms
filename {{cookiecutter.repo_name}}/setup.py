"""{{cookiecutter.project_name}}

{{cookiecutter.description}}
"""
import os.path
import sys

from setuptools import setup

sys.path.append(os.path.dirname(__file__))
import versioneer


setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
