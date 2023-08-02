def get_bytes(value: int, step=0, *, unit=8):
    return (value >> (unit * step)) & ((1 << unit) - 1)


def get_bits(value: int, start=0, *, size=-1):
    value >>= start
    if size == -1:
        return value
    return value & ((1 << size) - 1)


class YUVStandard:
    ...


class _Missing:
    def __eq__(self, other) -> bool:
        return False

    def __bool__(self):
        return False

    def __repr__(self) -> str:
        return "..."


MISSING = _Missing()
