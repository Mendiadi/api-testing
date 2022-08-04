import requests
from API.base_api import BaseApi
from Models.user_result import UserResult
from Models.book import BookModel



class BookApi(BaseApi):
    def __init__(self, url: str, header: dict):
        super().__init__(url, header)
        self._url = f"{self._base_url}BookStore/v1/"

    def get_books(self) -> [list]:
        """
        call get request and convert them to
        book objects list, return the exists list
        of books in the store
        :return: list of obj books
        """
        res = self.session.get(url=f"{self._url}Books")
        if res.ok:
            books = res.json()
            book_list = []
            for book in books['books']:
                b = BookModel(**book)
                book_list.append(b)
            return res.status_code, book_list
        return res.status_code, res.text

    def post_books_to_user(self, books: dict) -> requests.Response:
        """
        call post request and update books in given user
        :param books: dict of userid,collection of isbn
        :return: response object
        """
        res = self.session.post(url=f"{self._url}Books", data=books)
        return res

    def delete_books_to_user(self, user_id: str) -> requests.Response:
        """
        Call delete request and clear all the books list
        from given user by id
        :param user_id: id of the user needs to delete books
        :return: response object
        """
        res = self.session.delete(url=f"{self._url}Books/?UserId={user_id}")
        return res

    def put_book_by_isbn(self, isbn: str, data: dict):
        """
        put request to add one book and update it
        :param isbn: book isbn string
        :param data: data dict of userid and isbn
        :return: if code ok return code and user obj
        otherwise return code and text info of response
        """
        res = self.session.put(url=f"{self._url}Books/{isbn}", data=data)
        if res.ok:
            user = UserResult(**res.json())
            return res.status_code, user
        return res.status_code, res.text

    def delete_book(self,data:dict) -> requests.Response:
        res = self.session.delete(url=f"{self._url}Book",data=data)
        return res