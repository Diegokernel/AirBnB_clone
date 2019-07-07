#!/usr/bin/python3
'''state class module'''
from models.base_model import BaseModel


class State(BaseModel):
    '''class for state'''
    name = ""

    def __init__(self, *args, **kwargs):
        """__init__ - Method initializer of instance
        args: self
        return: nothing
        """
        super().__init__(self, *args, **kwargs)
