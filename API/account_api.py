from API.base_api import BaseApi
from Models.user_result import UserResult
import json


class AccountApi(BaseApi):
    def __init__(self,url:str,header:dict):
        super().__init__(url,header)
        self._url = f"{self._base_url}Account/v1"




    def post_account(self,account:json) -> (int,str):
        response = self.session.post(f"{self._url}/User", json=account)
        if response.ok:
            return response.status_code, UserResult(**response.json())
        return response.status_code,response.text

    def delete_user_by_id(self,user_id:str):
        res = self.session.delete(f"{self._url}/User/{user_id}")
        if res.ok:
            try:
                return res.status_code,UserResult(**res.json())
            except TypeError:
                pass
        return res.status_code,res.text

    def get_user_by_id(self,user_id:str):
        res = self.session.get(f"{self._url}/User/{user_id}")
        if res.ok:
            return res.status_code,UserResult(**res.json())
        return res.status_code,res.text
