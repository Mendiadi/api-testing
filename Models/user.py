from Models.base_obj import BaseObject


class User(BaseObject):
    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str, phone: str,
                 userStatus: int):
        self._id = id
        self._username = username
        self._firstName = firstName
        self._lastName = lastName
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

    @property
    def password(self) -> str:
        return self._password