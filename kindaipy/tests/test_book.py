"""Tests for Book object."""
from bs4 import BeautifulSoup
from kindaipy.book import Book
import unittest


class TestBook(unittest.TestCase):
    """必要なメタデータの属性があること、スクレイピングした内容を確認する."""

    def setUp(self):
        """Bookはダウンロード指定時にも使用する資料のURLで初期化する."""
        self.book = Book('http://kindai.ndl.go.jp/info:ndljp/pid/922693')

    def test_book_has_permalink(self):
        """Bookのインスタンスはpermalinkの属性をもつこと."""
        self.assertTrue(hasattr(self.book, 'permalink'))

    def test_book_has_correct_permalink(self):
        """permalinkはNDLの資料permalinkと同一であること."""
        self.assertEqual(self.book.permalink,
                         'http://kindai.ndl.go.jp/info:ndljp/pid/922693')

    def test_book_has_key(self):
        """資料keyを属性としてもつこと."""
        self.assertTrue(hasattr(self.book, 'key'))

    def test_book_got_key_content(self):
        """keyはURL最後の番号であること."""
        self.assertEqual(self.book.key, '922693')

    def test_book_has_title(self):
        """資料の題名となるtitle属性をもつこと."""
        self.assertTrue(hasattr(self.book, 'title'))

    def test_book_got_title_content(self):
        """資料のtitleをもつこと.スクレイピングで取得する."""
        self.assertEqual(self.book.title, '正義の叫')

    def test_book_has_permalink_page(self):
        """permalink_pageはURLではなくWebページのオブジェクト."""
        self.assertTrue(hasattr(self.book, 'permalink_page'))

    def test_book_has_permalink_page_as_bs_object(self):
        """permalink_pageはBeautifulSoupオブジェクトとしてもつこと."""
        self.assertIsInstance(self.book.permalink_page, BeautifulSoup)

    def test_get_metadata(self):
        self.assertIsInstance(self.book.metadata, dict)

    def test_book_has_metadata(self):
        self.assertTrue(hasattr(self.book, 'metadata'))

    def test_lookup_from_metadata_from_query(self):
        self.assertEqual(self.book.metadata_like('title'), '正義の叫')

    def test_book_has_total_spread(self):
        self.assertTrue(hasattr(self.book, 'total_spread'))

    def test_book_has_number_of_total_spread(self):
        self.assertEqual(self.book.total_spread, 20)

    def test_book_has_spreads(self):
        self.assertTrue(hasattr(self.book, 'spreads'))

    def test_book_has_correct_number_of_spreads(self):
        self.assertEqual(len(self.book.spreads), 20)

    def test_book_has_spreads_with_image_url(self):
        self.assertEqual(self.book.spreads[0].image_url,
                         ('http://dl.ndl.go.jp/view/jpegOutput?'
                          'itemId=info%3Andljp%2Fpid%2F922693'
                          '&contentNo=1&outputScale=1'))

    def test_book_has_spread_at(self):
        self.assertTrue(hasattr(self.book, 'spread_at'))


if __name__ == '__main__':
    unittest.main()
