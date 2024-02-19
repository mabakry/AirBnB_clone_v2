#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        DB_USER = getenv('HBNB_MYSQL_USER')
        DB_PASS = getenv('HBNB_MYSQL_PWD')
        DB_HOST = getenv('HBNB_MYSQL_HOST')
        DB_NAME = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                .format(DB_USER, DB_PASS, DB_HOST, DB_NAME),
                                pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        classes = [User, State, City, Amenity, Place, Review]
        resault_dict = {}
        for this_class in classes:
            if cls is None or cls is this_class:
                objs = self.__session.query(this_class).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    resault_dict[key] = obj
        return (resault_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
