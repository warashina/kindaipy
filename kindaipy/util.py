"""kindai.pyに関する共通処理のモジュール.

URLの文字列処理などを実装する.
"""
from urllib.parse import urlencode


def expand_params(params):
    """パラメーターの辞書を引数にURLエンコードされた文字列を返す.

    OrderedDictを引数にすることで期待通りの順番のURLパラメータが返る.
    """
    return urlencode(params)
