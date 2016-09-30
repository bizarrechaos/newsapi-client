import json
import pytest
import responses

from news import newsapi


class TestNewsAPI(object):

    def test_news_api(self):
        n = newsapi.NewsAPI('testapikey')
        assert n.apikey == 'testapikey'
        assert n.baseurl == 'https://newsapi.org/v1'
        assert n.articlesuri == '/articles'
        assert n.sourcesuri == '/sources'

    @responses.activate
    def test_get_sources_without_cats(self):
        n = newsapi.NewsAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(n.baseurl, n.sourcesuri),
                      status=200,
                      body=json.dumps({'sources': [{'id': 'test'}]}))
        assert n.get_sources([]) == ['test']

    @responses.activate
    def test_get_sources_with_cats(self):
        n = newsapi.NewsAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(n.baseurl, n.sourcesuri),
                      status=200,
                      body=json.dumps({'sources': [{'id': 'test',
                                                    'category': 'test'}]}))
        assert n.get_sources(['test']) == ['test']

    @responses.activate
    def test_get_categories(self):
        n = newsapi.NewsAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(n.baseurl, n.sourcesuri),
                      status=200,
                      body=json.dumps({'sources': [{'category': 'test'}]}))
        assert n.get_categories() == set(['test'])

    @responses.activate
    def test_get_articles_without_cats(self):
        n = newsapi.NewsAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(n.baseurl, n.articlesuri),
                      status=200,
                      body=json.dumps({'articles': ['test']}))
        assert n.get_articles(None, ['test'], 'top') == ['test']

    @responses.activate
    def test_get_articles_with_cats(self):
        n = newsapi.NewsAPI('testapikey')
        responses.add(responses.GET,
                      '{0}{1}'.format(n.baseurl, n.sourcesuri),
                      status=200,
                      body=json.dumps({'sources': [{'id': 'test',
                                                    'category': 'test'}]}))
        responses.add(responses.GET,
                      '{0}{1}'.format(n.baseurl, n.articlesuri),
                      status=200,
                      body=json.dumps({'articles': ['test']}))
        assert n.get_articles(['test'], [], 'top') == ['test']
