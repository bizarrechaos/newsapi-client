#! /usr/bin/env python

"""news.py

Usage:
    news [-a <apikey>] get (categories|(sources [<category>...]|articles (source <source>...|category <category>...) [-s <sortby>]))

Options:
    -a <apikey>, --apikey <apikey>    Use the provided apikey.
    -s <sortby>, --sort <sortby>      Sort the articles returned by (top, latest, popular) [default: top].
    -h, --help                        Show this page.
    -v, --version                     Show the application version.

Examples:
    news get categories                         Get all categories.
    news get sources                            Get all sources.
    news get sources general                    Get all sources classified as general.
    news get sources general music              Get all sources classified as general, and music.
    news get articles source cnn                Get all articles from cnn.
    news get articles source cnn cnbc           Get all articles from cnn, and cnbc.
    news get articles category general          Get all articles from all sources classified as general.
    news get articles category general music    Get all articles from all sources classified as general, and music.
"""

import newsapilib

from docopt import docopt


if __name__ == "__main__":
    args = docopt(__doc__, version='news.py 1.0.0')
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
                                                      args['--sort']))
