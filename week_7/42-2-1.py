content = input('Podaj tekst do odwrócenia: ')
try:
    if content == '':
        raise ValueError('Tekst nie został podany!')

    print(content[::-1])
except ValueError as error:
    print(error)
