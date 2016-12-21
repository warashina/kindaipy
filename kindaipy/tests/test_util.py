import unittest
import kindaipy.util as util
from collections import OrderedDict


class TestUtil(unittest.TestCase):

    def test_expand_params(self):
        params = OrderedDict([
            ('itemId',      'info:ndljp/pid/922693'),
            ('contentNo',   '5'),
            ('outputScale', '1'),
        ])
        encoded_params = util.expand_params(params)
        self.assertEqual(
          encoded_params,
          'itemId=info%3Andljp%2Fpid%2F922693&contentNo=5&outputScale=1')

if __name__ == '__main__':
    unittest.main()
