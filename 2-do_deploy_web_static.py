#!/usr/bin/python3
"""
Fabric script s
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.73.198.109', '35.231.28.80']


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if exists(archive_path) is False:
        return False
    try:
        file_ext = archive_path.split("/")[1]
        no_ext = file_ext.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/" + no_ext + "/")
        run("sudo tar -xzf /tmp/" + file_ext + " -C " + path + no_ext + "/")
        run("sudo rm /tmp/" + file_ext)
        run("sudo mv /data/web_static/releases/" + no_ext +
            "/web_static/* /data/web_static/releases/" + no_ext + "/")
        run("sudo rm -rf /data/web_static/releases/" + no_ext + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/" + no_ext +
            "/ /data/web_static/current")
        return True
    except:
        return False
