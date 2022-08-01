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
                 name: str,
                 category: Category = Category(10,"sample"),
                 photoUrls:list = "sample",
                 tags: [Tag] = Tag(1,"test"),
                 status:Status = Status.available):
        if not isinstance(id,int):
            raise TypeError("id not integer")
        if not isinstance(name,str):
            raise TypeError("name not string")
        if not isinstance(category,(Category,dict)):
            raise TypeError("category not list or dict")
        if not isinstance(photoUrls,(list,str)):
            raise TypeError("photoUrls not list")
        if not isinstance(tags,(list,Tag)):
            raise TypeError("tags not list")
        if not isinstance(status,(Status,str)):
            raise TypeError("status not Status")
        self._id = id
        self._name = name
        try:
            self._category = category.to_json()
        except AttributeError:
            self._category = category
        self._photoUrls = photoUrls
        self._tags = tags
        try:
            self._status = status.value
        except AttributeError:
            self._status = status

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def photoUrls(self) -> list[str]:
        return self._photoUrls


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





