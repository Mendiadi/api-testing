import requests
from Models.pets import Pet
from Models.tag import Tag
from API.constent import *
import json
class PetApi:

    def __init__(self):
        self._url = URL
        self._headers = HEADER_JSON
        self.session = requests.session()
        self.session.headers.update(self._headers)

    def post_pet(self, pet: Pet) -> [dict]:
        response =  self.session.post(f"{self._url}/pet", json=pet.to_json())
        return response.status_code, response.content

    def put_pet(self, pet: Pet) -> [dict]:
        response =  self.session.put(f"{self._url}/pet", json=pet.to_json())
        try:
            return response.status_code, response.json()
        except:
            return response.status_code, response.content

    def post_id(self, id: int, name: str, status: str) -> [Pet]:
        response =  self.session.post(f"{self._url}/pet/{id}?name={name}&status={status}")
        print(response)

        if response.ok:
            pet = response.json()
            pet_obj = Pet(**pet)
            return response.status_code, pet_obj
        else:
            return response.status_code, response.content

    def find_pet_by_tag(self, tags: [Tag]) -> [Pet]:
        response =  self.session.get(url=f"{self._url}/pet/findByTags?tags={tags}")
        result_list = []
        if response.ok:
            for pet in response.json():
                new_pet = Pet(**pet)
                result_list.append(new_pet)
            return response.status_code, result_list
        return response.status_code, response.content

    def get_pet_by_status(self, status: str) -> [Pet]:
        response =  self.session.get(url=f"{self._url}/pet/findByStatus?status={status}")
        result_list = []
        if response.ok:
            for pet in response.json():
                new_pet = Pet(**pet)
                result_list.append(new_pet)
            return response.status_code, result_list
        return response.status_code, response.content

    def find_pet_by_id(self, id: int) -> (int, Pet):
        response =  self.session.get(url=f"{self._url}/pet/{id}")
        if response.ok:
            return response.status_code, Pet(**json.loads(response.content))
        return response.status_code, response.content

    def delete_pet_by_id(self,id:int):
        response =  self.session.delete(f"{self._url}/pet/{id}")
        return response.status_code, response.text


if __name__ == '__main__':
    a = PetApi()
    c, p = a.post_id(PET_DATA['id'],"adi","sold")
    print(c, p)
