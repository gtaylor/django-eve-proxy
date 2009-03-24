import httplib
import urllib
from datetime import datetime, timedelta
from xml.dom import minidom
from django.db import models

# You generally never want to change this unless you have a very good reason.
API_URL = 'api.eve-online.com'

class CachedDocumentManager(models.Manager):
    """
    This manager handles querying or retrieving CachedDocuments.
    """
    def cache_from_eve_api(self, cached_doc, url_path, params):
        """
        Connect to the EVE API server, send the request, and cache it to
        a CachedDocument. This is typically not something you want to call
        directly. Use api_query().
        """
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        # This is the connection to the EVE API server.
        conn = httplib.HTTPConnection(API_URL)
        # Combine everything into an HTTP request.
        conn.request("POST", url_path, params, headers)
        # Retrieve the response from the server.
        response = conn.getresponse()
        # Save the response (an XML document) to the CachedDocument.
        cached_doc.body = response.read()
    
        # Parse the response via minidom
        dom = minidom.parseString(cached_doc.body)
        # Set the CachedDocument's time_retrieved and cached_until times based
        # on the values in the XML response. This will be used in future
        # requests to see if the CachedDocument can be retrieved directly or
        # if it needs to be re-cached.
        cached_doc.time_retrieved = datetime.utcnow()
        cached_doc.cached_until = dom.getElementsByTagName('cachedUntil')[0].childNodes[0].nodeValue
    
        # Finish up and return the resulting document just in case.
        cached_doc.save()
        return cached_doc
    
    def api_query(self, url_path, params=None):
        """
        Transparently handles querying EVE API or retrieving the document from
        the cache.
        
        Arguments:
        url_path: (string) Path to the EVE API page to query. For example:
                           /eve/ErrorList.xml.aspx
        params: (dictionary/string) A dictionary of extra parameters to include.
                                    May also be a string representation of
                                    the query: userID=1&characterID=xxxxxxxx
        """
        if type({}) == type(params):
            # If 'params' is a dictionary, convert it to a URL string.
            params = urllib.urlencode(params)
        elif params == None or params.strip() == '':
            # For whatever reason, EVE API freaks out if there are no parameters.
            # Add a bogus parameter if none are specified. I'm sure there's a
            # better fix for this.
            params = 'odd_parm=1'
        
        # Combine the URL path and the parameters to create the full query.
        query_name = '%s?%s' % (url_path, params)
        
        # Retrieve or create a new CachedDocument based on the full URL
        # and parameters.
        cached_doc, created = self.get_or_create(url_path=query_name)
    
        # EVE uses UTC.
        current_eve_time = datetime.utcnow()

        # Figure out if we need hit EVE API and re-cache, or just pull from
        # the local cache (based on cached_until).
        if created or \
          cached_doc.cached_until == None or \
          current_eve_time > cached_doc.cached_until:
            # Cache from EVE API
            self.cache_from_eve_api(cached_doc, url_path, params)
            
        return cached_doc

class CachedDocument(models.Model):
    """
    This is a cached XML document from the EVE API.
    """
    url_path = models.CharField(max_length=255)
    body = models.TextField()
    time_retrieved = models.DateTimeField(blank=True, null=True)
    cached_until = models.DateTimeField(blank=True, null=True)

    # The custom manager handles the querying.
    objects = CachedDocumentManager()