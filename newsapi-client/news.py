#! /usr/bin/env python

"""news.py

Usage:
    news [options] get ((sources|articles [<source>]) [<category>]|categorys)

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
    n = newsapilib.newsapi.NewsAPI(c.apikey)
    if args['get']:
        if args['sources']:
            newsapilib.output.printSrcs(n.getSources())
