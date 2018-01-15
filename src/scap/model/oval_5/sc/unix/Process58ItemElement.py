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

from .EntityItemCapabilityType import EntityItemCapabilityType

logger = logging.getLogger(__name__)

@element(local_name='command_line', min=0, cls=EntityItemType, max=1)
@element(local_name='exec_time', min=0, cls=EntityItemType, max=1)
@element(local_name='pid', min=0, cls=EntityItemType, max=1)
@element(local_name='ppid', min=0, cls=EntityItemType, max=1)
@element(local_name='priority', min=0, cls=EntityItemType, max=1)
@element(local_name='ruid', min=0, cls=EntityItemType, max=1)
@element(local_name='scheduling_class', min=0, cls=EntityItemType, max=1)
@element(local_name='start_time', min=0, cls=EntityItemType, max=1)
@element(local_name='tty', min=0, cls=EntityItemType, max=1)
@element(local_name='user_id', min=0, cls=EntityItemType, max=1)
@element(local_name='exec_shield', min=0, cls=EntityItemType, max=1)
@element(local_name='loginuid', min=0, cls=EntityItemType, max=1)
@element(local_name='posix_capability', list='posix_capabilitys', min=0, cls=EntityItemCapabilityType, max=None)
@element(local_name='selinux_domain_label', list='selinux_domain_labels', min=0, cls=EntityItemType, max=None)
@element(local_name='session_id', min=0, cls=EntityItemType, max=1)
class Process58ItemElement(ItemType):
    pass
