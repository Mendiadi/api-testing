from API.baseApi import BaseApi

class StoreApi(BaseApi):


    def __init__(self):
        super().__init__()
        self._url = f"{self._base_url}/store"

    def get_inventory(self):
        response = self.session.get(f"{self._url}/inventory")
        return response.status_code,response.json()