"""
Unit and regression test for the {{cookiecutter.repo_name}} package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import {{cookiecutter.repo_name}}


def test_{{cookiecutter.repo_name}}_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "{{cookiecutter.repo_name}}" in sys.modules
