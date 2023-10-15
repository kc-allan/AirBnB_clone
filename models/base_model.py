#!/usr/bin/python3
""" defines all common attributes/methods for other classes """

from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):

        DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                            value, DATE_TIME_FORMAT)

                elif key[0] =="id":
                    self.__dict__[key] = str(value)

                else:
                    self.__dict__[key] = value

    def __str__(self):

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        mp_objects = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                mp_objects[key] = value.isoformat()

            else:
                mp_objects[key] = value

        mp_objects["__class__"] = self.__class__.__name__
        
        return mp_objects
    
