#!/usr/bin/python3
""" Module Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class"""
    text = ""
    user_id = ""
    place_id = ""
