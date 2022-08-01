from enum import Enum
from Models.base_obj import BaseObject
from Models.tag import Tag
from Models.category import Category
class Status(Enum):
    available = "available"
    pending = "pending"
    sold = "sold"

class Pet(BaseObject):
    def __init__(self,
                 id: int,
                 name: str= None,
                 category: Category = None,
                 photoUrls= None,
                 tags: list[Tag]= None,
                 status:Status = None):
        self._id = id
        self._name = name
        self._category = category
        self._photoUrls = photoUrls
        self._tags = tags
        self._status = status

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name



    @id.setter
    def id(self,id:int):
        self._id = id

    @property
    def status(self) -> Status:
        return self._status

    @property
    def tag(self):
        return self._tags


if __name__ == '__main__':
    pet = Pet(12342,"eadi",status=Status("dfgdg"))





