from Models.base_obj import BaseObj

class BookModel(BaseObj):
    def __init__(self,isbn:str,title:str,subTitle:str,author:str,
                 publish_date:str,publisher:str,pages:str,description:str,website:str):

        if not isinstance(isbn,str):
            raise TypeError("isbn not string")
        if not isinstance(title, str):
            raise TypeError("title not string")
        if not isinstance(subTitle, str):
            raise TypeError("subTitle not string")
        if not isinstance(author, str):
            raise TypeError("author not string")
        if not isinstance(publish_date, str):
            raise TypeError("publish_date not string")
        if not isinstance(publisher, str):
            raise TypeError("publisher not string")
        if not isinstance(pages, str):
            raise TypeError("pages not string")
        if not isinstance(description, str):
            raise TypeError("description not string")
        if not isinstance(website, str):
            raise TypeError("website not string")
        self._isbn = isbn
        self._title = title
        self._subTitle = subTitle
        self._author = author
        self._publish_date = publish_date
        self._publisher =publisher
        self._pages = pages
        self._description =description
        self._website =website