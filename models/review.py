#!/usr/bin/python3
"""creates a review class that inherits from BaseModel"""
from models.base_model import BaseModels


class Review(BaseModel):
    """Public class attributes"""

    place_id = ""
    user_id = ""
    text = ""
