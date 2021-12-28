pol_en = {'papuga': 'parrot',
          'lew': 'lion',
          'kot': 'cat',
          'pies': 'dog',
          'ptak': 'bird'
          }

en_pol = {}
for polish, english in pol_en.items():
    en_pol[english] = polish

question = input('Co chcesz zrobić? pol-ang [1], ang-pol [2]: ')
if question not in ['1', '2']:
    print('Nie rozumiem, spróbuj jeszcze raz.')
    quit()

if question == '1':
    word = input('Napisz słowo po polsku: ')
    if word not in pol_en:
        print('Nie ma takiego słowa w słowniku.')

    print(f'To oznacza {pol_en[word]}')

else:
    word = input('Napisz słowo po angielsku: ')
    if word not in en_pol:
        print('Nie ma takiego słowa w słowniku.')
        quit()

    print(f'To oznacza {en_pol[word]}')
