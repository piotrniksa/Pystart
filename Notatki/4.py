pesel = '18210177915'
check = '13791379131'

control = 0
for pesel_digit, check_digit in zip(pesel, check):
    control += int(pesel_digit) * int(check_digit)

if str(control)[-1] == '0':
    print('Pesel jest prawidłowy')
else:
    print('Pesel jest nieprawidłowy')
