"""Book module for kindai.py.

Initalize with permalink
ユニークなpermalinkを持つ資料のモジュール
"""
import kindaipy.util as util
import re

class Book(object):
    """Bookオブジェクトは国会図書館デジタルライブラリーの個別資料を表す.

    書名や著者などのメタデータもこのクラスで管理する.
    """

    def __init__(self, permalink):
        """permalinkで初期化する."""
        self.permalink = permalink
        self.permalink_page = util.get_permalink_page(permalink)
        self.metadata = self.get_metadata()
        self.key = util.get_key(permalink)
        self.title = self.metadata_like('title')

    def get_metadata(self):
        dts = self.permalink_page.select('dl.detail-metadata-list dt')
        dds = self.permalink_page.select('dl.detail-metadata-list dd')
        metadata = {}
        for i, dt in enumerate(dts):
            metadata.update({dt.contents[0]:dds[i].contents[0].strip()})

        return metadata

    def metadata_like(self, query):
        query_regexp = '\(' + query + '\)'
        for key, value in self.metadata.items():
            m = re.search(query_regexp ,key)
            if m != None:
                return value
