# encoding: utf-8

from __future__ import print_function
from workflow import Workflow, web, ICON_NETWORK
import sys
import re

TABLENAME = "unit_alfred_workflow"


def number_to_string(number):
    return ('%.30f' % number).rstrip('0').rstrip('.')

def add_action(wf, unit_from, unit_to, rate):
    try:
        rate = float(rate)
        unit_from = unit_from.upper()
        unit_to   = unit_to.upper()

        table = wf.stored_data(TABLENAME)
        table[(unit_from, unit_to)] = rate
        table[(unit_to, unit_from)] = 1 / rate
        wf.store_data(TABLENAME, table)

        print('1%s = %s%s' % (unit_from, number_to_string(rate), unit_to), file=sys.stdout)
        print('1%s = %s%s' % (unit_to, number_to_string(1/rate), unit_from), file=sys.stdout)
        sys.stdout.flush()
    except ValueError:
        pass


def main(wf):
    query0 = wf.args[0]

    if 'add' in query0:
        [_, unit_from, unit_to, rate] = query0.split(',')
        add_action(wf, unit_from, unit_to, rate)


if __name__ == '__main__':
    wf = Workflow()
    exited = wf.run(main)
    sys.exit(exited)
