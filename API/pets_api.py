from Models.pets import Pet
from Models.tag import Tag
from API.baseApi import BaseApi


class PetApi(BaseApi):

    def __init__(self, url: str):
        super().__init__(url)
        self._url = f"{self._base_url}/pet"

    def post_pet(self, pet: Pet) -> [dict]:
        response = self.session.post(f"{self._url}", json=pet.to_json())
        return response.status_code, response.text

    def put_pet(self, pet: Pet) -> [dict]:
        response = self.session.put(f"{self._url}", json=pet.to_json())
        return response.status_code, response.text

    def post_id(self, id: int, name: str, status: str) -> [Pet]:
        response = self.session.post(f"{self._url}/{id}?name={name}&status={status}")
        print(response)

        if response.ok:
            pet = response.json()
            pet_obj = Pet(**pet)
            return response.status_code, pet_obj
        else:
            return response.status_code, response.text

    def find_pet_by_tag(self, tags: [Tag]) -> [Pet]:
        response = self.session.get(url=f"{self._url}/findByTags?tags={tags}")
        result_list = []
        if response.ok:
            for pet in response.json():
                new_pet = Pet(**pet)
                result_list.append(new_pet)
            return response.status_code, result_list
        return response.status_code, response.text

    def get_pet_by_status(self, status: str) -> [Pet]:
        response = self.session.get(url=f"{self._url}/findByStatus?status={status}")
        result_list = []
        if response.ok:
            for pet in response.json():
                new_pet = Pet(**pet)
                result_list.append(new_pet)
            return response.status_code, result_list
        return response.status_code, response.text

    def find_pet_by_id(self, id: int) -> (int, Pet):
        response = self.session.get(url=f"{self._url}/{id}")
        if response.ok:
            return response.status_code, Pet(**response.json())
        return response.status_code, response.text

    def delete_pet_by_id(self, id: int) -> (int, str):
        response = self.session.delete(f"{self._url}/{id}")
        return response.status_code, response.text

    def post_upload_photo(self, id: int, file: str) -> (int, str):
        response = self.session.post(f"{self._url}/{id}/uploadImage", data=file)
        return response.status_code, response.text


if __name__ == '__main__':
    a = PetApi()
    r = a.find_pet_by_id(1)
    print(r)
