from Models.base_obj import BaseObject

class Tag(BaseObject):

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


    def __init__(self,id:int,name:str):
        if not isinstance(id,int):
            raise TypeError("id not integer")
        if not isinstance(name,str):
            raise TypeError("name not string")
        self._id = id
        self._name = name