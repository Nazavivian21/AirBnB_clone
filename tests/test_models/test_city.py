#!/usr/bin/python3

"""City unittest module"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_attributes(self):
        """Test City class attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
