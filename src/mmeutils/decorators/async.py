# decorators/async.py
# v1.0.0

"""A collection of general-use Python asynchronous function decorators."""

#region Imports

import asyncio
import functools
import json

import aiohttp
import aiohttp.web
import httpx

from typing import Awaitable, Callable, Dict, List

#endregion

#region Exports

__all__: List[str] = [
    'retry_http_async',
    'retry_empty_dict_async',
    'retry_json_error_async',
    'retry_on_exception_async',
]

#endregion

#region Decorators

async def retry_http_async(func: Callable[..., Awaitable], *, retries: int=3, sleep: float=0.4) -> Callable[..., Awaitable]:
    """Retries an async function call when an HTTP error occurs.
    
    Supported web libraries: aiohttp, httpx
    """

    @functools.wraps(func)
    async def retry_wrapper(*args, retries=retries, **kwargs):

        while retries > 0:

            try:

                result = await func(*args, **kwargs)

                return result
            
            except (
                        aiohttp.ClientPayloadError,
                        aiohttp.ConnectionTimeoutError,
                        aiohttp.web.HTTPError,
                        aiohttp.web.HTTPRequestTimeout,
                        httpx.HTTPError,
                        httpx.ConnectError,
                        httpx.TimeoutException,
                    ):

                retries -= 1

                await asyncio.sleep(sleep)

                if retries == 0:
                    raise

    return retry_wrapper


async def retry_empty_dict_async(func: Callable[..., Awaitable[Dict]], *, retries: int=3) -> Callable[..., Awaitable[Dict]]:
    """Retries an async function call when an empty dictionary is returned."""

    @functools.wraps(func)
    async def retry_wrapper(*args, retries=retries, **kwargs):

        result = {}

        while len(result.keys()) == 0 and retries > 0:
            result = await func(*args, **kwargs)
            retries -= 1
        
        return result

    return retry_wrapper


async def retry_json_error_async(func: Callable[..., Awaitable], *, retries: int=3) -> Callable[..., Awaitable]:
    """Retries an async function call when a JSON decode error occurs."""

    @functools.wraps(func)
    async def retry_wrapper(*args, retries=retries, **kwargs):
        while retries > 0:
            try:
                result = await func(*args, **kwargs)
                return result
            
            except json.JSONDecodeError:
                retries -= 1

                if retries == 0:
                    raise

    return retry_wrapper


async def retry_on_exception_async(func: Callable[..., Awaitable], *, retries: int=3) -> Callable[..., Awaitable]:
    """Retries an async function call when any exception (`Exception`) is raised."""

    @functools.wraps(func)
    async def retry_wrapper(*args, retries=retries, **kwargs):
        while retries > 0:
            try:
                result = await func(*args, **kwargs)
                return result
            
            except Exception:
                retries -= 1

                if retries == 0:
                    raise

    return retry_wrapper

#endregion
