#!/usr/bin/python3

import json
import os
"""
this moduleis responsible for serializing instances to a JSON file
and deserializing a JSON file to instances.
"""


class FileStorage:
    """that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists """
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(self.__file_path, 'r') as file:
            data = json.load(file)
            obj_dict = {
                    key: self.get_class_by_name()[value["__class__"]](**value)
                    for key, value in data.items()}
            self.__objects = obj_dict

    def get_class_by_name(self):
        """Returns the class type based on the class name."""

        from models.base_model import BaseModel

        class_mapping = {
            'BaseModel': BaseModel,
        }
        return class_mapping
