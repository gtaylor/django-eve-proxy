import httplib
import urllib
from datetime import datetime, timedelta
from xml.parsers.expat import ExpatError
from xml.etree import ElementTree
from django.db import models
from django.conf import settings
from eve_proxy.proxy_exceptions import InvalidAPIResponseException
from eve_proxy.api_error_exceptions import APIQueryErrorException

# To change this, create a variable in your local_settings.py called
# EVE_API_URL, which will be grabbed from here.
API_URL = getattr(settings, 'EVE_API_URL', 'api.eve-online.com')

class CachedDocumentManager(models.Manager):
    """
    This manager handles querying or retrieving CachedDocuments.
    """
    def cache_from_eve_api(self, cached_doc, url_path, params, no_cache=False):
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
    
        try:
            # Parse the response via minidom
            tree = ElementTree.fromstring(cached_doc.body)
        except ExpatError:
            raise InvalidAPIResponseException(cached_doc.body)

        # Set the CachedDocument's time_retrieved and cached_until times based
        # on the values in the XML response. This will be used in future
        # requests to see if the CachedDocument can be retrieved directly or
        # if it needs to be re-cached.
        cached_doc.time_retrieved = datetime.utcnow()
        try:
            cached_doc.cached_until = tree.find('cachedUntil').text
        except IndexError:
            # When we see failure here, we can safely assume that the response
            # is malformed, since all API responses have a cachedUntil tag.
            raise InvalidAPIResponseException(cached_doc.body)
    
        # Finish up and return the resulting document just in case.
        if no_cache == False:
            cached_doc.save()

        return tree
    
    def api_query(self, url_path, params=None, no_cache=False):
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
            # If 'params' is a dictionary, we're good to go.
            pass
        elif params == None or params.strip() == '':
            # For whatever reason, EVE API freaks out if there are no parameters.
            # Add a bogus parameter if none are specified. I'm sure there's a
            # better fix for this.
            params = {'odd_parm': '1'}
        
        # Convert params to a URL encoded string.    
        params = urllib.urlencode(params)
        
        # Combine the URL path and the parameters to create the full query.
        query_name = '%s?%s' % (url_path, params)
        
        if no_cache:
            # If no_cache is enabled, don't even attempt a lookup.
            cached_doc = CachedDocument()
            created = False
        else:
            # Retrieve or create a new CachedDocument based on the full URL
            # and parameters.
            cached_doc, created = self.get_or_create(url_path=query_name)
    
        # EVE uses UTC.
        current_eve_time = datetime.utcnow()

        # Figure out if we need hit EVE API and re-cache, or just pull from
        # the local cache (based on cached_until).
        if no_cache or created or \
          cached_doc.cached_until == None or \
          current_eve_time > cached_doc.cached_until:
            # Cache from EVE API
            tree = self.cache_from_eve_api(cached_doc, url_path, params, 
                                    no_cache=no_cache)
        else:
            # Parse the document here since it was retrieved from the
            # database cache instead of queried for.
            tree = ElementTree.fromstring(cached_doc.body)
        
        if not tree:
            # When we see failure here, we can safely assume that the response
            # is malformed, since all API responses have a cachedUntil tag.
            raise InvalidAPIResponseException(cached_doc.body)
        
        # Check for the presence errors. Only check the bare minimum,
        # generic stuff that applies to most or all queries. User-level code
        # should check for the more specific errors.
        error_node = tree.find('error')
        if error_node != None:
            error_code = int(error_node.get('code'))
            error_message = error_node.text
            raise APIQueryErrorException(error_code, error_message)
            
        return cached_doc
    
    def clean_expired_entries(self):
        """
        Cleanses the cache of any expired CachedDocument objects. This can
        be called periodically if the user is concerned about DB bloat.
        """
        CachedDocument.objects.filter(cached_until__lte=datetime.now).delete()

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