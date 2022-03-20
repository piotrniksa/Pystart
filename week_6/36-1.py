from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_field(self):
        return pi * self.radius ** 2

    def calculate_circuit(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    r = float(input('Podaj promień: '))
    circle = Circle(r)
    print(f'Pole wynosi {circle.calculate_field():.2f}')
    print(f'Obwód wynosi {circle.calculate_circuit():.2f}')


def test_circle_field():
    # given
    r = 10
    c = Circle(r)

    # when
    field = c.calculate_field()

    # then
    assert field == pi * r * r


def test_circle_circuit():
    # given
    r = 10
    c = Circle(r)

    # when
    circuit = c.calculate_circuit()

    # then
    assert circuit == 2 * pi * r
