#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes(self):
        """Test State class attributes"""
        state = State()
        self.assertEqual(state.name, "")
