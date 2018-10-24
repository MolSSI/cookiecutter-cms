import os
try:
    from conda_build import api
    from conda_build.environ import create_env
except ImportError as e:
    e.msg += "\nNote:\n"
    e.msg += "-------\n"
    e.msg += "\nYou need to make sure that 'conda-build' is installed:"
    e.msg += "\n    hint ---> `conda install conda-build`"
    raise

def setup_dev_env(ask):
    # grab metadata (assume a simple setup with one build variant)
    metadata = api.render(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conda-recipe'))[0][0]

    # use the package name to create the env name
    pkg_name = metadata.get_value('package/name')
    env_name = pkg_name + '-dev'

    deps = metadata.get_value('requirements/run') + metadata.get_value('test/requires')
    env_prefix = os.path.join(os.environ['CONDA_PREFIX'], 'envs', env_name)
    print("A development environment {} will be set up for you,".format(env_name))
    print("    at prefix ({}),".format(env_prefix))
    print("    with packages [{}],".format(", ".join(deps)))
    print("If this environment already exists it will be updated as needed to fulfill these dependencies.")
    if ask:
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
        while not answer.startswith(('y','n')):
            print("{} is not valid, please answer 'yes' or 'no'")
            answer = question()
        if answer.startswith('n'):
            return
    create_env(
            env_prefix,
            deps,
            env=env_name,
            config=metadata.config,
            subdir=metadata.config.subdir)

if __name__ == '__main__':
    setup_dev_env(True)

