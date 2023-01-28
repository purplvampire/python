# Type Hint
from typing import List # Tuple, Set, etc...


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book(Name '{self.name}', Type '{self.book_type}', Weight {self.weight}g)>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

    @staticmethod
    def static_method():
        print("Called static_method.")

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books
    
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."