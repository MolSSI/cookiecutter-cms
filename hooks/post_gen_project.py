"""
Post Cookie Generation script(s)

These scripts are executed from the output folder.
If any error is raised, the cookie cutter creation fails and crashes
"""

import os
import subprocess as sp


def decode_string(string):
    """Helper function to convert byte-string to string, but allows normal strings"""
    try:
        return string.decode()
    except AttributeError:
        return string


def invoke_shell(command, error_ok=False, print_output=True):
    
    return_code = 0 # Successful return code

    try:
        output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        output = e.output
        return_code = e.returncode
        if not error_ok:
            raise e
    if print_output:
        print(decode_string(output))
    return decode_string(output), return_code


def git_init_and_tag():
    """
    Invoke the initial git and tag with 0.0.0 to make an initial version for
    Versioneer to ID if not already in a git repository.
    """
    
    # Check if we are in a git repository - calling `git status` outside of a git repository will return 128
    _, return_code = invoke_shell("git status", error_ok=True, print_output=False)
    # Create a repository and commit if not in one.
    if return_code == 128:
        # Initialize git
        invoke_shell("git init")


        # Add files created by cookiecutter 
        invoke_shell("git add .")
        invoke_shell(
            "git commit -m \"Initial commit after CMS Cookiecutter creation, version {}\"".format(
                '{{ cookiecutter._cms_cc_version }}'))
        
        # change default branch name to main
        # safer than --init-branch=main
        # because it works with older versions of git
        invoke_shell("git branch -M main")
        
        # Check for a tag
        version = invoke_shell("git tag", error_ok=True)
        # Tag if no tag exists
        if not version:
            invoke_shell("git tag 0.0.0 -m \"Initial commit from MolSSI cookie cutter\"")
    else:
        print("\ngit repository detected. "
              "CookieCutter files have been created in {{ cookiecutter.repo_name }} directory.")


def remove_rtd():
    include_rtd = '{{ cookiecutter.include_ReadTheDocs }}'
    if include_rtd == "n":
        rtd_env = os.path.join("docs", "requirements.yaml")
        os.remove('.readthedocs.yaml')
        os.remove(rtd_env)


def random_file_cleanup_removal():
    """Remove random files which can be generated under certain conditions"""
    random_file_list = [
        "default.profraw",  # Remove default.profraw files, see #105
    ]
    for random_file in random_file_list:
        try:
            os.remove(random_file)
        except FileNotFoundError:
            pass


remove_rtd()
random_file_cleanup_removal()
git_init_and_tag()
