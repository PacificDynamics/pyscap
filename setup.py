#!/usr/bin/env python

# Copyright 2016 Casey Jaymes

# This file is part of pyscap.
#
# Expatriate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyscap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyscap.  If not, see <http://www.gnu.org/licenses/>.

from glob import glob
from os.path import join
from os.path import dirname
import re
from setuptools import find_packages
from setuptools import setup

with open(join(dirname(__file__), 'VERSION.txt'), 'r') as f:
    VERSION = f.read().strip()

with open(join(dirname(__file__), 'README.rst'), 'r') as f:
    README = f.read()

with open(join(dirname(__file__), 'CHANGELOG.rst'), 'r') as f:
    CHANGELOG = f.read()

with open(join(dirname(__file__), 'CLASSIFIERS.txt'), 'r') as f:
    CLASSIFIERS = [line.strip() for line in f]

with open(join(dirname(__file__), 'KEYWORDS.txt'), 'r') as f:
    KEYWORDS = ' '.join([line.strip() for line in f])

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    REQUIREMENTS = [line.strip() for line in f]

long_description = README + '\n' + CHANGELOG

setup(name='pyscap',
    version=VERSION,
    license='GPL',
    description='A security scanner consuming and generating SCAP content',
    long_description=long_description,
    author='Casey Jaymes',
    author_email='cjaymes@gmail.com',
    url='https://github.com/cjaymes/pyscap',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=REQUIREMENTS,
    tests_require=[
        'pytest',
    ],
    zip_safe=True,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyscap = scap:main',
        ]
    },
    python_requires='>=3',
)
