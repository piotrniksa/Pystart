class Car:
    def __init__(self, name: str, price: float, max_speed: int):
        self.name = name
        self.price = float(price)
        self.max_speed = int(max_speed)

    def get_info(self):
        return f'{self.name}, cena: {self.price}, prędkość maksymalna: {self.max_speed}'


if __name__ == '__main__':
    cars = []
    for _ in range(3):
        name = input('Nazwa: ')
        price = float(input('Cena: '))
        max_speed = int(input('Prędkość maksymalna: '))
        cars.append(Car(name, price, max_speed))
        print('__' * 10)\

    for car in sorted(cars, key=lambda c: c.price, reverse=True):
        print(car.get_info())

    for car in sorted(cars, key=lambda c: c.max_speed):
        print(car.get_info())


def test_class_car():
    car = Car(name='Polonez', price=1000, max_speed=160)

    assert isinstance(car, Car)
    assert car.name == 'Polonez'
