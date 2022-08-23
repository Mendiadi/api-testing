from Models.user import User
from API.baseApi import BaseApi


class ApiUser(BaseApi):
    """
    Class to make the request calls to account
    """

    def __init__(self, url: str):
        super().__init__(url)
        self._url = f"{self._base_url}/user"

    def get_user_login(self, username: str, password: str) -> (int, str):
        """
        request get method with username and password
        should login if account exists
        :param username: username of the account (string)
        :param password: password of the account (string)
        :return: response status code and response text
        """
        response = self.session.get(f"{self._url}/login?username={username}&password={password}")
        return response.status_code, response.text

    def get_user_logout(self) -> (int, str):
        """
        request get method to logout account that already logged in
        :return: response status code and response text
        """
        response = self.session.get(f"{self._url}/logout")
        return response.status_code, response.text

    def post_create_user(self, data: dict) -> (int, str):
        """
        make post request and create new user
        :param data: new data to create user
        :return:  response status code and response text
        """
        response = self.session.post(f"{self._url}", json=data)
        return response.status_code, response.text

    def post_create_user_with_list(self, data: list) -> (int, str):
        response = self.session.post(f"{self._url}/createWithList", json=data)
        if response.ok:
            user_list = list()
            for user in response.json():
                user_list.append(user)
            return response.status_code,user_list
        return response.status_code, response.text

    def get_user_by_username(self, username: str) -> [int, User]:
        response = self.session.get(f"{self._url}/{username}")
        if response.ok:
            user = User(**response.json())
            return response.status_code, user
        return response.status_code, response.text

    def put_update_user(self, username: str, user: User) -> (int, str):
        response = self.session.put(f"{self._url}/{username}", json=user.to_json())
        return response.status_code, response.text

    def delete_user(self, username: str) -> (int, str):
        response = self.session.delete(f"{self._url}/{username}")
        return response.status_code, response.text
