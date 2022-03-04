__all__ = (
    "BaseAdapter",
    "DiscordAdapter",
)


import attr
import requests
from abc import ABC, abstractmethod
from datetime import datetime
from io import StringIO
from json import dumps

from .models import Data


@attr.s()
class BaseAdapter(ABC):
    @abstractmethod
    def handle(self, data: Data) -> None:
        raise NotImplementedError


@attr.s(slots=True, frozen=True)
class DiscordAdapter(BaseAdapter):
    webhook_url: str = attr.field()

    def handle(self, data: Data) -> None:
        requests.post(
            self.webhook_url,
            data={
                "username": "ODL Logger -- GER",
            },
            files={
                f"odl-ger-{datetime.utcnow().timestamp()}.json": StringIO(dumps(data.d))
            },
        )
