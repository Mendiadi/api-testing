from Models.base_obj import BaseObj


class UserResult(BaseObj):
    def __init__(self, userId: str = None, username: str =None, books: [str] = None,userID: str = None):
        if  userId and not userID:
            self._userId = userId
        else:
            self._userId = userID
        self._username = username
        self._books = books

    @property
    def userId(self) -> str:
        return self._userId

    @property
    def username(self) -> str:
        return self._username

    @property
    def books(self) -> [str]:
        return self._books
