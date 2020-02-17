#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', "requests" ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'betamax']

setup(
    author="Sommalia",
    author_email='sommalia@protonmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Wrapper package for using the moco api interface",
    entry_points={
        'console_scripts': [
            'moco_wrapper=moco_wrapper.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='moco_wrapper',
    name='moco_wrapper',
    packages=find_packages(include=['moco_wrapper']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sommalia/moco-wrapper',
    version='0.3.0.post2',
    zip_safe=False,
)