import json
import pytest
import logging
from Models.tag import Tag
from Models.pets import Pet, Status
from Models.user import User
from API.pets_api import PetApi
from API.api_user import ApiUser
from API.constent import PET_DATA,PET_DATA2,USER_DATA
from API.store_api import StoreApi

LOGGER = logging.getLogger(__name__)

################# FIXTURES #################################

@pytest.fixture(scope="session")
def get_user()->User:
    user = User(**USER_DATA)
    return user

@pytest.fixture(scope="session")
def get_user_api() -> ApiUser:
    api = ApiUser()
    return api

@pytest.fixture(scope="session")
def get_pet_api() -> PetApi:
    api = PetApi()
    return api


@pytest.fixture(scope="session")
def get_pet() -> Pet:
    return Pet(**PET_DATA)

@pytest.fixture(scope="session")
def get_store_api() -> StoreApi:
    api = StoreApi()
    return api

################### PET TESTS ##############################


def test_post_pet(get_pet_api):
    LOGGER.info("test_post_pet executing")
    api = get_pet_api
    pet = Pet(**PET_DATA2)
    code, response = api.post_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert json.loads(response) == pet.to_json()

def test_put_pet(get_pet_api):
    LOGGER.info("test_put_pet executing")
    api = get_pet_api
    pet = Pet(**PET_DATA2)
    code, response = api.put_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert response == pet.to_json()

@pytest.mark.parametrize("status,excepted",
                         [(("sold"), (Status.sold.value)),
                          (("pending"), (Status.pending.value)),
                          (("available"), (Status.available.value))])
def test_get_pet_by_status(get_pet_api, status, excepted):
    api = get_pet_api
    LOGGER.info("test_get_pet_by_status executing")
    code, pets = api.get_pet_by_status(status)
    assert code == 200
    for pet in pets:
        LOGGER.info(f"PET CONTENT OF STATUS {status} : {pet.to_json()}")
        assert pet.status == excepted



def test_find_by_tag(get_pet_api):
    tags = [Tag(1, "test"), Tag(2, "foo")]
    LOGGER.info("test_find_by_tags execute")
    api = get_pet_api
    code, response = api.find_pet_by_tag(tags)
    assert code == 200
    for pet in response:
        assert pet.tag.to_json() in tags


def test_post_id_pet(get_pet_api):
    LOGGER.info("test_post_id_pet execute")
    api = get_pet_api
    code, response = api.post_id(PET_DATA2['id'],"adi","sold")
    try:
        LOGGER.info(f"response: {response.to_json()}, code: {code}")
    except:
        LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200
    assert response.name == "adi" and response.status == "sold" and response.id == 10


def test_find_pet_by_id(get_pet_api):
    LOGGER.info("test_find_pet_by_id execute")
    api = get_pet_api
    code, pet = api.find_pet_by_id(PET_DATA2['id'])
    try:
        LOGGER.info(f"response: {pet.to_json()} code: {code}")
    except:
        LOGGER.info(f"response: {pet} code: {code}")
    assert code == 200
    assert pet.id == 10

def test_delete_pet_by_id(get_pet,get_pet_api):
    LOGGER.info("test_delete_pet_by_id executing")
    pet = get_pet
    api = get_pet_api
    code, response = api.delete_pet_by_id(pet.id)
    LOGGER.info(f"code: {code} msg: {response}")
    assert code == 200
    assert response == "Pet deleted"


############## USER TESTS #############################

def test_post_create_user(get_user_api,get_user):
    api = get_user_api
    code, response = api.post_create_user(get_user.to_json())
    LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200


def test_post_create_users(get_user,get_user_api):
    api = get_user_api
    code, response = api.post_create_user_with_list([get_user.to_json()])
    LOGGER.info(f"response - {response}, code: {code}")
    assert code == 200

def test_get_user_login(get_user,get_user_api):
    api = get_user_api
    code, response = api.get_user_login(get_user.username,get_user.password)
    LOGGER.info(f"code : {code} response: {response}")
    assert code == 200

def test_put_update_user(get_user_api,get_user):
    api = get_user_api
    code,response = api.put_update_user(get_user.username)
    LOGGER.info(f"code: {code}, response: {response}")
    assert code == 200


def test_get_user_logout(get_user_api):
    api = get_user_api
    code, response = api.get_user_logout()
    LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200
    assert response == "User logged out"

def test_get_user_by_username(get_user_api,get_user):
    api = get_user_api
    response = api.get_user_by_username(get_user.username)
    LOGGER.info(f"send : {get_user.to_json()}  \nresponse: {response.to_json()}")
    assert response.id == get_user.id and response.username == get_user.username


def test_delete_user(get_user_api,get_user):
    api = get_user_api
    code,response = api.delete_user(get_user.username)
    LOGGER.info(f"code: {code}, response : {response}")
    assert code == 200

############ STORE TEST#####################

def test_get_inventory(get_store_api):
    api = get_store_api
    code, response = api.get_inventory()
    LOGGER.info(f"code : {code}, response:{response}")
    assert code == 200

