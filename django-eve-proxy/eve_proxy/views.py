from django.http import HttpResponse
from eve_proxy.models import CachedDocument

def retrieve_xml(request):
    """
    A view that forwards EVE API requests through the cache system, either
    retrieving a cached document or querying and caching as needed.
    """
    # This is the URL path (minus the parameters).
    url_path = request.META['PATH_INFO']
    # The parameters attached to the end of the URL path.
    params = request.META['QUERY_STRING']
    # The query system will retrieve a cached_doc that was either previously
    # or newly cached depending on cache intervals.
    cached_doc = CachedDocument.objects.api_query(url_path, params)
    # Return the document's body as XML.
    return HttpResponse(cached_doc.body, mimetype='text/xml')
