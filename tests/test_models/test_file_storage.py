#!/usr/bin/python3


"""FileStorage unittest module"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.test_file = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file

    def tearDown(self):
        """Clean up after the tests"""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        """Test that new adds an object to __objects"""
        user = User()
        self.storage.new(user)
        key = "User." + user.id
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], user)

    def test_save(self):
        """Test that save properly serializes objects to file"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        key = "User." + user.id
        self.assertIn(key, data)
        self.assertEqual(data[key]['__class__'], 'User')
        self.assertEqual(data[key]['id'], user.id)

    def test_reload(self):
        """Test that reload properly deserializes objects from file"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = "User." + user.id
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, user.id)
        self.assertEqual(self.storage.all()[key].__class__.__name__, 'User')

    def test_reload_no_file(self):
        """Test that reload does nothing if file does not exist"""
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_invalid_file(self):
        """Test reload with invalid JSON file"""
        with open(self.test_file, 'w') as f:
            f.write("not a json")
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    def test_save_empty(self):
        """Test save with no objects in storage"""
        self.storage.save()
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, {})

    def test_eval(self):
        """Test that eval recreates correct class instances"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = "User." + user.id
        self.assertIsInstance(self.storage.all()[key], User)
