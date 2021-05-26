
# Author: 猴子
# Date: 2021-05-23 15:09:28
# LastEditTime: 2021-05-24 12:15:42
# FilePath: /code/color/get.py
__all__ = [
    "background",
    "txt",
]


class main(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                setattr(self, name, f"\033[{getattr(self, name)}m")


class txt(main):
    # 黑色
    black = 30
    # 红色
    red = 31
    # 绿色
    green = 32
    # 黃色
    yellow = 33
    # 蓝色
    blue = 34
    # 紫红色
    Fuchsia = 35
    # 青蓝色
    cyan = 36
    # 白色
    white = 37


class background(main):
    # 黑色
    black = 40
    # 红色
    red = 41
    # 绿色
    green = 42
    # 黃色
    yellow = 43
    # 蓝色
    blue = 44
    # 紫红色
    Fuchsia = 45
    # 青蓝色
    cyan = 46
    # 白色
    white = 47


txt = txt()
background = background()
