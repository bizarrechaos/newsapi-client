from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('./requirements.txt')

# reqs is a list of requirement
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='newsapi-client',
    version='0.0.1dev',
    author='bizarrechaos',
    packages=['news'],
    license='Apache License Version 2.0',
    description='newsapi.org command line client and wrapper',
    long_description=open('README.txt').read(),
    install_requires=reqs,
    url='https://github.com/bizarrechaos/newsapi-client',
    entry_points='''
        [console_scripts]
        news = newsapi-client.__main__:main
    '''
)
