#!/usr/bin/python3
""" Fabric script that deletes out-of-date archives, using function do_clean"""
import os
from fabric.api import cd, lcd, run, env, local

env.hosts = ["34.207.63.58", "3.90.81.96"]


def do_clean(number=0):
    """Delete all unnecessary archives (all archives minus the number to keep)
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
