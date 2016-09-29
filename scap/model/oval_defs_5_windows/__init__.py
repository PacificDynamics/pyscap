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
TEST_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_test': {'map': 'tests', 'class': 'AccessTokenTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory57_test': {'map': 'tests', 'class': 'ActiveDirectory57TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_test': {'map': 'tests', 'class': 'ActiveDirectoryTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_test': {'map': 'tests', 'class': 'AuditEventPolicySubcategoriesTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_test': {'map': 'tests', 'class': 'AuditEventPolicyTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}cmdlet_test': {'map': 'tests', 'class': 'CmdletTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dnscache_test': {'map': 'tests', 'class': 'DnsCacheTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_test': {'map': 'tests', 'class': 'FileAuditedPermissions53TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_test': {'map': 'tests', 'class': 'FileAuditedPermissionsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_test': {'map': 'tests', 'class': 'FileEffectiveRights53TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_test': {'map': 'tests', 'class': 'FileEffectiveRightsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_test': {'map': 'tests', 'class': 'FileTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_sid_test': {'map': 'tests', 'class': 'GroupSidTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_test': {'map': 'tests', 'class': 'GroupTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_test': {'map': 'tests', 'class': 'InterfaceTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}license_test': {'map': 'tests', 'class': 'LicenseTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_test': {'map': 'tests', 'class': 'LockoutPolicyTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_test': {'map': 'tests', 'class': 'MetabaseTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_test': {'map': 'tests', 'class': 'NtUserTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_test': {'map': 'tests', 'class': 'PasswordPolicyTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}peheader_test': {'map': 'tests', 'class': 'PeHeaderTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_test': {'map': 'tests', 'class': 'PortTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_test': {'map': 'tests', 'class': 'PrinterEffectiveRightsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process58_test': {'map': 'tests', 'class': 'Process58TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_test': {'map': 'tests', 'class': 'ProcessTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_test': {'map': 'tests', 'class': 'RegistryTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_test': {'map': 'tests', 'class': 'RegKeyAuditedPermissions53TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_test': {'map': 'tests', 'class': 'RegKeyAuditedPermissionsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_test': {'map': 'tests', 'class': 'RegKeyEffectiveRights53TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_test': {'map': 'tests', 'class': 'RegKeyEffectiveRightsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serviceeffectiverights_test': {'map': 'tests', 'class': 'ServiceEffectiveRightsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_test': {'map': 'tests', 'class': 'ServiceTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceauditedpermissions_test': {'map': 'tests', 'class': 'SharedResourceAuditedPermissionsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceeffectiverights_test': {'map': 'tests', 'class': 'SharedResourceEffectiveRightsTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_test': {'map': 'tests', 'class': 'SharedResourceTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_sid_test': {'map': 'tests', 'class': 'SidSidTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_test': {'map': 'tests', 'class': 'SidTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}systemmetric_test': {'map': 'tests', 'class': 'SystemMetricTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_test': {'map': 'tests', 'class': 'UacTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}userright_test': {'map': 'tests', 'class': 'UserRightTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid55_test': {'map': 'tests', 'class': 'UserSid55TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid_test': {'map': 'tests', 'class': 'UserSidTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_test': {'map': 'tests', 'class': 'UserTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_test': {'map': 'tests', 'class': 'VolumeTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi57_test': {'map': 'tests', 'class': 'Wmi57TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_test': {'map': 'tests', 'class': 'WmiTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_test': {'map': 'tests', 'class': 'WuaUpdateSearcherTestElement', 'min': 0, 'max': None},
}
OBJECT_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_object': {'map': 'objects', 'class': 'AccessTokenObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory57_object': {'map': 'objects', 'class': 'ActiveDirectory57ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_object': {'map': 'objects', 'class': 'ActiveDirectoryObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_object': {'map': 'objects', 'class': 'AuditEventPolicySubcategoriesObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_object': {'map': 'objects', 'class': 'AuditEventPolicyObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}cmdlet_object': {'map': 'objects', 'class': 'CmdletObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dnscache_object': {'map': 'objects', 'class': 'DnsCacheObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_object': {'map': 'objects', 'class': 'FileAuditedPermissions53ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_object': {'map': 'objects', 'class': 'FileAuditedpermissionsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_object': {'map': 'objects', 'class': 'FileEffectiveRights53ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_object': {'map': 'objects', 'class': 'FileEffectiveRightsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_object': {'map': 'objects', 'class': 'FileObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_sid_object': {'map': 'objects', 'class': 'GroupSidObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_object': {'map': 'objects', 'class': 'GroupObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_object': {'map': 'objects', 'class': 'InterfaceObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}license_object': {'map': 'objects', 'class': 'LicenseObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_object': {'map': 'objects', 'class': 'LockoutPolicyObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_object': {'map': 'objects', 'class': 'MetabaseObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_object': {'map': 'objects', 'class': 'NtUserObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_object': {'map': 'objects', 'class': 'PasswordPolicyObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}peheader_object': {'map': 'objects', 'class': 'PeHeaderObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_object': {'map': 'objects', 'class': 'PortObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_object': {'map': 'objects', 'class': 'PrinterEffectiveRightsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process58_object': {'map': 'objects', 'class': 'Process58ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_object': {'map': 'objects', 'class': 'ProcessObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_object': {'map': 'objects', 'class': 'RegistryObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_object': {'map': 'objects', 'class': 'RegKeyAuditedPermissions53ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_object': {'map': 'objects', 'class': 'RegKeyAuditedPermissionsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_object': {'map': 'objects', 'class': 'RegKeyEffectiveRights53ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_object': {'map': 'objects', 'class': 'RegKeyEffectiveRightsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serviceeffectiverights_object': {'map': 'objects', 'class': 'ServiceEffectiveRightsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_object': {'map': 'objects', 'class': 'ServiceObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceauditedpermissions_object': {'map': 'objects', 'class': 'SharedResourceAuditedPermissionsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceeffectiverights_object': {'map': 'objects', 'class': 'SharedResourceEffectiveRightsObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_object': {'map': 'objects', 'class': 'SharedResourceObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_sid_object': {'map': 'objects', 'class': 'SidSidObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_object': {'map': 'objects', 'class': 'SidObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}systemmetric_object': {'map': 'objects', 'class': 'SystemMetricObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_object': {'map': 'objects', 'class': 'UacObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}userright_object': {'map': 'objects', 'class': 'UserRightObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid55_object': {'map': 'objects', 'class': 'UserSid55ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid_object': {'map': 'objects', 'class': 'UserSidObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_object': {'map': 'objects', 'class': 'UserObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_object': {'map': 'objects', 'class': 'VolumeObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi57_object': {'map': 'objects', 'class': 'Wmi57ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_object': {'map': 'objects', 'class': 'WmiObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_object': {'map': 'objects', 'class': 'WuaUpdateSearcherObjectElement', 'min': 0, 'max': None},
}
STATE_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_state': {'map': 'states', 'class': 'AccessTokenStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory57_state': {'map': 'states', 'class': 'ActiveDirectory57StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_state': {'map': 'states', 'class': 'ActiveDirectoryStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_state': {'map': 'states', 'class': 'AuditEventPolicySubcategoriesStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_state': {'map': 'states', 'class': 'AuditEventPolicyStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}cmdlet_state': {'map': 'states', 'class': 'CmdletStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dnscache_state': {'map': 'states', 'class': 'DnsCacheStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_state': {'map': 'states', 'class': 'FileAuditedPermissions53StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_state': {'map': 'states', 'class': 'FileAuditedpermissionsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_state': {'map': 'states', 'class': 'FileEffectiveRights53StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_state': {'map': 'states', 'class': 'FileEffectiveRightsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_state': {'map': 'states', 'class': 'FileStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_sid_state': {'map': 'states', 'class': 'GroupSidStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_state': {'map': 'states', 'class': 'GroupStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_state': {'map': 'states', 'class': 'InterfaceStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}license_state': {'map': 'states', 'class': 'LicenseStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_state': {'map': 'states', 'class': 'LockoutPolicyStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_state': {'map': 'states', 'class': 'MetabaseStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_state': {'map': 'states', 'class': 'NtUserStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_state': {'map': 'states', 'class': 'PasswordPolicyStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}peheader_state': {'map': 'states', 'class': 'PeHeaderStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_state': {'map': 'states', 'class': 'PortStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_state': {'map': 'states', 'class': 'PrinterEffectiveRightsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process58_state': {'map': 'states', 'class': 'Process58StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_state': {'map': 'states', 'class': 'ProcessStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_state': {'map': 'states', 'class': 'RegistryStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_state': {'map': 'states', 'class': 'RegKeyAuditedPermissions53StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_state': {'map': 'states', 'class': 'RegKeyAuditedPermissionsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_state': {'map': 'states', 'class': 'RegKeyEffectiveRights53StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_state': {'map': 'states', 'class': 'RegKeyEffectiveRightsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serviceeffectiverights_state': {'map': 'states', 'class': 'ServiceEffectiveRightsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_state': {'map': 'states', 'class': 'ServiceStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceauditedpermissions_state': {'map': 'states', 'class': 'SharedResourceAuditedPermissionsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceeffectiverights_state': {'map': 'states', 'class': 'SharedResourceEffectiveRightsStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_state': {'map': 'states', 'class': 'SharedResourceStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_sid_state': {'map': 'states', 'class': 'SidSidStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_state': {'map': 'states', 'class': 'SidStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}systemmetric_state': {'map': 'states', 'class': 'SystemMetricStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_state': {'map': 'states', 'class': 'UacStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}userright_state': {'map': 'states', 'class': 'UserRightStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid55_state': {'map': 'states', 'class': 'UserSid55StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid_state': {'map': 'states', 'class': 'UserSidStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_state': {'map': 'states', 'class': 'UserStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_state': {'map': 'states', 'class': 'VolumeStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi57_state': {'map': 'states', 'class': 'Wmi57StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_state': {'map': 'states', 'class': 'WmiStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_state': {'map': 'states', 'class': 'WuaUpdateSearcherStateElement', 'min': 0, 'max': None},
}
