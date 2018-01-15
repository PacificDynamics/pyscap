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

from .EntityItemAdsTypeType import EntityItemAdsTypeType
from .EntityItemNamingContextType import EntityItemNamingContextType

logger = logging.getLogger(__name__)

@element(local_name='naming_context', max=1, min=0, cls=EntityItemNamingContextType)
@element(local_name='relative_dn', max=1, nillable=True, min=0, cls=EntityItemType)
@element(local_name='attribute', max=1, nillable=True, min=0, cls=EntityItemType)
@element(local_name='object_class', max=1, min=0, cls=EntityItemType)
@element(local_name='adstype', max=1, min=0, cls=EntityItemAdsTypeType)
@element(local_name='value', max=None, list='values', min=0, cls=EntityItemType)
class ActiveDirectoryItemElement(ItemType):
    pass
