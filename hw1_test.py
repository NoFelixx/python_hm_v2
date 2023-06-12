from hw1 import ColorsEnum, SizesEnum
def test_colors_enum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"


def test_sizes_enum():
    assert SizesEnum.XL == "XL"
    assert SizesEnum.L == "L"
    assert SizesEnum.M == "M"
    assert SizesEnum.S == "S"
    assert SizesEnum.XS == "XS"