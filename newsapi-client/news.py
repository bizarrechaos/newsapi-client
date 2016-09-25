#! /usr/bin/env python

"""news.py

Usage:
    news [options] get ((sources [<category>...]|articles [<category>|<source>])|categories)

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
    CATEGORIES = None
    if args['get']:
        if args['sources']:
            if args['<category>']:
                CATEGORIES = args['<category>']
            newsapilib.output.printSrcs(n.getSources(CATEGORIES))
        elif args['categories']:
            newsapilib.output.printCats(n.getCategories())
