#!/usr/bin/python3


"""BaseModel unittest module"""


import unittest
from models.base_model import BaseModel
import datetime
import json


class TestBaseModel(unittest.TestCase):
    """ BaseModel unittest class"""

    def setUp(self):
        """
        Initializes the TestBaseModel class by creating an instance of the
        BaseModel class and assigning a name attribute to it.
        This method is called before each test case is run
        """
        self.base_obj = BaseModel()
        self.base_obj.name = "Benedict Abudu"

    def tearDown(self):
        """
        Removes the instance of the BaseModel class stored in the `base_obj`
        attribute. This method is called after each test case is run.
        """
        del self.base_obj

    def test_instantiation(self):
        """
            Checks that an instance  is created.
        """
        self.assertIsInstance(self.base_obj, BaseModel)
        self.assertEqual("Benedict Abudu", self.base_obj.name)
        self.assertTrue(hasattr(self.base_obj, 'id'))
        self.assertTrue(hasattr(self.base_obj, 'created_at'))
        self.assertTrue(hasattr(self.base_obj, 'updated_at'))
        self.assertTrue(hasattr(self.base_obj, 'name'))

    def test_id(self):
        """
            Checks the id of the instance.
        """
        self.assertIsNotNone(self.base_obj.id)
        self.assertEqual("<class 'str'>", str(type(self.base_obj.id)))
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.base_obj.id)

    def test_updated_created_time(self):
        """
            Check the created_at and updated_at attributes.
        """
        self.assertIsNotNone(self.base_obj.created_at)
        self.assertIsNotNone(self.base_obj.updated_at)
        self.assertEqual("<class 'datetime.datetime'>",
                         str(type(self.base_obj.created_at)))
        self.assertEqual(self.base_obj.updated_at.year,
                         self.base_obj.created_at.year)

    def test_updated_created_diff(self):
        """
        Check if updated_at attribute changes after being saved
        """
        self.base_obj.save()
        self.assertEqual("<class 'datetime.datetime'>",
                         str(type(self.base_obj.updated_at)))
        self.assertNotEqual(self.base_obj.updated_at, self.base_obj.created_at)

    def test_str(self):
        """Test the string representation of the object"""
        self.assertTrue(str(self.base_obj).startswith('[BaseModel]'))
        self.assertIn(self.base_obj.id, str(self.base_obj))
        self.assertIn(str(self.base_obj.__dict__), str(self.base_obj))

    def test_to_dict(self):
        """
            Checks the to_dict method of the BaseModel class.
        """
        self.assertIsInstance(self.base_obj.to_dict(), dict)
        self.assertEqual("BaseModel", (self.base_obj.to_dict())["__class__"])
        self.assertEqual("<class 'str'>",
                         str(type((self.base_obj.to_dict())["created_at"])))
        self.assertEqual("<class 'str'>",
                         str(type((self.base_obj.to_dict())["updated_at"])))

    def test_kwargs_instance_creation(self):
        """
            Checks that a new BaseModel instance is created using kwargs.
        """
        base_obj_dict = self.base_obj.to_dict()
        new_base_model = BaseModel(**base_obj_dict)
        self.assertEqual(new_base_model.id, self.base_obj.id)
        self.assertTrue(isinstance(new_base_model.created_at,
                        datetime.datetime))
        self.assertTrue(isinstance(new_base_model.updated_at,
                        datetime.datetime))
        new_base_model_dict = new_base_model.to_dict()
        self.assertEqual(base_obj_dict, new_base_model_dict)

    def test_serialization_deserialization(self):
        """
        Test serialization and deserialization of BaseModel instances.
        """
        base_obj_json = json.dumps(self.base_obj.to_dict())
        deserialized_obj = BaseModel(**json.loads(base_obj_json))

        self.assertEqual(deserialized_obj.id, self.base_obj.id)
        self.assertEqual(deserialized_obj.created_at, self.base_obj.created_at)
        self.assertEqual(deserialized_obj.updated_at, self.base_obj.updated_at)
        self.assertEqual(deserialized_obj.name, self.base_obj.name)
