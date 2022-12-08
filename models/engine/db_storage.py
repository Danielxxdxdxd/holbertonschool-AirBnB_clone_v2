#!/usr/bin/python3
""""""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = getenv('HBNB_MYSQL_USER')
        pw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        dir = "mysql+mysqldb://{}:{}@{}/{}"\
            .format(user, pw, host, db)

        self.__engine = create_engine(dir, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            list_class = [State, City, User, Place, Review, Amenity]
            for classes in list_class:
                for obj in self.__session.query(classes).all():
                    dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return dict

    def new(self, obj):
        """"""
        self.__session.add(obj)

    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        data_base_session = sessionmaker(bind=self.__engine,
                                         expire_on_commit=False)
        Session = scoped_session(data_base_session)
        self.__session = Session()

    def close(self):
        """"""
        self.__session.close()
