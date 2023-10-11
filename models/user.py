#!/usr/bin/python3
""" defines user class """

from models.base_model import BaseModel

class User(BaseModel):
    """ defines a class User that inherits from BaseModel """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
