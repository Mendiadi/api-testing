import requests
from API.constent import *


class BaseApi:
    def __init__(self,url:str):
        self._base_url = url
        self._headers = {"accept": "application/json"}
        self.session = requests.session()
        self.session.headers.update(self._headers)
