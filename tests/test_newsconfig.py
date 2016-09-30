import pytest

from news import newsconfig


class TestNewsConfig(object):

    def test_news_config_with_path(self):
        n = newsconfig.NewsConfig('./news.cfg.example')
        assert n.configpath == './news.cfg.example'

    def test_news_config_without_path(self, capsys):
        try:
            with pytest.raises(SystemExit):
                n = newsconfig.NewsConfig()
        except:
            n = newsconfig.NewsConfig()
            assert n.apikey == n.set_api_key(None)

    def test_news_config_with_tmp_path(self):
        with pytest.raises(SystemExit):
            n = newsconfig.NewsConfig('/tmp/notafile')
