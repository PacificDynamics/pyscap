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

from scap.model.decorators import *

from ..EntityStateType import EntityStateType

from .StateType import StateType

logger = logging.getLogger(__name__)

@element(local_name='printer_name', cls=EntityStateType, min=0)
@element(local_name='trustee_sid', cls=EntityStateType, min=0)
@element(local_name='standard_delete', cls=EntityStateType, min=0)
@element(local_name='standard_read_control', cls=EntityStateType, min=0)
@element(local_name='standard_write_dac', cls=EntityStateType, min=0)
@element(local_name='standard_write_owner', cls=EntityStateType, min=0)
@element(local_name='standard_synchronize', cls=EntityStateType, min=0)
@element(local_name='access_system_security', cls=EntityStateType, min=0)
@element(local_name='generic_read', cls=EntityStateType, min=0)
@element(local_name='generic_write', cls=EntityStateType, min=0)
@element(local_name='generic_execute', cls=EntityStateType, min=0)
@element(local_name='generic_all', cls=EntityStateType, min=0)
@element(local_name='printer_access_administer', cls=EntityStateType, min=0)
@element(local_name='printer_access_use', cls=EntityStateType, min=0)
@element(local_name='job_access_administer', cls=EntityStateType, min=0)
@element(local_name='job_access_read', cls=EntityStateType, min=0)
class PrinterEffectiveRightsStateElement(StateType):
    pass
