import ConfigParser
import sys

from os.path import expanduser, isfile


class NewsConfig(object):
    """handles reading, writing, and validating the configuration for newsapi.org"""
    def __init__(self, configpath=None, apikey=None):
        super(NewsConfig, self).__init__()
        self.section = 'newsapi.org'
        self.configpath = self.setConfigPath(configpath)
        self.apikey = self.setApiKey(apikey)

    def setConfigPath(self, configpath):
        if configpath is None:
            #set config path to the default of the users home directory
            try:
                userhome = expanduser('~')
            except:
                userhome = './'
            configfilename = 'news.cfg'
            configpath = '%s/%s' % (userhome, configfilename)
        return configpath

    def setApiKey(self, apikey):
        if apikey is None:
            if not isfile(self.configpath):
                print '%s does not exist' % self.configpath
                reply = str(raw_input('Would you like to create a new config? [y/n]: ')).lower().strip()
                if reply[0] != 'y':
                    print 'No config to parse, creation declined, exiting...'
                    sys.exit(1)
                apikey = str(raw_input('What is your newsapi.org apikey?: '))
                if not apikey:
                    print 'No config to parse, apikey is not valid, exiting...'
                    sys.exit(2)
                self.createConfig('apikey', apikey)
            apikey = self.readConfig('apikey')
        return apikey

    def createConfig(self, key, value):
        parser = ConfigParser.SafeConfigParser()
        parser.add_section(self.section)
        parser.set(self.section, key, value)
        with open(self.configpath, 'w') as fout:
            parser.write(fout)

    def readConfig(self, key):
        parser = ConfigParser.SafeConfigParser()
        parser.read(self.configpath)
        return parser.get(self.section, key)

