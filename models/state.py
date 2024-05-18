#!/usr/bin/python3
from base_model import BaseModel


class State(BaseModel):
    """The State class inherits from BaseModel and defines \
          attributes for a state."""

    def __init__(self, name=""):
        """Initializes a new instance of the State class."""
        super().__init__()
        self.name = name

    def __str__(self):
        """Returns a string representation of the State class."""
        return "[State] ({}) - Name: {}".format(self.id, self.name)
