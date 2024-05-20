#!/usr/bin/python3


"""BaseModel unittest module"""
import unittest
from models.base_model import BaseModel
import datetime
import json


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Setup method to create an instance of BaseModel before each test"""
        self.base_obj = BaseModel()
        self.base_obj.name = "Benedict Abudu"

    def tearDown(self):
        """Teardown method to remove the instance of BaseModel after each test"""
        del self.base_obj

    def test_instantiation(self):
        """Test if BaseModel instance is correctly initialized"""
        self.assertIsInstance(self.base_obj, BaseModel)
        self.assertEqual("Benedict Abudu", self.base_obj.name)
        self.assertTrue(hasattr(self.base_obj, 'id'))
        self.assertTrue(hasattr(self.base_obj, 'created_at'))
        self.assertTrue(hasattr(self.base_obj, 'updated_at'))
        self.assertTrue(hasattr(self.base_obj, 'name'))

    def test_id_and_time_attributes(self):
        """Test if id, created_at, and updated_at attributes are correctly initialized"""
        self.assertIsNotNone(self.base_obj.id)
        self.assertEqual("<class 'str'>", str(type(self.base_obj.id)))
        self.assertIsNotNone(self.base_obj.created_at)
        self.assertIsNotNone(self.base_obj.updated_at)
        self.assertEqual("<class 'datetime.datetime'>", str(type(self.base_obj.created_at)))
        self.assertEqual("<class 'datetime.datetime'>", str(type(self.base_obj.updated_at)))
        self.assertEqual(self.base_obj.updated_at.year, self.base_obj.created_at.year)

    def test_updated_at_on_save(self):
        """Test if updated_at attribute is updated on calling the save method"""
        original_updated_at = self.base_obj.updated_at
        self.base_obj.save()
        self.assertNotEqual(self.base_obj.updated_at, original_updated_at)

    def test_str_representation(self):
        """Test the string representation of the BaseModel instance"""
        expected_str = "[BaseModel] ({}) {}".format(self.base_obj.id, self.base_obj.__dict__)
        self.assertEqual(str(self.base_obj), expected_str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        base_dict = self.base_obj.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)
        self.assertIn('name', base_dict)
        self.assertEqual("<class 'str'>", str(type(base_dict['created_at'])))
        self.assertEqual("<class 'str'>", str(type(base_dict['updated_at'])))

    def test_kwargs_instance_creation(self):
        """Test if a new BaseModel instance can be created using kwargs"""
        base_obj_dict = self.base_obj.to_dict()
        new_base_model = BaseModel(**base_obj_dict)
        self.assertEqual(new_base_model.id, self.base_obj.id)
        self.assertTrue(isinstance(new_base_model.created_at, datetime.datetime))
        self.assertTrue(isinstance(new_base_model.updated_at, datetime.datetime))
        new_base_model_dict = new_base_model.to_dict()
        self.assertEqual(base_obj_dict, new_base_model_dict)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization of BaseModel instances"""
        base_obj_json = json.dumps(self.base_obj.to_dict())
        deserialized_obj = BaseModel(**json.loads(base_obj_json))

        self.assertEqual(deserialized_obj.id, self.base_obj.id)
        self.assertEqual(deserialized_obj.created_at, self.base_obj.created_at)
        self.assertEqual(deserialized_obj.updated_at, self.base_obj.updated_at)
        self.assertEqual(deserialized_obj.name, self.base_obj.name)
