from setuptools import setup


setup(
    name='newsapi-client',
    version='0.0.1dev',
    author='bizarrechaos',
    packages=['news'],
    license='Apache License Version 2.0',
    description='newsapi.org command line client and wrapper',
    install_requires=['docopt==0.6.2', 'requests==2.11.1'],
    url='https://github.com/bizarrechaos/newsapi-client',
    entry_points='''
        [console_scripts]
        news = newsapi-client.__main__:main
    '''
)
