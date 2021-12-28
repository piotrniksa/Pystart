pol_en = {'papuga': 'parrot',
          'lew': 'lion',
          'kot': 'cat',
          'pies': 'dog',
          'ptak': 'bird'
          }
# To zadziała, ale jeśli nie ma klucza w słowniku to się wysypie.
# print(pol_en['kot'])
# print(pol_en['koń'])

print(pol_en.get('koń', 'unknown'))
