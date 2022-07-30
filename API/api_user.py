import json

import  requests
from API.constent import *
class ApiUser:
    def __init__(self):
        self._url = URL
        self._headers = HEADER_JSON
        self.session = requests.session()
        self.session.headers.update(self._headers)


    def get_user_logout(self) -> (int,str):
        response = self.session.get(f"{self._url}/user/logout")
        return response.status_code,response.text

    def post_create_user(self,data: dict):
        response = self.session.post(f"{self._url}/user",json=data)
        return response.status_code, response.content

    def post_create_user_with_list(self,data: list):
        response = self.session.post(f"{self._url}/user/createWithList",json=data)
        return response.status_code, response.content