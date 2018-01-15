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

from .EntityStateAuditType import EntityStateAuditType
from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='account_logon', cls=EntityStateAuditType, min=0)
@element(local_name='account_management', cls=EntityStateAuditType, min=0)
@element(local_name='detailed_tracking', cls=EntityStateAuditType, min=0)
@element(local_name='directory_service_access', cls=EntityStateAuditType, min=0)
@element(local_name='logon', cls=EntityStateAuditType, min=0)
@element(local_name='object_access', cls=EntityStateAuditType, min=0)
@element(local_name='policy_change', cls=EntityStateAuditType, min=0)
@element(local_name='privilege_use', cls=EntityStateAuditType, min=0)
@element(local_name='system', cls=EntityStateAuditType, min=0)
class AuditEventPolicyStateElement(StateType):
    pass
