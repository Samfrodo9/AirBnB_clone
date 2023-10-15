#!/usr/bin/python3

"""A module that defines review of user"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
