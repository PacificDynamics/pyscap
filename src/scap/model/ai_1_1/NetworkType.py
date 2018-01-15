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

from .IPNetRangeType import IPNetRangeType
from .ITAssetType import ITAssetType
from .NetworkCIDRType import NetworkCIDRType
from .NetworkNameType import NetworkNameType

logger = logging.getLogger(__name__)

@element(local_name='network-name', cls=NetworkNameType, min=0)
@element(local_name='ip-net-range', cls=IPNetRangeType, min=0)
@element(local_name='cidr', cls=NetworkCIDRType, min=0)
class NetworkType(ITAssetType):
    pass
