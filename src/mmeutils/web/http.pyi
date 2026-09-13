import httpx
import requests

from typing import Optional

__all__ = ['get_with_retry']

def get_with_retry(url: str, *, session: requests.Session | None) -> requests.Response: ...

def get_with_retry_httpx(
            url: str,
            *,
            client: Optional[httpx.Client],
            follow_redirects: bool,
        ) -> httpx.Response: ...

async def get_with_retry_async(
            url: str,
            *,
            client: Optional[httpx.AsyncClient],
            follow_redirects: bool,
        ) -> httpx.Response: ...
