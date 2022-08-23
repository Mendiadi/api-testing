from Models.base_obj import BaseObject
from enum import Enum


class OrderStatus(Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class Oreder(BaseObject):
    def __init__(self, id: int, petId: int, quantity: int, shipDate: str, status: (OrderStatus, str), complete: bool):

        if not isinstance(id, int):
            raise TypeError("id not integer")
        if not isinstance(petId, int):
            raise TypeError("petId not integer")
        if not isinstance(quantity, int):
            raise TypeError("quantity not integer")
        if not isinstance(shipDate, str):
            raise TypeError("shipDate not string")
        if not isinstance(status, (OrderStatus, str)):
            raise TypeError("status not OrderStatus")
        if not isinstance(complete, bool):
            raise TypeError("complete not bool")
        self._id = id
        self._petId = petId
        self._quantity = quantity
        self._shipDate = shipDate

        self._status = status

        self._complete = complete

    @property
    def id(self) -> int:
        return self._id
