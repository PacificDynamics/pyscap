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
import re

from .xpath.Expression import Expression
from .xpath.Literal import Literal
from .xpath.Operator import Operator

logger = logging.getLogger(__name__)
class Node(object):
    FUNCTION_LIBRARY = {

    }
    def __init__(self, parent):
        self.parent = parent
        self._document = None

    def _tokenize(self, expr):
        tokens = []

        t = ''
        for i in range(len(expr)):
            if len(t) > 0:
                if t[0] in '\'"':
                    # string literal
                    t += expr[i]
                    if expr[i] == t[0] and t[-1] != '\\':
                        tokens.append(t)
                        t = ''
                elif t == '-':
                    tokens.append(t)
                    t = expr[i]
                elif re.fullmatch(r'[0-9.]+', t) and (expr[i].isdigit() or expr[i] == '.'):
                    t += expr[i]
                elif t[0] == '$' and expr[i].isalpha():
                    t += expr[i]
                elif t.isspace():
                    t = expr[i]
                elif t in ':/.!<>':
                    if t + expr[i] in ['::', '//', '..', '!=', '<=', '>=']:
                        tokens.append(t + expr[i])
                        t = ''
                    else:
                        tokens.append(t)
                        t = expr[i]
                elif t in '()[]@,\'"*|+=':
                    tokens.append(t)
                    t = expr[i]
                elif expr[i] in '()[]@,\'"*|+=':
                    tokens.append(t)
                    tokens.append(expr[i])
                    t = ''
                elif expr[i].isalnum() or expr[i] == '-':
                    t += expr[i]
                else:
                    tokens.append(t)
                    t = expr[i]
            else:
                if expr[i].isspace():
                    continue
                t += expr[i]
        if t != '':
            tokens.append(t)

        return tokens

    def xpath(self, expr, version=1.0, context_position=1, context_size=1, variables={}):
        if version != 1.0:
            raise NotImplementedError('Only XPath 1.0 has been implemented')

        tokens = self._tokenize(expr)
        logger.debug('Tokens: ' + str(tokens))

        stack = []
        for token in tokens:
            if token == '(':
                e = Expression()
                logger.debug('Processing sub expression ' + str(e))
                stack.append(e)
            elif token == ')':
                logger.debug('End of sub expression ' + str(e))
                i = stack.pop()
                logger.debug('Popped ' + str(i) + ' off stack, adding to expression ' + str(stack[-1]))
                stack[-1].children.append(i)
            elif re.fullmatch(r'[0-9.]+', token):
                if '.' in token:
                    l = Literal(float(token))
                else:
                    l = Literal(int(token))

                if len(stack) > 0 and isinstance(stack[-1], Operator):
                    op = stack.pop()
                    op.children.append(l)
                    logger.debug('Pushing ' + str(op) + ' back on stack')
                    stack.append(op)
                else:
                    logger.debug('Pushing ' + str(l) + ' on stack')
                    stack.append(l)
            elif token[0] in '\'"':
                l = Literal(token[1:-2])
                logger.debug('Pushing ' + str(l) + ' on stack')
                stack.append(l)
            elif token in Operator.OPERATORS:
                if token == '-' and (len(stack) == 0 or isinstance(stack[-1], Operator)):
                    o = Operator('negate')
                else:
                    o = Operator(token)
                    o.children.append(stack.pop())
                logger.debug('Pushing ' + str(o) + ' on stack')
                stack.append(o)
            else:
                raise ValueError('Unknown token: ' + str(token))

        while(len(stack) > 1):
            i = stack.pop()
            logger.debug('Adding ' + str(i) + ' to children of ' + str(stack[-1]))
            stack[-1].children.append(i)
        i = stack.pop()
        logger.debug('Final pop off stack got ' + str(i))

        return i.evaluate()

    def get_type(self):
        raise NotImplementedError('get_type has not been implemented in class ' + self.__class__.__name__)

    def escape(self, text):
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        return text

    def unescape(self, text):
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&apos;')
        return text