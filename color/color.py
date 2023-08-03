from typing_extensions import Self

from ._utils import YUVStandard, get_bits, get_bytes
from .types import RGBA
from .vars import NAMES_COLORS

__all__ = ("Color",)

YUV_BT470 = YUVStandard()
# WR=0.299, WG=0.587


class Color(RGBA):
    @classmethod
    def from_str(cls, s: str) -> Self:
        ...

    @classmethod
    def from_name(cls, name: str) -> Self:
        return cls.from_rgb(NAMES_COLORS.get(name, 0))

    @classmethod
    def from_rgb(cls, value: int) -> Self:
        return cls(get_bytes(value, 2), get_bytes(value, 1), get_bytes(value))

    @classmethod
    def from_rgb24(cls, value: int) -> Self:
        return cls(get_bytes(value), get_bytes(value, 1), get_bytes(value, 2))

    @classmethod
    def from_rgb565(cls, value: int) -> Self:
        return cls.from_rgb(
            get_bits(value, 11, size=5),  # r
            get_bits(value, 5, size=6),  # g
            get_bits(value, 0, size=5),  # b
        )

    @classmethod
    def from_rgb555(cls, value: int) -> Self:
        return cls.from_rgb(
            get_bytes(value, 2, unit=5),  # r
            get_bytes(value, 1, unit=5),  # g
            get_bytes(value, 0, unit=5),  # b
        )

    @classmethod
    def from_rgba(cls, value: int) -> Self:
        return cls(
            get_bytes(value, 3),  # r
            get_bytes(value, 2),  # g
            get_bytes(value, 1),  # b
            get_bytes(value, 0),  # a
        )

    @classmethod
    def from_yuv(cls, y: int, u: int, v: int) -> Self:
        """
        [YUV Wiki](https://en.wikipedia.org/wiki/Y%E2%80%B2UV)
        """
        # TODO
        return cls.from_rgb()
