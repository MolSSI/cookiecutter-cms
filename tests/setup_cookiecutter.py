"""
Simulates a cookiecutter run
"""

from subprocess import Popen, PIPE, STDOUT
import sys

project = sys.argv[1]
lic = sys.argv[2]
depend = sys.argv[3]
windows = sys.argv[4]
print("Options: open_source_license=%s, dependency_source=%s, windows_ci=%s" % (lic, depend, windows))

# Setup the options
options = [project, # Repo name
           project, # Project name
           project, # First module name
           "cookie monster", # Author name
           "cookiemonster@trash.can", # Author email
           "", # Description
           lic, # License
           depend, # Dependency
           windows] # Windows

# Open a thread
p = Popen(["cookiecutter", "."], stdin=PIPE, stdout=PIPE)

# Communicate options
opts = "\n".join(options).encode("UTF-8")
output = p.communicate(opts)[0].decode()

# Print the output for prosperity
print("\n".join(output.split(": ")))
