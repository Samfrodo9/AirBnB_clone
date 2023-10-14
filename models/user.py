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

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User attributes"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation of User Class"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def to_dict(self):
        """Convert User instance to a dictionary."""
        user_dict = super().to_dict()  # Get the dictionary from the base class
        user_dict["email"] = self.email
        user_dict["password"] = self.password
        user_dict["first_name"] = self.first_name
        user_dict["last_name"] = self.last_name

        return user_dict
