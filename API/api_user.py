from Models.user import User
from API.baseApi import BaseApi


class ApiUser(BaseApi):

    def __init__(self, url: str):
        super().__init__(url)
        self._url = f"{self._base_url}/user"

    def get_user_login(self, username: str, password: str) -> (int, str):
        response = self.session.get(f"{self._url}/login?username={username}&password={password}")
        return response.status_code, response.text

    def get_user_logout(self) -> (int, str):
        response = self.session.get(f"{self._url}/logout")
        return response.status_code, response.text

    def post_create_user(self, data: dict) -> (int,str):
        response = self.session.post(f"{self._url}", json=data)
        return response.status_code, response.text

    def post_create_user_with_list(self, data: list)  -> (int,str):
        response = self.session.post(f"{self._url}/createWithList", json=data)
        return response.status_code, response.text

    def get_user_by_username(self, username: str) -> [int, User]:
        response = self.session.get(f"{self._url}/{username}")
        if response.ok:
            user = User(**response.json())
            return response.status_code, user
        return response.status_code, response.text

    def put_update_user(self, username: str, user: User)  -> (int,str):
        response = self.session.put(f"{self._url}/{username}", json=user.to_json())
        return response.status_code, response.text

    def delete_user(self, username: str)  -> (int,str):
        response = self.session.delete(f"{self._url}/{username}")
        return response.status_code, response.text
