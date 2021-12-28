mind = 'Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie.'
dog_1 = 'Pies'
dog_2 = 'pies'
how_many_dog = 0

for d in mind.split():
    if d == dog_1 or d == dog_2:
        how_many_dog += 1

print(f'W zdaniu "{mind}" słowo "pies" wystąpiło {how_many_dog} razy!')
