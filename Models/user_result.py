from Models.base_obj import BaseObj

class UserResult(BaseObj):
    def __init__(self,userId:str,username:str,books:[str]):
        self._userId = userId
        self._username =username
        self._books = books

    @property
    def userId(self) -> str:
        return self._userId
