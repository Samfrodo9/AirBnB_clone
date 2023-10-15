#!/usr/bin/python3

"""A module that defines city of user"""

from models.base_model import BaseModel


class City(BaseModel):
    """A city class definition"""

    state_id = ""
    name = ""
