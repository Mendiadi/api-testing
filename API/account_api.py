from API.base_api import BaseApi

class AccountApi(BaseApi):
    def __init__(self,url:str):
        super().__init__(url)
        self._url = f"{self._base_url}/Account/v1/"