#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv


class DBStorage:
    """The Database Storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the class object"""
        self.__engine = create_engine('mysql+mysqldb://'
                                      f'{getenv("HBNB_MYSQL_USER")}:'
                                      f'{getenv("HBNB_MYSQL_PWD")}@'
                                      f'{getenv("HBNB_MYSQL_HOST")}/'
                                      f'{getenv("HBNB_MYSQL_DB")}',
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current session all objects depending
        on the class or not"""
        objs = {}
        if cls is not None:
            cls_objs = self.__session.query(cls).all()
            for obj in cls_objs:
                objs.update({cls + "." + obj.id: obj})
        else:
            cls_objs = self.__session.query("User", "State", "City", "Amenity",
                                            "Place", "Review").all()
            for obj in cls_objs:
                objs.update({obj.__class__.__name__ + "." + obj.id: obj})
        return objs

    def new(self, obj):
        """add new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """closes the session"""
        self.__session.remove()
