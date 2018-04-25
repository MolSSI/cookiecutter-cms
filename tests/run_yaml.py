"""
Runs arbitrary YAML commands
"""

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


def gen_commands(name, commands):
    """
    Runs YAML commands and prints their output
    """
  
    print("Generating bash file to run the following:") 
    ret = []
    for command in commands:
        command = " ".join([os.path.expandvars(x) for x in command.split()])
        print("  %s" % command)
        ret.append(command)

    ret = "\n".join(ret)
    with open(name, "w") as ofile:
        ofile.write(ret)
    

if __name__ == "__main__":
    filename = sys.argv[1]
    key = sys.argv[2]
    out_name = sys.argv[3]

    commands = parse_yaml(filename, key)
    gen_commands(out_name, commands)
