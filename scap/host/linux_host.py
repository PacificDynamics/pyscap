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

from scap.host.host import Host
from scap.model.cpe_2_3.cpe import CPE
import xml.etree.ElementTree as ET
import re, logging

logger = logging.getLogger(__name__)
class LinuxHost(Host):
    def __init__(self, uname, target):
        self.target = target
        self.facts = {'uname': uname}

        # TODO lsb_release -a

    def discover_hardware(self):
        self.facts['root_uuid'] = self.target.line_from_priv_command("blkid -o value `mount -l | grep 'on / ' | awk '{print $1}'` | head -n1").strip()
        logger.debug('Root FS UUID: ' + self.facts['root_uuid'])

        # TODO hardware CPEs

        self.facts['hardware'] = {}
        self.facts['cpe'] = []
        # ai.computing_device.motherboard-guid
        try:
            path = [self.facts['hardware']]
            indents = [0]
            lines = self.target.lines_from_priv_command('lshw')
            for line in lines:
                m = re.match(r'^([ ]+)\*-(\S+)', line)
                if m:
                    if 'vendor' in path[-1] and 'product' in path[-1] and path[-1]['vendor'] != '000000000000':
                        cpe = CPE(part='h', vendor=path[-1]['vendor'], product=path[-1]['product'])
                        if 'version' in path[-1]:
                            cpe.set_value('version', path[-1]['version'])
                        self.facts['cpe'].append(cpe)

                    indent = len(m.group(1))
                    hw_class = m.group(2)
                    cur_indent = indents[-1]
                    if indent > cur_indent:
                        # child; push onto the path
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    elif indent == cur_indent:
                        # sibling; pop then push
                        path.pop()
                        indents.pop()
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    else:
                        # indent < cur_indent
                        # parent; ascend till the indent is equal
                        parent_indent = indents[-1]
                        while parent_indent >= indent:
                            path.pop()
                            indents.pop()
                            parent_indent = indents[-1]
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    continue

                m = re.match(r'^\s+([^:]+): (.*)\s*$', line)
                if m:
                    if m.group(1) == 'configuration':
                        path[-1][m.group(1)] = {}

                        # the below mess is because the values don't escape spaces
                        # so guessing is required
                        keys = []
                        in_key = True
                        (k,v) = ('','')
                        for c in m.group(2):
                            if in_key:
                                if c == '=':
                                    in_key = False
                                elif c == ' ':
                                    # not a key, append to prev value
                                    path[-1][m.group(1)][keys[-1]] += ' ' + k
                                    k = ''
                                else:
                                    k += c
                            else:
                                if c == ' ':
                                    in_key = True
                                    path[-1][m.group(1)][k] = v
                                    keys.append(k)
                                    (k,v) = ('','')
                                else:
                                    v += c
                        path[-1][m.group(1)][k] = v
                    elif m.group(1) == 'capabilities':
                        path[-1][m.group(1)] = m.group(2).split(' ')
                    else:
                        path[-1][m.group(1)] = m.group(2)
        except RuntimeError as e:
            logger.warning("Couldn't run lshw on host using sudo" + str(e))

        import pprint
        pp = pprint.PrettyPrinter()
        logger.debug(pp.pformat(self.facts['hardware']))

        for cpe in self.facts['cpe']:
            logger.debug(cpe.to_uri_string())

        # TODO ai.circuit
        # TODO ai.network; this would likely be  used on routers, switches & other net devices

    def discover_software(self):
        # OS CPE
        cpe = CPE()
        cpe.set_value('part', 'o')
        cpe.set_value('vendor', 'linux')
        cpe.set_value('product', 'linux_kernel')

        m = re.match(r'^Linux \S+ ([0-9.]+)-(\S+)', self.facts['uname'])
        if m:
            cpe.set_value('version', m.group(1))
            cpe.set_value('update', m.group(2))
        self.facts['cpe'].append(cpe)

        # ai.computing_device.default-route
        ip_route = self.target.lines_from_command('ip route')
        logger.debug('ip_route: ' + str(ip_route))
        for line in ip_route:
            m = re.match(r'^default via ([0-9.]+) dev', line)
            if m:
                logger.debug('default-route: ' + m.group(1))
                self.facts['default_route'] = m.group(1)

        # ai.computing_device.fqdn
        fqdn = self.target.line_from_command('hostname --fqdn').strip()
        logger.debug('fqdn: ' + str(fqdn))
        self.facts['fqdn'] = fqdn

        # ai.computing_device.hostname
        hostname = self.target.line_from_command('hostname').strip()
        logger.debug('hostname: ' + str(hostname))
        self.facts['hostname'] = hostname

        # ai.computing_device/connections
        self.facts['connections'] = []
        for line in self.target.lines_from_command('ip addr'):
            # link line
            m = re.match(r'^\s+link/(ether|loopback) ([:a-f0-9]+)', line)
            if m:
                mac_address = m.group(2)
                continue

            # inet line
            m = re.match(r'^\s+inet ([0-9.]+)(/\d+)', line)
            if m:
                self.facts['connections'].append({'mac_address': mac_address, 'ip_address': m.group(1), 'subnet_mask': m.group(2)})
                continue

            # inet6 line
            m = re.match(r'^\s+inet6 ([0-9:]+)(/\d+)', line)
            if m:
                self.facts['connections'].append({'mac_address': mac_address, 'ip_address': m.group(1), 'subnet_mask': m.group(2)})
                continue

        # ai.service
        self.facts['network_services'] = []
        for line in self.target.lines_from_command('netstat -ln --ip'):
            m = re.match(r'^(tcp|udp)\s+\d+\s+\d+\s+([0-9.]+):([0-9]+)', line)
            if m:
                # NOTE: using tcp|udp as the protocol is in conflict with the ai standard's
                # intent, but since the port #s would not be unique otherwise and it's
                # almost impossible to accurately figure out what the port is being used
                # for, we use tcp & udp instead
                self.facts['network_services'].append({'ip_address': m.group(2), 'port': m.group(3), 'protocol': m.group(1)})

        # TODO ai.database
        # TODO ai.software
            # TODO application CPEs
        # TODO ai.website

    def test_rule(self, rule, values, content):
        pass

    def get_arf_1_1(self):
        asset_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset')
        asset_id = 'asset_' + self.facts['root_uuid']
        # TODO: fallback to mobo guid, eth0 mac address, eth0 ip address, hostname
        asset_el.attrib['id'] = asset_id

        ai = ET.SubElement(asset_el, '{http://scap.nist.gov/schema/asset-identification/1.1}computing-device')
        # motherboard should be the first discovered hardware cpe
        ai.attrib['cpe'] = self.facts['cpe'][0].to_uri_string()
        ai.attrib['default-route'] = self.facts['default_route']
        ai.attrib['fqdn'] = self.facts['fqdn']
        ai.attrib['hostname'] = self.facts['hostname']
        try:
            ai.attrib['motherboard-guid'] = self.facts['hardware']['configuration']['uuid']
        except KeyError:
            logger.debug("Couldn't parse motherboard-guid")
        conns = ET.SubElement(ai, '{http://scap.nist.gov/schema/asset-identification/1.1}connections')
        for c in self.facts['connections']:
            conn = ET.SubElement(conns, '{http://scap.nist.gov/schema/asset-identification/1.1}connection')
            # mac-address
            conn.attrib['mac-address'] = c['mac_address']
            # ip-address
            conn.attrib['ip-address'] = c['ip_address']
            # subnet-mask
            conn.attrib['subnet-mask'] = c['subnet_mask']

        # network services
        for svc in self.facts['network_services']:
            ai = ET.SubElement(asset_el, '{http://scap.nist.gov/schema/asset-identification/1.1}service')
            ai.attrib['host'] = svc['ip_address']
            ai.attrib['port'] = svc['port']
            ai.attrib['protocol'] = svc['protocol']

        report_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}report')
        import uuid
        report_id = 'report_' + uuid.uuid4().hex
        report_el.attrib['id'] = report_id

        # TODO embed content

        relationships = []
        rel_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}relationship')
        rel_el.attrib['subject'] = report_id
        rel_el.attrib['type'] = 'isAbout'
        rel_el.attrib['ref'] = asset_id

        # TODO createdFor relationship

        relationships.append(rel_el)

        return (asset_el, report_el, relationships)