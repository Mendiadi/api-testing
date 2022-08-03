from Models.base_obj import BaseObj


class BookModel(BaseObj):
    """
    Class for represent book model and type checking also
    """
    def __init__(self, isbn: str, title: str, subTitle: str = None, author: str = None,
                 publish_date: str = None, publisher: str = None, pages: int = None, description: str = None,
                 website: str = None):

        if not isinstance(isbn, str) :
            raise TypeError("isbn not string")
        if not isinstance(title, str):
            raise TypeError("title not string")
        if not isinstance(subTitle, str)and subTitle is not None:
            raise TypeError("subTitle not string")
        if not isinstance(author, str)and author is not None:
            raise TypeError("author not string")
        if not isinstance(publish_date, str)and publish_date is not None:
            raise TypeError("publish_date not string")
        if not isinstance(publisher, str)and publisher is not None:
            raise TypeError("publisher not string")
        if not isinstance(pages, int)and pages is not None:
            raise TypeError("pages not string")
        if not isinstance(description, str)and description is not None:
            raise TypeError("description not string")
        if not isinstance(website, str)and website is not None:
            raise TypeError("website not string")
        self._isbn = isbn
        self._title = title
        self._subTitle = subTitle
        self._author = author
        self._publish_date = publish_date
        self._publisher = publisher
        self._pages = pages
        self._description = description
        self._website = website
