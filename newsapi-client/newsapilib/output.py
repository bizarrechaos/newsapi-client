import json


def jprint(jsondoc):
    print json.dumps(jsondoc, sort_keys=True, indent=2, separators=(',', ': '))


def lprint(lst):
    for i in lst:
        print i
