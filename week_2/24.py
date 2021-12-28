word1 = input('Podaj pierwsze słowo: ')
word2 = input('Podaj drugie słowo: ')

# niedziela
# dzielenia

if sorted(word1) == sorted(word2):
    print('To są anagramy.')
else:
    print('To nie są anagramy.')
