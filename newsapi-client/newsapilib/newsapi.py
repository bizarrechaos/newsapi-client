import requests


class NewsAPI(object):
    """interacts with newsapi"""
    def __init__(self, apikey):
        super(NewsAPI, self).__init__()
        self.apikey = apikey
        self.baseurl = 'https://newsapi.org/v1'
        self.articlesuri = '/articles'
        self.sourcesuri = '/sources'

    def getSources(self):
        r = requests.get('%s%s' % (self.baseurl, self.sourcesuri), verify=False)
        return r.json()
    #get articles from source
    #get sources by category
    #get articles by category
    #get category
