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

import logging

from scap.model.xhtml import *
from scap.Model import Model

logger = logging.getLogger(__name__)
class SelectTag(Model):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'optgroup', 'list': '_elements', 'class': 'OptGroupTag', 'max': None},
            {'tag_name': 'option', 'list': '_elements', 'class': 'OptionTag', 'max': None},
        ],
        'attributes': {
            'name': {'type': 'StringType'},
            'size': {'type': 'NumberType'},
            'multiple': {'enum': ['multiple']},
            'disabled': {'enum': ['disabled']},
            'tabindex': {'type': 'TabIndexNumberType'},
            'onfocus': {'type': 'ScriptType'},
            'onblur': {'type': 'ScriptType'},
            'onchange': {'type': 'ScriptType'},
        },
    }
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_attrs)
