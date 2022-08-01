from Models.base_obj import BaseObject

class Tag(BaseObject):

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


    def __init__(self,id:int,name:str):
        self._id = id
        self._name = name