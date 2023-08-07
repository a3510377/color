from abc import ABC, abstractmethod
from typing import Any, Iterable, Union, overload

from typing_extensions import Self

from ._utils import MISSING, get_bytes

__all__ = (
    "RED_TYPE",
    "GREEN_TYPE",
    "BLUE_TYPE",
    "HUE_TYPE",
    "SATURATION_TYPE",
    "LIGHTNESS_TYPE",
    "Red",
    "Green",
    "Blue",
    "Hue",
    "Saturation",
    "Lightness",
    "RGB",
    "RGBA",
    "HSL",
    "HSV",
    "YUV",
)

RED_TYPE = Union[int, float, "Red"]
GREEN_TYPE = Union[int, float, "Green"]
BLUE_TYPE = Union[int, float, "Blue"]
ALPHA_TYPE = Union[int, float, "Alpha"]
HUE_TYPE = Union[int, float, "Hue"]
SATURATION_TYPE = Union[float, "Saturation"]
LIGHTNESS_TYPE = Union[float, "Lightness"]


class _Percent(float):
    """
    0~100% (float) => value = value
    """

    def __new__(cls, __x) -> Self:
        return super().__new__(cls, min(1, __x))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self:g}>"


class Saturation(_Percent):
    """"""


class Lightness(_Percent):
    """"""


class _PercentValue(int):
    """
    0~100% (float) => value = cls.max * percent

    0~max  (int)   => value = value
    """

    max = 0xFF

    def __new__(cls, __x: int | float) -> Self:
        return super().__new__(
            cls,
            int(min(cls.max, __x * cls.max if isinstance(__x, float) else __x)),
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self:g}>"


class Red(_PercentValue):
    """
    0~100% (float) => value = 255 * value

    0~255  (int)   => value = value
    """


class Green(_PercentValue):
    """
    0~100% (float) => value = 255 * value

    0~255  (int)   => value = value
    """


class Blue(_PercentValue):
    """
    0~100% (float) => value = 255 * value

    0~255  (int)   => value = value
    """


class Alpha(_PercentValue):
    """
    0~100% (float) => value = 255 * value

    0~255  (int)   => value = value
    """


class Hue(_PercentValue):
    """"""

    max = 360


class _IntColorTuple(Iterable, ABC):
    def __init__(self, value: Iterable[Any]) -> None:
        self._data = []

        if isinstance(value, _IntColorTuple):
            self._data = value._data
        elif isinstance(value, Iterable):
            self._data = list(value)
        else:
            raise ValueError("Invalid value")

    @abstractmethod
    def to_int(cls) -> int:
        raise NotImplementedError

    def __parse_int(self, value: Any) -> int:
        if isinstance(value, (int, float)):
            return int(value)
        elif isinstance(value, self.__class__):
            return value.to_int()

        raise ValueError(f"Invalid value: {value}")

    # ==
    def __eq__(self, __value: Any) -> bool:
        try:
            return +self == self.__parse_int(__value)
        except ValueError:
            return False

    # !=
    def __ne__(self, __value: Any) -> bool:
        return not self.__eq__(__value)

    # <
    def __lt__(self, __value: Any) -> bool:
        try:
            return +self < self.__parse_int(__value)
        except ValueError:
            return False

    # >
    def __gt__(self, __value: Any) -> bool:
        try:
            return +self > self.__parse_int(__value)
        except ValueError:
            return False

    # <=
    def __le__(self, __value: Any) -> bool:
        return self == __value or self < __value

    # >=
    def __ge__(self, __value: Any) -> bool:
        return self == __value or self > __value

    # +
    def __pos__(self) -> int:
        return self.to_int()

    # ~
    def __invert__(self) -> int:
        return ~self.to_int()

    # <<
    def __lshift__(self, __value: int) -> int:
        return +self << self.__parse_int(__value)

    # >>
    def __rshift__(self, __value: int) -> int:
        return +self >> self.__parse_int(__value)

    # &
    def __and__(self, __value: int) -> int:
        return +self & self.__parse_int(__value)

    # |
    def __or__(self, __value: int) -> int:
        return +self | self.__parse_int(__value)

    # ^
    def __xor__(self, __value: int) -> int:
        return +self ^ self.__parse_int(__value)

    def __contains__(self, item: Any):
        return item in self._data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i: Any):
        if isinstance(i, slice):
            return self.__class__(self._data[i])
        return self._data[i]

    def __setitem__(self, i: Any, item: Any):
        self._data[i] = item

    def __iter__(self):
        return iter(self._data)


