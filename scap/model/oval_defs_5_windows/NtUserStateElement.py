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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class NtUserStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'ntuser_state',
        'elements': [
            {'tag_name': 'key', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'name', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'sid', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'username', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'account_type', 'class': 'EntityStateNTUserAccountTypeType', 'min': 0},
            {'tag_name': 'logged_on', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'enabled', 'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            {'tag_name': 'date_modified', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'days_since_modified', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'filepath', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'last_write_time', 'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            {'tag_name': 'type', 'class': 'oval_defs_5.EntityStateRegistryTypeType', 'min': 0},
            {'tag_name': 'value', 'class': 'oval_defs_5.EntityStateAnySimpleType', 'min': 0},
        ],
    }
