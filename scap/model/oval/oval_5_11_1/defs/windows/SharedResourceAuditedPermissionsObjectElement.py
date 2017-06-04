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

from scap.model.oval.oval_5_11_1 import *
from scap.model.oval.oval_5_11_1.defs import *
from scap.model.oval.oval_5_11_1.defs.windows import *
from scap.model.oval.oval_5_11_1.defs.windows.ObjectType import ObjectType

logger = logging.getLogger(__name__)
class SharedResourceAuditedPermissionsObjectElement(ObjectType):
    MODEL_MAP = {
        'tag_name': 'sharedresourceauditedpermissions_object',
        'elements': [
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'set', 'class': 'scap.model.oval.oval_5_11_1.defs.SetElement', 'min': 0},
            {'tag_name': 'behaviors', 'class': 'SharedResourceAuditedPermissionsBehaviors', 'min': 0},
            {'tag_name': 'netname', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityObjectStringType'},
            {'tag_name': 'trustee_sid', 'class': 'scap.model.oval.oval_5_11_1.defs.EntityObjectStringType'},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-definitions-5', 'tag_name': 'filter', 'class': 'scap.model.oval.oval_5_11_1.defs.FilterElement', 'min': 0, 'max': None},
        ],
    }
