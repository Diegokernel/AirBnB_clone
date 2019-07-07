#!/usr/bin/python3
'''module for city'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City class that inherits from BaseModel class'''
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """__init__ - Method initializer of instance
        args: self
        return: nothing
        """
        super().__init__(self, *args, **kwargs)
