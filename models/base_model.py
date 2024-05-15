#!/usr/bin/python3


"""Defines the BaseModel class."""
from datetime import datetime
import uuid


class BaseModel:
    """The BaseModel class defines all common attributes for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if kwargs:
            pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel class."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel class."""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print(
        "\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]
        )
    )
