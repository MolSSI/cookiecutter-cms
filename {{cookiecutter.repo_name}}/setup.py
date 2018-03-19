"""
{{cookiecutter.project_name}}
{{cookiecutter.description}}
"""
from setuptools import setup
DOCLINES = __doc__.split("\n")

########################
VERSION = "0.0.0"  # Primary base version of the build
__version__ = VERSION
########################

setup(
    name='{{cookiecutter.repo_name}}',
    author='{{cookiecutter.author_name}}',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    version=__version__,
    license='{{cookiecutter.open_source_license}}',
    packages=['{{cookiecutter.repo_name}}', "{{cookiecutter.repo_name}}.tests"],
    # Optional include package data to ship with your package
    # We include the package version data
    package_data={'{{cookiecutter.repo_name}}': []  # + ["data/*.dat"]
                  },
    # Additional entries you may want simply uncomment the lines you want and fill in the data
    # author_email='me@place.org',      # Author email
    # url='http://www.my_package.com',  # Website
    # install_requires=[],              # Required packages, pulls from pip if needed; do not use for Conda deployment
    # platforms=['Linux',
    #            'Mac OS-X',
    #            'Unix',
    #            'Windows'],            # Valid platforms your code works on, adjust to your flavor
    # zip_safe=False,                   # Compress final package or not
    # python_requires=">=3.5",          # Python version restrictions

)
