from django.conf.urls.defaults import *

urlpatterns = patterns('eve_proxy.views',
    # This view can be used just like EVE API's http://api.eve-online.com.
    # Any parameters or URL paths are sent through the cache system and
    # forwarded to the EVE API site as needed.
    url(r'^', 'retrieve_xml', name='eve_proxy-retrieve_xml'),
)
