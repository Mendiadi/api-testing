from Models.base_obj import BaseObj



class LoginView(BaseObj):

    def __init__(self,userName:str,password:str):
        if not isinstance(userName,str):
            pass
        self._userName = userName
        self._password = password