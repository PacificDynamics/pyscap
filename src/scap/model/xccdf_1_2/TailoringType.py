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
from .TailoringIdPattern import TailoringIdPattern
from expatriate.model.xs.IdType import IdType
from .TailoringBenchmarkReferenceType import TailoringBenchmarkReferenceType
from .StatusType import StatusType
from .DcStatusType import DcStatusType
from .TailoringVersionType import TailoringVersionType
from .MetadataType import MetadataType
from .ProfileType import ProfileType
from .SignatureType import SignatureType

logger = logging.getLogger(__name__)

@attribute(local_name='id', type=TailoringIdPattern, required=True)
@attribute(local_name='Id', type=IdType)
@element(local_name='benchmark', cls=TailoringBenchmarkReferenceType, min=0, max=1)
@element(local_name='status', cls=StatusType, list='statuses', min=0, max=None)
@element(local_name='dc-status', cls=DcStatusType, list='dc_statuses', min=0, max=None)
@element(local_name='version', cls=TailoringVersionType, min=1, max=1)
@element(local_name='metadata', cls=MetadataType, list='metadata', min=0, max=None)
@element(local_name='Profile', cls=ProfileType, list='profiles', min=1, max=None)
@element(local_name='signature', cls=SignatureType, min=0, max=None)
class TailoringType(Model):
    pass
