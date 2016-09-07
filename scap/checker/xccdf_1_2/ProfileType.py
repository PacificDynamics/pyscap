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
import sys

from scap.Checker import Checker
from scap.model.xccdf_1_2.RuleType import RuleType
from scap.model.xccdf_1_2.GroupType import GroupType
from scap.model.xccdf_1_2.ValueType import ValueType

logger = logging.getLogger(__name__)
class ProfileType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(ProfileType, self).__init__(host, content, parent, args)

        if hasattr(content, 'extends'):
            raise NotImplementedError('@extends is not supported for Profile tags')

        # visit nodes of the benchmark & accumulate the values & rules
        self.value_content = {}
        self.value_operator = {}
        self.value_setting = {}

        self.rule_content = {}
        self.rule_weight = {}
        self.rule_severity = {}
        self.rule_role = {}
        self.rule_check = {}

        for value in self.content.parent.values.values():
            value.accept(self)
        for rule in self.content.parent.rules.values():
            rule.accept(self)
        for group in self.content.parent.groups.values():
            group.accept(self)

        self.checkers = {}
        for rule_id in self.rule_content:
            self.checkers[rule_id] = Checker.load(self.host, self.rule_check[rule_id], self, args)

    def visit(self, content):
        if isinstance(content, GroupType):
            group_id = content.id
            if group_id in self.content.selects and not self.content.selects[group_id].selected:
                return

            for value in content.values.values():
                value.accept(self)
            for rule in content.rules.values():
                rule.accept(self)
            for group in content.groups.values():
                group.accept(self)

        elif isinstance(content, ValueType):
            value_id = content.id
            logger.debug('Selecting value: ' + value_id)
            self.value_content[value_id] = content

            # set the default operator
            self.value_operator[value_id] = content.operator

            # set the default value
            if hasattr(content, 'complex_defaults') and len(content.complex_defaults) > 0:
                if None in content.complex_defaults:
                    self.value_setting[value_id] = content.complex_defaults[None].get_text()
                else:
                    self.value_setting[value_id] = list(content.complex_defaults.values())[0].get_text()
            elif hasattr(content, 'defaults') and len(content.defaults) > 0:
                if None in content.defaults:
                    self.value_setting[value_id] = content.defaults[None].get_text()
                else:
                    self.value_setting[value_id] = list(content.defaults.values())[0].get_text()
            elif hasattr(content, 'complex_values') and len(content.complex_values) > 0:
                if None in content.complex_values:
                    self.value_setting[value_id] = content.complex_values[None].get_text()
                else:
                    self.value_setting[value_id] = list(content.complex_values.values())[0].get_text()
            elif hasattr(content, 'values') and len(content.values) > 0:
                if None in content.values:
                    self.value_setting[value_id] = content.values[None].get_text()
                else:
                    self.value_setting[value_id] = list(content.values.values())[0].get_text()
            else:
                raise ValueError('Cannot determine profile value default: ' + value_id)
            logger.debug('Value ' + value_id + ' of type ' + self.value_content[value_id].type + ' ' + self.value_operator[value_id] + ' setting ' + str(self.value_setting[value_id]))

            if value_id in self.content.set_complex_values:
                logger.debug('Setting complex value: ' + value_id)
                self.value_setting[value_id] = self.content.set_complex_values[value_id].items
            elif value_id in self.content.set_values:
                logger.debug('Setting value: ' + value_id)
                self.value_setting[value_id] = self.content.set_values[value_id].get_text()
            elif value_id in self.content.refine_values:
                logger.debug('Refining value: ' + value_id)
                refine_value = self.content.refine_values[value_id]
                if hasattr(refine_value, 'operator'):
                    self.value_operator[value_id] = refine_value.operator
                if hasattr(refine_value, 'selector'):
                    self.value_setting[value_id] = content.values[refine_value.selector].get_text()
            else:
                return
            logger.debug('Overridden value ' + value_id + ' of type ' + self.value_content[value_id].type + ' ' + self.value_operator[value_id] + ' setting ' + str(self.value_setting[value_id]))

        elif isinstance(content, RuleType):
            rule_id = content.id
            if rule_id in self.content.selects and self.content.selects[rule_id].selected:
                self.rule_content[rule_id] = content
                logger.debug('Selecting rule ' + rule_id)
            else:
                logger.debug('Not selecting rule ' + rule_id)
                return

            # set rule defaults
            self.rule_weight[rule_id] = content.weight
            self.rule_severity[rule_id] = content.severity
            self.rule_role[rule_id] = content.role
            if hasattr(content, 'complex_check'):
                self.rule_check[rule_id] = content.complex_check
            elif hasattr(content, 'checks') and len(content.checks) > 0:
                if None in content.checks:
                    self.rule_check[rule_id] = content.checks[None]
                else:
                    self.rule_check[rule_id] = list(content.checks.values())[0]
            else:
                raise ValueError('Cannot determine profile rule check default: ' + rule_id)
            logger.debug('Rule ' + rule_id + ' weight: ' + self.rule_weight[rule_id] + ' severity: ' + self.rule_severity[rule_id] + ' role: ' + self.rule_role[rule_id] + ' check: ' + str(self.rule_check[rule_id]))

            if rule_id in self.content.refine_rules:
                logger.debug('Refining rule: ' + rule_id)
                refine_rule = self.content.refine_rules[rule_id]
                if hasattr(refine_rule, 'weight'):
                    self.rule_weight[rule_id] = refine_rule.weight
                if hasattr(refine_rule, 'selector'):
                    self.rule_check[rule_id] = content.checks[refine_rule.selector]
                if hasattr(refine_rule, 'severity'):
                    self.rule_severity[rule_id] = refine_rule.severity
                if hasattr(refine_rule, 'role'):
                    self.rule_role[rule_id] = refine_rule.role
                logger.debug('Overridden rule ' + rule_id + ' weight: ' + self.rule_weight[rule_id] + ' severity: ' + self.rule_severity[rule_id] + ' role: ' + self.rule_role[rule_id] + ' check: ' + str(self.rule_check[rule_id]))

    def check(self):
        results = {'rule_results': {}}
        for rule_id, rule_checker in list(self.rule_checkers.items()):
            results['rule_results'][rule_id] = rule_checker.check()
        return results
