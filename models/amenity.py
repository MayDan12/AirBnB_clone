#!/usr/bin/python3
"""This function Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class Represent an amenity.

    Attributes:
        name (str): This is the name of the amenity.
    """

    name = ""
