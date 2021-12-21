value1 = int(input('Podaj liczbę: '))
if value1 % 5 == 0 and value1 % 11 == 0:
    print('Twoja liczba jest podzielna przez 5 i 11')
elif value1 % 5 == 0 and value1 % 11 != 0:
    print('Twoja liczba jest podzielna przez 5 i nie jest podzielna przez 11')
elif value1 % 11 == 0 and value1 % 5 != 0:
    print('Twoja liczba jest podzielna przez 11 i nie jest podzielna przez 5.')
else:
    print('Twoja liczba nie jest podzielna ani przez 5, ani przez 11.')
