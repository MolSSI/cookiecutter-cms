# $CI_OS is ${{ matrix.os }}, as exported in GHA *.yaml
# $CONDA (miniconda installation path) is always defined in the GHA virtual environments
case ${CI_OS} in
    windows*)
        eval "$(${CONDA}/condabin/conda.bat shell.bash hook)";;
    macOS*)
        eval "$(${CONDA}/condabin/conda shell.bash hook)";;
    *)
        eval "$(conda shell.bash hook)";;
esac

if [[ -d ${CONDA}/envs/test ]] || [[ -d ${HOME}/.conda/envs/test ]]; then
    conda activate test
else
    conda activate
fi
