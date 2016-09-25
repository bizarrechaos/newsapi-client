import calendar
import json

from datetime import datetime
from itertools import izip_longest


def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )


def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )


def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data


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
            print json_loads_byteified(a)
            # dt = datetime.strptime(a['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            # dayname = calendar.day_name[datetime.date(dt).weekday()]
            # monthname = calendar.month_name[dt.month]
            # ad['publishedAt'] = 'at {}:{} on {}, {} {}, {}'.format(dt.hour, dt.minute, dayname, monthname, dt.day, dt.year)
            #print '{title}\nby {author} {publishedAt}\n{description}\n{url}'.format(**ad)
