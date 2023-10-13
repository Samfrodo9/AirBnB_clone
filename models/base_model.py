#!/usr/bin/python3

"""A Module that defines a Base Class"""

from models.__init__ import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A BaseModel class"""

    def __init__(self, *args, **kwargs):
        """An instantiation of the Base Model either created or from a dictionary"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ('created_at', 'updated_at'):
                    # value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f") This will also work
                    value = datetime.fromisoformat(value)  # Parse ISO format datetime
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """A string representation of the Base Model class"""
        # [<class name>] (<self.id>) <self._dict_>
        string = "[" + self.__class__.__name__ + "]"
        string = string + " (" + self.id + ") "
        string = string + str(self.__dict__)
        return string

    def save(self):
        """A method that updates 'updated at' with the current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """A module that returns a dictionary containing key/value of obj instance"""
        attributes = {}
        attributes['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                attributes[key] = value.isoformat()
            else:
                attributes[key] = value

        return attributes
