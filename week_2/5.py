value = int(input('Podaj liczbę: '))

for raw in range(1, value + 1):
    for col in range(1, value + 1):
        print(col, end=' ')
    print('')
    value -= 1
