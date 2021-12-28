sentence = '12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'
words = sentence.split(' ')
sum_kg = 0

for world in words:
    if world.isnumeric():
        sum_kg += int(world)

print(f'Łącznia waga produktów to {sum_kg} kg.')
