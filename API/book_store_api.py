import json
from Models.user_result import UserResult
from API.base_api import BaseApi
from Models.book import BookModel
class BookApi(BaseApi):
    def __init__(self,url:str,header:dict):
        super().__init__(url,header)
        self._url = f"{self._base_url}BookStore/v1/"

    def get_books(self) ->[ list]:
        res = self.session.get(url=f"{self._url}Books")
        if res.ok:
            books = res.json()
            book_list = []
            for book in books['books']:
                b = BookModel(**book)
                book_list.append(b)
            return res.status_code,book_list
        return res.status_code,res.text

    def post_books_to_user(self,books:dict):
        res = self.session.post(url=f"{self._url}Books",data=books)
        return res

    def delete_books_to_user(self,user_id:str):
        res = self.session.delete(url=f"{self._url}Books/?UserId={user_id}")
        return res

    def put_book_by_isbn(self,isbn:str,data:dict):
        res = self.session.put(url=f"{self._url}Books/{isbn}",data=data)
        if res.ok:
            user = UserResult(**res.json())
            return res.status_code, user
        return res.status_code,res.text


