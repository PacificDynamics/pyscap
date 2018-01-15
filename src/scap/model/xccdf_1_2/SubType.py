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

from . import SUB_USE_ENUMERATION
from .IdRefType import IdRefType
from expatriate.model.decorators import *

logger = logging.getLogger(__name__)

@attribute(local_name='use', enum=SUB_USE_ENUMERATION, default='value')
@element(local_name='sub', cls=defer_class_load('scap.model.xccdf_1_2.SubType', 'SubType'), list='subs')
class SubType(IdRefType):
    pass
