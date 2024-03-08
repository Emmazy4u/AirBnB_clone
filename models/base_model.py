#!/usr/bin/python3
"""The base model of the AirBnB project"""


import uuid
from datetime import datetime

class BaseModel:
    """
    parent class for taking care of initialization,
    serialization and deserialization of instances
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """prints customized string formated output"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """would update the public instance attr 'updated_at'"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containg keys/vaalues of __dict__
        of the instance
        """
        inst_dict_cpy = self.__dict__.copy()
        inst_dict_cpy["__class__"] = self.__class__.__name__
        inst_dict_cpy["created_at"] = self.created_at.isoformat()
        inst_dict_cpy["updated_at"] = self.updated_at.isoformat()
        return inst_dict_cpy

    def to_json(self):
        """implement saving logic for console"""
        pass
