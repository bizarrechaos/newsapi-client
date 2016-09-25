#! /usr/bin/env python

"""news.py

Usage:
    news [-a <apikey>] get ((sources [<category>...]|articles (<category>...|<source>...) [-s <sortby>])|categories)

Options:
    -a <apikey>, --apikey <apikey>    Use the provided apikey.
    -s <sortby>, --sort <sortby>      Sort the articles returned by (top, latest, popular) [default: top].
    -h, --help                        Show this page.
    -v, --version                     Show the application version.
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
            newsapilib.output.printSrcs(n.getSources(args['<category>']))
        elif args['categories']:
            newsapilib.output.printCats(n.getCategories())
        elif args['articles']:
            newsapilib.output.printArts(n.getArticles(args['<category>'],
                                                      args['<source>'],
                                                      args['-s']))
    print args
