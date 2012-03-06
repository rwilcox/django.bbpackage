#!/usr/bin/env python
"""
A quick script to install into your `Application Support/BBEdit/Scripts` folder.
This runs PyFlakes (requires PyFlakes to be installed at `/usr/local/bin` -
try ``/usr/bin/easy_install-2.6 pyflakes==0.4.0``) and reformats the results
so that they show up in BBEdit's search results / error / warnings window. Then
the errors can be stepped through one at a time.

I've bound this to control-shift-V. You must save your Python file first before
running the check.

FROM: <https://gist.github.com/1157742>
"""

from __future__ import print_function
import os
import re
import sys
from subprocess import Popen, PIPE

doc_file = os.environ['BB_DOC_PATH']
pyflakes = "/usr/local/bin/pyflakes"

out, err = Popen([pyflakes, doc_file], stdout=PIPE, stderr=PIPE).communicate()
if out:
    output = out
else:
    output = err

if not output:
    sys.exit(0)

line_format = re.compile('(?P<path>[^:]+):(?P<line>\d+):\s(?P<message>.*$)')
for line in output.splitlines():
    m = line_format.match(line)
    if not m:
        continue
    groups = m.groupdict()
    print('''  File "{path}", line {line}'''.format(**groups), file=sys.stderr)
    print(groups['message'], file=sys.stderr)
    print('^', file=sys.stderr)

sys.exit(1)
