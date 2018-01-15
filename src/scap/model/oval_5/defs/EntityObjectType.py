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
from expatriate.model.xs.BooleanType import BooleanType
from expatriate.model.xs.FloatType import FloatType
from expatriate.model.xs.HexBinaryType import HexBinaryType
from expatriate.model.xs.IntegerType import IntegerType
from expatriate.model.xs.StringType import StringType

from .. import CHECK_ENUMERATION
from .. import DATATYPE_ENUMERATION
from .. import OPERATION_ENUMERATION
from .. import VariableIdPattern

from . import EntityObjectFieldType

logger = logging.getLogger(__name__)

@attribute(local_name='datatype', enum=DATATYPE_ENUMERATION, default='string')
@attribute(local_name='operation', enum=OPERATION_ENUMERATION, default='equals')
@attribute(local_name='mask', type=BooleanType, default=False)
@attribute(local_name='var_ref', type=VariableIdPattern)
@attribute(local_name='var_check', enum=CHECK_ENUMERATION)
@element(local_name='field', list='fields', cls=EntityObjectFieldType, min=0, max=None)
class EntityObjectType(Model):
    def resolve_values(self, host, content, imports, export_names):
        if self.var_ref is not None:
            var = content.find_reference(self.var_ref)
            return var.resolve_values(content, imports, export_names, self.var_check)
        else:
            logger.debug('Resolved values to ' + str(([self.get_value()], self.datatype, self.operation, self.mask)))
            return [self.get_value()], self.datatype, self.operation, self.mask

    def __str__(self):
        return super(EntityObjectType, self).__str__() + ' = ' + str(self.get_value())

    DATATYPE_CLASS_MAPPING = {
        'binary': HexBinaryType,
        'boolean': BooleanType,
        'evr_string': StringType,
        'debian_evr_string': StringType,
        'fileset_revision': StringType,
        'float': FloatType,
        'ios_version': StringType,
        'int': IntegerType,
        'ipv4_address': StringType,
        'ipv6_address': StringType,
        'string': StringType,
        'version': StringType,
    }

    DATATYPE_ALLOWED_OPERATIONS = {
        'binary': [
            'equals',
            'not equal',
        ],
        'boolean': [
            'equals',
            'not equal',
        ],
        'evr_string': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
        ],
        'debian_evr_string': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
        ],
        'fileset_revision': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
        ],
        'float': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
        ],
        'ios_version': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
        ],
        'int': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
            'bitwise and',
            'bitwise or',
        ],
        'ipv4_address': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
            'subset of',
            'superset of',
        ],
        'ipv6_address': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
            'subset of',
            'superset of',
        ],
        'string': [
            'equals',
            'not equal',
            'case insensitive equals',
            'case insensitive not equal',
            'pattern match',
        ],
        'version': [
            'equals',
            'not equal',
            'greater than',
            'greater than or equal',
            'less than',
            'less than or equal',
        ],
        'record': [
            'equals',
            #'not equal', # not in spec
        ],
    }

    def _from_xml(self, parent, el):
        super(EntityObjectType, self)._from_xml(parent, el)

        if (
            self.datatype in EntityObjectType.DATATYPE_ALLOWED_OPERATIONS
            and self.operation not in EntityObjectType.DATATYPE_ALLOWED_OPERATIONS[self.datatype]
        ):
            raise ValueError('Invalid operation ' + self.operation + ' on datatype ' + self.datatype + ' for ' + self.__class__.__name__)

        if el.text is not None:
            if el.text == '':
                self.set_value('')
            elif self.datatype in EntityObjectType.DATATYPE_CLASS_MAPPING:
                self.set_value(EntityObjectType.DATATYPE_CLASS_MAPPING[self.datatype]().parse_value(el.text))

                # allow StringType-like enums & patterns
                if hasattr(self, 'get_value_enum') and self.get_value() not in self.get_value_enum():
                    raise ValueError(self.__class__.__name__ + ' requires a value in ' + str(self.get_value_enum()))
                if hasattr(self, 'get_value_pattern') and not re.fullmatch(self.get_value_pattern(), self.get_value()):
                    raise ValueError(self.__class__.__name__ + ' requires a value matching ' + self.get_value_pattern())

    def to_xml(self):
        el =  super(EntityObjectType, self).to_xml()
        if (
            self.datatype in EntityObjectType.DATATYPE_ALLOWED_OPERATIONS
            and self.operation not in EntityObjectType.DATATYPE_ALLOWED_OPERATIONS[self.datatype]
        ):
            raise ValueError('Invalid operation ' + self.operation + ' on datatype ' + self.datatype + ' for ' + self.__class__.__name__)

        if self.datatype in EntityObjectType.DATATYPE_CLASS_MAPPING:
            el.text = EntityObjectType.DATATYPE_CLASS_MAPPING[self.datatype]().produce_value(self.get_value())

        return el
