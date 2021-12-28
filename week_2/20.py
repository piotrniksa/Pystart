word = input('Podaj słowo do zliczenia: ')
counter = {}
for ll in word:
    if ll not in counter:
        counter[ll] = 0

    counter[ll] += 1

print(counter)
