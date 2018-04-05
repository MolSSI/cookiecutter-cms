"""
Simulates a cookiecutter run
"""

from subprocess import Popen, PIPE, STDOUT
import sys

project = sys.argv[1]
lic = sys.argv[2]
depend = sys.argv[3]
print("Options: open_source_license=%s, dependency_source=%s" % (lic, depend)) 

# Setup the options
options = [project, # Repo name
           project, # Project name
           project, # First module name
           "cookie monster", # Author name
           "", # Description
           lic, # License
           depend, # Dependency
           "1"] # Windows

# Open a thread
p = Popen(["cookiecutter", "."], stdin=PIPE, stdout=PIPE)

# Communicate options
opts = "\n".join(options).encode("UTF-8")
output = p.communicate(opts)[0].decode()

# Print the output for prosperity
print("\n".join(output.split(": ")))
