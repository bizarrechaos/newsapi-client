import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class NewsAPI(object):
    """interacts with newsapi"""
    def __init__(self, apikey):
        super(NewsAPI, self).__init__()
        self.apikey = apikey
        self.baseurl = 'https://newsapi.org/v1'
        self.articlesuri = '/articles'
        self.sourcesuri = '/sources'

    def getSources(self):
        sourceslist = []
        r = requests.get('%s%s' % (self.baseurl, self.sourcesuri), verify=False)
        r.raise_for_status()
        if r.ok:
            if r.json():
                if 'sources' in r.json():
                    if r.json()['sources']:
                        for source in r.json()['sources']:
                            if 'id' in source:
                                sourceslist.append(source['id'])
        return sourceslist
    #get articles from source
    #get sources by category
    #get articles by category
    #get category
