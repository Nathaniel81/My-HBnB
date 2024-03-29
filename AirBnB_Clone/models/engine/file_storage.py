#!/usr/bin/python3

    """_summary_

    Returns:
        _type_: _description_
    """

from json import dump, load
from os.path import exists
#from models.base_model import BaseModel
#from models.user import User

class FileStorage:
    """_summary_

    Returns:
        _type_: _description_
    """

    __file_storage = 'file.json'
    __objects = {}

    def all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return FileStorage.__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        FileStorage.__objects[type(obj).__name__ + '.'+ obj.id] = obj

    def save(self):
        """_summary_
        """

        nwdct = {}
        for k, v in FileStorage.__objects.items():
            nwdct[k] = v.to_dict()
        with open(FileStorage.__file_storage, 'w', encoding='utf8') as f:
            dump(nwdct, f)

    def reload(self):
        """_summary_
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if exists(FileStorage.__file_storage):
            with open(FileStorage.__file_storage) as f:
                dctrep = load(f)
            for v in dctrep.values():
                clsNm = v['__class__']
                del v['__class__']
                obj = eval(clsNm)(**v)
                self.new(obj)
