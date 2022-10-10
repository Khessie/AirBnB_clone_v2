#!/usr/bin/python3
from sqlalchemy import create_engine


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        engine = create_engine('mysql+mysql://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/HBNB_MYSQL_DB')