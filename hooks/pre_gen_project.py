"""
Pre Cookie Generation script(s)

If any error is raised, the cookie cutter creation fails and crashes
"""

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.first_module_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: {} is not a valid Python module name!'.format(module_name))

    # exits with status 1 to indicate failure
    sys.exit(1)
