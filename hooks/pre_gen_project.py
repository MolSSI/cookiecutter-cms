"""
Pre Cookie Generation script(s)

If any error is raised, the cookie cutter creation fails and crashes
"""

import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
EMAIL_REGEX = r'[^@]+@[^@]+\.[^@]+'

repo_name = '{{ cookiecutter.repo_name }}'
module_name = '{{ cookiecutter.first_module_name }}'

author_email = '{{ cookiecutter.author_email }}'

for key in [repo_name, module_name]:
    if not re.match(MODULE_REGEX, key):
        print(key, re.match(MODULE_REGEX, key))
        print('ERROR: "{}" is not a valid Python module name!'.format(key))

        # exits with status 1 to indicate failure
        sys.exit(1)

if not re.match(EMAIL_REGEX, author_email):
    print('ERROR: "{}" is not a valid email address!'.format(author_email))

    # exits with status 1 to indicate failure
    sys.exit(1)
