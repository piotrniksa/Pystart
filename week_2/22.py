pesel = '18210177915'
check = '13791379131'

control = 0
for index, _ in enumerate(pesel):
    control += int(pesel[index]) * int(check[index])

if str(control)[-1] == '0':
    print('Pesel jest prawidłowy')
else:
    print('Pesel jest nieprawidłowy')
