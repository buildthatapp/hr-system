#!/usr/bin/env python

import os

from setuptools import setup

README = None
with open(os.path.abspath('README.md')) as fh:
    README = fh.read()

setup(
  name='flask-hr',
  version='0.1.0',
  description=README,
  author='Louis Magdaleno',
  author_email='buildthatapp@gmail.com',
  url='http://www.flask.com',
  packages=['hr'],
  install_requires=[
    'Flask',
    'configobj',
    'Flask-Bootstrap',
    'Flask-Script',
    'Flask-SQLAlchemy',
    'Flask-Restless',
  ],
)
