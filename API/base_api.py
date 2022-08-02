import requests

"""
    config base settings for all api subclasses
"""

class BaseApi:
    def __init__(self,url:str):
        self._base_url = url
        self._headers = {"accept": "application/json"}
        self.session = requests.session()
        self.session.headers.update(self._headers)
        self.session.post(f"{self._base_url}/Account/v1/Authorized")
