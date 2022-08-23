import pytest
from API.account_api import AccountApi
from API.book_store_api import BookApi
from Models.user_result import UserResult
import logging
import requests
from API.constant import *

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def url(pytestconfig) -> str:
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return pytestconfig.getoption("url")


@pytest.fixture(scope="module")
def bearer_auth_session(url) -> [dict, UserResult]:
    """
    fixture to make authorize by the save acc data in
    constant,py file and after it verify by post request
    if the authorized complete success
    :param url: url to work with
    :return: header after adding bearer token
    """
    res = requests.post(f'{url}Account/v1/GenerateToken', data=selaUser)
    my_token = res.json()["token"]
    header = {'Authorization': f'Bearer {my_token}'}
    print(res.json())
    return header


@pytest.fixture(scope="module")
def account_api(url, bearer_auth_session) -> AccountApi:
    """
    fixture to return account api obj
    :param url: url from cli or default from pytest config
    :param bearer_auth_session: header with authorized token
    :return: AccountAip object
    """
    header = bearer_auth_session
    acc_api = AccountApi(url, header)
    return acc_api


@pytest.fixture(scope="module")
def book_api(url, bearer_auth_session) -> BookApi:
    """
    fixture to return book api obj
    :param url: url from cli or default from pytest config
    :param bearer_auth_session: header with authorized token
    :return: BookApi object
    """
    Url, auth = url, bearer_auth_session
    api = BookApi(Url, auth)
    return api


def test_authorized(account_api):
    """
    test if user is authorized
    :param account_api: account api fixture
    """
    LOGGER.info("test if user are authorized executing")
    api = account_api
    res = api.post_post_authorize(data=selaUser)
    LOGGER.info(f"response : {res.text}")
    assert res.status_code == 200
    assert res.text == "true"


def test_get_account(account_api):
    """
    test if get user by id given the relative acc
    excepted 200
    """
    api = account_api
    code, response = api.get_user_by_id(selaUserId)
    LOGGER.info(f"{response},code {code}")
    assert code == 200
    assert response.username == selaUser['userName']


def test_session_Bearer_wrong_token(account_api):
    """
    test if u can do get with wrong token
    excepted 401

    """
    api = account_api
    Authorization = api.session.headers["Authorization"]
    token = Authorization.split()[1]
    api.session.headers.update({'Authorization': f'Bearer bad{token}'})
    code, response = api.get_user_by_id(user_id=selaUserId)
    print(response)
    assert code == 401


def test_post_account_exists(account_api):
    """
    test post account with already exists user
    excepted 406

    """
    api = account_api
    code, res = api.post_account(selaUser)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 406


def test_post_account_invalid_password(account_api):
    LOGGER.info(f"post_account_invalid_password executing")
    api = account_api
    code, res = api.post_account({"userName": "sample2", "pass": "invalid"})
    LOGGER.info(res)
    assert code == 400


def test_post_account(account_api):
    """
    This test will not pass after 1 run ! server bug!

    """
    code, res = account_api.post_account(NEW_ACC)
    assert res.username == NEW_ACC['userName']
    LOGGER.info(f"{res}")
    code,res = account_api.delete_user_by_id(res.userId)
    LOGGER.info(f"{code}, {res}")


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


def test_put_book_invalid_isbn(book_api):
    LOGGER.info("test put book invalid isbn executing")
    data = {
        "userId": "string",
        "isbn": "string"
    }
    api = book_api
    code, res = api.put_book_by_isbn("235235", data)
    LOGGER.info(f"{res}")
    assert code == 400


def test_put_book_empty_data(book_api):
    LOGGER.info("test put book empty data executing")
    api = book_api
    code, res = api.put_book_by_isbn("9781593275846", {})
    LOGGER.info(f"{res}")
    assert code == 400


def test_put_book_to_user(book_api, account_api):
    LOGGER.info("test put book for user executing")
    api = book_api
    data = {"userId": selaUserId,
            "isbn": "9781593275846"
            }
    code, res = api.put_book_by_isbn(data["isbn"], data)
    LOGGER.info(res)
    assert code == 200
    code, res = account_api.get_user_by_id(data['userId'])
    LOGGER.info(code, res)
    assert data["isbn"] in [book.isbn for book in res.books]


def test_add_list_books(book_api, account_api):
    LOGGER.info("test_add_books_list executing")
    api = book_api
    res = api.post_books_to_user(BOOK_LIST_TO_ADD)
    assert res.status_code == 204
    LOGGER.info(f" res = {res.text}")
    code, res = account_api.get_user_by_id(selaUserId)
    LOGGER.info(f" res = {res},")
    assert code == 200
    assert BOOK_LIST_TO_ADD['collectionOfIsbns']['isbn'] in res.books


def test_get_book_exists(book_api):
    isbn_test_data = BOOKS_DELETE['isbn']
    book = book_api.get_book(isbn_test_data)
    LOGGER.info(book.to_json())
    assert book.isbn == isbn_test_data


def test_get_book_not_exists(book_api):
    isbn_test_data = "asdfasdfas"
    code = book_api.get_book(isbn_test_data)
    LOGGER.info(code)
    assert code == 400


def test_delete_book_to_user(book_api, account_api):
    LOGGER.info("test delete book to user executing")
    api = book_api
    res = api.delete_book(BOOKS_DELETE)
    LOGGER.info(res.text)
    assert res.status_code == 204
    assert BOOKS_DELETE not in account_api.get_user_by_id(selaUserId)[1].books


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


def test_delete_user_by_id(account_api):
    LOGGER.info(f"delete_user_by_id executing")
    api = account_api
    code, res = api.delete_user_by_id(selaUserId)
    LOGGER.info(f"code = {code}, res = {res}")
    assert code == 200
    code2, res2 = api.get_user_by_id(selaUserId)
    assert code2 == 401
    LOGGER.info(f"{code2}, {res}")
