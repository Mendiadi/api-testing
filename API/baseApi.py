import requests
from API.constent import *

class BaseApi:
    def __init__(self):
        self._base_url =  "https://petstore3.swagger.io/api/v3"
        self._headers = {"accept": "application/json"}
        self.session = requests.session()
        self.session.headers.update(self._headers)
