from API.base_api import BaseApi
from Models.user_result import UserResult
import json


class AccountApi(BaseApi):
    def __init__(self, url: str, header: dict):
        super().__init__(url, header)
        self._url = f"{self._base_url}Account/v1"

    def post_account(self, account: json) -> (int, str, UserResult):
        """
        make post request to add new account
        and if code ok its convert it to user object
         return 200 if success
        :param account: account data in json format
        :return: status_code , response text/user object
        """
        response = self.session.post(f"{self._url}/User", json=account)
        if response.ok:
            return response.status_code, UserResult(**response.json())
        return response.status_code, response.text

    def delete_user_by_id(self, user_id: str) -> (int, str, UserResult):
        """
        request delete account by id
         return 200 if success
        :param user_id: account id
        :return: status_code , response text/user object
        """
        res = self.session.delete(f"{self._url}/User/{user_id}")
        if res.ok:
            try:
                return res.status_code, UserResult(**res.json())
            except TypeError:
                pass
        return res.status_code, res.text

    def get_user_by_id(self, user_id: str) -> (int, str, UserResult):
        """
        get request to find account by id
        return 200 if success
        :param user_id: account id
        :return: status_code , response text/user object
        """
        res = self.session.get(f"{self._url}/User/{user_id}")
        if res.ok:
            return res.status_code, UserResult(**res.json())
        return res.status_code, res.text

