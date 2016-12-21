"""資料画像1枚にあたるモジュール.

資料画像はそれぞれjpeg画像へのリンクをもっており、Bookにページ数だけ存在する.
"""
from collections import OrderedDict
import kindaipy.util as util


class Spread(object):
    """Spreadクラスのインスタンスは資料画像1枚を表します."""

    def __init__(self, book, spread_number):
        """Bookのインスタンスとページ番号で初期化する."""
        self.book = book
        self.spread_number = spread_number

    def image_url(self) -> str:
        """資料keyとページNoをパラメーターに画像のURLを作成する."""
        params = OrderedDict([
            ('itemId',      'info:ndljp/pid/{0}'.format(str(self.book.key))),
            ('contentNo',   str(self.spread_number)),
            ('outputScale', '1'),
        ])
        image_url = 'http://dl.ndl.go.jp/view/jpegOutput?{0}'.format(
                    util.expand_params(params))
        return image_url
