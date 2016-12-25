"""Book module for kindai.py.

Initalize with permalink
ユニークなpermalinkを持つ資料のモジュール
"""
from kindaipy.spread import Spread
import kindaipy.util as util
import re

class Book(object):
    """Bookオブジェクトは国会図書館デジタルライブラリーの個別資料を表す.

    書名や著者などのメタデータもこのクラスで管理する.
    """

    def __init__(self, permalink):
        """permalinkで初期化する."""
        self.permalink =      permalink
        self.permalink_page = self.get_permalink_page()
        self.metadata =       self.get_metadata()
        self.key =            self.get_key()
        self.title =          self.get_title()
        self.total_spread =   self.get_total_spread()
        self.spreads =        self.get_spreads()

    def get_permalink_page(self):
        return util.get_permalink_page(self.permalink)

    def get_metadata(self):
        dts = self.permalink_page.select('dl.detail-metadata-list dt')
        dds = self.permalink_page.select('dl.detail-metadata-list dd')
        metadata = {}
        for i, dt in enumerate(dts):
            metadata.update({dt.contents[0]:dds[i].contents[0].strip()})

        return metadata

    def get_key(self):
        return util.get_key(self.permalink)

    def get_title(self):
        return self.metadata_like('title')

    def get_total_spread(self):
        page_menu = self.permalink_page.select('#sel-content-no option')
        return len(page_menu)

    def metadata_like(self, query):
        query_regexp = '\(' + query + '\)'
        for key, value in self.metadata.items():
            m = re.search(query_regexp ,key)
            if m != None:
                return value

    def get_spreads(self):
        spreads = []
        for i in enumerate(range(self.total_spread), start=1):
            spreads.append(Spread(self, i[0]))

        return spreads

    def spread_at(self, spread_number):
        pass
