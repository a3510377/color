from ._utils import get_bits, get_bytes, YUVStandard
from .vars import NAMES_COLORS

__all__ = ("Color",)

YUV_BT470 = YUVStandard()
# WR=0.299, WG=0.587


class Color:
    def __init__(self, r: int = 255, g: int = 255, b: int = 255, a: int = 255) -> None:
        self._rgba = tuple[int, int, int, int]([r, g, b, a])

    @classmethod
    def from_str(cls, s: str) -> "Color":
        ...

    @classmethod
    def from_name(cls, name: str) -> "Color":
        return cls.from_rgb(NAMES_COLORS.get(name, 0))

    @classmethod
    def from_rgb(cls, value: int) -> "Color":
        return cls(get_bytes(value, 2), get_bytes(value, 1), get_bytes(value))

    @classmethod
    def from_rgb24(cls, value: int) -> "Color":
        return cls(get_bytes(value), get_bytes(value, 1), get_bytes(value, 2))

    @classmethod
    def from_rgb565(cls, value: int) -> "Color":
        return cls.from_rgb(
            get_bits(value, 11, size=5),  # r
            get_bits(value, 5, size=6),  # g
            get_bits(value, 0, size=5),  # b
        )

    @classmethod
    def from_rgb555(cls, value: int) -> "Color":
        return cls.from_rgb(
            get_bytes(value, 2, unit=5),  # r
            get_bytes(value, 1, unit=5),  # g
            get_bytes(value, 0, unit=5),  # b
        )

    @classmethod
    def from_rgba(cls, value: int) -> "Color":
        return cls(
            get_bytes(value, 3),  # r
            get_bytes(value, 2),  # g
            get_bytes(value, 1),  # b
            get_bytes(value, 0),  # a
        )

    @classmethod
    def from_yuv(cls, y: int, u: int, v: int) -> "Color":
        """
        [YUV Wiki](https://en.wikipedia.org/wiki/Y%E2%80%B2UV)
        """
        # TODO
        return cls.from_rgb()

    # fmt: off
    @property
    def r(self) -> int: return self._rgba[0] # noqa
    @property
    def g(self) -> int: return self._rgba[1] # noqa
    @property
    def b(self) -> int: return self._rgba[2] # noqa
    @property
    def a(self) -> int: return self._rgba[2] # noqa
    # fmt: on
