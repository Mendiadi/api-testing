import pytest
import logging
import json
from Models.pets import Pet, Status
from API.pets_api import PetApi
LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def get_pet_api() -> PetApi:
    api = PetApi()
    return api

@pytest.fixture(scope="session")
def get_pet()->Pet:
    return Pet(21,"test")



@pytest.mark.parametrize("status,excepted",
                         [(("sold"),(Status.sold.value)),
                          (("pending"),(Status.pending.value)),
                          (( "available"),(Status.available.value))])
def test_get_pet_by_status(get_pet_api,status,excepted):
    api = get_pet_api
    LOGGER.info("test_get_pet_by_status executing")
    code,pets = api.get_pet_by_status(status)
    assert  code == 200
    for pet in pets:
        LOGGER.info(f"PET CONTENT OF STATUS {status} : {pet.to_json()}")
        assert pet.status == excepted



def test_put_pet(get_pet,get_pet_api):
    LOGGER.info("test_put_pet executing")
    api = get_pet_api
    code,response = api.put_pet(get_pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert response == get_pet.to_json()


def test_post_pet(get_pet,get_pet_api):
    LOGGER.info("test_post_pet executing")
    api = get_pet_api
    code,response = api.post_pet(get_pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert response == get_pet.to_json()



def test_find_by_tag(get_pet,get_pet_api):

    LOGGER.info("test_find_by_tags execute")
    api =get_pet_api
    code,response = api.find_pet_by_tag([get_pet.tag])
    assert code == 200
    for pet in response:
        LOGGER.info(f"response for {get_pet.tag}: {pet.to_json()}")
        assert pet.tag.to_json() == get_pet.tag.to_json()

def test_find_pet_by_id(get_pet_api):
    LOGGER.info("test_find_pet_by_id execute")
    api = get_pet_api
    code, pet = api.find_pet_by_id(10)
    try:
        LOGGER.info(f"response: {pet.to_json()} code: {code}")
    except:
        LOGGER.info(f"response: {pet} code: {code}")
    assert code == 200
    assert pet.id == 10