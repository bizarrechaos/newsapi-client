import calendar
import json

from datetime import datetime
from itertools import izip_longest


def jprint(jsondoc):
    print json.dumps(jsondoc, sort_keys=True, indent=2, separators=(',', ': '), ensure_ascii=False).encode('utf-8', 'replace')


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
            try:
                dt = datetime.strptime(a['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
                dayname = calendar.day_name[dt.date().weekday()]
                monthname = calendar.month_name[dt.month]
                time = dt.strftime("%H:%M")
                a['publishedAt'] = 'at {} on {}, {} {}, {}'.format(time, dayname, monthname, dt.day, dt.year)
                print u'{title}\nby {author} {publishedAt}\n{description}\n{url}\n'.format(**a)
            except:
                print a
                jprint(a)
