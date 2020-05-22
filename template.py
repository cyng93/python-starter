#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
# file: template.py
# vim: tabstop=4 shiftwidth=4 softtabstop=4 expandtab

import argparse
import os
from common import gen_cprint
from common import shell_exec


SCRIPT_BASENAME = os.path.basename(__file__)


cprint = gen_cprint(SCRIPT_BASENAME)


"""
ENTRY POINT
"""
if __name__ == '__main__':

    # 0. ARGUMENT RELEVANT (SETUP, CHECKING, EXTRACT)
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store_true', required=False,
                        help='either first/last arg')
    parser.add_argument('positional_arg1', metavar='<positional_arg1>',
                        nargs='?', const=str, help='1st arg')
    parser.add_argument('positional_arg2', metavar='<positional_arg2>',
                        nargs='?', const=str, help='2nd arg')
    parser.add_argument('positional_arg3', metavar='<positional_arg3>',
                        nargs='?', const=str, help='3rd arg')

    args = parser.parse_args()
    arg1 = args.positional_arg1
    arg2 = args.positional_arg2
    arg3 = args.positional_arg3
    flag = args.f

    print(f'positional_arg1: {arg1}'
          f'positional_arg2: {arg2}'
          f'positional_arg3: {arg3}'
          f'-u: {flag}')

    # Write code here...

    exit(0)
