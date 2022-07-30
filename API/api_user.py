import json
from Models.user import User
import  requests
from API.constent import *
class ApiUser:
    def __init__(self):
        self._url = URL
        self._headers = HEADER_JSON
        self.session = requests.session()
        self.session.headers.update(self._headers)

    def get_user_login(self,username:str,password:str) -> (int,str):
        response = self.session.get(f"{self._url}/user/login?username={username}&password={password}")
        return response.status_code, response.text


    def get_user_logout(self) -> (int,str):
        response = self.session.get(f"{self._url}/user/logout")
        return response.status_code,response.text

    def post_create_user(self,data: dict):
        response = self.session.post(f"{self._url}/user",json=data)
        return response.status_code, response.text

    def post_create_user_with_list(self,data: list):
        response = self.session.post(f"{self._url}/user/createWithList",json=data)
        return response.status_code, response.text

    def get_user_by_username(self,username:str) -> (User,str):
        response = self.session.get(f"{self._url}/user/{username}")
        if response.ok:
            user = User(**response.json())
            return user
        return response.text

    def put_update_user(self,username:str):
        response = self.session.put(f"{self._url}/user/{username}")
        return response.status_code, response.text

    def delete_user(self,username:str):
        response = self.session.delete(f"{self._url}/user/{username}")
        return response.status_code,response.text