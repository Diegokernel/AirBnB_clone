#!/usr/bin/python3
'''module for Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class inherits from BaseModel'''
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """__init__ - Method initializer of instance
        args: self
        return: nothing
        """
        super().__init__(self, *args, **kwargs)
