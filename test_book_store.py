import pytest
from API.account_api import AccountApi

@pytest.fixture(scope="session")
def url(pytestconfig) -> str:
    """
    give the url from pytest options
    :param pytestconfig: pytestconfig fixture
    :return: url to integrate
    """
    return pytestconfig.getoption("url")

@pytest.fixture(scope="session")
def account_api(url):
    acc = AccountApi(url)
    return acc