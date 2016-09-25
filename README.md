#:newspaper: newsapi-client

###A command line client for newsapi.org written in Python

####Installation:
- git clone
- pip install -r requirements.txt
- get an apikey from [newsapi](https://newsapi.org/)
- run it

####Usage overview:
```
news.py

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
```

####to do:
- pep8
- unit testing
- setuptools install
- pyhton3 compatibility

######powered by [newsapi](https://newsapi.org)
