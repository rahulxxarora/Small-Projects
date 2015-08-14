#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'gcrawler',
    'version': '1.0.2',
    'description': 'Crawls geeksforgeeks for interview section of a particular site',
    'long_description': open('README.md').read(),
    'author': 'Rahul Arora',
    'author_email': 'coderahul94@gmail.com',
    'license': 'MIT',
    'test_suite': 'tests',
    'url': 'https://github.com/rahulxxarora/Crawler-geeks',
    'install_requires': [
        'BeautifulSoup4>=4.3.1', 'requests'
    ],
    'packages': [
        'gcrawler',
        'tests'
    ],
    'classifiers': [
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License'
    ],
}

setup(**config)
