from Models.base_obj import BaseObject


class User(BaseObject):
    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str, phone: str,
                 userStatus: int):
        if not isinstance(id, int):
            raise TypeError("id not integer")
        if not isinstance(username, str):
            raise TypeError("username not string")
        if not isinstance(firstName, str):
            raise TypeError("firstname not string")
        if not isinstance(lastName, str):
            raise TypeError("lastname not string")
        if not isinstance(email, str):
            raise TypeError("email not string")
        if not isinstance(password, str):
            raise TypeError("password not string")
        if not isinstance(phone, str):
            raise TypeError("phone not string")
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

    @property
    def firstname(self) -> str:
        return self._firstName

    @firstname.setter
    def firstname(self, firstname: str):
        self._firstName = firstname
