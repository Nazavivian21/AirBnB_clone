#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from base_model import BaseModel


class User(BaseModel):
    """The User class inherits from BaseModel and defines attributes for a user."""

    def __init__(self, email="", password="", first_name="", last_name=""):
        """Initializes a new instance of the User class."""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """Returns a string representation of the User class."""
        return "[User] ({}) - Email: {}, First Name: {}, Last Name: {}".format(
            self.id, self.email, self.first_name, self.last_name
        )

    def set_password(self, password):
        """Sets the password for the user."""
        self.password = password

    def set_name(self, first_name, last_name):
        """Sets the first name and last name for the user."""
        self.first_name = first_name
        self.last_name = last_name
