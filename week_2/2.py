list_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
podzielne_4 = []
podzielne_5 = []
for n in list_01:
    if n % 4 == 0:
        podzielne_4.append(n)

for n in list_01:
    if n % 5 == 0:
        podzielne_5.append(n)

print('Ilość liczb podzielnych przez 4 to', len(podzielne_4))
print('Ilość liczb podzielnych przez 5 to', len(podzielne_5))
