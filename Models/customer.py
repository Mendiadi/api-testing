from base_obj import BaseObject
from address import Address


class Customer(BaseObject):
    def __init__(self, id: int, username: str, address: Address):
        self._id = id
        self._username = username
        self._address = address

    @property
    def id(self) -> int:
        return self._id
