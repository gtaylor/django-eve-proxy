==============
django-eve-api
==============

django-eve-api is a set of `Django`_ models meant to make querying the EVE data 
API trivial. All parsing of the data returned by the API is handled, as are 
cache recycle times via django-eve-proxy.

**NOTE: django-eve-api is not stable enough for the development of third party 
applications just yet (aside from django-eve-db). You are welcome 
(and encouraged) to tinker, just be aware that things are still rapidly 
changing and may break periodically.**

Source: https://github.com/gtaylor/django-eve-api

.. _Django: http://djangoproject.com

---------------
Getting Started
---------------

For details on how to get started using this software, see the 
`Getting Started`_ page. Note that since this app requires django-eve-db and 
django-eve-proxy, it may be better to just install `django-eve`_, which wraps 
all of these into a neat starter project framework.

.. _Getting Started: https://github.com/gtaylor/django-eve-api/wiki/Getting-started
.. _django-eve: http://code.google.com/p/django-eve/

-----------
Development
-----------

This software and all related projects are primarily developed by 
Blackman Industries, a software consulting and development EVE Corporation. 
Please consider sending ISK if this software has saved you time or 
benefited you.

-------
Support
-------

For support, you may either file an issue in our issue tracker, or send a 
message to our `mailing list`_.

.. _mailing list: http://groups.google.com/group/django-eve
