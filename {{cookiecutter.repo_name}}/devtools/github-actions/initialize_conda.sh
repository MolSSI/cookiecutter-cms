# $CI_OS is $matrix.os, as exported in GHA *.yaml
# $CONDA (miniconda installation path) is always defined in the GHA virtual environments
case ${CI_OS} in
    windows*)
        eval "$(${CONDA}/condabin/conda.bat shell.bash hook)";;
    *)
        eval "$(${CONDA}/condabin/conda shell.bash hook)";;
esac
