#!/usr/bin/python3
""" Defines the Amenityy class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity
    Attributes:
    name (str): The name of the amenity.
    """

    name = ""
