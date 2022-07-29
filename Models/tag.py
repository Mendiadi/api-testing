from Models.base_obj import BaseObject

class Tag(BaseObject):

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    def __init__(self):
        self._id = 1
        self._name = ""