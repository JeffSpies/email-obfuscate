#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()
# history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='email_obfuscator',
    version='0.1.0',
    description='An empirically-based, email obfuscation library for Python',
    long_description=readme # + '\n\n' + history,
    author='Jeff Spies',
    author_email='jspies@gmail.com',
    url='https://github.com/jeffspies/py-email-obfuscator',
    packages=[
        'email_obfuscator',
    ],
    package_dir={'email_obfuscator':
                 'email_obfuscator'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache2",
    zip_safe=False,
    keywords='email obfuscate obfuscation obfuscator spam',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
    # test_suite='tests',
    # tests_require=test_requirements
)