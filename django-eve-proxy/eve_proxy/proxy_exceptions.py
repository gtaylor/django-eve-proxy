class APIAuthException(Exception):
    """
    Raised when an invalid userID and/or authKey were provided.
    """
    def __str__(self):
        return "An authentication was encountered while querying the EVE API."
    
class APINoUserIDException(Exception):
    """
    Raised when a userID is required, but missing or mal-formed.
    """
    def __str__(self):
        return "This query requires a valid userID, but yours is either missing or invalid."
    
class InvalidAPIResponseException(Exception):
    """
    Raised when an unrecognizable response is received from the API. This
    usually shows up when you're using a proxy that is bugging out.
    """
    def __init__(self, body):
        self.body = body
        
    def __str__(self):
        return "An invalid API response was received:\r\n%s" % self.body