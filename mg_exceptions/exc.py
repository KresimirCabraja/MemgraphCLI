import requests


class Error(Exception):
    ...


class WebsiteNotFoundError(requests.exceptions.ConnectionError):
    ...


class ShortestPathNotFoundError(Error):
    ...
