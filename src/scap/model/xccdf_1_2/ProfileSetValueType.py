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

from expatriate.model.xs.StringType import StringType
from expatriate.model.decorators import *
from expatriate.model.xs.NCNameType import NCNameType

logger = logging.getLogger(__name__)

@attribute(local_name='idref', type=NCNameType, required=True)
class ProfileSetValueType(StringType):
    def apply(self, item):
        from scap.model.xccdf_1_1.ValueType import ValueType
        if not isinstance(item, ValueType):
            raise ValueError('Trying to set value (' + self.idref + ') on an item of the wrong type: ' + item.__class__.__name__)

        logger.debug('Setting value ' + item.id + ' to ' + self.value)
        item.value = self.value
