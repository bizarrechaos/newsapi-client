import ConfigParser
import sys

from os.path import expanduser, isfile


class NewsConfig(object):
    """handles reading, writing, and validating
       the configuration for newsapi.org"""
    def __init__(self, configpath=None, apikey=None):
        super(NewsConfig, self).__init__()
        self.section = 'newsapi.org'
        self.configpath = self.set_config_path(configpath)
        self.apikey = self.set_api_key(apikey)

    def set_config_path(self, configpath):
        if configpath is None:
            # set config path to the default of the users home directory
            configpath = '{}/{}'.format(expanduser('~'), 'news.cfg')
        return configpath

    def set_api_key(self, apikey):
        if apikey is None:
            if isfile(self.configpath):
                apikey = self.read_config('apikey')
            else:
                print '{} does not exist'.format(self.configpath)
                print 'create {}, or use the -a flag'.format(self.configpath)
                sys.exit(1)
        return apikey

    def read_config(self, key):
        parser = ConfigParser.SafeConfigParser()
        parser.read(self.configpath)
        return parser.get(self.section, key)
