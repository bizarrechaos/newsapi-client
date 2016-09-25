import json

from itertools import izip_longest


def jprint(jsondoc):
    print json.dumps(jsondoc, sort_keys=True, indent=2, separators=(',', ': '))


def printSrcs(lst):
    if lst:
        for a,b,c in izip_longest(lst[::3],lst[1::3],lst[2::3],fillvalue=' '):
            print '%-30s%-30s%s' % (a,b,c)


def printCats(cats):
    if cats:
        for c in cats:
            print c


def printArts(arts):
    if arts:
        for a in arts:
            jprint(a)
            break
