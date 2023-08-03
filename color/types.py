from typing import Iterable, Union, overload

from ._utils import MISSING

__all__ = (
    "RED",
    "GREEN",
    "BLUE",
    "HUE",
    "SATURATION",
    "LIGHTNESS",
    "Red",
    "Green",
    "Blue",
    "Hue",
    "Saturation",
    "Lightness",
    "RGB",
    "HSL",
    "HSV",
    "YUV",
)

RED = Union[int, float, "Red"]
GREEN = Union[int, float, "Green"]
BLUE = Union[int, float, "Blue"]
HUE = Union[int, float, "Hue"]
SATURATION = Union[float, "Saturation"]
LIGHTNESS = Union[float, "Lightness"]


class _Float(float):
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self:g}>"


class _PercentValue(_Float):
    """
    0~100% (float) => value = cls.max * percent
    0~max  (int)   => value = value
    """

    max = 0xFF

    def __new__(cls, __x):
        return super().__new__(
            cls,
            int(min(cls.max, __x * cls.max if isinstance(__x, float) else __x)),
        )


class _Percent(_Float):
    """
    0~100% (float) => value = value
    """

    def __new__(cls, __x):
        return super().__new__(cls, min(1, __x))


class Red(_PercentValue):
    """"""


class Green(_PercentValue):
    """"""


class Blue(_PercentValue):
    """"""


class Hue(_PercentValue):
    """"""

    max = 360


class Saturation(_Percent):
    """"""


class Lightness(_Percent):
    """"""


class RGB(tuple):
    @overload
    def __new__(cls, r: RED, g: GREEN, b: BLUE) -> "RGB":
        ...

    @overload
    def __new__(cls, d: tuple[RED, GREEN, BLUE]) -> "RGB":
        ...

    def __new__(cls, r=MISSING, g=MISSING, b=MISSING) -> "RGB":
        if isinstance(r, Iterable):
            if len(r) != 3:
                raise ValueError("Iterable must have 3 items")
            r, g, b = r

        if r is MISSING or g is MISSING or b is MISSING:
            raise ValueError("Missing value")

        return super().__new__(cls, (r, g, b))

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


class HSL(tuple):
    @overload
    def __new__(cls, h: HUE, s: SATURATION, l: LIGHTNESS) -> "HSL":
        ...

    @overload
    def __new__(cls, d: tuple[HUE, SATURATION, LIGHTNESS]) -> "HSL":
        ...

    def __new__(cls, h=MISSING, s=MISSING, l=MISSING) -> "HSL":
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
    def __new__(cls, h: HUE, s: SATURATION, v: float) -> "HSL":
        ...

    @overload
    def __new__(cls, d: tuple[HUE, SATURATION, float]) -> "HSL":
        ...

    def __new__(cls, h=MISSING, s=MISSING, v=MISSING) -> "HSL":
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
    def __new__(cls, y: float, u: float, v: float) -> "YUV":
        ...

    @overload
    def __new__(cls, d: tuple[float, float, float]) -> "YUV":
        ...

    def __new__(cls, y=MISSING, u=MISSING, v=MISSING) -> "YUV":
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
