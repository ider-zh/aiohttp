import asyncio
import sys
from abc import ABC, abstractmethod


PY_35 = sys.version_info >= (3, 5)


class AbstractRouter(ABC):

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def resolve(self, request):
        """Return MATCH_INFO for given request"""


class AbstractMatchInfo(ABC):

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def handler(self, request):
        """Execute matched request handler"""

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def expect_handler(self, request):
        """Expect handler for 100-continue processing"""

    @property  # pragma: no branch
    @abstractmethod
    def http_exception(self):
        """HTTPException instance raised on router's resolving, or None"""

    @abstractmethod  # pragma: no branch
    def get_info(self):
        """Return a dict with additional info useful for introspection"""


class AbstractView(ABC):

    def __init__(self, request):
        self._request = request

    @property
    def request(self):
        return self._request

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def __iter__(self):
        while False:  # pragma: no cover
            yield None

    if PY_35:  # pragma: no branch
        @abstractmethod
        def __await__(self):
            return  # pragma: no cover


class AbstractResolver(ABC):

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def resolve(self, hostname):
        """Return IP address for given hostname"""

    @asyncio.coroutine  # pragma: no branch
    @abstractmethod
    def close(self):
        """Release resolver"""
