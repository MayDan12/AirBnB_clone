#!/usr/bin/python3
"""This defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This class represents the BaseModel of the project."""

    def __init__(self, *args, **kwargs):
        """
        This initialize a new BaseModel.

        Args:
            *args (any): this tuple of arguments
            **kwargs (dict): This is the Key/value pairs of attributes.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """ This Update updated_at with the current datetime and save """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ The dictionnary representation of the BaseModel """
        dict_repr = self.__dict__.copy()
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        dict_repr["__class__"] = self.__class__.__name__
        return dict_repr

    def __str__(self):
        """ The string representation of the BaseModel instance """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
