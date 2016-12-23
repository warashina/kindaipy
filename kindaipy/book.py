"""Book module for kindai.py.

Initalize with permalink
ユニークなpermalinkを持つ資料のモジュール
"""
import kindaipy.util as util

class Book(object):
    """Bookオブジェクトは国会図書館デジタルライブラリーの個別資料を表す.

    書名や著者などのメタデータもこのクラスで管理する.
    """

    def __init__(self, permalink):
        """permalinkで初期化する."""
        self.permalink = permalink
        self.permalink_page = util.get_permalink_page(permalink)
        self.key = util.get_key(permalink)
        self.title = ''
