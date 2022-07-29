from base_obj import BaseObject


class Address(BaseObject):

    def __init__(self, street: str, city: str, state: str, zip: str):
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, street: str):
        self._street = street

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str):
        self._state = state

    @property
    def zip(self) -> str:
        return self._zip

    @zip.setter
    def zip(self, zip: str):
        self._zip = zip
