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
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

from .EntityItemAuditType import EntityItemAuditType
from .EntityItemRegistryHiveType import EntityItemRegistryHiveType
from .EntityItemWindowsViewType import EntityItemWindowsViewType

logger = logging.getLogger(__name__)

@element(local_name='hive', max=1, min=0, cls=EntityItemRegistryHiveType)
@element(local_name='key', max=1, nillable=True, min=0, cls=EntityItemType)
@element(local_name='trustee_sid', max=1, min=0, cls=EntityItemType)
@element(local_name='trustee_name', max=1, min=0, cls=EntityItemType)
@element(local_name='standard_delete', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='standard_read_control', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='standard_write_dac', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='standard_write_owner', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='standard_synchronize', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='access_system_security', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='generic_read', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='generic_write', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='generic_execute', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='generic_all', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_query_value', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_set_value', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_create_sub_key', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_enumerate_sub_keys', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_notify', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_create_link', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_wow64_64key', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_wow64_32key', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='key_wow64_res', max=1, min=0, cls=EntityItemAuditType)
@element(local_name='windows_view', max=1, min=0, cls=EntityItemWindowsViewType)
class RegKeyAuditedPermissionsItemElement(ItemType):
    pass
