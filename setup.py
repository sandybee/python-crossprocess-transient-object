#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import os


def get_module_version():
    """
    get version number from the VERSION file at the root of the project
    """
    version_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'VERSION'
        )
    )

    return open(version_file, 'r').read()

setup(
    name='crossprocess',
    version=get_module_version(),
    description='How to keep object internals between processes',
    url='http://github.com/sandybee/python-crossprocess-transient-object',
    author='Eric VILLARD',
    author_email='dev@eviweb.fr',
    license='MIT',
    packages=['crossprocess'],
    zip_safe=False
)
