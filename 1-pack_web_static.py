#!/usr/bin/python3
"""create archive module"""
from genericpath import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """function to zip files"""
    new_date = datetime.now()
    new_date = new_date.strftime('%Y%m%d%H%M%S')
    if isdir('versions') is False:
        local('mkdir versions')
    print(f"Packing web_static to versions/web_static_{new_date}.tgz")
    var = local(f'tar -cvzf versions/web_static_{new_date}.tgz web_static')

    if var.succeeded:
        return f'versions/web_static_{new_date}.tgz'
    return None
