import unittest
from book import Book

class TestBook(unittest.TestCase):

    def test_book_has_title(self):
        book = Book()
        self.assertTrue(hasattr(book, "title"))
