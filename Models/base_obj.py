import json
class BaseObj:

    def to_json(self) -> json:
        res = {}
        for k,v in self.__dict__.items():
            res[k.replace("_","")] = v
        return json.dumps(res)