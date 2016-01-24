#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

from os import path

import colorize_pinyin


here = path.abspath(path.dirname(__file__))


setup(
    name='colorize_pinyin',
    version=colorize_pinyin.__version__,
    description=colorize_pinyin.__doc__.strip().splitlines()[0],
    long_description=colorize_pinyin.__doc__,
    url='https://github.com/ratijas/colorize_pinyin',
    author='Ratijas',
    author_email='ratijas.t@me.com',
    license='WTFPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'Topic :: Education',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',

        # Pick your license as you wish (should match "license" above)
        'License :: Public Domain',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='find search chinese pinyin tones colorize',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'colorize_pinyin=colorize_pinyin:main',
        ],
    },
)
