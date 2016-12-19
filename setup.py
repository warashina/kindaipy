from setuptools import setup, find_packages
import sys

sys.path.append('./kindaipy')
sys.path.append('./kindaipy/tests')

setup(
    name = 'kindaipy',
    version = '0.0.1',
    description='This is test codes for travis ci',
    url = 'https://github.com/warashina/kindaipy'
    packages = find_packages(),
)
