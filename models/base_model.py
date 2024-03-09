#!/usr/bin/python4
"""The base model of the AirBnB project"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    parent class for representing the BaseMOdel for
    the HBnB project.
    """

    def __init__(self, *args, **kwargs):
        """Instantiating the BaseModel."""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key in ["updated_at", "created_at"]:
                    setattr(self, key, datetime.strptime(val, time_format))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())

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
