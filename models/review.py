#!/usr/bin/python3

"""A module that defines review of user"""

from models.base_model import BaseModel

class Review(BaseModel):
	"""A Review class"""
	place_id = ""
	user_id = ""
	text = ""
