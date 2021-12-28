text = input('Proszę podać tekst do podliczenia: ')
text_list = text.split(' ')
counter = {}
for word in text_list:
    if word not in counter:
        counter[word] = 0

    counter[word] += 1

print(counter)
