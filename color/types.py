from typing import Iterable, Union, overload

from ._utils import MISSING

__all__ = (
    "Red",
    "Green",
    "Blue",
    "RGB",
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
    max = 0xFF

    def __new__(cls, __x):
        if isinstance(__x, float):
            __x *= cls.max
        return super().__new__(cls, int(min(cls.max, __x)))


class _Percent(_Float):
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
    def __new__(cls, h: Hue, s: Saturation, l: Lightness) -> "HSL":
        ...

    @overload
    def __new__(cls, d: tuple[Hue, Saturation, Lightness]) -> "HSL":
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
    def __new__(cls, h: Hue, s: Saturation, v: int) -> "HSL":
        ...

    @overload
    def __new__(cls, d: tuple[Hue, Saturation, Lightness]) -> "HSL":
        ...

    def __new__(cls, h=MISSING, s=MISSING, v=MISSING) -> "HSL":
        if isinstance(h, Iterable):
            if len(h) != 3:
                raise ValueError("Iterable must have 3 items")
            h, s, v = h

        if h is MISSING or s is MISSING or v is MISSING:
            raise ValueError("Missing value")

        return super().__new__(cls, (h, s, v))

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
    def v(self) -> int:
        """Return the lightness value using a :class:`Lightness` instance"""
        return self[2]
