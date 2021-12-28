text1 = input('Podaj pierwsze wyrażenie: ')
text2 = input('Podaj drugie wyrażenie: ')

print(f'Znaki wspólne dla obu tych wyrażeń to {list(set(text1) & set(text2))}')
