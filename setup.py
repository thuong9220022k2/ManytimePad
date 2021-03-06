#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='mtp',
    version='1.0.0',
    description='Many-Time Pad Interactive',
    packages=find_packages(),
    scripts=['cli.py'],
    install_requires=[
        "urwid==2.0.1"
    ],
    entry_points={
    	'console_scripts': ['mtp=cli:main']
    }
)