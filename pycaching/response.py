from flask import Response


class CachedResponse(Response):
    """
    views wraped by @cached can return this (which inherits from flask.Response)
    to override the cache TTL dynamically
    """

    timeout = None

    def __init__(self, response, timeout):
        self.__dict__ = response.__dict__
        self.timeout = timeout
