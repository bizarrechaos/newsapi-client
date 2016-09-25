import json


def jprint(jsondoc):
    print json.dumps(jsondoc, sort_keys=True, indent=2, separators=(',', ': '))


def printSrcs(lst):
    for a,b,c in zip(lst[::3],lst[1::3],lst[2::3]):
        print '%-30s%-30s%s' % (a,b,c)


def printCats(cats):
    for c in cats:
        print c


def printArts(arts):
    jprint(arts[0])
