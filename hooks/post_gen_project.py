"""
Post Cookie Generation script(s)

These scripts are executed from the output folder.
If any error is raised, the cookie cutter creation fails and crashes
"""

import os
import subprocess as sp


def decode_string(string):
    """Helper function to covert byte-string to string, but allows normal strings"""
    try:
        return string.decode()
    except AttributeError:
        return string


def invoke_shell(command):
    try:
        output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        # Trap and print the output in a helpful way
        print(decode_string(e.output), decode_string(e.returncode))
        print(e.output)
        raise e
    print(decode_string(output))


def git_init_and_tag():
    """Invoke the initial git and tag with 0.0.0 to make an initial version for Versioneer to ID"""
    # Initialize git
    invoke_shell("git init")
    # Add files
    invoke_shell("git add .")
    invoke_shell(
        "git commit -m \"Initial commit after CMS Cookiecutter creation, version {}\"".format(
            '{{ cookiecutter._cms_cc_version }}'))
    # Set the 0.0.0 tag
    invoke_shell("git tag 0.0.0")


def remove_windows_ci():
    include_windows = '{{ cookiecutter.Include_Windows_continuous_integration }}'
    if include_windows == "n":
        # Remove with appveyor to be a safe delete
        os.remove("appveyor.yml")


remove_windows_ci()
git_init_and_tag()
