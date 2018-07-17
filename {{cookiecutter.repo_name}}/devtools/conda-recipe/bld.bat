# Build the python package, don't let setuptools/pip try to get packages
"%PYTHON%" setup.py install --no-deps
if errorlevel 1 exit 1
