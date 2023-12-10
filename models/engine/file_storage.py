#!/usr/bin/python3
"""This function Defines the FileStorage class."""
import json


class FileStorage:
    """
    This class represent an abstracted storage engine.

    Attributes:
        __file_path (str): This is the path of the file where we save objects.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This returns the dictionary __objects. """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects obj with key <obj_class_name>.id """
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """ Serialize __objects to the JSON file __file_path """
        objects = FileStorage.__objects
        obj_dict = {obj: objects[obj].to_dict() for obj in objects.keys()}

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects,
        if it exists
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
