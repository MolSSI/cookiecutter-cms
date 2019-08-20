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


def invoke_shell(command, expected_error=True, print_output=True):

    try:
        output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        # Trap and print the output in a helpful way
        print(decode_string(e.output), decode_string(e.returncode))
        print(e.output)
        output = e.output
        if not expected_error:
            raise e
    if print_output:
        print(decode_string(output))
    return decode_string(output)


def git_init_and_tag():
    """Invoke the initial git and tag with 0.0.0 to make an initial version for Versioneer to ID if not already in a git repository."""
    
    # Check if we are in a git repository
    directory_status = invoke_shell("git status", expected_error=True, print_output=False)
    # Create a repository and commit if not in one.
    if 'fatal' in directory_status:
        # Initialize git
        invoke_shell("git init")

        # Add files created by cookiecutter 
        invoke_shell("git add .")
        invoke_shell(
            "git commit -m \"Initial commit after CMS Cookiecutter creation, version {}\"".format(
                '{{ cookiecutter._cms_cc_version }}'))
        
        # Check for a tag
        version = invoke_shell("git tag", expected_error=True)
        # Tag if no tag exists
        if not version:
            invoke_shell("git tag 0.0.0")
    else:
        print("\ngit repository detected. CookieCutter files have been created in {{ cookiecutter.repo_name }} directory.")


def remove_windows_ci():
    include_windows = '{{ cookiecutter.Include_Windows_continuous_integration }}'
    if include_windows == "n":
        # Remove with appveyor to be a safe delete
        os.remove("appveyor.yml")

remove_windows_ci()
git_init_and_tag()