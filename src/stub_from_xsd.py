#!/usr/bin/env python

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

import argparse
import logging
import os
import expatriate

from scap import register_namespaces
from scap.ColorFormatter import ColorFormatter
from scap.Model import Model
from scap.model.xs.SchemaElement import SchemaElement

rootLogger = logging.getLogger()
ch = logging.StreamHandler()
ch_formatter = ColorFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(ch_formatter)
rootLogger.addHandler(ch)

rootLogger.setLevel(logging.INFO)
logger = logging.getLogger(__name__)

register_namespaces()

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--content', required=True, nargs=1)
arg_parser.add_argument('--output', required=True, nargs=1)
args = vars(arg_parser.parse_args())
for arg in args:
    logger.debug('Argument: ' + arg + ' = ' + str(args[arg]))

if args['content'] is None or len(args['content']) == 0:
    arg_parser.error('No content specified (--content)')
if args['output'] is None or len(args['output']) == 0:
    arg_parser.error('No output specified (--output)')

content = args['content'][0]
logger.debug('Loading content file: ' + content)
with open(content, mode='r', encoding='utf_8') as f:
    doc = expatriate.Document()
    doc.parse(f.read())
    content = doc.root_element
    model = Model.load(None, content)
    if not isinstance(model, SchemaElement):
        arg_parser.error('Invalid content. Expecting xsd (XMLSchema) file')

rootLogger.setLevel(logging.DEBUG)

output = args['output'][0]
logger.debug('Creating class stubs in path: ' + output)

if not os.path.isdir(output):
    os.makedirs(output, mode=0o755, exist_ok=True)

model.stub(output)
