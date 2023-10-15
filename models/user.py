#!/usr/bin/python3
"""
A module user that defines user properties
"""


from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """
    User Defines user properties

    Args:
                    BaseModel (Class): Base class of AIR BNB

    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
