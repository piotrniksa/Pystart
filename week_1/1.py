height = float(input('Podaj swój wzrost w metrach: '))
weight = float(input('Podaj swoją wagę w kilogramach: '))
bmi = weight / height ** 2
print(f'Twoje BMI wynosi {bmi:.2f}')
