#!/usr/bin/python3
"""create archive module"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """function to zip files"""
    new_date = datetime.now()
    new_date = new_date.strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions/')
    var = local(f'tar -cvf versions/web_static_{new_date}.tgz web_static/')

    if var.succeeded:
        return 'versions/web_static_' + new_date + '.tgz'
    return None
