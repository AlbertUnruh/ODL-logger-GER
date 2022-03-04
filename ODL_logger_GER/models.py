__all__ = ("Data",)


import attr


@attr.s(slots=True, frozen=True)
class Data:
    d: dict = attr.field()
