#!/usr/bin/python3

"""A module that defines AMenities of state of user"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """An Amenity class"""

    name: str = ""
