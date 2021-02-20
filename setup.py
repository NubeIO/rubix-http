from distutils.core import setup
from os.path import join, dirname

import setuptools

import rubix_http

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(name='rubix-http',
      version=rubix_http.__version__,
      author=rubix_http.__author__,
      description=rubix_http.__doc__.strip(),
      packages=setuptools.find_packages(),
      install_requires=install_requires,
      )
