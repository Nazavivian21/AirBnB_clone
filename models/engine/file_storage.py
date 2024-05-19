#!/usr/bin/python3

"""FileStorage class module"""
import json
import models


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
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
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to _objects
        (only if the JSON file (_file_path) exists).
        """
         try:
             with open(FileStorage.__file_path, encoding="UTF8") as f:
                 FileStorage.__objects = json.load(f)
             for key, val in FileStorage.__objects.items():
                 clss_name = val["__class__"]
                 clss_name = models.classes[class_name]
                 FileStorage.__objects[key] = class_name(**val)
         except FileNotFoundError:
             pass
