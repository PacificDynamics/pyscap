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

from scap.model.oval_defs_5_windows.State import State
import logging

logger = logging.getLogger(__name__)
class regkeyauditedpermissions_state(State)
    def __init__(self):
        super(regkeyauditedpermissions_state, self).__init__(
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_state')

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}hive',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}trustee_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_delete',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_read_control',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_dac',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_owner',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_synchronize',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_system_security',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_read',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_write',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_execute',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_all',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_query_value',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_set_value',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_create_sub_key',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_enumerate_sub_keys',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_notify',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_create_link',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_wow64_64key',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_wow64_32key',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_wow64_res',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}windows_view',
        ])
