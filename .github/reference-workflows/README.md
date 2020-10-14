# Reference GitHub Actions Workflows

This directory contains the reference workflows for all of the GitHub Actions generated from the Cookiecutter

Another GHA Workflow validates that the outputs of this folder match the outputs of the Cookiecutter

That same workflow also has an approximate implementation of the GHA to at least try to emulate its steps.

To regenerate the references, run the "regenerate_references.sh" script from the "tests" directory in the root of the 
Cookiecutter. There is a bit of manual adjustment required if the scripts change, but this is at least a simple test.
