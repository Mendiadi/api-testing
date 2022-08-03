import pytest
from API.account_api import AccountApi
from Models.user_result import UserResult
from Models.login_view import LoginView
import  logging
import requests
from API.constant import selaUser,selaUserId
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
    api = account_api
    code, res = api.post_account({"userName":"sample2","pass":"invalid"})
    LOGGER.info(res)
    assert code == 400

def test_delete_user_by_id(account_api):
    api = account_api
    code,res = api.delete_user_by_id(selaUserId)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 200
    assert api.get_user_by_id(selaUserId)[0] != 200


