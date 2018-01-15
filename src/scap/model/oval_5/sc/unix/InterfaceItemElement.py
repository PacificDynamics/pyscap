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

from ..EntityItemIPAddressStringType import EntityItemIPAddressStringType
from ..EntityItemType import EntityItemType

from .EntityItemInterfaceType import EntityItemInterfaceType

logger = logging.getLogger(__name__)

@element(local_name='name', min=0, cls=EntityItemType, max=1)
@element(local_name='type', min=0, cls=EntityItemInterfaceType, max=1)
@element(local_name='hardware_addr', min=0, cls=EntityItemType, max=1)
@element(local_name='inet_addr', min=0, cls=EntityItemIPAddressStringType, max=1)
@element(local_name='broadcast_addr', min=0, cls=EntityItemIPAddressStringType, max=1)
@element(local_name='netmask', min=0, cls=EntityItemIPAddressStringType, max=1)
@element(local_name='flag', list='flags', min=0, cls=EntityItemType, max=None)
class InterfaceItemElement(ItemType):
    pass
