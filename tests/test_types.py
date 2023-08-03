from color.types import HSL, HSV, RGB, YUV


def test_RGB() -> None:
    assert RGB(0, 255, 0) == RGB(0, 255, 0)
    assert RGB(0, 255, 0) == (0, 255, 0)
    assert RGB(0, 255, 0) != [0, 255, 0]
    assert RGB(0, 255, 0) != {0, 255, 0}


def test_HSL() -> None:
    assert HSL(0, 255, 0) == HSL(0, 255, 0)
    assert HSL(0, 255, 0) == (0, 255, 0)
    assert HSL(0, 255, 0) != [0, 255, 0]
    assert HSL(0, 255, 0) != {0, 255, 0}


def test_HSV() -> None:
    assert HSV(0, 0.1, 0) == HSV(0, 0.1, 0)
    assert HSV(360, 1, 1) == (360, 1, 1)
    assert HSV(360, 1, 1) != [0, 0.1, 0]
    assert HSV(360, 1, 1) != {0, 0.1, 0}


def test_YUV() -> None:
    assert YUV(0, 1, 0) == YUV(0, 1, 0)
    assert YUV(0, 1, 0) == (0, 1, 0)
    assert YUV(0, 1, 0) != [0, 1, 0]
    assert YUV(0, 1, 0) != {0, 1, 0}
