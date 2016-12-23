"""kindai.pyに関する共通処理のモジュール.

URLの文字列処理などを実装する.
"""
from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urlencode


def expand_params(params):
    """パラメーターの辞書を引数にURLエンコードされた文字列を返す.

    OrderedDictを引数にすることで期待通りの順番のURLパラメータが返る.
    """
    return urlencode(params)

def get_permalink_page(url):
    """Get webpage with bs4."""
    r = requests.get(url)
    return BeautifulSoup(r.text)

def get_key(url):
    m = re.search("\d+$", url)
    return m.group(0)
