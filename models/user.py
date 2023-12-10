#!/usr/bin/python3
"""This function defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represent a User.

    Attributes:
        email (str): This is the email of the user.
        password (str): This is the password of the user.
        first_name (str): This is the first name of the user.
        last_name (str): This is the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
