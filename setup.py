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
      version=VERSION,
      description="A Django-based EVE API proxy.",
      long_description=LONG_DESCRIPTION,
      author='Gregory Taylor',
      author_email='snagglepants@gmail.com',
      url='https://github.com/gtaylor/django-eve-proxy',
      license='GPL',
      platforms=['any'],
      packages=[
          'eve_proxy',
          'eve_proxy.migrations'
      ],
      requires=['django'],
      provides=['eve_proxy'],
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
)

