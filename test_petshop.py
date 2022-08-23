import pytest
import logging
from Models.tag import Tag
from Models.pets import Pet, Status
from Models.user import User
from API.pets_api import PetApi
from API.api_user import ApiUser
from API.constent import USER_DATA, PET_DATA, USER_DATA2, USER_DATA3, PET_ORDER_DATA
from API.store_api import StoreApi
from Models.category import Category
from Models.orders import Oreder

LOGGER = logging.getLogger(__name__)


################# FIXTURES #################################

@pytest.fixture(scope="session")
def url(pytestconfig):
    """
    fixture for handle url arg
    :param pytestconfig: pytest config
    :return: url to work with
    """
    return pytestconfig.getoption("url")


@pytest.fixture(scope="session")
def get_user() -> User:
    """
    fixutre to init user obj
    :return: User obj
    """
    user = User(**USER_DATA)
    return user


@pytest.fixture(scope="session")
def get_user_api(url) -> ApiUser:
    """
    fixture to init user api obj
    :param url: url to integrate
    :return: ApiUser obj
    """
    api = ApiUser(url)
    return api


@pytest.fixture(scope="session")
def get_pet_api(url) -> PetApi:
    api = PetApi(url)
    return api


@pytest.fixture(scope="session")
def get_pet() -> Pet:
    return Pet(**PET_DATA)


@pytest.fixture(scope="session")
def get_store_api(url) -> StoreApi:
    api = StoreApi(url)
    return api


@pytest.fixture(scope="session")
def get_order() -> Oreder:
    return Oreder(**PET_ORDER_DATA)


################### PET TESTS ##############################

@pytest.mark.pet
def test_post_pet(get_pet_api, get_pet):
    LOGGER.info("test_post_pet executing")
    api = get_pet_api
    pet = get_pet
    code, response = api.post_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert api.find_pet_by_id(pet.id)[1] == pet


@pytest.mark.pet
def test_put_pet(get_pet_api, get_pet):
    LOGGER.info("test_put_pet executing")
    api = get_pet_api
    pet = get_pet
    pet.name = "yossi"
    code, response = api.put_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 200
    assert pet == api.find_pet_by_id(pet.id)[1]


@pytest.mark.pet
def test_find_pet_by_id(get_pet_api, get_pet):
    LOGGER.info("test_find_pet_by_id execute")
    api = get_pet_api
    code, pet_res = api.find_pet_by_id(get_pet.id)
    try:
        LOGGER.info(f"response: {pet_res} code: {code}")
    except Exception:
        LOGGER.info(f"response: {pet_res} code: {code}")
    assert code == 200
    assert get_pet == pet_res


@pytest.mark.pet
def test_post_id_pet(get_pet_api, get_pet):
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
def test_get_pet_by_status(get_pet_api, status, excepted):
    api = get_pet_api
    LOGGER.info("test_get_pet_by_status executing")
    code, pets = api.get_pet_by_status(status)
    assert code == 200
    for pet in pets:
        LOGGER.info(f"PET CONTENT OF STATUS {status} : {pet.to_json()}\n")
        assert pet.status == excepted


@pytest.mark.pet
def test_find_by_tag(get_pet_api):
    tags = [Tag(1, "test"), Tag(2, "foo")]
    LOGGER.info("test_find_by_tags execute")
    api = get_pet_api
    code, response = api.find_pet_by_tag(tags)
    assert code == 200
    for pet in response:
        assert pet.tag.to_json() in tags


@pytest.mark.pet
def test_upload_image_to_pet(get_pet_api, get_pet):
    LOGGER.info("test_upload_image_to_pet executing")
    api = get_pet_api
    image_path = "/tmp/inflector3832436340023087946.tmp"
    code, response = api.post_upload_photo(get_pet.id, image_path)
    assert code == 200
    LOGGER.info(response)
    assert image_path in api.find_pet_by_id(get_pet.id)[1].photoUrls


@pytest.mark.pet
def test_delete_pet_by_id(get_pet, get_pet_api):
    LOGGER.info("test_delete_pet_by_id executing")
    pet = get_pet
    api = get_pet_api
    code, response = api.delete_pet_by_id(pet.id)
    LOGGER.info(f"code: {code} msg: {response}")
    assert code == 200
    assert api.find_pet_by_id(get_pet.id)[0] == 404


@pytest.mark.pet
def test_post_id_pet_not_exists(get_pet_api):
    LOGGER.info("test_post_id_pet_not_exists execute")
    api = get_pet_api
    code, response = api.post_id(5281, "adi", "sold")
    LOGGER.info(f"response: {response}, code: {code}")
    assert code == 404


######### invalid ##################
@pytest.mark.pet
def test_put_pet_not_exists_pet(get_pet_api):
    LOGGER.info("test_put_pet executing")
    api = get_pet_api
    pet = Pet(id=5579, name="oracle", photoUrls=["string"], tags=[Tag(1, "test").to_json()],
              status=Status.available, category=Category(7, "lions"))
    code, response = api.put_pet(pet)
    LOGGER.info(f"\nresponse pet = {response}")
    assert code == 404


