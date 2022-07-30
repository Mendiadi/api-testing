from Models.base_obj import BaseObject


class User(BaseObject):
    def __init__(self, id: int, username: str, firstname: str, lastname: str, email: str, password: str, phone: str,
                 userStatus: int):
        self._id = id
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password
        self._phone = phone
        self._userStatus = userStatus

    @property
    def id(self) -> int:
        return self._id

    @property
    def username(self) -> str:
        return self._username