#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """review relationship with place"""
            from models import storage
            objs = storage.all("Review")
            return [value for key, value in objs.items()
                    if value.place_id == Place.id]

        @property
        def amenities(self):
            """return the list of all instances on amenities"""
            from models import storage
            objs = storage.all("Amenity")
            return [key for key in objs.keys() if key in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj=None):
            """append all Amenity instances"""
            if type(obj).__name__ == 'Amenity':
                new_amenity = 'Amenity' + '.' + obj.id
                self.amenity_ids.append(new_amenity)
