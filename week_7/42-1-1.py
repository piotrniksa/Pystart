names = [
    'Wojtek',
    'Krysia',
    'Basia',
    'Wiola',
    'Antek',
    'Aneta',
    'Ksawery'
]

for i, name in enumerate(names):
    print(f'{i}. {name}')

try:
    number = int(input('Które imie wybierasz? '))
    print(names[number])
except IndexError as e:
    print('Nie mam takiego imienia.')
    print(e)
except (TypeError, ValueError) as error:
    print('Nie rozumiem.')
    print(error)
