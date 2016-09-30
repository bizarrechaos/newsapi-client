import calendar

from datetime import datetime
from itertools import izip_longest


def print_srcs(lst):
    if lst:
        for a, b, c in izip_longest(lst[::3],
                                    lst[1::3],
                                    lst[2::3],
                                    fillvalue=' '):
            print '{0:30}{1:30}{2}'.format(a, b, c)


def print_cats(cats):
    if cats:
        for c in cats:
            print c


def print_arts(arts):
    if arts:
        for a in arts:
            for b in a:
                if a[b] is None:
                    a[b] = 'None'
            if a['publishedAt'] != 'None':
                try:
                    dt = datetime.strptime(a['publishedAt'],
                                           "%Y-%m-%dT%H:%M:%SZ")
                except:
                    try:
                        dt = datetime.strptime(a['publishedAt'],
                                               "%Y-%m-%dT%H:%M:%S.%fZ")
                    except Exception as e:
                        raise e
                dayname = calendar.day_name[dt.date().weekday()]
                monthname = calendar.month_name[dt.month]
                time = dt.strftime("%H:%M")
                a['publishedAt'] = ('at {0} on {1}, {2} {3}, {4}'
                                    .format(time,
                                            dayname,
                                            monthname,
                                            dt.day,
                                            dt.year))
            print (u'{title}\nby {author} {publishedAt}\n'
                   '{description}\n{url}\n'.format(**a))
