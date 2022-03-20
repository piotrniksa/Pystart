class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        total = self.value + other.value
        return LengthUnit(total)

    def __sub__(self, other):
        total = self.value - other.value
        return LengthUnit(total)

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100


def test_add_lenght_units():
    # given
    obj1 = LengthUnit(20)
    obj2 = LengthUnit(50)

    # when
    obj3 = obj1 + obj2

    # then
    assert obj3.value == 70


def test_sub_lenght_units():
    # given
    obj1 = LengthUnit(20)
    obj2 = LengthUnit(50)

    # when
    obj3 = obj2 - obj1

    # then
    assert obj3.value == 30
