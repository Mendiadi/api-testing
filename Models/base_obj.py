
from abc import ABC



class BaseObject(ABC):

    def to_json(self) -> dict:
        result = {}
        for k, v in self.__dict__.items():
            if v is not None:
                result[k.replace("_","")] = v
        return result

