import requests
from Models.pets import Pet
from Models.tag import Tag
class PetApi:

    def __init__(self):
        self._url = "https://petstore3.swagger.io/api/v3"
        self._headers = {"accept":"application/json"}
        self.session = requests.session()
        self.session.headers.update(self._headers)

    def post_pet(self,pet:Pet) -> [dict]:
        response = requests.session().post(f"{self._url}/pet",data=pet.to_json())
        return response.status_code,response.json()


    def put_pet(self,pet:Pet) -> [dict]:
        response = requests.session().put(f"{self._url}/pet",data=pet.to_json())
        return response.status_code,response.json()

    def post_id(self,id: int,name:str,status:str) -> [Pet]:
        response = requests.session().post(f"{self._url}/pet/{id}?name={name}&status={status}")
        print(response)

        if response.ok:
            pet = response.json()
            pet_obj = Pet(**pet)
            return response.status_code, pet_obj
        else:
            return response.status_code,response.content


    def find_pet_by_tag(self,tags:[Tag]) -> [Pet]:
        response = requests.session().get(url=f"{self._url}/pet/findByTags?tags={tags}")
        result_list = []
        if response.ok:
            for pet in response.json():
                new_pet = Pet(**pet)
                result_list.append(new_pet)
            return response.status_code,result_list
        return response.status_code,response.json()



    def get_pet_by_status(self,status:str) -> [Pet]:
        response =  requests.session().get(url=f"{self._url}/pet/findByStatus?status={status}")
        result_list = []
        if response.ok:
            for pet in response.json():
                new_pet = Pet(**pet)
                result_list.append(new_pet)
            return response.status_code,result_list
        return response.status_code, response.json()

    def find_pet_by_id(self,id:int) -> (int, Pet):
        response = requests.session().get(url=f"{self._url}/pet/{id}")
        if response.ok:
            return response.status_code,Pet(**response.json())
        return response.status_code, response.json()

if __name__ == '__main__':
    a = PetApi()
    c, p=a.post_id(1,"adi","sold")
    print(c,p)