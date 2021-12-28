from math import floor

min_ = int(input('Podaj wartość najmniejszą: '))
max_ = int(input('Podaj wartość największą: '))

for number in range(min_, max_ + 1):
    is_prime = True
    for divider in range(2, floor(number ** 0.5) + 1):
        if number % divider == 0:
            is_prime = False

    if is_prime:
        print(number)
