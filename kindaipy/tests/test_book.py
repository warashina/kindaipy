import unittest
from kindaipy.book import Book

class TestBook(unittest.TestCase):

    def test_book_has_title(self):
        book = Book()
        self.assertTrue(hasattr(book, "title"))

if __name__ == '__main__':
    unittest.main()
