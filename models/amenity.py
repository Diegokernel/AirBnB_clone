#!/usr/bin/python3
"""module for amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """__init__ - Method initializer of instance
        args: self
        return: nothing
        """
        super().__init__(self, *args, **kwargs)
