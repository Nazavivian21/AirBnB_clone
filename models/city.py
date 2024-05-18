#!/usr/bin/python3

from base_model import BaseModel


class City(BaseModel):
    """The City class inherits from BaseModel and defines \
          attributes for a city."""

    def __init__(self, state_id="", name=""):
        """Initializes a new instance of the City class."""
        super().__init__()
        self.state_id = state_id
        self.name = name

    def __str__(self):
        """Returns a string representation of the City class."""
        return "[City] ({}) - Name: {}, State ID: {}".format(
            self.id, self.name, self.state_id
        )
