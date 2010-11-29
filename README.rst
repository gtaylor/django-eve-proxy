================
django-eve-proxy
================

django-eve-proxy is a Django app that allows you to host an EVE API proxy that
is open to web requests or internal requests programatically. Honors EVE API 
cache expiration intervals and updates as needed (which means you don't have 
to worry about stuff like cachedUntil).

Source: https://github.com/duointeractive/django-eve-proxy

---------------------
Example Python Access
---------------------

::

    # Query with no parameters.
    cached_doc = CachedDocument.objects.api_query('/eve/ErrorList.xml.aspx', params=None)
    # Print the results from EVE API as a string.
    print cached_doc.body
 
    # A query with parameters.
    cached_doc = CachedDocument.objects.api_query('/account/Characters.xml.aspx', 
      params={
       'apiKey': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 
       'userID': 'xxxxxxx'
      })
    
    # Print the results from EVE API as a string.
    print cached_doc.body

-------------------
Example HTTP Access
-------------------

Instead of pointing your script at http://api.eve-online.com, point it at 
http://proxy.yoursite.com.

----------------
Database Support
----------------

django-eve-proxy runs on all of the databases supported by 
Django (currently SQLite, Postgres, MySQL, Oracle, and a few others 
unofficially), but does experience some difficulty when using databases in 
encodings other than UTF-8 (which is what CCP sends their XML data back as). 
Notably, SQLite will run into occasional encoding errors that must be handled 
on your end.

------------
Installation
------------
To install, download the latest django-eve-proxy release from the _Downloads_ 
section, run `setup.py install` as with any Python package, and add 
`eve_proxy` to your setting.py `INSTALLED_APPS` tuple. For those what would 
like to expose the HTTP proxy, you'll need to add an entry to your `urls.py` 
that points to `eve_proxy.urls`. More detailed may be found in the INSTALL file.

---------------
Example Project
---------------

If you'd like to see an example Django project using django-eve-proxy, 
download  eve_proxy_site.zip file via the **Downloads** button on our github
page.

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
