import  requests
from API.constent import *
class ApiUser:
    def __init__(self):
        self._url = URL
        self._headers = HEADER_JSON
        self.session = requests.session()
        self.session.headers.update(self._headers)


    def get_user_logout(self):
        response = self.session.get(f"{self._url}/user/logout")
        return response.status_code,response.text