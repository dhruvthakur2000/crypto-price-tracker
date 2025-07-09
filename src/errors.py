
class APIError(Exception):
    """Raised when the API call fails or returns unexpected data."""
    def __init__(self, message="An error occurred while fetching data from the API."):
        super().__init__(message)
