__all__ = ("Handler",)


import attr

from .adapters import BaseAdapter
from .models import Data
from .tor import TorRequest


@attr.s(slots=True)
class Handler:
    adapter: BaseAdapter | None = attr.field(
        default=None,
        validator=lambda *x: isinstance(x[-1], BaseAdapter) or x[-1] is None,
    )
    url: str | None = attr.field(default=None)

    def set_adapter(self, adapter: BaseAdapter) -> None:
        assert isinstance(adapter, BaseAdapter)
        self.adapter = adapter

    def request(self, url: str | None = None) -> Data:
        with TorRequest() as session:
            result = session.get(url or self.url)
        data = Data(d=result.json())
        if self.adapter is not None:
            self.adapter.handle(data)
        return data
