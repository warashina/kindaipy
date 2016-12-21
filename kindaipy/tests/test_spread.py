from kindaipy.book import Book
from kindaipy.spread import Spread
import unittest


class TestSpread(unittest.TestCase):

    def setUp(self):
        self.book = Book('http://kindai.ndl.go.jp/info:ndljp/pid/922693')
        self.book.key = '922693'
        self.spread_number = '5'
        self.spread = Spread(self.book, self.spread_number)

    def test_spread_has_book(self):
        self.assertTrue(hasattr(self.spread, 'book'))

    def test_spread_can_read_book_permalink(self):
        self.assertEqual(
            self.spread.book.permalink,
            'http://kindai.ndl.go.jp/info:ndljp/pid/922693')

    @unittest.skip("Not implemented.")
    def test_spread_uri(self):
        self.assertEqual(self.spread.uri,
                         'http://dl.ndl.go.jp/info:ndljp/pid/922693/5')

    def test_spread_image_uri(self):
        self.assertEqual(self.spread.image_url(),
                         ('http://dl.ndl.go.jp/view/jpegOutput?'
                          'itemId=info%3Andljp%2Fpid%2F922693'
                          '&contentNo=5&outputScale=1'))


if __name__ == '__main__':
    unittest.main()
