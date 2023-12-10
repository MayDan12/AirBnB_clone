#!/usr/bin/python3
"""This defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class represent a place.

    Attributeses:
        city_id (str): this is the City id.
        user_id (str): This is the User id.
        name (str): This is the name of the place.
        description (str): This is the description of the place.
        number_rooms (int): This is the number of rooms of the place.
        number_bathrooms (int): This is the number of bathrooms of the place.
        max_guest (int): This is the maximum number of guests of the place.
        price_by_night (int): This is the price by night of the place.
        latitude (float): This is the latitude of the place.
        longitude (float): This is the longitude of the place.
        amenity_ids (list): This is the list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
