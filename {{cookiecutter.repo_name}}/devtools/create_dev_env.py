import os
import argparse
from pathlib import Path
from conda.common.serialize import yaml_load
from conda_env.pip_util import pip_args
import subprocess as sp
try:
    from conda_build import api
    from conda_build.environ import create_env
    from conda_build.config import Config
    from conda_build.conda_interface import url_path
except ImportError as e:
    e.msg += "\nNote:\n"
    e.msg += "-------\n"
    e.msg += "\nYou need to make sure that 'conda-build' is installed:"
    e.msg += "\n    hint ---> `conda install conda-build`"
    raise

def ask_yn():
    def question():
        prompt = "Continue? [Y/n]"
        try:
            return raw_input(prompt).lower() or 'y'
        except KeyboardInterrupt:
            print('')
            return 'n'
        except NameError:
            return input(prompt).lower() or 'y'

    answer = question()
    while not answer.startswith(('y', 'n')):
        print("{} is not valid, please answer 'yes' or 'no'")
        answer = question()
    if answer.startswith('n'):
        return False
    else:
        return True


parser = argparse.ArgumentParser(
    description=
    "Creates a conda environment with the specified python version, and the run/test requirements of the provided recipe"
)

parser.add_argument("-n", "--name", type=str, help="The name of the environment, existing environments will be updated")
parser.add_argument("-p", "--python", type=str, help="The version of python to be installed in environment")
parser.add_argument("-c", "--channel", type=str, nargs="+", help="Additional channel(s) to search for packages (searched in order given, before defaults)")
parser.add_argument("-y", "--yes", dest='ask', action='store_false')
parser.add_argument("--file", type=str, help="An environment file (yaml) from which additional packages will be taken")
parser.add_argument("recipe_path", type=str, help="The path to the recipe that will be used")

parser.set_defaults(ask=True)


def setup_dev_env(args):
    # grab metadata (assume a simple setup with one build variant)

    print(args.__dict__)

    name = None
    channels = args.channel if args.channel else []
    deps = []
    pip_deps = []

    if args.file:
        args_yaml = yaml_load(Path(args.file).read_text())
        name = args_yaml.get('name', name)
        pip_deps = []
        for dep in args_yaml['dependencies']:
            if isinstance(dep, type(args_yaml)):
                pip_deps.extend(dep.get('pip', []))
                deps.append('pip')
            else:
                deps.append(dep)
        channels = args_yaml.get('channels', channels)


    # merge the channels arg and channels from the file if given/present
    config = Config()
    config.channel_urls = []
    for url in channels:
        if os.path.isdir(url):
            url = url_path(str(Path(url).resolve()))
        config.channel_urls.append(url)

    # Determine the env name: priority cli_flag > env.yaml > "test" (default)
    name = args.name or name or 'test'

    # Parse recipe metadata
    recipe = api.render(args.recipe_path, config=config)[0][0]

    # Merge deps in the env file with those from the recipe, remove dups
    deps = deps + recipe.get_value('requirements/run') + recipe.get_value('test/requires')

    # Set the python version
    if args.python:
        py_i = deps.index('python')
        deps[py_i] = "python {}".format(args.python)

    print("CONDA ENV NAME  {}".format(name))
    print("PYTHON VERSION  {}".format(args.python or '<default>'))
    print("CONDA FILE NAME {}".format(args.file or '<none>'))
    print("CONDA PATH      {}".format(os.environ['CONDA_PREFIX']))
    print("CONDA PACKAGES  {}".format(deps))
    print("CONDA CHANNELS  {}".format(channels))
    print("PIP PACKAGES    {}".format(pip_deps))
    if args.ask:
        if not ask_yn():
            return
    env_prefix = os.path.join(os.environ['CONDA_PREFIX'], 'envs', name)
    create_env(env_prefix, deps, env=name, config=recipe.config, subdir=recipe.config.subdir)

    if pip_deps:
        pip_invoke, _  = pip_args(env_prefix)
        for pkg in pip_deps:
            sp.run(pip_invoke + ["install", pkg], check=True)

    # we are done.



if __name__ == '__main__':
    args = parser.parse_args()
    setup_dev_env(args)
