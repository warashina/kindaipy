from collections import OrderedDict
import kindaipy.util as util


class Spread(object):
    def __init__(self, book, spread_number):
        self.book = book
        self.spread_number = spread_number

    def image_url(self) -> str:
        params = OrderedDict([
            ('itemId',      'info:ndljp/pid/{0}'.format(str(self.book.key))),
            ('contentNo',   str(self.spread_number)),
            ('outputScale', '1'),
        ])
        image_url = 'http://dl.ndl.go.jp/view/jpegOutput?{0}'.format(
                    util.expand_params(params))
        return image_url
