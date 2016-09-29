"""news

Usage:
    news [-a apikey] get categories
    news [-a apikey] get sources [<categories>...]
    news [-a apikey] get articles source <source>... [-s <sortby>]
    news [-a apikey] get articles category <category>... [-s <sortby>]

Options:
    -a <apikey>, --apikey <apikey>    Use the provided apikey.
    -s <sortby>, --sort <sortby>      Sort the articles returned by
                                      (top, latest, popular) [default: top].
    -h, --help                        Show this page.
    -v, --version                     Show the application version.

Examples:
    news get categories                         All categories.
    news get sources                            All sources.
    news get sources general                    Sources from one category.
    news get sources general music              Sources from many categories.
    news get articles source cnn                Articles from one source.
    news get articles source cnn cnbc           Articles from many sources.
    news get articles category general          Articles from one category.
    news get articles category general music    Articles from many categories.
"""

import newsapilib

from docopt import docopt


def main():
    args = docopt(__doc__, version='news.py 0.0.1dev')
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


if __name__ == "__main__":
    main()
