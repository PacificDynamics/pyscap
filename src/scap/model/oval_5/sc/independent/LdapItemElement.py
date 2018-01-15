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

from expatriate.model.Model import Model
from expatriate.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

from ..EntityItemType import EntityItemType

from .EntityItemLdaptypeType import EntityItemLdaptypeType

logger = logging.getLogger(__name__)

@element(local_name='suffix', cls=EntityItemType, min=0, max=1)
@element(local_name='relative_dn', cls=EntityItemType, min=0, max=1, nillable=True)
@element(local_name='attribute', cls=EntityItemType, min=0, max=1, nillable=True)
@element(local_name='object_class', cls=EntityItemType, min=0, max=1)
@element(local_name='ldaptype', cls=EntityItemLdaptypeType, min=0, max=1)
@element(local_name='value', cls=EntityItemType, min=0, max=None)
class LdapItemElement(ItemType):
    pass
