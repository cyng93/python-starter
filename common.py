#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
# file: common.py
# vim: tabstop=4 shiftwidth=4 softtabstop=4 expandtab

import os
import subprocess
import sys


SCRIPT_BASENAME = os.path.basename(__file__)


def gen_cprint(script_basename):
    def cprint(msg):
        """
        cprint()

          custom print function
          output format : `-- [script_basename] <actual_msg>`
        """
        if script_basename:
            print(f'-- [{script_basename}] {msg}', flush=True)
        else:
            print(f'-- {msg}', flush=True)

    return cprint


cprint = gen_cprint(SCRIPT_BASENAME)


def shell_exec(cmdline, check=True, timeout=None, logfile=None, silent=False):
    # Run shell command-line and print stdout/stderr to stdout
    # If the return value is non-zero, exception would be raised
    cprint(f'Running: {cmdline}')
    output = b''
    try:
        proc = subprocess.run(cmdline,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              shell=True, check=check, timeout=timeout)
        output = proc.stdout
        retcode = proc.returncode
    except subprocess.CalledProcessError as ex:
        output = ex.output
        raise ex
    finally:
        output = output.decode('utf-8', errors='ignore').replace('\r\n', '\n')
        cprint('')
        if logfile:
            with open(logfile, 'w') as f:
                f.write(output)
        elif not silent:
            sys.stdout.buffer.write(output.encode('utf-8', errors='ignore'))
    return output, retcode
