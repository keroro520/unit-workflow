# encoding: utf-8

from __future__ import print_function
from workflow import Workflow
import sys
import re


def main(wf):
    query0 = wf.args[0]

    try:
        result = float(query0)
        result = ('%.30f' % result)
        result = result.rstrip('0').rstrip('.')
        print(result, file=sys.stdout, end='')
        sys.stdout.flush()
    except ValueError:
        pass


if __name__ == '__main__':
    wf = Workflow()
    exited = wf.run(main)
    sys.exit(exited)
