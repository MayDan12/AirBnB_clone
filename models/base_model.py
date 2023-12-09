#!/usr/bin/python 3

import uuid
from datetime import datetime
"""
    This import the datetime modules to get the date
"""

class BaseModel:
    """This BaseModel class will serve as the base for other classes"""
    def __init__(self, *args, **kwargs):
        """
            The __init__ method initializes instances of the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """This returns a representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """The save method updates the updated ate attribute to the current date and time wheever itis called"""
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
