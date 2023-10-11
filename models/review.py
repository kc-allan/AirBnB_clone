#!/usr/bin/python3
""" defines a Review class """

from models.base_model import BaseModel

class Review(BaseModel):
    """ defines a Review class """

    place_id = ""
    user_id = ""
    text = ""
