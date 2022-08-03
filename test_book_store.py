import pytest
from API.account_api import AccountApi
from API.book_store_api import BookApi
from Models.user_result import UserResult
from Models.login_view import LoginView
import  logging
import requests
from API.constant import selaUser,selaUserId,BOOK_LIST_TO_ADD,BOOKS_DELETE
LOGGER = logging.getLogger(__name__)


def bearer_auth_session() -> [dict,UserResult]:
    header = {'accept': 'application/json'}
    #response = requests.post("https://bookstore.toolsqa.com/Account/v1/User",data=selaUser,headers=header)
   # if response.ok:
    #user = UserResult(**response.json())
    res = requests.post( 'https://bookstore.toolsqa.com/Account/v1/GenerateToken',data=selaUser,headers=header)
    my_token = res.json()["token"]
    header = {'Authorization': f'Bearer {my_token}'}
    auth = requests.post("https://bookstore.toolsqa.com/Account/v1/Authorized",data=selaUser)
    assert auth.status_code == 200
    print(res.json())
    return header


@pytest.fixture(scope="session")
def url(pytestconfig) -> str:
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return pytestconfig.getoption("url")

@pytest.fixture(scope="module")
def account_api(url):
    header = bearer_auth_session()
    acc_api = AccountApi(url,header)
    return acc_api

# @pytest.fixture(scope="module")
# def user_auth(bearer_auth_session) -> UserResult:
#     return bearer_auth_session

@pytest.fixture(scope="module")
def book_api(url):
    api = BookApi(url,bearer_auth_session())
    return api

@pytest.fixture(scope="module")
def account_auth() -> LoginView:
    return selaUser


def test_session_Bearer_token(account_api):
    api = account_api
    code,response = api.get_user_by_id(selaUserId)
    LOGGER.info(f"{response},code {code}")
    assert code == 200
    assert response.username == selaUser['userName']


def test_session_Bearer_wrong_token(account_api):
    api = account_api
    Authorization = api.session.headers["Authorization"]
    token = Authorization.split()[1]
    api.session.headers.update({'Authorization': f'Bearer bad{token}'})
    code,response = api.get_user_by_id(user_id=selaUserId)
    print(response)
    assert code == 401

def test_post_account_exists(account_api,account_auth):
    api = account_api
    code,res = api.post_account(account_auth)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 406

def test_post_account_invalid_password(account_api):
    LOGGER.info(f"post_account_invalid_password executing")
    api = account_api
    code, res = api.post_account({"userName":"sample2","pass":"invalid"})
    LOGGER.info(res)
    assert code == 400

def test_delete_user_by_id(account_api):
    LOGGER.info(f"delete_user_by_id executing")
    api = account_api
    code,res = api.delete_user_by_id(selaUserId)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 200
    assert api.get_user_by_id(selaUserId)[0] != 200

#########################################
def test_get_books(book_api):
    LOGGER.info(f"get_books executing")
    api = book_api
    code, res = api.get_books()
    assert code == 200
    try:
        for book in res:
            LOGGER.info(f"{book.to_json()}")
    except AttributeError:
        LOGGER.info(res)

def test_add_list_books(book_api,account_api):
    LOGGER.info("test_add_books_list executing")
    api = book_api
    res = api.post_books_to_user(BOOK_LIST_TO_ADD)
    assert res.status_code == 204
    LOGGER.info(f" res = {res.text}")
    code ,res = account_api.get_user_by_id(selaUserId)
    LOGGER.info(f" res = {res}")
    assert code == 200
    assert  BOOK_LIST_TO_ADD['collectionOfIsbns']['isbn'] in res.books


def test_delete_books_to_user(book_api):
    LOGGER.info("test_delete_books_to_user executing")
    api = book_api
    res = api.delete_books_to_user(selaUserId)
    LOGGER.info(f" res = {res.text}")
    assert res.status_code == 204
    code, res = account_api.get_user_by_id(selaUserId)
    LOGGER.info(f" res = {res}")
    assert code == 200
    assert BOOK_LIST_TO_ADD['collectionOfIsbns']['isbn'] not in res.books
