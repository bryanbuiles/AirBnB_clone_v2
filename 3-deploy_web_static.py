#!/usr/bin/python3
"""
Fabric script s
"""

from datetime import datetime
from fabric.api import put, run, env, local
from os.path import exists, isdir
env.hosts = ['34.73.198.109', '35.231.28.80']


def do_pack():
    """tbz"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


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


def deploy():
    """ creates and distributes an archive to your web servers """
    zip_file = do_pack()
    if zip_file is None:
        return False
    else:
        return do_deploy(zip_file)
