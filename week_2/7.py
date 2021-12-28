text = 'Hello World'
for char in text:
    print(char)

print(list(reversed(text)))
print(text[::-1])
print(text[2:6])
print(' ' in text)
print('World' in text)
print('Kacper' in text)
print(text.upper())
print(text.lower())
print(text.replace('World', 'Piotr'))
