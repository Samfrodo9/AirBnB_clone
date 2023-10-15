#!/usr/bin/python3
from models.state import State
from models.base_model import BaseModel

s = State()
print(isinstance(s, BaseModel))