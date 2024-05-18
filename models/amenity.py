#!/usr/bin/python3

from base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity class inherits from BaseModel and defines \
        attributes for an amenity."""

    def __init__(self, name=""):
        """Initializes a new instance of the Amenity class."""
        super().__init__()
        self.name = name

    def __str__(self):
        """Returns a string representation of the Amenity class."""
        return "[Amenity] ({}) - Name: {}".format(self.id, self.name)
