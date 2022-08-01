import json
import pytest
import logging
from Models.tag import Tag
from Models.pets import Pet, Status
from Models.user import User
from API.pets_api import PetApi
from API.api_user import ApiUser
from API.constent import USER_DATA, PET_DATA
from API.store_api import StoreApi

LOGGER = logging.getLogger(__name__)

"""
 לעשות get לחיות אחרי כל בדיקה ולבדוק לפי זה
"""
################# FIXTURES #################################

@pytest.fixture(scope="session")
def get_user() -> User:
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

@pytest.mark.pet
def test_post_pet(get_pet_api,get_pet):
    LOGGER.info("test_post_pet executing")
    api = get_pet_api
    pet = get_pet
    code, response = api.post_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert api.find_pet_by_id(pet.id)[1].to_json() == pet.to_json()


@pytest.mark.pet
def test_put_pet(get_pet_api):
    LOGGER.info("test_put_pet executing")
    api = get_pet_api
    pet = Pet(id=1,name="oracle")
    code, response = api.put_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert response == api.find_pet_by_id(pet.id)[1].to_json()

@pytest.mark.pet
def test_find_pet_by_id(get_pet_api,get_pet):
    LOGGER.info("test_find_pet_by_id execute")
    api = get_pet_api
    pet = Pet(id=1,name="oracle")
    code, pet_res = api.find_pet_by_id(pet.id)
    try:
        LOGGER.info(f"response: {pet.to_json()} code: {code}")
    except Exception:
        LOGGER.info(f"response: {pet} code: {code}")
    assert code == 200
    assert pet.id == pet_res.id and pet.name == pet_res.name

@pytest.mark.pet
def test_post_id_pet(get_pet_api,get_pet):
    LOGGER.info("test_post_id_pet execute")
    api = get_pet_api
    pet = get_pet
    code, response = api.post_id(pet.id, "adi", "sold")
    try:
        LOGGER.info(f"response: {response.to_json()}, code: {code}")
    except Exception:
        LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200
    get_pet = api.find_pet_by_id(pet.id)[1]
    assert get_pet.name == "adi" and get_pet.status == Status.sold.value




@pytest.mark.pet
@pytest.mark.parametrize("status,excepted",
                         [("sold", Status.sold.value),
                          ("pending", Status.pending.value),
                          ("available", Status.available.value)])
def test_get_pet_by_status(get_pet_api, status, excepted):#***
    api = get_pet_api
    LOGGER.info("test_get_pet_by_status executing")
    code, pets = api.get_pet_by_status(status)
    assert code == 200
    for pet in pets:
        LOGGER.info(f"PET CONTENT OF STATUS {status} : {pet.to_json()}\n")
        assert pet.status == excepted


@pytest.mark.pet
def test_find_by_tag(get_pet_api):#***
    tags = [Tag(1, "test"), Tag(2, "foo")]
    LOGGER.info("test_find_by_tags execute")
    api = get_pet_api
    code, response = api.find_pet_by_tag(tags)
    assert code == 200
    for pet in response:
        assert pet.tag.to_json() in tags




@pytest.mark.pet
def test_delete_pet_by_id(get_pet, get_pet_api):
    LOGGER.info("test_delete_pet_by_id executing")
    pet = get_pet
    api = get_pet_api
    code, response = api.delete_pet_by_id(pet.id)
    LOGGER.info(f"code: {code} msg: {response}")
    assert code == 200
    assert response == "Pet deleted"


############## USER TESTS #############################
@pytest.mark.user
def test_post_create_user(get_user_api, get_user):
    api = get_user_api
    code, response = api.post_create_user(get_user.to_json())
    LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200


@pytest.mark.user
def test_post_create_users(get_user, get_user_api):
    api = get_user_api
    code, response = api.post_create_user_with_list([get_user.to_json()])
    LOGGER.info(f"response - {response}, code: {code}")
    assert code == 200


@pytest.mark.user
def test_get_user_login(get_user, get_user_api):
    api = get_user_api
    code, response = api.get_user_login(get_user.username, get_user.password)
    LOGGER.info(f"code : {code} response: {response}")
    assert code == 200


@pytest.mark.user
def test_put_update_user(get_user_api, get_user):
    api = get_user_api
    code, response = api.put_update_user(get_user.username)
    LOGGER.info(f"code: {code}, response: {response}")
    assert code == 200


@pytest.mark.user
def test_get_user_logout(get_user_api):
    api = get_user_api
    code, response = api.get_user_logout()
    LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200
    assert response == "User logged out"


@pytest.mark.user
def test_get_user_by_username(get_user_api, get_user):
    api = get_user_api
    response = api.get_user_by_username(get_user.username)
    LOGGER.info(f"send : {get_user.to_json()}  \nresponse: {response.to_json()}")
    assert response.id == get_user.id and response.username == get_user.username


@pytest.mark.user
def test_delete_user(get_user_api, get_user):
    api = get_user_api
    code, response = api.delete_user(get_user.username)
    LOGGER.info(f"code: {code}, response : {response}")
    assert code == 200


############ STORE TEST#####################
@pytest.mark.store
def test_get_inventory(get_store_api):
    api = get_store_api
    code, response = api.get_inventory()
    LOGGER.info(f"code : {code}, response:{response}")
    assert code == 200
