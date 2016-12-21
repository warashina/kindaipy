"""Tests for Book object."""
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

    @unittest.skip("Not implemented.")
    def test_book_got_key_content(self):
        """keyはURL最後の番号であること."""
        self.assertEqual(self.book.key, '922693')

    def test_book_has_title(self):
        """資料の題名となるtitle属性をもつこと."""
        self.assertTrue(hasattr(self.book, 'title'))

    @unittest.skip("Not implemented.")
    def test_book_got_title_content(self):
        """資料のtitleをもつこと.スクレイピングで取得する."""
        self.assertEqual(self.book.title, '正義の叫')


if __name__ == '__main__':
    unittest.main()
