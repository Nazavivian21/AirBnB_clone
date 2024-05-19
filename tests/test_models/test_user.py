import unittest
from datetime import datetime
from time import sleep
from user import User


class TestUser(unittest.TestCase):
    def test_create_user(self):
        """Test creating a new user instance"""
        user = User(
            email="john@example.com",
            password="secure_password",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "secure_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_set_password(self):
        """Test setting the password for a user"""
        user = User()
        user.set_password("new_password")
        self.assertEqual(user.password, "new_password")

    def test_set_name(self):
        """Test setting the first name and last name for a user"""
        user = User()
        user.set_name("Jane", "Smith")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")

    def test_str(self):
        """Test the string representation of a user"""
        user = User(
            email="jane@example.com",
            password="pass123",
            first_name="Jane",
            last_name="Smith",
        )
        expected_str = "[User] ({}) - Email: jane@example.com,\
              First Name: Jane, Last Name: Smith".format(
            user.id
        )
        self.assertEqual(str(user), expected_str)

    def test_save(self):
        """Test updating the updated_at attribute"""
        user = User()
        original_updated_at = user.updated_at
        sleep(1)
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)

    def test_to_dict(self):
        """Test converting a user instance to a dictionary"""
        user = User(
            email="user@example.com",
            password="pass456",
            first_name="Alex",
            last_name="Johnson",
        )
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["password"], "pass456")
        self.assertEqual(user_dict["first_name"], "Alex")
        self.assertEqual(user_dict["last_name"], "Johnson")
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())

    def test_from_dict(self):
        """Test recreating a User instance from a dictionary"""
        user = User(
            email="user@example.com",
            password="pass456",
            first_name="Alex",
            last_name="Johnson",
        )
        user_dict = user.to_dict()
        recreated_user = User(**user_dict)
        self.assertEqual(recreated_user.__class__.__name__, "User")
        self.assertEqual(recreated_user.id, user.id)
        self.assertEqual(recreated_user.created_at, user.created_at)
        self.assertEqual(recreated_user.updated_at, user.updated_at)
        self.assertEqual(recreated_user.email, user.email)
        self.assertEqual(recreated_user.password, user.password)
        self.assertEqual(recreated_user.first_name, user.first_name)
        self.assertEqual(recreated_user.last_name, user.last_name)

    def test_custom_attributes(self):
        """Test converting and recreating an instance with custom attributes"""
        user = User()
        user.custom_attribute = "value"
        user_dict = user.to_dict()
        recreated_user = User(**user_dict)
        self.assertEqual(recreated_user.custom_attribute, "value")

    def test_datetime_attributes(self):
        """Test converting and recreating an \
            instance with datetime attributes"""
        created_at = datetime.now()
        updated_at = created_at + timedelta(days=1)
        user = User(
            created_at=created_at.isoformat(),
            updated_at=updated_at.isoformat(),
        )
        user_dict = user.to_dict()
        recreated_user = User(**user_dict)
        self.assertEqual(recreated_user.created_at, created_at)
        self.assertEqual(recreated_user.updated_at, updated_at)
