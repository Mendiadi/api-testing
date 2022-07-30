from Models.base_obj import BaseObject
from enum import Enum

class OrderStatus(Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"

class Oreder(BaseObject):
    def __init__(self,id:int,petId:int,quantity:int,shipDate:str,status:OrderStatus,complete:bool):
        self._id = id
        self._petId =petId
        self._quantity = quantity
        self._shipDate = shipDate
        self._status = status
        self._complete = complete

    