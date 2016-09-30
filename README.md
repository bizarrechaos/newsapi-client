#:newspaper: newsapi-client [![Build Status](https://travis-ci.org/bizarrechaos/newsapi-client.svg?branch=master)](https://travis-ci.org/bizarrechaos/newsapi-client)

###A command line client for newsapi.org written in Python

####Installation:

You can install the latest available version of newsapi-client from GitHub using pip:

```
pip install git+git://github.com/bizarrechaos/newsapi-client.git
```

You can also clone the repository and install newsapi-client:

```
git clone https://github.com/bizarrechaos/newsapi-client.git
cd newsapi-client
python setup.py install
```

####Configuration:

You will need to get an apikey from [newsapi](https://newsapi.org/).

By default newsapi-client will look in your home directory for a configuration file that contains your newsapi apikey. The file should look like this:

```
[newsapi.org]
apikey = thisisanapikey
# 'thisisanapikey' should be replaced with your actual apikey
```

If you do not wish to use an apikey use the -a/--apikey flag to pass your apikey at runtime.

####Usage overview:
```
news

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
```

######powered by [newsapi](https://newsapi.org)
