#!/usr/bin/python
# Copyright (c) 2010-2011 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import time
from setuptools import setup, find_packages
name = 'swiftkeystone2'

TOPDIR = os.path.abspath(os.path.dirname(__file__))
VFILE  = os.path.join(TOPDIR, name, '__pistonversion__.py')

args = filter(lambda x: x[0] != '-', sys.argv)
command = args[1] if len(args) > 1 else ''

if command == 'sdist':
    PISTON_VERSION = os.environ['PISTON_VERSION']
    with file(VFILE, 'w') as f:
        f.write('''#!/usr/bin/env python\nVERSION = '%s'\n''' % PISTON_VERSION)
elif command == 'develop':
    PISTON_VERSION = time.strftime('9999.0.%Y%m%d%H%M%S', time.localtime())
    with file(VFILE, 'w') as f:
        f.write('''#!/usr/bin/env python\nVERSION = '%s'\n''' % PISTON_VERSION)
elif command is None:
    PISTON_VERSION = '9999999999-You_did_not_set_a_version'
else:
    assert os.path.exists(VFILE), '%s does not exist, please run sdist or develop' % VFILE
    from swiftkeystone2 import __pistonversion__ as pistonversion
    PISTON_VERSION = pistonversion.VERSION

setup(
    name=name,
    version=PISTON_VERSION,
    description='Swift Keystone2',
    license='Apache License (2.0)',
    author='Chmouel Boudjnah',
    author_email='chmouel@chmouel.com',
    url='https://github.com/chmouel/%s' % name,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[],  # removed for better compat
    entry_points={
        'paste.app_factory': ['main=identity:app_factory'],
        'paste.filter_factory': [
            'keystone2=swiftkeystone2.middleware:filter_factory',
            ],
        },
    )
