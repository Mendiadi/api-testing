from Models.base_obj import BaseObj



class LoginView(BaseObj):

    def __init__(self,userName:str,password:str):
        if not isinstance(userName,str):
            raise TypeError("username not string")
        if not isinstance(password, str):
            raise TypeError("password not string")
        self._userName = userName
        self._password = password

