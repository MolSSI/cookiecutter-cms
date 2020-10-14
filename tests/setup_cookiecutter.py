"""
Simulates a cookiecutter run
"""

from subprocess import Popen, PIPE, STDOUT
from os.path import abspath
import sys

project = sys.argv[1]
lic = sys.argv[2]
depend = sys.argv[3]
provider = sys.argv[4]
rtd = sys.argv[5]
try:
    cookie_path = abspath(sys.argv[6])
except IndexError:
    cookie_path = "."

print("Options: open_source_license=%s, dependency_source=%s, ci_provider=%s, rtd=%s" % (lic, depend, provider, rtd))

# Setup the options
options = [project,  # Repo name
           project,  # Project name
           project,  # First module name
           "cookie monster",  # Author name
           "cookiemonster@trash.can",  # Author email
           "",  # Description
           lic,  # License
           depend,  # Dependency
           provider,  # ci_provider
           rtd] 

# Open a thread
p = Popen(["cookiecutter", cookie_path], stdin=PIPE, stdout=PIPE)

# Communicate options
opts = "\n".join(options).encode("UTF-8")
output = p.communicate(opts)[0].decode()
try:
    if p.returncode != 0:
        raise RuntimeError("Cookiecutter did not run successfully!")
finally:
    # Print the output for prosperity
    print("\n".join(output.split(": ")))
