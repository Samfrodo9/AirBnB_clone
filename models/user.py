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
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
	
    def to_dict(self):
        """A module that returns a dictionary containing key/value of obj instance"""
        attributes = {}
        attributes['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                if value == "":
                    continue
                else:
                    attributes[key] = value.isoformat()
            else:
                if value == "":
                    continue
                else:
                    attributes[key] = value

        return attributes
