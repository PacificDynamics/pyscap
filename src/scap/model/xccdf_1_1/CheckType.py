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
from expatriate.model.xs.AnyUriType import AnyUriType
from expatriate.model.xs.NCNameType import NCNameType
from expatriate.model.xs.StringType import StringType

from .CheckContentRefType import CheckContentRefType
from .CheckContentType import CheckContentType
from .CheckExportType import CheckExportType
from .CheckImportType import CheckImportType
from .MessageType import MessageType

logger = logging.getLogger(__name__)

@attribute(local_name='system', type=AnyUriType, required=True)
@attribute(local_name='id', type=NCNameType)
@attribute(local_name='selector', default='', type=StringType)
@element(local_name='check-import', cls=CheckImportType, list='check_imports', min=0, max=None)
@element(local_name='check-export', cls=CheckExportType, list='check_exports', min=0, max=None)
@element(local_name='check-content-ref', cls=CheckContentRefType, list='check_content_refs', min=0, max=None)
@element(local_name='check-content', cls=CheckContentType, min=0, max=1)
class CheckType(Model):
    def __str__(self):
        s = self.__class__.__name__ + ' '

        if self.id is not None:
            s += self.id + ':'

        s += self.system + ':'

        s += '['
        if len(self.check_content_refs) > 0:
            for ref in self.check_content_refs:
                if ref.name is None:
                    s += ref.href + ', '
                else:
                    s += ref.href + '#' + ref.name + ', '
        return s + ']'

    def check(self, benchmark, host):
        if self.id is not None and self.id in host.facts['checklist'][benchmark.id]['check']:
            return host.facts['checklist'][benchmark.id]['check'][self.id]

        if self.system not in CHECK_SYSTEM_ENUMERATION:
            return {
                'result': 'error',
                'messages': [
                    MessageType(
                        tag_name='message',
                        value='Unknown system ' + self.system,
                        severity='error'
                    ),
                ],
                'imports': {},
            }

        # This element identifies a value to be retrieved from the checking
        # system during testing of a target system. The value-id attribute is
        # merely a locally unique id. It must match the id attribute of a Value
        # object in the Benchmark.
        import_names = []
        for check_import in self.check_imports:
            import_names += check_import.import_name

        # This specifies a mapping from an XCCDF Value object to a checking
        # system variable. The value-id attribute must match the id attribute of
        # a Value object in the Benchmark.
        exports = {}
        for check_export in self.check_exports:
            exports.update(check_export.map(benchmark))

        # If two or more check-content-ref elements appear, then they represent
        # alternative locations from which a tool may obtain the check content.
        # Tools should process the alternatives in order, and use the first one
        # found.
        result = {
            'result': 'notchecked',
            'messages': [
                MessageType(
                    tag_name='message',
                    value='No checks available',
                    severity='error'
                ),
            ],
            'imports': {}
        }
        for check_ref in self.check_content_refs:
            try:
                result = check_ref.check(benchmark, host, exports, import_names)
            except:
                result['result'] = 'error'
                result['messages'] = [
                    MessageType(
                        tag_name='message',
                        value='Error using check reference ' + str(check_ref),
                        severity='error'
                    )
                ]
                break

            if result['result'] not in ['error', 'unknown', 'notchecked']:
                break
            # otherwise, we keep trying check_refs

        # If both check-content-ref elements and check-content elements appear,
        # tools should use the check-content only if all references are
        # inaccessible.
        if result['result'] not in ['error', 'unknown', 'notchecked']:
            # try check content
            try:
                result = self.check_content.check(benchmark, host, exports, import_names)
            except:
                result['result'] = 'error'
                result['messages'] = [
                    MessageType(
                        tag_name='message',
                        value='Error using check content ' + str(self.check_content),
                        severity='error'
                    )
                ]

        for check_import in self.check_imports:
            if (
                'imports' not in result
                or check_import.import_name not in result['imports']
            ):
                raise ValueError('Expected import not returned by check: ' + check_import.import_name)

        # TODO need to assign imports to import variables

        if self.id is not None:
            host.facts['checklist'][benchmark.id]['check'][self.id] = result

        return result
