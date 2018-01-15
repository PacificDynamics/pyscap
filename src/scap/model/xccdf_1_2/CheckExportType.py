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
from expatriate.model.xs.NCNameType import NCNameType
from expatriate.model.xs.StringType import StringType

logger = logging.getLogger(__name__)

@attribute(local_name='value-id', type=NCNameType, required=True)
@attribute(local_name='export-name', type=StringType, required=True)
class CheckExportType(Model):
    def map(self, benchmark):
        # go through benchmark till we find value referenced by
        # check_export.value_id
        v = benchmark.find_reference(self.value_id)
        if v is None:
            raise ValueError('Could not find Value ' + self.value_id)

        # we assume value has been resolved

        return {self.export_name: v.value}
