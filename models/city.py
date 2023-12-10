#!/usr/bin/python3
"""This function defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """This class represent a city.

    Attributes:
        state_id (str): This is the state id.
        name (str): This is the name of the city.
    """

    state_id = ""
    name = ""
