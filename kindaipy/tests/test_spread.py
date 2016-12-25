"""Tests for Spread object."""
from kindaipy.book import Book
from kindaipy.spread import Spread
import unittest


class TestSpread(unittest.TestCase):
    """BookのPermalinkやkeyとページ番号から画像URLを作成する."""

    def setUp(self):
        """Bookのインスタンスとページ番号で初期化する."""
        self.book = Book('http://dl.ndl.go.jp/info:ndljp/pid/922693')
        self.book.key = '922693'
        self.spread_number = '5'
        self.spread = Spread(self.book, self.spread_number)

    def test_spread_has_book(self):
        """インスタンスがbookの属性を持っていること."""
        self.assertTrue(hasattr(self.spread, 'book'))

    def test_spread_can_read_book_permalink(self):
        """bookのpermalinkを読めること."""
        self.assertEqual(
            self.spread.book.permalink,
            'http://dl.ndl.go.jp/info:ndljp/pid/922693')

    @unittest.skip("Not implemented.")
    def test_spread_uri(self):
        """ブラウザで閲覧するための正しい資料ページURLが得られること."""
        self.assertEqual(self.spread.uri,
                         'http://dl.ndl.go.jp/info:ndljp/pid/922693/5')

    def test_spread_image_uri(self):
        """資料画像ダウンロードのための正しいURLが得られること."""
        self.assertEqual(self.spread.image_url,
                         ('http://dl.ndl.go.jp/view/jpegOutput?'
                          'itemId=info%3Andljp%2Fpid%2F922693'
                          '&contentNo=5&outputScale=1'))


if __name__ == '__main__':
    unittest.main()
