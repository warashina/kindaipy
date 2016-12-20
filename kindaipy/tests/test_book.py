import unittest
from kindaipy.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('http://kindai.ndl.go.jp/info:ndljp/pid/922693')

    def test_book_has_permalink(self):
        self.assertTrue(hasattr(self.book, 'permalink'))

    def test_book_has_correct_permalink(self):
        self.assertEqual(self.book.permalink, 'http://kindai.ndl.go.jp/info:ndljp/pid/922693')

    def test_book_has_key(self):
        self.assertTrue(hasattr(self.book, 'key'))

    @unittest.skip("Not implemented.")
    def test_book_got_key_content(self):
        self.assertEqual(self.book.key, '922693')

    def test_book_has_title(self):
        self.assertTrue(hasattr(self.book, 'title'))

    @unittest.skip("Not implemented.")
    def test_book_got_title_content(self):
        self.assertEqual(self.book.title, '正義の叫')

if __name__ == '__main__':
    unittest.main()
