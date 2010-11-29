"""
This module contains all exceptions relating to the proxy itself, which
does NOT include EVE API errors. Exceptions belonging in here include parser
errors, transport errors, and other network/db/parsing issues.
"""
class InvalidAPIResponseException(Exception):
    """
    Raised when an unrecognizable response is received from the API. This
    usually shows up when you're using a proxy that is bugging out.
    """
    def __init__(self, body):
        self.body = body
        
    def __str__(self):
        return "An invalid API response was received:\r\n%s" % self.body