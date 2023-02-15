#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'updated_at' or k == 'created_at':
                    self.__dict__[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        #return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        newdict = self.__dict__.copy()
        newdict['__class__'] = type(self).__name__
        #newdict['__class__'] = __class__.__name__
        newdict['created_at'] = newdict['created_at'].isoformat()
        newdict['updated_at'] = newdict['updated_at'].isoformat()
        return newdict

