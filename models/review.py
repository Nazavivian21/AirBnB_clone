#!/usr/bin/python3

from base_model import BaseModel


class Review(BaseModel):
    """The Review class inherits from BaseModel and defines \
        attributes for a review."""

    def __init__(self, place_id="", user_id="", text=""):
        """Initializes a new instance of the Review class."""
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def __str__(self):
        """Returns a string representation of the Review class."""
        return "[Review] ({}) - Place ID: {}, User ID: {}, Text: {}".format(
            self.id, self.place_id, self.user_id, self.text
        )
