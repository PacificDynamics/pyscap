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

from .ChoiceGroupIDPattern import ChoiceGroupIDPattern
from .ChoiceIDPattern import ChoiceIDPattern
from .ChoiceType import ChoiceType
from .QuestionType import QuestionType

logger = logging.getLogger(__name__)

@attribute(local_name='default_answer_ref', type=ChoiceIDPattern)
@element(local_name='choice', list='choices', cls=ChoiceType, min=0, max=None)
@element(local_name='choice_group_ref', list='choice_group_refs', type=ChoiceGroupIDPattern, min=0, max=None)
class ChoiceQuestionType(QuestionType):
    pass
