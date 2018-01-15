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

VERSION = '0.1'

def register_namespaces():
    from expatriate.model.Model import Model

    Model.register_namespace('scap.model.ai_1_1', 'http://scap.nist.gov/schema/asset-identification/1.1')
    Model.register_namespace('scap.model.arf_1_1', 'http://scap.nist.gov/schema/asset-reporting-format/1.1')
    Model.register_namespace('scap.model.arf_rel_1_0', 'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0')
    Model.register_namespace('scap.model.cpe_1_0', 'http://cpe.mitre.org/XMLSchema/cpe/1.0')
    Model.register_namespace('scap.model.cpe_dict_2_3', 'http://cpe.mitre.org/dictionary/2.0')
    Model.register_namespace('scap.model.cpe_lang_2_3', 'http://cpe.mitre.org/language/2.0')
    Model.register_namespace('scap.model.cpe_naming_2_3', 'http://cpe.mitre.org/naming/2.0')
    Model.register_namespace('scap.model.dc_elements_1_1', 'http://purl.org/dc/elements/1.1/')
    Model.register_namespace('scap.model.tmsad_1_0', 'http://scap.nist.gov/schema/xml-dsig/1.0')
    Model.register_namespace('scap.model.ocil_2_0', 'http://scap.nist.gov/schema/ocil/2.0')
    Model.register_namespace('scap.model.ocil_2_0', 'http://scap.nist.gov/schema/ocil/2')
    Model.register_namespace('scap.model.oval_5', 'http://oval.mitre.org/XMLSchema/oval-common-5')
    Model.register_namespace('scap.model.oval_5.defs', 'http://oval.mitre.org/XMLSchema/oval-definitions-5')
    Model.register_namespace('scap.model.oval_5.defs.independent', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent')
    Model.register_namespace('scap.model.oval_5.defs.linux', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux')
    Model.register_namespace('scap.model.oval_5.defs.windows', 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows')
    Model.register_namespace('scap.model.oval_5.dir', 'http://oval.mitre.org/XMLSchema/oval-directives-5')
    Model.register_namespace('scap.model.oval_5.sc', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5')
    Model.register_namespace('scap.model.oval_5.sc.linux', 'http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux')
    Model.register_namespace('scap.model.oval_5.var', 'http://oval.mitre.org/XMLSchema/oval-variables-5')
    Model.register_namespace('scap.model.scap_source_1_2', 'http://scap.nist.gov/schema/scap/source/1.2')
    Model.register_namespace('scap.model.rep_core_1_1', 'http://scap.nist.gov/schema/reporting-core/1.1')
    Model.register_namespace('scap.model.vuln_0_4', 'http://scap.nist.gov/schema/vulnerability/0.4')
    Model.register_namespace('scap.model.xal_2_0', 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')
    Model.register_namespace('scap.model.xccdf_1_1', 'http://checklists.nist.gov/xccdf/1.1')
    Model.register_namespace('scap.model.xccdf_1_2', 'http://checklists.nist.gov/xccdf/1.2')
    Model.register_namespace('scap.model.xccdf_p_1_1', 'http://checklists.nist.gov/xccdf-p/1.1')
    Model.register_namespace('scap.model.xccdf_p_0_2_3', 'http://www.cisecurity.org/xccdf/platform/0.2.3')
    Model.register_namespace('scap.model.xhtml', 'http://www.w3.org/1999/xhtml')
    Model.register_namespace('scap.model.xlink', 'http://www.w3.org/1999/xlink')
    Model.register_namespace('scap.model.xml_cat_1_1', 'urn:oasis:names:tc:entity:xmlns:xml:catalog')
    Model.register_namespace('scap.model.xmldsig_2000_09', 'http://www.w3.org/2000/09/xmldsig#')
    Model.register_namespace('scap.model.xnl_2_0', 'urn:oasis:names:tc:ciq:xsdschema:xNL:2.0')

def main():
    import argparse
    import atexit
    import expatriate
    from io import StringIO
    import locale
    import logging
    import os
    import pathlib
    import pprint
    import sys
    import time
    import xml.dom.minidom

    from scap import register_namespaces
    from scap.ColorFormatter import ColorFormatter
    from expatriate.model.Model import Model
    from scap.Host import Host
    from scap.Inventory import Inventory
    from scap.Reporter import Reporter

    # set up logging
    rootLogger = logging.getLogger()
    ch = logging.StreamHandler()
    fh = logging.FileHandler(filename="pyscap.log", mode='w')
    fh_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(fh_formatter)
    ch_formatter = ColorFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(ch_formatter)
    rootLogger.addHandler(ch)
    rootLogger.addHandler(fh)

    rootLogger.setLevel(logging.DEBUG)
    ch.setLevel(logging.WARNING)

    # report start time & end time
    logger = logging.getLogger(__name__)
    logger.debug('Start: ' + time.asctime(time.localtime()))

    register_namespaces()

    output = None
    def end_func():
        if output is not None:
            output.close()
        logger.debug('End: ' + time.asctime(time.localtime()))
    atexit.register(end_func)

    # set up argument parsing
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--version', '-V', action='version', version='%(prog)s 1.0')
    arg_parser.add_argument('--verbose', '-v', action='count')
    arg_parser.add_argument('--output', '-o', nargs='?', default='-')
    arg_parser.add_argument('--inventory', nargs='+')
    arg_parser.add_argument('--host', nargs='+')

    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument('--list-hosts', help='outputs a list of the hosts', action='store_true')
    group.add_argument('--parse', help='parse the supplied files', nargs='+', type=argparse.FileType('r'))
    group.add_argument('--detect', help='detect facts about the host', action='store_true')
    group.add_argument('--collect', help='collect system characteristics about the host', action='store_true')
    group.add_argument('--benchmark', help='benchmark hosts and produce a report', action='store_true')
    # group.add_argument('--test', help='perform a test on the selected hosts', nargs='+')

    # pre-parse arguments
    args = arg_parser.parse_known_args()
    if len(args) <= 0:
        arg_parser.error('No valid operation was given')

    # change verbosity
    if args[0].verbose:
        if(args[0].verbose == 1):
            ch.setLevel(logging.INFO)
            logger.debug('Set console logging level to INFO')
        elif(args[0].verbose == 2):
            ch.setLevel(logging.DEBUG)
            logger.debug('Set console logging level to DEBUG')
        elif(args[0].verbose >= 3):
            ch.setLevel(logging.NOTSET)
            logger.debug('Set console logging level to NOTSET')

    # set up the modes
    if args[0].list_hosts:
        logger.info("List hosts operation")
    elif args[0].parse:
        logger.info('File parsing operation')
    elif args[0].detect:
        logger.info("Detect operation")
    elif args[0].collect:
        logger.info("Collect operation")
        arg_parser.add_argument('--content', required=True, nargs='+')
    elif args[0].benchmark:
        logger.info("Benchmark operation")
        arg_parser.add_argument('--content', required=True, nargs='+')
        arg_parser.add_argument('--data_stream', nargs=1)
        arg_parser.add_argument('--checklist', nargs=1)
        arg_parser.add_argument('--profile', nargs=1)
        arg_parser.add_argument('--pretty', action='store_true')
    else:
        arg_parser.error('No valid operation was given')

    # final argument parsing
    args = vars(arg_parser.parse_args())
    for arg in args:
        logger.debug('Argument: ' + arg + ' = ' + str(args[arg]))

    # expand the hosts
    inventory = Inventory()
    if args['inventory'] is not None:
        for filename in args['inventory']:
            try:
                with open(filename, 'r') as fp:
                    logger.debug('Loading inventory from ' + filename)
                    Inventory().readfp(fp)
            except IOError:
                logger.error('Could not read from inventory file ' + filename)
    else:
        filename = str(pathlib.Path(os.path.expanduser('~')) / '.pyscap' / 'inventory.ini')
        try:
            with open(filename, 'r') as fp:
                logger.debug('Loading inventory from ' + filename)
                Inventory().readfp(fp)
        except IOError:
            logger.error('Could not read from inventory file ' + filename)

    if args['host'] is None or len(args['host']) == 0:
        arg_parser.error('No host specified (--host)')

    hosts = []
    for hostname in args['host']:
        host = Host.load(hostname)
        hosts.append(host)

    # open output if it's not stdout
    if args['output'] != '-':
        output = open(args['output'], mode='wb')
    else:
        output = sys.stdout.buffer

    detection_collectors = [
        'UniqueIdCollector',
        'CpeCollector',
        'FqdnCollector',
        'HostnameCollector',
        'NetworkConnectionCollector',
        'NetworkServiceCollector',
        'IdentityCollector',
    ]

    if args['list_hosts']:
        print('Hosts: ')
        for host in hosts:
            print(host.hostname)

    elif args['parse']:
        for uri in args['parse']:
            logger.debug('Loading content file: ' + uri)
            doc = expatriate.Document()
            doc.parse_file(uri)
            content = doc.root_element
            model = Model.load(None, content)
            logger.debug('Loaded ' + uri + ' successfully')

    elif args['detect']:
        for host in hosts:
            host.connect()

            # run detection collectors
            for col_name in detection_collectors:
                col = host.load_collector(col_name, {})
                col.collect()

            host.disconnect()

            logger.info('Host detection dump:')
            pp = pprint.PrettyPrinter(width=132)
            pp.pprint(host.facts)

    elif args['collect']:
        if args['content'] is None or len(args['content']) == 0:
            arg_parser.error('No content specified (--content)')

        # this mode will collect oval system characteristics
        for host in hosts:
            host.connect()

            # run detection collectors
            for col_name in detection_collectors:
                col = host.load_collector(col_name, {})
                col.collect()

            raise NotImplementedError('System characteristic collection is not implemented')

            host.disconnect()

    elif args['benchmark']:
        ### Loading.Import
        # Import the XCCDF document into the program and build an initial internal
        # representation of the Benchmark object, Groups, Rules, and other objects.
        # If the file cannot be read or parsed, then Loading fails. (At the
        # beginning of this step, any inclusion processing specified with XInclude
        # elements should be performed. The resulting XML information set should be
        # validated against the XCCDF schema given in Appendix A.) Go to the next
        # step: Loading.Noticing.

        if args['content'] is None or len(args['content']) == 0:
            arg_parser.error('No content specified (--content)')

        from scap.model.xccdf_1_1.BenchmarkType import BenchmarkType as xccdf_1_1_BenchmarkType
        from scap.model.xccdf_1_2.BenchmarkType import BenchmarkType as xccdf_1_2_BenchmarkType
        benchmark_model = None
        for uri in args['content']:
            logger.debug('Loading content file: ' + uri)
            with open(uri, mode='r', encoding='utf_8') as f:
                doc = expatriate.Document()
                doc.parse_file(uri)
                content = doc.root_element
                model = Model.load(None, content)

                if (
                    isinstance(model, xccdf_1_1_BenchmarkType)
                    or isinstance(model, xccdf_1_2_BenchmarkType)
                ):
                    benchmark_model = model

        for host in hosts:
            host.connect()

            # run detection collectors
            for col_name in detection_collectors:
                col = host.load_collector(col_name, {})
                col.collect()

            benchmark_model.noticing()

            benchmark_model.selected_profiles = []
            if args['profile'] is None or len(args['profile']) == 0:
                # check them all
                benchmark_model.selected_profiles.extend(benchmark_model.profiles.keys())
            else:
                for profile in args['profile']:
                    if profile not in list(benchmark_model.profiles.keys()):
                        raise ValueError('Unable to select non-existent profile: ' + profile + ' Available profiles: ' + str(benchmark_model.profiles.keys()))
                    benchmark_model.selected_profiles.append(profile)

            benchmark_model.resolve()

            benchmark_model.process(host)

            host.disconnect()

        rep = Reporter.load(args, model)
        report = rep.report(hosts)

        logger.debug('Preferred encoding: ' + locale.getpreferredencoding())
        sio = StringIO()
        report.write(sio, encoding='unicode', xml_declaration=True)
        sio.write("\n")
        if args['pretty']:
            pretty_xml = xml.dom.minidom.parseString(sio.getvalue()).toprettyxml(indent='  ')
            output.write(pretty_xml.encode(locale.getpreferredencoding()))
        else:
            output.write(sio.getvalue().encode(locale.getpreferredencoding()))

    else:
        arg_parser.error('No valid operation was given')
