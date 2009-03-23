#!/usr/bin/env python
"""
django-eve-proxy (example.py) - Example Python API Usage

Copy this file to the root of your Django project's directory and un-comment
the desired example below to see a live example of direct API access.
"""
import os
# Set up the Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from eve_proxy.models import CachedDocument

if __name__ == "__main__":
    # Query with no parameters.
    #cached_doc = CachedDocument.objects.api_query('/eve/ErrorList.xml.aspx', None)
    
    # A query with parameters.
    """
    cached_doc = CachedDocument.objects.api_query('/account/Characters.xml.aspx', 
      {'apiKey': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 
       'userID': 'xxxxxxx'})
    """
    
    # Print the results from EVE API as a string.
    print cached_doc.body