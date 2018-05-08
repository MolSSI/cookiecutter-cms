#!/bin/bash

# Build the python package
$PYTHON setup.py install --single-version-externally-managed --record=record.txt
