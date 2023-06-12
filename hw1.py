class SimplifiedEnum(type):
    def __new__(cls, name, bases, attrs):
        keys = attrs.pop("__keys")
        values = keys
        enum_dict = dict(zip(keys, values))
        enum_dict["__keys"] = keys
        enum_dict["__values"] = values
        enum_dict.update(attrs)
        return super().__new__(cls, name, bases, enum_dict)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
