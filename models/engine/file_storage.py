#!/usr/bin/python3


import json
import os


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    _file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """
        This method sets in dictionary __objects
        the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to _objects
        (only if the JSON file (_file_path) exists).
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**value)
