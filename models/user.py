#!/usr/bin/python3
"""creates a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
