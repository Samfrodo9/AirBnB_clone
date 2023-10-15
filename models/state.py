#!/usr/bin/python3

"""A module that defines state of user"""

from models.base_model import BaseModel


class State(BaseModel):
    """A state class"""

    name: str = ""
