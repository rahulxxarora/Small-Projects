#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'mewe',
    'version': '1.0.3',
    'description': 'Search word meaning on Merriam-Webster website.',
    'long_description': open('README.md').read(),
    'author': 'Rahul Arora',
    'author_email': 'coderahul94@gmail.com',
    'license': 'MIT',
    'test_suite': 'tests',
    'url': 'https://github.com/rahulxxarora/MeWe-API',
    'install_requires': [
        'BeautifulSoup4>=4.3.1', 'requests'
    ],
    'packages': [
        'mewe',
        'tests'
    ],
    'classifiers': [
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License'
    ],
    'keywords': [
        'dictionary',
        'web scraping',
        'word',
        'meanings'
    ],
}

setup(**config)
