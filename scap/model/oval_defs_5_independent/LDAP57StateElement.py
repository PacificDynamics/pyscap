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
class LDAP57StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'ldap57_state',
        'elements': [
            {'tag_name': 'suffix', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'relative_dn', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'attribute', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'object_class', 'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            {'tag_name': 'ldaptype', 'class': 'EntityStateLdaptypeType', 'min': 0},
            {'tag_name': 'value', 'class': 'oval_defs_5.EntityStateRecordType', 'min': 0},
        ],
    }
