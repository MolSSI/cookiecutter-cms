"""
Additional functionality not directly related to {{cookiecutter.project_name}}.
"""

import os

def test():
    """
    Runs a smoke test suite through pytest after the module is installed.
    """

    try:
        import pytest
    except ImportError:
        raise RuntimeError('Testing module `pytest` is not installed. Run `conda install pytest`')

    abs_test_dir = os.path.sep.join([os.path.abspath(os.path.dirname(__file__)), "tests"])
    pytest.main(['-rws', '-v', '--capture=sys', abs_test_dir])
