# http.py
# v0.5.0

"""HTTP Utility Functions"""

#region Imports

import httpx
import requests

from typing import List, Optional

from ..decorators import retry_http
from ..decorators.aio import retry_http_async

#endregion

#region Exports

__all__: List[str] = [
    'get_with_retry',
    'get_with_retry_httpx',
]

#endregion

#region Functions

@retry_http
def get_with_retry(
            url: str,
            *,
            session: Optional[requests.Session],
        ) -> requests.Response:

    """Helper function to perform a simple GET web request with retries.

    :param url: The URL to fetch.
    :type url: str

    :param session: An optional `requests.Session` object
        to use for the request.
    
    :return: A `requests.Response`.
    :rtype: requests.Response
    """
    if session:
        return session.get(url)
    
    else:
        return requests.get(url)


@retry_http
def get_with_retry_httpx(
            url: str,
            *,
            client: Optional[httpx.Client],
            follow_redirects: bool=True,
        ) -> httpx.Response:

    """Helper function to perform a simple GET web request with retries.
    This variant uses httpx instead of requests.

    :param url: The URL to fetch.
    :type url: str

    :param client: An optional `httpx.Client` object
        to use for the request.

    :param follow_redirects: Follow redirects by default.
    :type follow_redirects: bool
    
    :return: An `httpx.Response`.
    :rtype: httpx.Response
    """
    if client:
        return client.get(url, follow_redirects=follow_redirects)
    
    else:
        return httpx.get(url, follow_redirects=follow_redirects)


@retry_http_async
async def get_with_retry_async(
            url: str,
            *,
            client: Optional[httpx.AsyncClient],
            follow_redirects: bool=True,
        ) -> httpx.Response:

    """Helper function to perform a simple GET web request with retries.
    This variant uses asynchronous httpx instead of requests.

    :param url: The URL to fetch.
    :type url: str

    :param client: An optional `httpx.AsyncClient` object
        to use for the request.

    :param follow_redirects: Follow redirects by default.
    :type follow_redirects: bool

    :return: An `httpx.Response`.
    :rtype: httpx.Response
    """
    if client:
        return await client.get(url, follow_redirects=follow_redirects)
    
    else:
        async with httpx.AsyncClient() as client:
            return await client.get(url, follow_redirects=follow_redirects)

#endregion
