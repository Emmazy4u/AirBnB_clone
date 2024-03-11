#!/usr/bin/python3
"""creates a city class that inherits from BaseModel"""
from models.base_model import BaseMdel


class City(BaseModel):
    """Public class attributes"""

    state_id = ""
    name = ""
