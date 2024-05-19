#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_to_dict(self):
        """Test converting a BaseModel instance to a dictionary"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(
            instance_dict["created_at"], instance.created_at.isoformat()
        )
        self.assertEqual(
            instance_dict["updated_at"], instance.updated_at.isoformat()
        )

    def test_from_dict(self):
        """Test recreating a BaseModel instance from a dictionary"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        recreated_instance = BaseModel(**instance_dict)
        self.assertEqual(recreated_instance.__class__.__name__, "BaseModel")
        self.assertEqual(recreated_instance.id, instance.id)
        self.assertEqual(recreated_instance.created_at, instance.created_at)
        self.assertEqual(recreated_instance.updated_at, instance.updated_at)

    def test_custom_attributes(self):
        """Test converting and recreating an instance with custom attributes"""
        instance = BaseModel()
        instance.custom_attribute = "value"
        instance_dict = instance.to_dict()
        recreated_instance = BaseModel(**instance_dict)
        self.assertEqual(recreated_instance.custom_attribute, "value")

    def test_datetime_attributes(self):
        """Test converting and recreating an instance \
              with datetime attributes"""
        created_at = datetime.now()
        updated_at = created_at + timedelta(days=1)
        instance = BaseModel(
            created_at=created_at.isoformat(),
            updated_at=updated_at.isoformat(),
        )
        instance_dict = instance.to_dict()
        recreated_instance = BaseModel(**instance_dict)
        self.assertEqual(recreated_instance.created_at, created_at)
        self.assertEqual(recreated_instance.updated_at, updated_at)

    def test_custom_subclass(self):
        """Test converting and recreating an instance of a custom subclass"""

        class CustomModel(BaseModel):
            """A custom subclass of BaseModel"""

            pass

        instance = CustomModel()
        instance_dict = instance.to_dict()
        recreated_instance = CustomModel(**instance_dict)
        self.assertEqual(recreated_instance.__class__.__name__, "CustomModel")
