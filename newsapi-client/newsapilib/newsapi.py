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

    def getSources(self, cats):
        sourceslist = []
        r = requests.get('{}{}'.format(self.baseurl, self.sourcesuri), verify=False)
        r.raise_for_status()
        if r.ok:
            if r.json():
                if 'sources' in r.json():
                    if r.json()['sources']:
                        for source in r.json()['sources']:
                            if 'id' in source:
                                if not cats:
                                    sourceslist.append(source['id'])
                                else:
                                    if 'category' in source:
                                        for cat in cats:
                                            if source['category'] == cat:
                                                sourceslist.append(source['id'])
        return sourceslist

    def getCategories(self):
        categorieslist = []
        r = requests.get('{}{}'.format(self.baseurl, self.sourcesuri), verify=False)
        r.raise_for_status()
        if r.ok:
            if r.json():
                if 'sources' in r.json():
                    if r.json()['sources']:
                        for source in r.json()['sources']:
                            if 'category' in source:
                                categorieslist.append(source['category'])
        return set(categorieslist)

    def getArticles(self, cats, srcs, sortby):
        articleslist = []
        if cats:
            srcs += self.getSources(cats)
        for src in srcs:
            r = requests.get('{}{}?source={}&sortBy={}&apiKey={}'.format(self.baseurl,
                                                                         self.articlesuri,
                                                                         src,
                                                                         sortby,
                                                                         self.apikey))
            if r.ok:
                if r.json():
                    if 'articles' in r.json():
                        articleslist += r.json()['articles']
        return articleslist
