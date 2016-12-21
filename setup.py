from setuptools import setup, find_packages
import sys

sys.path.append('./kindaipy')
sys.path.append('./kindaipy/tests')

setup(
    name = 'kindaipy',
    version = '0.0.1',
    description='Kindai.py is Japanese NDL Digital Collection downloader. One of a port of the kindai.rb',
    url = 'https://github.com/warashina/kindaipy',
    packages = ["kindaipy"],
    package_dir={'kindaipy':'kindaipy'},
)
