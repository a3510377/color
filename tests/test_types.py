from color.types import RGB, RGBA


def test_RGB() -> None:
    def assert_rgb(rgb: RGB) -> None:
        assert rgb.r == 0xFF
        assert rgb.g == 0xF0
        assert rgb.b == 0x0F

    rgb = RGB(0xFF_F0_0F)
    assert_rgb(rgb)
    assert_rgb(RGB(rgb))
    assert_rgb(RGB(0xFF, 0xF0, 0x0F))
    assert_rgb(RGB((0xFF, 0xF0, 0x0F)))
    assert_rgb(RGB(RGBA(0xFF_F0_0F_AA)))

    assert rgb > 0xFF_F0_00
    assert rgb < 0xFF_F0_FF
    assert rgb != 0xFF_F0_00
    assert rgb == 0xFF_F0_0F
    assert rgb >= 0xFF_F0_0F
    assert rgb <= 0xFF_F0_0F
    assert rgb << 1 == 0x1FFE01E
    assert rgb >> 1 == 0x7FF807
    assert rgb & 0xFF_F0_00 == 0xFF_F0_00
    assert rgb | 1 == 0xFFF00F
    assert rgb ^ 1 == 0xFFF00E

    assert rgb.to_int() == 0xFF_F0_0F
    assert RGB(RGBA(0xFF_F0_0F_AA)) == 0xFF_F0_0F


def test_RGBA() -> None:
    def assert_rgba(rgb: RGBA) -> None:
        assert rgb.r == 0xFF
        assert rgb.g == 0xF0
        assert rgb.b == 0x0F
        assert rgb.a == 0xAA

    assert_rgba(RGBA(0xFF, 0xF0, 0x0F, 0xAA))
    assert_rgba(RGBA((0xFF, 0xF0, 0x0F, 0xAA)))
    assert_rgba(RGBA(0xFF_F0_0F_AA))
    assert_rgba(RGBA(RGBA(0xFF_F0_0F_AA)))

    assert RGBA(0xFF_F0_0F_AA) == 0xFF_F0_0F_AA
    assert RGBA(0xFF_F0_0F_AA).to_int() == 0xFF_F0_0F_AA
    assert RGBA(RGB(0xFF_F0_0F)) == 0xFF_F0_0F_FF


# def test_HSL() -> None:
#     assert HSL(0, 255, 0) == HSL(0, 255, 0)
#     assert HSL(0, 255, 0) == (0, 255, 0)
#     assert HSL(0, 255, 0) != [0, 255, 0]
#     assert HSL(0, 255, 0) != {0, 255, 0}


# def test_HSV() -> None:
#     assert HSV(0, 0.1, 0) == HSV(0, 0.1, 0)
#     assert HSV(360, 1, 1) == (360, 1, 1)
#     assert HSV(360, 1, 1) != [0, 0.1, 0]
#     assert HSV(360, 1, 1) != {0, 0.1, 0}


# def test_YUV() -> None:
#     assert YUV(0, 1, 0) == YUV(0, 1, 0)
#     assert YUV(0, 1, 0) == (0, 1, 0)
#     assert YUV(0, 1, 0) != [0, 1, 0]
#     assert YUV(0, 1, 0) != {0, 1, 0}
