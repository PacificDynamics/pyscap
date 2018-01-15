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

from ..EntityStateType import EntityStateType

from .EntityStateNTUserAccountTypeType import EntityStateNTUserAccountTypeType
from .EntityStateRegistryTypeType import EntityStateRegistryTypeType
from .EntityStateRegistryTypeType import EntityStateRegistryTypeType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='key', cls=EntityStateType, min=0)
@element(local_name='name', cls=EntityStateType, min=0)
@element(local_name='sid', cls=EntityStateType, min=0)
@element(local_name='username', cls=EntityStateType, min=0)
@element(local_name='account_type', cls=EntityStateNTUserAccountTypeType, min=0)
@element(local_name='logged_on', cls=EntityStateType, min=0)
@element(local_name='enabled', cls=EntityStateType, min=0)
@element(local_name='date_modified', cls=EntityStateType, min=0)
@element(local_name='days_since_modified', cls=EntityStateType, min=0)
@element(local_name='filepath', cls=EntityStateType, min=0)
@element(local_name='last_write_time', cls=EntityStateType, min=0)
@element(local_name='type', cls=EntityStateRegistryTypeType, min=0)
@element(local_name='value', cls=EntityStateType, min=0)
class NtUserStateElement(StateType):
    pass
