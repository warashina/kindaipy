"""Tests for Util module."""
from collections import OrderedDict
import kindaipy.util as util
import unittest


class TestUtil(unittest.TestCase):
    """Utilモジュール内の各メソッドをテストする."""

    def test_expand_params(self):
        """パラメーターをURLエンコードする.OrderdDictで順序を保持する."""

        params = OrderedDict([
            ('itemId',      'info:ndljp/pid/922693'),
            ('contentNo',   '5'),
            ('outputScale', '1'),
        ])
        encoded_params = util.expand_params(params)
        self.assertEqual(encoded_params,
                         ('itemId=info%3Andljp%2Fpid%2F922693&'
                          'contentNo=5&outputScale=1'))


if __name__ == '__main__':
    unittest.main()
