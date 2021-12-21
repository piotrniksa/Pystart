number1 = float(input('Podaj pierwszą liczbę: '))
number2 = float(input('Podaj drugą liczbę: '))
if number1 > number2:
    print(f'{number1} jest większe od {number2}')
elif number1 == number2:
    print(f'{number1} i {number2} są równe.')
else:
    print(f'{number2} jest większa od {number1}')
