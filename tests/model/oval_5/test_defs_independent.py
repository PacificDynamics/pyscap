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

import importlib
import logging
import os
import pathlib
import pkgutil
import sys

import pytest
# import all the classes in the package
import scap.model.oval_5.defs.independent as pkg
import scap.model.oval_5.sc.independent as pkg
from expatriate.model.Model import Model
from scap.Host import Host
from scap.Inventory import Inventory
from scap.model.oval_5.defs.EntityObjectType import EntityObjectType

for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass
for m_finder, m_name, m_ispkg in pkgutil.iter_modules(path=pkg.__path__):
    try:
        mod = importlib.import_module(pkg.__name__ + '.' + m_name, pkg.__name__)
        globals()[m_name] = getattr(mod, m_name)
    except AttributeError:
        pass

Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')
Model.register_namespace('scap.model.oval_5.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
Model.register_namespace('scap.model.oval_5.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
Model.register_namespace('scap.model.oval_5.sc', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5')
Model.register_namespace('scap.model.oval_5.sc.independent', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
try:
    with open(filename, 'r') as fp:
        logger.debug('Loading inventory from ' + filename)
        Inventory().readfp(fp)
except IOError:
    logger.error('Could not read from inventory file ' + filename)

host = Host.load('localhost')

@pytest.mark.parametrize("oval_family, env_var", (
    ('linux', 'HOME'),
    ('windows', 'USERNAME'),
))
def test_env_var58(oval_family, env_var):
    if host.facts['oval_family'] != oval_family:
        pytest.skip('Does not apply to platform')

    obj = EnvironmentVariable58ObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.name = EntityObjectType(value=env_var)
    obj.name.datatype = 'string'
    obj.name.operation = 'equals'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], EnvironmentVariable58ItemElement)
    assert items[0].status == 'exists'
    assert items[0].value.get_value() != ''

def test_env_var58_missing():
    obj = EnvironmentVariable58ObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.name = EntityObjectType(value='nope')
    obj.name.datatype = 'string'
    obj.name.operation = 'equals'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], EnvironmentVariable58ItemElement)
    assert items[0].status == 'not exists'

@pytest.mark.parametrize("oval_family, env_var", (
    ('linux', 'HOME'),
    ('windows', 'USERNAME'),
))
def test_env_var(oval_family, env_var):
    if host.facts['oval_family'] != oval_family:
        pytest.skip('Does not apply to platform')

    obj = EnvironmentVariableObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.name = EntityObjectType(value=env_var)
    obj.name.datatype = 'string'
    obj.name.operation = 'equals'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], EnvironmentVariableItemElement)
    assert items[0].status == 'exists'
    assert items[0].value.get_value() != ''

def test_env_var_missing():
    obj = EnvironmentVariableObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.name = EntityObjectType(value='nope')
    obj.name.datatype = 'string'
    obj.name.operation = 'equals'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], EnvironmentVariableItemElement)
    assert items[0].status == 'not exists'

@pytest.mark.parametrize('oval_family', [('linux'), ('windows')])
def test_family(oval_family):
    if host.facts['oval_family'] != oval_family:
        pytest.skip('Does not apply to platform')

    obj = FamilyObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FamilyItemElement)
    assert items[0].family.text == oval_family

