# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

from scap.Model import Model
from scap.model.decorators import *
from scap.model.types import *

class InitFixture(Model):
    MODEL_MAP = {
        'tag_name': 'InitFixture',
        'attributes': {
            'attr': {},
            'in_attr': {'in': 'test_attr'},
            'dash-attr': {},
            'default_attr': {'default': 'Default'},
        },
        'elements': [
            {'tag_name': 'list',    'list': 'list_', 'class': 'EnclosedFixture'},
            {'tag_name': 'dict',    'dict': 'dict_', 'class': 'EnclosedFixture'},
            {'tag_name': 'in_test', 'in': 'test_in', 'class': 'EnclosedFixture'},
            {'tag_name': 'dash-test', 'class': 'EnclosedFixture'},
            {'xmlns': 'http://jaymes.biz/test2', 'tag_name': '*', 'in': 'test2_elements'},
            {'tag_name': '*'},
        ]
    }
