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

from expatriate.model.decorators import *

from ..EntityObjectType import EntityObjectType

from .EntityObjectRegistryHiveType import EntityObjectRegistryHiveType
from .ObjectType import ObjectType
from .RegkeyAuditPermissions53Behaviors import RegkeyAuditPermissions53Behaviors

logger = logging.getLogger(__name__)

@element(local_name='behaviors', cls=RegkeyAuditPermissions53Behaviors, min=0)
@element(local_name='hive', cls=EntityObjectRegistryHiveType, min=0)
@element(local_name='key', cls=EntityObjectType, nillable=True, min=0)
@element(local_name='trustee_sid', cls=EntityObjectType, min=0)
class RegKeyAuditedPermissions53ObjectElement(ObjectType):
    pass
