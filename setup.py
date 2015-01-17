#!/usr/bin/env python
from distutils.core import setup

from filewatch import VERSION

setup(name='filewatch',
      version=VERSION,
      description='Python File Watcher',
      author='Ben Emery',
      url='https://github.com/benemery/filewatch',
      download_url='https://github.com/benemery/filewatch/tarball/%s' % VERSION,
      packages=['filewatch', ],
     )