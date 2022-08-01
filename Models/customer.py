from base_obj import BaseObject
from address import Address


class Customer(BaseObject):
    def __init__(self, id: int, username: str, address: Address):
        if not isinstance(id,int):
            raise TypeError("id not integer")
        if not isinstance(username, str):
            raise TypeError("username not string")
        if not isinstance(address, (Address,str)):
            raise TypeError("username not string")
        self._id = id
        self._username = username
        self._address = address

    @property
    def id(self) -> int:
        return self._id
