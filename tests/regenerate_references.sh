#!/usr/bin/env bash

# Regenerate the reference workflow scripts, accepts a path to the

for LIC in 1 2
do
  for DEP in 1 2 3
  do
    for RTD in 1 2
    do
        SEQUENCE=_"$LIC"_"$DEP"_"$RTD"
        python setup_cookiecutter.py prj${SEQUENCE} ${LIC} ${DEP} ${RTD} ..
        mkdir -p CI_files
        mv prj${SEQUENCE}/.github/workflows/CI.yaml CI_files/CI${SEQUENCE}.yaml
        rm -rf prj${SEQUENCE}
    done
  done
done
