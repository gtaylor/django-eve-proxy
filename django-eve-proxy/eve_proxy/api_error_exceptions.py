"""
This module contains exceptions for all of the EVE API's error codes.

See http://wiki.eve-id.net/APIv2_Eve_ErrorList_XML for a complete list.
"""
class APIQueryErrorException():
    """
    This is an error returned by the EVE API. See the URL at the top of
    this module for how to get an up to date list.
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __unicode__(self):
        return "%s (Error Code: %s)" % (self.message, self.code)

    def __str__(self):
        return self.__unicode__()