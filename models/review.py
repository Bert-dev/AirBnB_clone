#!/usr/bin/python3
""" Define the review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represent a Review

    Attributes:
    place_id (str): The place id.
    user_id (str): The User id.
    text (str): The text of te review.
    """

    place_id = ""
    user_id = ""
    text = ""
