import requests
from Models.login_view import LoginView
"""
    config base settings for all api subclasses
"""

class BaseApi:
    def __init__(self,url:str,session):
        self._base_url = url
        self.session = session