@pytest.mark.parametrize(
    "oval_family, hash_type,hash_value",
    [
        # Need separate test for linux & windows because line ending difference changes the hashes
        ('linux', 'MD5', '088c92cb4d6c96cc3981678e4355fa4a'),
        ('linux', 'SHA-1', '8d1f3a9fe1fdef59204dbbbe163e1098c49d142b'),
        ('linux', 'SHA-224', '05dfa237b19462f5042625fd6301c03aa31b7ab23ec1ab990fd0aac6'),
        ('linux', 'SHA-256', '2eb5d6d679443b74e168948cba53f689572d7b0fabf4052016cd71241cb31356'),
        ('linux', 'SHA-384', '220d7a9e4035522342bda46f02dc9c0fd2dc20a9ad97cc005ff973f5f56c3461bedaffd506bd363593730102d8bf384c'),
        ('linux', 'SHA-512', '9e50035cb3b290015ce44dbd4152ee3dc506677b98329129c1440144fa1da591e1d77a3522ee780d5390391431ebee4336eb4ddaa1af20adfef07aacf71b65f8'),
        ('windows', 'MD5', '64383C3236AA3F8E8416C2D284A6C368'),
        ('windows', 'SHA-1', '703884F0C787F3A287815FE4A793F71591671894'),
        #('windows', 'SHA-224', ''), # not supported by powershell
        ('windows', 'SHA-256', '09617D45A40CB8CC577C73996D4723513F6C04E68D8AE6B0F1F25B3F34178748'),
        ('windows', 'SHA-384', '0EDEAB27A4C3008F80DADBE116997CADAA47A6327C3E9CC420578CA843D904E089E7A83D5701CE80DD0B5CE1237322E0'),
        ('windows', 'SHA-512', '5055CE3D494D4E003EA8F875E50BAC35AA4EFF13AEBADA45FC295763E2386FE007EC901F968D6D64BBA5DE1B3A17904E11ADDDE470A36DA018DCD660475FF2B7'),
    ]
)
def test_filehash58_filepath(oval_family, hash_type, hash_value):
    if host.facts['oval_family'] != oval_family:
        pytest.skip('Does not apply to platform')

    obj = FileHash58ObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.filepath = EntityObjectType(value=str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml'))
    obj.filepath.datatype = 'string'
    obj.filepath.operation = 'equals'
    obj.hash_type = EntityObjectType(value=hash_type)

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FileHash58ItemElement)
    assert items[0].status == 'exists'
    assert items[0].hash_type.text == hash_type
    assert items[0].hash.text == hash_value

@pytest.mark.parametrize(
    "oval_family, md5, sha1",
    [
        # Need separate test for linux & windows because line ending difference changes the hashes
        ('linux', '088c92cb4d6c96cc3981678e4355fa4a', '8d1f3a9fe1fdef59204dbbbe163e1098c49d142b'),
        ('windows', '64383C3236AA3F8E8416C2D284A6C368', '703884F0C787F3A287815FE4A793F71591671894'),
    ]
)
def test_filehash_filepath(oval_family, md5, sha1):
    if host.facts['oval_family'] != oval_family:
        pytest.skip('Does not apply to platform')

    obj = FileHashObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.filepath = EntityObjectType(value=str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml'))
    obj.filepath.datatype = 'string'
    obj.filepath.operation = 'equals'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], FileHashItemElement)
    assert items[0].status == 'exists'
    assert items[0].md5.text == md5
    assert items[0].sha1.text == sha1

# test_ldap57
# test_ldap
# test_sql57
# test_sql

def test_textfile54():
    obj = TextFileContent54ObjectElement()
    obj.id = 'oval:biz.jaymes:obj:42'
    obj.filepath = EntityObjectType(value=str(pathlib.Path(str(pytest.config.rootdir)) / 'tests' / 'model' / 'test_xlink.xml'))
    obj.filepath.datatype = 'string'
    obj.filepath.operation = 'equals'
    obj.pattern = EntityObjectType(value=r'xmlns:test="http://([^/]+)/test"')
    obj.pattern.datatype = 'string'
    obj.pattern.operation = 'pattern match'
    obj.instance = EntityObjectType(value=1)
    obj.instance.datatype = 'int'
    obj.instance.operation = 'equals'

    items = obj.evaluate(host, None, {}, [])
    assert len(items) == 1
    assert isinstance(items[0], TextFileContentItemElement)
    assert items[0].status == 'exists'
    assert items[0].text.get_value() == 'xmlns:test="http://jaymes.biz/test"'
    assert len(items[0].subexpressions) == 1
    assert items[0].subexpressions[0].get_value() == 'jaymes.biz'
