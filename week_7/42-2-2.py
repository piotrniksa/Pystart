fruits = []

try:
    for _ in range(0, 5):
        fruit = input('Podaj nazwę owoca: ')
        if fruit in fruits:
            raise ValueError('Ten owoc już tu leży!')

        fruits.append(fruit)
except ValueError as e:
    print(e)

print(fruits)
