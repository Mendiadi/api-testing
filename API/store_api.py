from API.baseApi import BaseApi
from Models.orders import Oreder


class StoreApi(BaseApi):

    def __init__(self, url: str):
        super().__init__(url)
        self._url = f"{self._base_url}/store"

    def get_inventory(self):
        response = self.session.get(f"{self._url}/inventory")
        return response.status_code, response.json()

    def post_order(self, order: Oreder):
        response = self.session.post(url=f"{self._url}/order", json=order.to_json())
        return response.status_code, response.json()

    def find_order_by_id(self, id: int) -> (int, Oreder):
        response = self.session.get(url=f"{self._url}/order/{id}")
        if response.ok:
            return response.status_code, Oreder(**response.json())
        return response.status_code, response.text

    def delete_order_by_id(self, id: int):
        response = self.session.delete(url=f"{self._url}/order/{id}")
        return response.status_code, response.text
