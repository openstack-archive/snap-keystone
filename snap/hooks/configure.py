#!/usr/bin/env python

# Copyright 2017 Canonical Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import sys

from subprocess import check_output

LOG = logging.getLogger(__name__)

def _get_config(key):
    cmd = ['snapctl', 'get', key]
    return check_output(cmd)

def check_install_method():
    value = _get_config('install-method').rstrip()
    if value and value not in ['classic', 'strict']:
        LOG.error('install-method value {} is not valid'.format(value))
        sys.exit(1)

def main():
    logging.basicConfig(level=logging.INFO)
    check_install_method()

if __name__ == '__main__':
    main()
