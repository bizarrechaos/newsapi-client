#! /usr/bin/env python

"""news.py

Usage:
    news test [options]

Options:
    -a APIKEY, --apikey APIKEY    Use the provided apikey.
    -h, --help                    Show this page.
    -v, --version                 Show the application version.
"""

import newsapilib

from docopt import docopt


if __name__ == "__main__":
    args = docopt(__doc__, version='news.py 0.0.1')
    if args['--apikey']:
        c = newsapilib.newsconfig.NewsConfig(apikey=args['--apikey'])
    else:
        c = newsapilib.newsconfig.NewsConfig()
    print args
    print c.apikey
    print c.configpath
    print c.section
