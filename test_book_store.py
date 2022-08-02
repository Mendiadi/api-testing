import pytest
from API.account_api import AccountApi
from Models.login_view import LoginView
import  logging
import requests
from API.constant import selaUser,selaUserId
LOGGER = logging.getLogger(__name__)
@pytest.fixture(scope="session")
def bearer_auth_session():
    header = {'accept': 'application/json'}
    res = requests.post( 'https://bookstore.toolsqa.com/Account/v1/GenerateToken',data=selaUser,headers=header)
    my_token = res.json()["token"]
    session = requests.session()
    session.headers.update(header)
    session.headers.update({'Authorization': f'Bearer {my_token}'})
    return session


@pytest.fixture(scope="session")
def url(pytestconfig) -> str:
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return pytestconfig.getoption("url")

@pytest.fixture(scope="session")
def account_api(url,bearer_auth_session):
    session = bearer_auth_session
    acc_api = AccountApi(url,session)
    return acc_api

@pytest.fixture(scope="module")
def account_auth() -> LoginView:
    return selaUser

@pytest.fixture(scope="session")
def user_id():
    return selaUserId



def test_session_Bearer_token(account_api):
    api = account_api
    code,response = api.get_user_by_id("860189b4-4a95-4e96-8079-4a4f69ea3a0b")
    print(response)
    assert code == 200


def test_session_Bearer_wrong_token(account_api):
    api = account_api
    Authorization = api.session.headers["Authorization"]
    token = Authorization.split()[1]
    api.session.headers.update({'Authorization': f'Bearer bad{token}'})
    code,response = api.get_user_by_id('860189b4-4a95-4e96-8079-4a4f69ea3a0b')
    print(response)
    assert code == 401

def test_post_account_exists(account_api,account_auth):
    api = account_api
    code,res = api.post_account(account_auth)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 406


def test_delete_user_by_id(account_api,user_id):
    api = account_api
    code,res = api.delete_user_by_id(user_id)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 200
    assert api.get_user_by_id(user_id)[0] != 200

