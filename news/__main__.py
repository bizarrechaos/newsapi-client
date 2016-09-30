"""news

Usage:
    news [-a apikey] get categories
    news [-a apikey] get sources [<category>...]
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

from docopt import docopt

from . import newsconfig
from . import output
from . import newsapi


def main():
    args = docopt(__doc__, version='news.py 1.0')
    if args['--apikey']:
        c = newsconfig.NewsConfig(apikey=args['--apikey'])
    else:
        c = newsconfig.NewsConfig()
    n = newsapi.NewsAPI(c.apikey)
    if args['get']:
        if args['sources']:
            output.print_srcs(n.get_sources(args['<category>']))
        elif args['categories']:
            output.print_cats(n.get_categories())
        elif args['articles']:
            output.print_arts(n.get_articles(args['<category>'],
                                             args['<source>'],
                                             args['--sort']))


if __name__ == "__main__":
    main()
