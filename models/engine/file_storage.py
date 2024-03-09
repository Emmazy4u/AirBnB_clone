#!/usr/bin/python3
"""Handling all the file storage requirements as well as
serialization and deserialization functions
"""


from models.base_model import BaseModel
import os
import json

class FileStorage:
    """class that serializes instances to a JSON file 
    and deserializes JSON file to instances
    """
    #path to Jsonfile
    __file_path = "file.json"
    #empty but stores all obj by <class name>.id
    __objects = {}
    def all(self):
        """returns the __objects dictionary"""
        return (FileStorage.__objects)
    def new(self, obj):
        """inputs obj into the __objects dictionary 
        using the format <obj class name>.id
        """
        #obtaining the class name
        cls_name_of_obj = obj.__class__.__name__
        obj_key = "{}.{}".format(cls_name_of_obj, obj.id)
        FileStorage.__objects[obj_key] = obj
    def save(self):
        """serializes __objects to the JSON 
        file path: __file_path
        """
        temp_obj_bank = FileStorage.__objects
        obj_as_dict = {} #initially empty
        for key in temp_obj_bank.keys():
            obj_as_dict = temp_obj_bank[key].to_dict()
        with open (FileStorage.__file_path, "w+", encoding="utf-8") as json_file:
            json.dump(obj_as_dict, json_file)
    def reload(self):
        """deserializes the JSON file to __objects if the __file_path exist,
        else do nothing, no exceptions
        """
        if os.path.isfile(FileStorage.__file_path):
            file_path = FileStorage.__file_path
            with open(file_path, "r", encoding="utf-8") as json_file:
                try:
                   obj_as_dict = json.load(json_file)
                   for obj_item in obj_as_dict.values():
                       class_name = obj_item["__class__"]
                       #Since we are creating object instances the attribute 
                       #__class__ should not be supplied as part of the 
                       #arguments to the init function of the class(identified 
                       #by class_name) all the other arguments are valid.
                       del obj_item["__class__"]
                       #Use the previously defined new function to create a new 
                       #__obj. The double asterics expands the dictionary to 
                       #allow every key value pair from object_item dict to be 
                       #passed to the __init__() method of the class identified 
                       #by class_name
                       self.new(eval(class_name)(**obj_item))
                except Exception:
                    pass
