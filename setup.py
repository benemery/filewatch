#!/usr/bin/env python
from distutils.core import setup

from filewatch import VERSION

with open('README.rst', 'rb') as fin:
    README = fin.read()

PACKAGE_NAME = 'filewatch'

setup(name=PACKAGE_NAME,
      version=VERSION,
      description='Python File Watcher',
      package_data={PACKAGE_NAME: ['{}.ini'.format(PACKAGE_NAME), ], },
      long_description=README,
      author='Ben Emery',
      url='https://github.com/benemery/%s' % PACKAGE_NAME,
      download_url='https://github.com/benemery/%s/tarball/%s' % (VERSION, PACKAGE_NAME),
      packages=[PACKAGE_NAME, ],
     )