pos_num = []

while len(pos_num) < 4:
    n = int(input('Podaj liczbę dodatnią: '))
    if n > 0:
        pos_num.append(n)

print('Najmniejsza liczba: ', sorted(pos_num)[0], 'Największa liczba: ', max(pos_num))