class RGB(_IntColorTuple):
    # fmt: off
    @overload
    def __init__(cls, r: RED_TYPE, g: GREEN_TYPE, b: BLUE_TYPE) -> Self: ... # noqa
    @overload
    def __init__(cls, __d: tuple[RED_TYPE, GREEN_TYPE, BLUE_TYPE]) -> Self: ... # noqa
    @overload
    def __init__(cls, __value: int) -> Self: ... # noqa
    @overload
    def __init__(cls, __value: Self) -> Self: ... # noqa
    @overload
    def __init__(cls, __value: "RGBA") -> Self: ... # noqa
    # fmt: on

    def __init__(self, r=MISSING, g=MISSING, b=MISSING) -> Self:
        # parse value from RGBA
        if isinstance(r, RGBA):
            r, g, b, _ = r
        # parse iterable -> (r, g, b) or RGB
        elif isinstance(r, Iterable):
            if len(r) != 3:
                raise ValueError("Iterable must have 3 items")
            r, g, b = r
        # parse value -> 0xff_ff_ff
        elif isinstance(r, int) and g is MISSING and b is MISSING:
            if r < 0 or r > 0xFFFFFF:
                raise ValueError("Value must be between 0 and 0xFFFFFF")
            r, g, b = get_bytes(r, 2), get_bytes(r, 1), get_bytes(r)
        # raise error if missing value
        elif r is MISSING or g is MISSING or b is MISSING:
            raise ValueError("Missing value")

        return super().__init__((r, g, b))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} r={self.r:g} g={self.g:g} b={self.g:g}>"

    @property
    def r(self) -> Red:
        """Return the blue value using a :class:`Red` instance"""
        return Red(self[0])

    @property
    def g(self) -> Green:
        """Return the blue value using a :class:`Green` instance"""
        return Green(self[1])

    @property
    def b(self) -> Blue:
        """Return the blue value using a :class:`Blue` instance"""
        return Blue(self[2])

    def to_int(self) -> int:
        """Return the integer value"""
        return (self.r << 16) + (self.g << 8) + self.b


class RGBA(_IntColorTuple):
    # fmt: off
    @overload
    def __init__(cls, r: RED_TYPE, g: GREEN_TYPE, b: BLUE_TYPE, a: ALPHA_TYPE) -> Self: ... # noqa
    @overload
    def __init__(cls, __d: tuple[RED_TYPE, GREEN_TYPE, BLUE_TYPE, ALPHA_TYPE]) -> Self: ... # noqa
    @overload
    def __init__(cls, __value: int) -> Self: ... # noqa
    @overload
    def __init__(cls, __value: Self) -> Self: ... # noqa
    @overload
    def __init__(cls, __value: "RGB", *, a: Alpha = ...) -> Self: ... # noqa
    # fmt: on

    def __init__(cls, r=MISSING, g=MISSING, b=MISSING, a=MISSING) -> Self:
        # parse value from RGB
        if isinstance(r, RGB):
            r, g, b, a = *r, 0xFF
        # parse iterable -> (r, g, b, a) or RGBA
        elif isinstance(r, Iterable):
            if len(r) != 4:
                raise ValueError("Iterable must have 4 items")
            r, g, b, a = r
        # parse value -> 0xff_ff_ff_ff
        elif isinstance(r, int) and g is MISSING and b is MISSING and a is MISSING:
            if r < 0 or r > 0xFFFFFFFF:
                raise ValueError("Value must be between 0 and 0xFFFFFFFF")
            r, g, b, a = *RGB(r >> 8), get_bytes(r)
        # raise error if missing value
        elif r is MISSING or g is MISSING or b is MISSING or a is MISSING:
            raise ValueError("Missing value")

        return super().__init__((r, g, b, a))

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} r={self.r:g} "
            f"g={self.g:g} b={self.g:g} a={self.a:g}>"
        )

    @property
    def r(self) -> Red:
        """Return the blue value using a :class:`Red` instance"""
        return Red(self[0])

    @property
    def g(self) -> Green:
        """Return the blue value using a :class:`Green` instance"""
        return Green(self[1])

    @property
    def b(self) -> Blue:
        """Return the blue value using a :class:`Blue` instance"""
        return Blue(self[2])

    @property
    def a(self) -> Alpha:
        """Return the alpha value using a :class:`Alpha` instance"""
        return Alpha(self[3])

    def to_int(self) -> int:
        """Return the integer value"""
        return (self.r << 24) + (self.g << 16) + (self.b << 8) + self.a