@pytest.mark.pet
def test_find_pet_by_id_with_id_that_not_exists(get_pet_api):
    LOGGER.info("test_find_pet_by_id_invalid_id execute")
    api = get_pet_api
    code, pet_res = api.find_pet_by_id(223432)
    LOGGER.info(f"response: {pet_res} code: {code}")
    assert code == 404


@pytest.mark.pet
def test_get_pet_by_status_invalid(get_pet_api):
    api = get_pet_api
    LOGGER.info("test_get_pet_by_status invalid executing")
    code, pets = api.get_pet_by_status("status")
    assert code == 400
    LOGGER.info(f"PET CONTENT OF STATUS {pets} : {code}\n")


############## USER TESTS #############################
@pytest.mark.user
def test_post_create_user(get_user_api, get_user):
    api = get_user_api
    code, response = api.post_create_user(get_user.to_json())
    LOGGER.info(f"response: {response}, code: {code}")
    assert code == 200
    assert api.get_user_by_username(get_user.username)[1].to_json() == get_user.to_json()


@pytest.mark.user
def test_post_create_users_list(get_user_api):
    api = get_user_api
    list_of_users = [User(**USER_DATA2).to_json(), User(**USER_DATA3).to_json()]
    code, response = api.post_create_user_with_list(list_of_users)
    LOGGER.info(f"response - {response}, code: {code}")
    assert code == 200
    for user_dict in list_of_users:
        assert user_dict == api.get_user_by_username(user_dict['username'])[1].to_json()


@pytest.mark.user
def test_get_user_login(get_user, get_user_api):
    api = get_user_api
    code, response = api.get_user_login(get_user.username, get_user.password)
    LOGGER.info(f"code : {code} response: {response}")
    assert code == 200


@pytest.mark.user
def test_put_update_user(get_user_api, get_user):
    api = get_user_api
    user = get_user
    user.firstname = "yossi"
    code, response = api.put_update_user(get_user.username, user)
    LOGGER.info(f"code: {code}, response: {response}")
    assert code == 200
    assert api.get_user_by_username(get_user.username)[1].firstname == "yossi"


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
    code, response = api.get_user_by_username(get_user.username)
    assert code == 200
    LOGGER.info(f"send : {get_user.to_json()}  \nresponse: {response}")
    assert response.to_json() == get_user.to_json()


@pytest.mark.user
def test_delete_user(get_user_api, get_user):
    api = get_user_api
    code, response = api.delete_user(get_user.username)
    LOGGER.info(f"code: {code}, response : {response}")
    assert code == 200
    code, res = get_user_api.get_user_by_username(get_user.username)
    LOGGER.info(code, res)
    assert code == 404
    assert "user not found" in res.lower()


############ STORE TEST#####################

@pytest.mark.store
def test_get_inventory(get_store_api):
    LOGGER.info("test_get_inventory executing")
    api = get_store_api
    code, response = api.get_inventory()
    LOGGER.info(f"code : {code}, response before adding:{response}")
    assert code == 200
    count_placed_inventory = response['placed']
    order = Oreder(122, 22, 3, "2022-08-01T10:25:47.688+00:00", 'placed', False)
    code = api.post_order(order)[0]
    if code == 200:
        res = api.get_inventory()[1]
        count_placed_inventory_after_post = res['placed']
        LOGGER.info(f"response before after{res}")
        api.delete_order_by_id(122)
        assert count_placed_inventory < count_placed_inventory_after_post


@pytest.mark.store
def test_order_pet(get_store_api, get_order):
    LOGGER.info("test_order_pet executing")
    api = get_store_api
    order = get_order
    code, response = api.post_order(order)
    LOGGER.info(f"code : {code}, response:{response}")
    assert code == 200
    assert api.find_order_by_id(order.id)[1].to_json() == order.to_json()


@pytest.mark.store
def test_find_order_by_id(get_store_api, get_order):
    LOGGER.info("test_order_pet invalid id executing")
    order = get_order
    api = get_store_api
    code, response = api.find_order_by_id(order.id)
    LOGGER.info(f"code : {code}, response:{response.to_json()}")
    assert code == 200
    assert response.to_json() == order.to_json()


@pytest.mark.store
def test_find_order_invalid_id(get_store_api):
    LOGGER.info("test_find_order invalid id executing")
    api = get_store_api
    code, response = api.find_order_by_id(556)
    LOGGER.info(f"code : {code}, response:{response}")
    assert code == 404


@pytest.mark.store
def test_delete_order_by_id(get_store_api, get_order):
    LOGGER.info("test_delete_porder_by_id _executing")
    api = get_store_api
    code, response = api.delete_order_by_id(get_order.id)
    LOGGER.info(f"code : {code}, response:{response}")
    assert code == 200
    assert api.find_order_by_id(get_order.id)[0] == 404
