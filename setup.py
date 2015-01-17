#!/usr/bin/env python
from distutils.core import setup

from filewatch import VERSION

with open('README.rst', 'rb') as fin:
    README = fin.read()

setup(name='filewatch',
      version=VERSION,
      description='Python File Watcher',
      long_description=README,
      author='Ben Emery',
      url='https://github.com/benemery/filewatch',
      download_url='https://github.com/benemery/filewatch/tarball/%s' % VERSION,
      packages=['filewatch', ],
     )