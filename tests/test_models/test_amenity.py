#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """Test Amenity class attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
