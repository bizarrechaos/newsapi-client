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
            try:
                userhome = expanduser('~')
            except:
                userhome = './'
            configfilename = 'news.cfg'
            configpath = '{}/{}'.format(userhome, configfilename)
        return configpath

    def set_api_key(self, apikey):
        if apikey is None:
            if not isfile(self.configpath):
                print '{} does not exist'.format(self.configpath)
                reply = (str(raw_input('Create a new config '
                         '[y/n]: ')).lower().strip())
                if reply[0] != 'y':
                    print 'No config to parse, creation declined, exiting...'
                    sys.exit(1)
                apikey = str(raw_input('newsapi.org apikey: '))
                if not apikey:
                    print 'No config to parse, apikey is not valid, exiting...'
                    sys.exit(2)
                self.create_config('apikey', apikey)
            apikey = self.read_config('apikey')
        return apikey

    def create_config(self, key, value):
        parser = ConfigParser.SafeConfigParser()
        parser.add_section(self.section)
        parser.set(self.section, key, value)
        with open(self.configpath, 'w') as fout:
            parser.write(fout)

    def read_config(self, key):
        parser = ConfigParser.SafeConfigParser()
        parser.read(self.configpath)
        return parser.get(self.section, key)
