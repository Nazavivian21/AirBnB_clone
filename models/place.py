#!/usr/bin/python3

from base_model import BaseModel


class Place(BaseModel):
    """The Place class inherits from BaseModel and defines \
          attributes for a place."""

    def __init__(
        self,
        city_id="",
        user_id="",
        name="",
        description="",
        number_rooms=0,
        number_bathrooms=0,
        max_guest=0,
        price_by_night=0,
        latitude=0.0,
        longitude=0.0,
        amenity_ids=[],
    ):
        """Initializes a new instance of the Place class."""
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

    def __str__(self):
        """Returns a string representation of the Place class."""
        return "[Place] ({}) - Name: {}, City ID: {}, User ID: {}".format(
            self.id, self.name, self.city_id, self.user_id
        )
