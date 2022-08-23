from Models.base_obj import BaseObject


class Category(BaseObject):

    def __init__(self, id: int, name: str):
        if not isinstance(id, int):
            raise TypeError("id not integer")
        if not isinstance(name, str):
            raise TypeError("name not string")
        self._id = id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
