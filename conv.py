# encoding: utf-8

from __future__ import print_function, division
from workflow import Workflow, web, ICON_NETWORK
import sys
import re


TABLENAME = "unit_alfred_workflow"
INIT_TABLE = {("MB", "B"): 1024 * 1024,
              ("MB", "KB"): 1024,
              ("MB", "GB"): 1/1024,
              ("B", "KB"): 1/1024,
              ("B", "MB"): 1/1024 * 1/1024,
              ("B", "GB"): 1/1024 * 1/1024 * 1/1024,
              ("KB", "B"): 1024,
              ("KB", "MB"): 1/1024,
              ("KB", "GB"): 1/1024 * 1/1024,
              ("GB", "B"): 1/1024 * 1/1024 * 1/1024,
              ("GB", "KB"): 1/1024 * 1/1024,
              ("GB", "MB"): 1/1024}
wf = Workflow()
if wf.stored_data(TABLENAME) is None:
    wf.store_data(TABLENAME, INIT_TABLE)
TABLE = wf.stored_data(TABLENAME)


ACTION_PATTERN = r'^(?P<number>\d+(\.\d+)*)(?P<type>[a-zA-Z]+)$'
def next_action(query):
    matched = re.match(ACTION_PATTERN, query)
    if matched is None:
        return 0, "***"

    typo = matched.group("type").upper()
    if typo in [f for (f, _) in TABLE.keys()]:
        return float(matched.group("number")), typo

    return float(matched.group("number")), "***"


def number_to_string(number):
    return ('%.30f' % number).rstrip('0').rstrip('.')


def conv_unit(wf, number, unit):
    convs = [(f, t, rate)
             for ((f, t), rate) in TABLE.items() if f == unit]

    for (f, t, rate) in convs:
        before_number = number_to_string(number)
        after_number  = number_to_string(number * rate)
        wf.add_item('%s%s = %s%s' % (before_number, f, after_number, t),
                    after_number,
                    arg=after_number,
                    valid=True,
                    icon=ICON_NETWORK)


def add_action(wf, unit_from, unit_to, rate):
    try:
        rate = number_to_string(float(rate))
        unit_from = unit_from.upper()
        unit_to   = unit_to.upper()
        wf.add_item('Add Item: 1%s = %s%s' % (unit_from, rate, unit_to),
                    '',
                    arg='add,%s,%s,%s' % (unit_from, unit_to, rate),
                    valid=True,
                    icon=ICON_NETWORK)
    except ValueError:
        pass


def main(wf):
    query0 = wf.args[0]

    if query0 == "add" and len(wf.args) == 4:
        add_action(wf, wf.args[1], wf.args[2], wf.args[3])
    else:
        number, unit = next_action(query0)
        if unit != "***":
            conv_unit(wf, number, unit)
        else:
            wf.add_item(' ', ' ', valid=False, icon=ICON_NETWORK)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    exited = wf.run(main)
    sys.exit(exited)
