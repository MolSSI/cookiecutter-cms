{{cookiecutter.project_name}}
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.repo_name}}/workflows/CI/badge.svg)](https://github.com/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.repo_name}}/actions?query=branch%3Amaster+workflow%3ACI)
[![Travis Build Status](https://travis-ci.com/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.project_name}}.svg?branch=master)](https://travis-ci.com/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.project_name}})
{% if cookiecutter.Include_Windows_continuous_integration == "y" -%}
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/REPLACE_WITH_APPVEYOR_LINK/branch/master?svg=true)](https://ci.appveyor.com/project/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.project_name}}/branch/master)
{% endif -%}
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.project_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/{{cookiecutter.project_name}}/branch/master)

{{cookiecutter.description}}

### Copyright

Copyright (c) {% now 'utc', '%Y' %}, {{cookiecutter.author_name}}


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version {{cookiecutter._cms_cc_version}}.
