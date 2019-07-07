#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    '''class for User'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """__init__ - Method initializer of instance
        args: self
        return: nothing
        """
        super().__init__(self, *args, **kwargs)
