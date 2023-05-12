#!/usr/bin/python
""" This Fabric script  distributes an archive to
your web servers, using the function do_deploy """
from fabric.api import *
import os

env.hosts = ["100.25.45.246", "54.236.26.56"]
use_sudo = True


def do_deploy(archive_path):
    """ This funcyion deploys an archive to a server """
    if os.path.exists(archive_path):
        try:
            myFile = archive_path.split("/")
            myFile = myFile[-1]
            newFile = myFile.strip(".tgz")
            sudo("touch /tmp/{}".myFile)
            put(archive_path, "/tmp/{}".format(myFile))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(myFile, newFile))
            run("rm /tmp/{}".format(myFile))
            run(rm -rf /data/web_static/current)
            run("ln -sf /data/web_static/releases/{}./data/web_static/current".format(newFile))
            return True
        except Exception as e:
            return False
    else:
        return False
