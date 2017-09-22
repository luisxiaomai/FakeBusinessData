#!/usr/bin/env python
# coding=utf-8

import os
import io

from setuptools import setup, find_packages



version = '0.1.0'




setup(
    name='Faker',
    version=version,
    description="Faker is a Python package that help you fake realistic test data in CSV.",
    entry_points={
        'console_scripts': ['faker=faker.cli:execute_from_command_line','csvfaker = faker.csvfaker.csvfaker:main'],
    },
    keywords='faker data mock',
    license='MIT License',
    packages=find_packages(),
    platforms=["any"],
    install_requires=[
        "python-dateutil>=2.4",
        "six",
    ],

    extras_require={
        ':python_version=="2.7"': [
            'ipaddress',
        ],
        ':python_version=="3.0"': [
            'importlib',
        ],
        ':python_version=="3.2"': [
            'ipaddress',
        ],
    }
)
