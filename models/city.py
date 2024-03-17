#!/usr/bin/python3
"""Defines a class representing an Amenity."""

# Importing the base model class
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity."""

    def __init__(self):
        """Initialize the Amenity object."""
        super().__init__()
        self.name = ""
