class PublisherException(Exception):
    """Base Exception for Publisher"""
    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(PublisherException, self).__init__(message, *args, **kwargs)
