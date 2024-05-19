#!/usr/bin/python3

import unittest
from datetime import datetime, timedelta
from models.user import User


class TestUser(unittest.TestCase):

    def test_create_user(self):
        """Test creating a new user instance"""
        user = User()
        user.email = "john@example.com"
        user.password = "secure_password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "secure_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_set_password(self):
        """Test setting the password for a user"""
        user = User()
        user.password = "new_password"
        self.assertEqual(user.password, "new_password")

    def test_set_name(self):
        """Test setting the first name and last name for a user"""
        user = User()
        user.first_name = "Jane"
        user.last_name = "Smith"
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")

    def test_save(self):
        """Test updating the updated_at attribute"""
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)

    def test_to_dict(self):
        """Test converting a user instance to a dictionary"""
        user = User()
        user.email = "user@example.com"
        user.password = "pass456"
        user.first_name = "Alex"
        user.last_name = "Johnson"
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["password"], "pass456")
        self.assertEqual(user_dict["first_name"], "Alex")
        self.assertEqual(user_dict["last_name"], "Johnson")

    def test_from_dict(self):
        """Test recreating a User instance from a dictionary"""
        user = User()
        user.email = "john@example.com"
        user.password = "secure_password"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        recreated_user = User(**user_dict)
        self.assertEqual(recreated_user.__class__.__name__, "User")
        self.assertEqual(recreated_user.id, user.id)
        self.assertEqual(recreated_user.created_at, user.created_at)
        self.assertEqual(recreated_user.updated_at, user.updated_at)
        self.assertEqual(recreated_user.email, "john@example.com")
        self.assertEqual(recreated_user.password, "secure_password")
        self.assertEqual(recreated_user.first_name, "John")
        self.assertEqual(recreated_user.last_name, "Doe")

    def test_custom_attributes(self):
        """Test converting and recreating an instance with custom attributes"""
        user = User()
        user.email = "user@example.com"
        user.password = "pass456"
        user.first_name = "Alex"
        user.last_name = "Johnson"
        user_dict = user.to_dict()
        recreated_user = User(**user_dict)
        self.assertEqual(recreated_user.email, "user@example.com")
        self.assertEqual(recreated_user.password, "pass456")
        self.assertEqual(recreated_user.first_name, "Alex")
        self.assertEqual(recreated_user.last_name, "Johnson")

    def test_datetime_attributes(self):
        """Test converting and recreating an instance \
              with datetime attributes"""
        created_at = datetime.now()
        updated_at = created_at + timedelta(days=1)
        user = User()
        user.created_at = created_at
        user.updated_at = updated_at
        user_dict = user.to_dict()
        recreated_user = User(**user_dict)
        self.assertEqual(recreated_user.created_at, created_at)
        self.assertEqual(recreated_user.updated_at, updated_at)