class HSL(tuple):
    @overload
    def __new__(cls, h: HUE_TYPE, s: SATURATION_TYPE, l: LIGHTNESS_TYPE) -> Self:
        ...

    @overload
    def __new__(cls, d: tuple[HUE_TYPE, SATURATION_TYPE, LIGHTNESS_TYPE]) -> Self:
        ...

    def __new__(cls, h=MISSING, s=MISSING, l=MISSING) -> Self:
        if isinstance(h, Iterable):
            if len(h) != 3:
                raise ValueError("Iterable must have 3 items")
            h, s, l = h

        if h is MISSING or s is MISSING or l is MISSING:
            raise ValueError("Missing value")

        return super().__new__(cls, (h, s, l))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} h={self.h:g} s={self.s:g} l={self.l:g}>"

    @property
    def h(self) -> Hue:
        """Return the hue value using a :class:`Hue` instance"""
        return Hue(self[0])

    @property
    def s(self) -> Saturation:
        """Return the saturation value using a :class:`Saturation` instance"""
        return Saturation(self[1])

    @property
    def l(self) -> Lightness:
        """Return the lightness value using a :class:`Lightness` instance"""
        return Lightness(self[2])


class HSV(tuple):
    @overload
    def __new__(cls, h: HUE_TYPE, s: SATURATION_TYPE, v: float) -> Self:
        ...

    @overload
    def __new__(cls, d: tuple[HUE_TYPE, SATURATION_TYPE, float]) -> Self:
        ...

    def __new__(cls, h=MISSING, s=MISSING, v=MISSING) -> Self:
        if isinstance(h, Iterable):
            if len(h) != 3:
                raise ValueError("Iterable must have 3 items")
            h, s, v = h

        if h is MISSING or s is MISSING or v is MISSING:
            raise ValueError("Missing value")

        return super().__new__(cls, (Hue(h), Saturation(s), min(v, 1)))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} h={self.h:g} s={self.s:g} l={self.v:g}>"

    @property
    def h(self) -> Hue:
        """Return the hue value using a :class:`Hue` instance"""
        return Hue(self[0])

    @property
    def s(self) -> Saturation:
        """Return the saturation value using a :class:`Saturation` instance"""
        return Saturation(self[1])

    @property
    def v(self) -> float:
        """Return the lightness value using a :class:`Lightness` instance"""
        return self[2]


class YUV(tuple):
    @overload
    def __new__(cls, y: float, u: float, v: float) -> Self:
        ...

    @overload
    def __new__(cls, d: tuple[float, float, float]) -> Self:
        ...

    def __new__(cls, y=MISSING, u=MISSING, v=MISSING) -> Self:
        if isinstance(y, Iterable):
            if len(y) != 3:
                raise ValueError("Iterable must have 3 items")
            y, u, v = y

        if y is MISSING or u is MISSING or v is MISSING:
            raise ValueError("Missing value")

        return super().__new__(cls, (min(y, 1), min(u, 1), min(v, 1)))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} y={self.y:g} u={self.u:g} v={self.v:g}>"

    @property
    def y(self) -> float:
        """Return the y value"""
        return self[0]

    @property
    def u(self) -> float:
        """Return the u value"""
        return self[1]

    @property
    def v(self) -> float:
        """Return the v value"""
        return self[2]
