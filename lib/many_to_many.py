from operator import attrgetter

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author is self])

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string.")

    name = property(get_name, set_name)

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError("Title must be a string.")

    title = property(get_title, set_title)

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author

    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of the Author class.")

    author = property(get_author, set_author)

    def get_book(self):
        return self._book

    def set_book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise ValueError("Book must be an instance of the Book class.")

    book = property(get_book, set_book)

    def get_date(self):
        return self._date

    def set_date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise ValueError("Date must be a string.")

    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties

    def set_royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise ValueError("Royalties must be a number.")

    royalties = property(get_royalties, set_royalties)

    @classmethod
    def contracts_by_date(cls, date=None):
        """Returns contracts sorted by date. If a specific date is provided, it filters contracts by that date."""
        if date:
            return sorted([contract for contract in cls.all if contract.date == date], key=attrgetter('date'))
        return sorted(cls.all, key=attrgetter('date'))