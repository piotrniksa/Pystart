products = {
    'granat': 3.5,
    'proch': 10,
    'mp40': 100,
    'kałach': 1500
}
print('Dzisiejsze promocje: ')
for name, price in products.items():
    print(f'nazwa: {name} \t cena: {price}')

product = input('Co podać? ')
if product not in products:
    print('Tego nie mamy na stanie. ')
    quit()

price = products[product]
quantity = int(input('Należy podać ilość: '))

print(f'Do zapłaty {quantity * price} PLN')
