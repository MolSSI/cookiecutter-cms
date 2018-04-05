"""
Runs arbitrary YAML commands
"""

from subprocess import check_output 
import os
import sys
import yaml


def parse_yaml(filename, key):
    """
    Opens a YAML file.
    """

    with open(filename, "r") as infile:
        ret = yaml.load(infile) 

    return ret[key]


def run_commands(commands):
    """
    Runs YAML commands and prints their output
    """
    
    for command in commands:
        command_list = [os.path.expandvars(x) for x in command.split()]
        print("Running command: %s\n" % " ".join(command_list))
        print(check_output(command_list).decode("UTF-8"))

if __name__ == "__main__":
    filename = sys.argv[1]
    key = sys.argv[2]

    commands = parse_yaml(filename, key)
    run_commands(commands)
