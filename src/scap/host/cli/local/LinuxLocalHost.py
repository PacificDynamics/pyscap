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
import os
import selectors
from subprocess import Popen, PIPE
import sys

from scap.host.cli.LocalHost import LocalHost
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class LinuxLocalHost(LocalHost):
    def __init__(self, hostname):
        super(LinuxLocalHost, self).__init__(hostname)

        # so we short circuit any detection
        self.facts['oval_family'] = 'linux'

    def _send_stdin(self, p, data):
        p.stdin.write(data)
        p.stdin.close()

    def exec_command(self, cmd):
        #cmd = 'sh -c "' + cmd.replace('"', r'\"') + '"'
        logger.debug("Sending command: " + cmd)
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True, universal_newlines=True)

        # note; can't use p.communicate; have to figure out if we get a prompt
        # because there isn't if within sudo timeout
        self._cmd_out_buf = ''
        self._cmd_err_buf = ''
        sel = selectors.DefaultSelector()
        sel.register(p.stdout, selectors.EVENT_READ)
        sel.register(p.stderr, selectors.EVENT_READ)
        while True:
            ready_list = sel.select(10)
            if len(ready_list) == 0:
                # timeout
                p.stdin.close()
                break
            for (key, events) in ready_list:
                if key.fileobj is p.stdout and events & selectors.EVENT_READ:
                    outs = p.stdout.buffer.read1(1024).decode()
                    if len(outs) > 0:
                        self._recv_stdout(p, outs)
                elif key.fileobj is p.stderr and events & selectors.EVENT_READ:
                    errs = p.stderr.buffer.read1(1024).decode()
                    if len(errs) > 0:
                        self._recv_stderr(p, errs)

            if p.stdout.closed and p.stderr.closed:
                p.stdin.close()
                p.poll()
                break

            if p.poll() is not None:
                p.stdin.close()
                break

        if not p.stderr.closed:
            errs = p.stderr.buffer.read1(1024).decode()
            if len(errs) > 0:
                self._recv_stderr(p, errs)

        if not p.stdout.closed:
            outs = p.stdout.buffer.read1(1024).decode()
            if len(outs) > 0:
                self._recv_stdout(p, outs)

        sel.unregister(p.stdout)
        sel.unregister(p.stderr)
        sel.close()

        out_lines = str.splitlines(self._cmd_out_buf)
        out_lines = [line.strip('\x0A\x0D') for line in out_lines]
        err_lines = str.splitlines(self._cmd_err_buf)
        err_lines = [line.strip('\x0A\x0D') for line in err_lines]

        return (p.returncode, out_lines, err_lines)
