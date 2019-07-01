#!/usr/bin/python3
"""file_strorage | AirBnB_clone
This module storage  classs for that serializes instances to a JSON
fle and deserializes JSON file to instances.
"""
from json import dumps, loads
from os import path
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
    to instances
    Attributes:
    - Class: __nb_objects.
    Methods: __init__."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all - returns the dictionary __objects.
        Args: nothing.
        Return: returns the dictionary __objects."""

        return FileStorage.__objects

    def new(self, obj):
        """new - sets in __objects the obj with key <obj class name>.id
        Args:
        - obj: object created.
        Return: nothing"""

        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """save - serializes __objects to the JSON file
        Args: nothing.
        Return: nothing"""
        return_dict = {}
        objects = FileStorage.__objects

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            for obj in objects:
                return_dict[obj] = objects[obj].to_dict()
            file.write(dumps(return_dict))

    def reload(self):
        """reload - deserializes the JSON file to __objects
        Args: nothing.
        Return: returns the dictionary __objects."""

        if not path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
            content_file = file.read()  # In this case, return string of dict.
            content_deserialized = loads(content_file)  # Result = dict
            print(type(content_deserialized))

            for key in content_deserialized:
                dict_value = content_deserialized[key]
                name_class = dict_value["__class__"]
                new_obj = eval(name_class)(**dict_value)
                FileStorage.__objects[key] = new_obj
