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

from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)
class InterfaceItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
            {'tag_name': 'name', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'index', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'type', 'max': 1, 'min': 0, 'class': 'EntityItemInterfaceTypeType'},
            {'tag_name': 'hardware_addr', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemType'},
            {'tag_name': 'inet_addr', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIPAddressStringType'},
            {'tag_name': 'broadcast_addr', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIPAddressStringType'},
            {'tag_name': 'netmask', 'max': 1, 'min': 0, 'class': 'scap.model.oval_5.sc.EntityItemIPAddressStringType'},
            {'tag_name': 'addr_type', 'max': None, 'list': 'addr_types', 'min': 0, 'class': 'EntityItemAddrTypeType'},
        ],
        'attributes': {
        },
    }

