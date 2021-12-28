word1 = input('Podaj pierwsze słowo: ')
word2 = input('Podaj drugie słowo: ')

if word1 == word2[::-1]:
    print('To są palindromy')
else:
    print('To nie są palindromy')
