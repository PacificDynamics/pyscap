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
from scap.model.xhtml.AContentType import AContentType

logger = logging.getLogger(__name__)
class ATag(AContentType):
    MODEL_MAP = {
        'attributes': {
            'charset': {'type': 'CharsetType'},
            'type': {'type': 'ContentTypeType'},
            'name': {'type': 'NMTokenType'},
            'href': {'type': 'UriType'},
            'hreflang': {'type': 'LanguageCodeType'},
            'rel': {'type': 'LinkTypesType'},
            'rev': {'type': 'LinkTypesType'},
            'shape': {'type': 'ShapeType', 'default': 'rect'},
            'coords': {'type': 'CoordsType'},
        },
    }
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_attrs)
    MODEL_MAP['attributes'].update(ATTRIBUTE_GROUP_focus)
