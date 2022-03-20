value = input('Proszę podać liczbę lub "koniec" aby zakonczyć: ')
summary = 1
while value != 'koniec':
    number = int(value)
    if number % 2 == 0:
        summary *= number

    value = input('Proszę podać liczbę lub "koniec" aby zakonczyć: ')

print(f'Iloczyn wartości parzystych to {summary}')
