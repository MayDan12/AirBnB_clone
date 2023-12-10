#!/usr/bin/python3
"""This function defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represent a review.

    Attributes:
        place_id (str): This is the Place id.
        user_id (str): This is the User id.
        text (str): This is the text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
