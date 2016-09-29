import sys
import pytest

from news import output


class TestOutput(object):

    def test_print_srcs(self, capsys):
        lst = ['one', 'two', 'three']
        output.print_srcs(lst)
        out, err = capsys.readouterr()
        assert out == '{:30}{:30}{}\n'.format(lst[0], lst[1], lst[2])

    def test_print_cats(self, capsys):
        lst = ['one', 'two', 'three']
        output.print_cats(lst)
        out, err = capsys.readouterr()
        assert out == '{}\n{}\n{}\n'.format(lst[0], lst[1], lst[2])

    def test_print_arts(self, capsys):
        arts = [{u'description': u'This is a description',
                 u'title': u'This is a title',
                 u'url': u'http://example.com',
                 u'author': u'bizarrechaos',
                 u'publishedAt': u'2016-09-29T21:38:14Z'}]
        bystring = 'by bizarrechaos at 21:38 on Thursday, September 29, 2016'
        output.print_arts(arts)
        out, err = capsys.readouterr()
        assert out == '{}\n{}\n{}\n{}\n\n'.format(arts[0]['title'],
                                                  bystring,
                                                  arts[0]['description'],
                                                  arts[0]['url'])

    def test_print_arts_with_none(self, capsys):
        arts = [{u'description': u'This is a description',
                 u'title': u'This is a title',
                 u'url': u'http://example.com',
                 u'author': None,
                 u'publishedAt': u'2016-09-29T21:38:14Z'}]
        bystring = 'by None at 21:38 on Thursday, September 29, 2016'
        output.print_arts(arts)
        out, err = capsys.readouterr()
        assert out == '{}\n{}\n{}\n{}\n\n'.format(arts[0]['title'],
                                                  bystring,
                                                  arts[0]['description'],
                                                  arts[0]['url'])

    def test_print_arts_miliseconds(self, capsys):
        arts = [{u'description': u'This is a description',
                 u'title': u'This is a title',
                 u'url': u'http://example.com',
                 u'author': u'bizarrechaos',
                 u'publishedAt': u'2016-09-29T21:38:14.123Z'}]
        bystring = 'by bizarrechaos at 21:38 on Thursday, September 29, 2016'
        output.print_arts(arts)
        out, err = capsys.readouterr()
        assert out == '{}\n{}\n{}\n{}\n\n'.format(arts[0]['title'],
                                                  bystring,
                                                  arts[0]['description'],
                                                  arts[0]['url'])

    def test_print_arts_broken_date(self):
        with pytest.raises(ValueError):
            arts = [{u'description': u'This is a description',
                     u'title': u'This is a title',
                     u'url': u'http://example.com',
                     u'author': u'bizarrechaos',
                     u'publishedAt': u'2016-09-29T21:38:14.123ZFAIL'}]
            output.print_arts(arts)
