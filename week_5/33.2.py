from urllib.request import urlopen
from json import loads

URL = 'http://danepubliczne.imgw.pl/api/data/synop/'

with urlopen(URL) as file:
    data = loads(file.read().deocde('utf-8'))
    city = input('Dla jakiego miasta sprawdzić informację o pogodzie? ')

    info = [row for row in data if row['stacja'] == city]
    if len(info) == 0:
        print('Nie wiem jaka będzie tam pogoda.')
    else:
        temperature = info[0]['temperatura']
        pressure = info[0]['ciśnienie']

        print(f'Temperatura to: {temperature}, ciśnienie {pressure}.')
