#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
import models

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place',cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
    
    @property
    def reviews(self):
        """ Return the list of Reviews by Place """
        from models import storage
        reviews_by_place = []
        for rev in storage.all(Review).values():
            if rev.place_id == self.id:
                reviews_by_place.append(rev)
        return reviews_by_place
