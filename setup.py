#!/usr/bin/env python
from distutils.core import setup
from eve_proxy import VERSION

LONG_DESCRIPTION = open('README.rst', 'r').read()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities'
]

KEYWORDS = 'EVE Online CCP Django proxy'

setup(name='django-eve-proxy',
      version=version,
      description="A Django-based EVE API proxy.",
      long_description=LONG_DESCRIPTION,
      author='Gregory Taylor',
      author_email='snagglepants@gmail.com',
      url='https://github.com/gtaylor/django-eve-proxy',
      license='GPL',
      platforms=['any'],
      packages=[
          'eve_api',
          'eve_api.api_puller', 'eve_api.api_puller.account',
          'eve_api.api_puller.character', 'eve_api.api_puller.corporation',
          'eve_api.api_puller.eve', 'eve_api.api_puller.map',
          'eve_api.api_puller.server',
          'eve_api.management', 'eve_api.management.commands',
          'eve_api.migrations',
          'eve_api.models',
          'eve_api.tests',
      ],
      requires=['django'],
      provides=['django-eve-proxy'],
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
)

